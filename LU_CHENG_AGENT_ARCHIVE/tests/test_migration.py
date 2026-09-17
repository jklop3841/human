import copy
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path
from jsonschema import ValidationError

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'tools'))
import archive
import benchmark_v2
import migrate
import reader
import apply_upgrade

class MigrationTests(unittest.TestCase):
    def test_freeze_projection_and_all_references(self):
        result=archive.validate(ROOT)
        self.assertEqual(result['errors'],[])
        self.assertEqual((result['frozen_files'],result['patch_files']),(136,41))
        self.assertEqual((result['projected_records'],result['classified_claims']),(71,62))
        self.assertEqual(migrate.build(ROOT,check=True)['changed_files'],[])

    def test_record_round_trip_and_claim_scope(self):
        for r in migrate.rows(ROOT/migrate.VOLUME/'records.jsonl'):
            original=migrate.rows(ROOT/r['legacy_ref'])[r['legacy_line']-1]
            self.assertEqual(original,r['payload'])
            self.assertEqual(migrate.digest(migrate.encoded(original)),r['payload_sha256'])
            self.assertEqual(archive.resolve(r['legacy_id'])['canonical_id'],r['canonical_id'])
        species=archive.resolve('AA04-S001')['payload']
        self.assertEqual(species['status'],'HYPOTHESIZED')
        self.assertEqual({c['epistemic_status'] for c in species['claims']},{'HYPOTHESIZED','TESTED','REJECTED'})

    def test_raw_lock_detects_wording_change(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)/'archive';shutil.copytree(ROOT,root,ignore=shutil.ignore_patterns('__pycache__','work_runs'))
            seed=migrate.rows(root/'GLOBAL/human_seeds/records.jsonl')[0]
            (root/seed['raw_source_path']).write_text('A polished replacement is forbidden')
            self.assertTrue(any('H0 wording/hash changed' in e for e in archive.validate(root)['errors']))

    def test_frozen_original_tamper_rejected_before_projection(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)/'archive';shutil.copytree(ROOT,root,ignore=shutil.ignore_patterns('__pycache__','work_runs'))
            (root/migrate.VOLUME/'baseline_v0.4/README.md').write_text('changed')
            with self.assertRaisesRegex(ValueError,'Frozen content changed'):migrate.build(root)

    def test_human_seed_example_never_promoted(self):
        seeds=migrate.rows(ROOT/'GLOBAL/human_seeds/records.jsonl')
        self.assertTrue(all(s['purpose']=='PROJECT_GOVERNANCE' for s in seeds))
        self.assertNotIn('蜉蝣这么短的生命', ''.join(s['raw_human_seed'] for s in seeds))
        for r in migrate.rows(ROOT/migrate.VOLUME/'records.jsonl'):
            self.assertEqual(r['human_seed_refs'],[])

    def test_dpd_null_and_threshold_boundaries(self):
        q={'dimensions':{k:4 for k in archive.DIMENSIONS},'evidence_refs':['review.json']}
        self.assertTrue(archive.quality_gate(q)['full_volume_eligible'])
        q['dimensions']['generativity']=2.9
        self.assertFalse(archive.quality_gate(q)['full_volume_eligible'])
        q['dimensions']={k:3.5 for k in archive.DIMENSIONS}
        self.assertTrue(archive.quality_gate(q)['full_volume_eligible'])
        q['dimensions']['generativity']=None
        self.assertIsNone(archive.quality_gate(q)['average'])
        q['dimensions']['generativity']=True
        with self.assertRaises(ValueError):archive.quality_gate(q)

    def response(self):
        return {'schema_version':'1.0','run_id':'LC-RUN-20260906-0001','model':'FIXTURE_MODEL','version':'TEST_ONLY',
          'reaction_class':'R0','prior_changed':False,'search_changed':False,'prior_change_description':'',
          'external_domains_discovered':[],'generated_beyond_source':[],'already_familiar':[],
          'counterfactual_without_archive':'Synthetic fixture, no actual generation.','human_contribution':'None in this test fixture.',
          'model_contribution':'None; fixture only.','hpc_score':0,'hpc_rationale':'Synthetic test only; not a measured zero.',
          'criticisms':[],'rejected_claims':[],'next_tests':[],'evidence_refs':['answer.json'],
          'hpc_basis':'READER_SELF_REPORT_NOT_CAUSAL_ESTIMATE'}

    def receipt(self):
        return {'run_id':'LC-RUN-20260906-0001','mode':'observational_reader','provider':'FIXTURE_PROVIDER','model':'FIXTURE_MODEL','version':'TEST_ONLY',
          'identity_evidence':'Synthetic fixture only','session_id':'FIXTURE_SESSION','fresh_context':True,'memory_disabled':True,
          'prior_conversation_exposure':False,'generation_timestamp':'TEST_ONLY','timestamp_source':'operator_observation',
          'synthetic_fixture':True,'settings_fingerprint':'TEST_ONLY','input_bundle_sha256':'0'*64,'browsing_policy':'disabled'}

    def test_template_conflicts_and_nested_adapter(self):
        template=migrate.read_json(ROOT/'migration/input_patch_v1.0/templates/15_READER_RESPONSE_TEMPLATE.json')
        with self.assertRaisesRegex(ValueError,'Template'):reader.normalize(template)
        response=self.response();response['reader']={k:response.pop(k) for k in ['model','version','run_id']}
        normalized=reader.normalize(response)
        self.assertEqual(normalized,self.response())
        response['model']='CONFLICT'
        with self.assertRaisesRegex(ValueError,'Conflicting'):reader.normalize(response)
        for value in [None,True,6,-1]:
            r=self.response();r['hpc_score']=value
            with self.assertRaises(ValueError):reader.normalize(r)

    def test_real_intake_rejects_fixtures_and_empty_evidence(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)
            for name,data in [('reply',self.response()),('receipt',self.receipt())]:
                (p/(name+'.json')).write_text(json.dumps(data))
            (p/'input.txt').write_text('Synthetic test input')
            with self.assertRaises(ValidationError):reader.import_reaction(p/'reply.json',p/'receipt.json',p/'input.txt',p/'out')
            self.assertEqual(reader.summary(p/'out')['reader_reports'],0)
            self.assertIsNone(reader.summary(p/'out')['hpc_self_report_mean'])
        r=self.response();r['reaction_class']='R5'
        with self.assertRaisesRegex(ValueError,'changed search'):reader.check_behavior(r)

    def test_v2_preparation_preserves_old_policy_and_blinding(self):
        with tempfile.TemporaryDirectory() as d:
            out=Path(d)/'run';r=benchmark_v2.prepare(out)
            self.assertEqual(r['prepared_calls'],54);self.assertEqual(r['real_calls'],0)
            manifest=migrate.read_json(out/'runner_only/manifest.json')
            self.assertEqual({c['condition'] for c in manifest['calls']},{'A','B','C'})
            prompt=next((out/'prompts').glob('*.txt')).read_text()
            self.assertIn('3 search queries and 5 page opens',prompt)
            self.assertNotIn('hpc_score',prompt);self.assertNotIn('Lu Cheng',prompt)
            self.assertIn('Do not browse',(ROOT/migrate.VOLUME/'baseline_v0.4/benchmark/common_prompt.txt').read_text())
            self.assertEqual(benchmark_v2.blind(out,Path(d)/'review')['architectures_exported'],0)
            with self.assertRaises(ValueError):benchmark_v2.prepare(out)

    def test_v2_controlled_intake_rejects_fixture(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d);run=p/'run';benchmark_v2.prepare(run)
            reply={'architectures':[],'search_log':[],'external_domain_candidates':[]}
            for name,data in [('answer',reply),('reaction',self.response()),('receipt',self.receipt())]:
                (p/(name+'.json')).write_text(json.dumps(data))
            with self.assertRaises(ValidationError):
                benchmark_v2.import_call(run,'LC-RUN-20260906-0001',p/'answer.json',p/'reaction.json',p/'receipt.json')
            self.assertFalse((run/'raw').exists())

    def test_v2_import_and_reviewer_export_in_temporary_test_only_campaign(self):
        # Positive branch coverage using authored fixtures in a deleted temporary directory.
        # No provider calls occur; these records never enter the archive result ledger.
        with tempfile.TemporaryDirectory(prefix='lcaa_synthetic_tooling_test_') as d:
            p=Path(d);run=p/'run';benchmark_v2.prepare(run)
            c=migrate.read_json(run/'runner_only/manifest.json')['calls'][0]
            a={'architecture_id':'FIXTURE_A','name':'SECRET_TEST_NAME','components':['test node'],'state_store':'test artifact',
               'decision_rules':['test rule'],'messages':['test receipt'],'lifecycle':'finite','resource_budget':'four',
               'expected_advantage':'test expectation','failure_modes':['test failure'],'falsification':'test falsifier',
               'sandbox':'fixture only','nearest_known':'test baseline','prior_trace':[]}
            b=copy.deepcopy(a);b['architecture_id']='FIXTURE_B'
            answer={'architectures':[a,b],'search_log':[],'external_domain_candidates':[]}
            (p/'answer.json').write_text(json.dumps(answer))
            reaction=self.response();reaction['run_id']=c['run_id'];(p/'reaction.json').write_text(json.dumps(reaction))
            meta=self.receipt();meta.update(run_id=c['run_id'],mode='v2_controlled',synthetic_fixture=False,
                input_bundle_sha256=c['prompt_sha256'],browsing_policy='equal_budget_search',query_count=0,page_open_count=0,
                search_audit_complete=True,architecture_sealed_before_reflection=True,
                architecture_sha256_before_reflection=migrate.digest((p/'answer.json').read_bytes()))
            (p/'receipt.json').write_text(json.dumps(meta))
            result=benchmark_v2.import_call(run,c['run_id'],p/'answer.json',p/'reaction.json',p/'receipt.json')
            self.assertEqual(result['status'],'RECORDED_REQUIRES_INDEPENDENT_REVIEW')
            with self.assertRaisesRegex(ValueError,'Session reused'):
                benchmark_v2.import_call(run,c['run_id'],p/'answer.json',p/'reaction.json',p/'receipt.json')
            result=benchmark_v2.blind(run,p/'review')
            self.assertEqual(result['architectures_exported'],2)
            text=(p/'review/architectures.json').read_text()
            for forbidden in ['SECRET_TEST_NAME','prior_trace','model_slot','FIXTURE_PROVIDER']:
                self.assertNotIn(forbidden,text)
        self.assertEqual(reader.summary(ROOT/'GLOBAL/reader_reactions')['reader_reports'],0)

if __name__=='__main__':unittest.main()
