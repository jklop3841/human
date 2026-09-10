import copy, csv, json, sys, tempfile, unittest
from pathlib import Path
from jsonschema import Draft202012Validator

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'tools'))
import atlas, benchmark, cost_sandbox

class IntegrityTests(unittest.TestCase):
    def test_legacy_status_and_fields_remain_accepted(self):
        cases={
         'observation':{'observation_id':'old','title':'old','domain':'unknown','origin':'human',
                        'raw_observation':'original text','epistemic_status':'OBSERVED','provenance':'untyped legacy extension'},
         'primitive':{'primitive_id':'old','name':'old','definition':'old','derived_from':[],
                      'epistemic_status':'ABSTRACTED','provenance':'untyped legacy extension'},
         'architecture_species':{'species_id':'old','name':'old','parent_prior_ids':[],
                                  'primitives':[],'interaction_rules':[],'falsification':[],'status':'ARCHIVED'}}
        for kind,case in cases.items():
            old=Draft202012Validator(json.loads((ROOT/f'schemas/v0.3/{kind}.schema.json').read_text()))
            new=Draft202012Validator(json.loads((ROOT/f'schemas/{kind}.schema.json').read_text()))
            self.assertTrue(old.is_valid(case));self.assertTrue(new.is_valid(case))
            opted={**case,'schema_version':'0.4'}
            self.assertFalse(new.is_valid(opted),'v0.4 must require explicit provenance and claims')

    def test_corpus_references_layers_and_raw_fidelity(self):
        report=atlas.validate(ROOT)
        self.assertEqual(report['errors'],[])
        self.assertEqual(report['archived_files_checked'],15)

    def test_stimuli_balanced_and_seed_species_excluded(self):
        b=(ROOT/'benchmark/materials/B.txt').read_text();c=(ROOT/'benchmark/materials/C.txt').read_text()
        self.assertEqual(len(b.split()),len(c.split()))
        for i in range(1,11):
            self.assertIn(f'P{i:02d}',b);self.assertIn(f'P{i:02d}',c)
        for s in atlas.read_rows(ROOT/'corpus/species.jsonl'):
            self.assertNotIn(s['species_id'],b);self.assertNotIn(s['name'],b)

    def test_sandbox_equality_and_adverse_regime(self):
        cfg=json.loads((ROOT/'experiments/cost_config.json').read_text())
        r=cost_sandbox.trace('rapid_switch',0,100)
        dormant=cost_sandbox.simulate(r,'dormant_pool',cfg)
        matched=cost_sandbox.simulate(r,'cold_lru_transient',cfg)
        warm=cost_sandbox.simulate(r,'warm_lru',cfg)
        self.assertEqual(dormant,matched)
        self.assertGreater(dormant['total_cost'],warm['total_cost'])
        self.assertLessEqual(dormant['peak_stored_capsules'],cfg['capacity'])

    def make_run(self,base,synthetic=False):
        cfg=json.loads((ROOT/'benchmark/config.json').read_text())
        cfg.update(run_mode='synthetic_tooling_test' if synthetic else 'real_collection',replicates=1,
                   task_ids=['T01'],models=[cfg['models'][0]])
        path=base/'config.json';atlas.write_json(path,cfg);run=base/'run'
        benchmark.prepare(run,path)
        benchmark.register(run,'M01','FIXTURE_PROVIDER','FIXTURE_MODEL','test-only','Synthetic test fixture, never a real model')
        return run

    def reply(self):
        a={'architecture_id':'x','name':'NAME_MUST_NOT_LEAK','components':['node'],
          'state_store':'external artifact','decision_rules':['choose by local queue'],
          'messages':['receipt'],'lifecycle':'finite task','resource_budget':'four capsules',
          'expected_advantage':'bounded active work','failure_modes':['wrong cue'],
          'falsification':'higher cost at equal accuracy','sandbox':'replay a finite trace',
          'nearest_known':'cached worker pool','prior_trace':[{'record_id':'P01','influence':'TRACE_MUST_NOT_LEAK'}]}
        b=copy.deepcopy(a);b['architecture_id']='y';b['decision_rules']=['choose by explicit schedule']
        return {'architectures':[a,b]}

    def metadata(self,idx):
        return {'session_id':f'FIXTURE_SESSION_{idx}','settings_fingerprint':'FIXTURE_SETTINGS',
          'generation_timestamp':'synthetic-test-not-a-generation-time','fresh_context':True,'memory_disabled':True,
          'browsing_disabled':True,'prior_conversation_exposure':False,'metadata_source':'operator_observation',
          'synthetic_fixture':True}

    def test_real_run_rejects_fixture_and_preserves_zero_calls(self):
        with tempfile.TemporaryDirectory(prefix='atlas_tooling_test_') as d:
            base=Path(d);run=self.make_run(base,False);call=benchmark.manifest(run)['calls'][0]
            atlas.write_json(base/'reply.json',self.reply());atlas.write_json(base/'meta.json',self.metadata(1))
            with self.assertRaisesRegex(ValueError,'Synthetic'):
                benchmark.import_reply(run,call['call_id'],base/'reply.json',base/'meta.json')
            report=benchmark.analyze(run,[])
            self.assertEqual(report['recorded_external_calls'],0)
            self.assertIsNone(report['macro_B_minus_A'])
            self.assertEqual(report['status'],'NO_REAL_RESULTS')

    def test_blinding_paired_aggregation_and_fixture_isolation(self):
        with tempfile.TemporaryDirectory(prefix='atlas_tooling_test_') as d:
            base=Path(d);run=self.make_run(base,True);calls=benchmark.manifest(run)['calls']
            atlas.write_json(base/'reply.json',self.reply())
            for i,c in enumerate(calls):
                atlas.write_json(base/'meta.json',self.metadata(i))
                result=benchmark.import_reply(run,c['call_id'],base/'reply.json',base/'meta.json')
                self.assertEqual(result['eligibility'],'eligible')
            with self.assertRaisesRegex(ValueError,'overwrite'):
                benchmark.import_reply(run,calls[0]['call_id'],base/'reply.json',base/'meta.json')
            out=base/'review';result=benchmark.blind(run,out)
            self.assertEqual(result['eligible_architectures_exported'],6)
            text=(out/'architectures.json').read_text()
            self.assertNotIn('NAME_MUST_NOT_LEAK',text);self.assertNotIn('TRACE_MUST_NOT_LEAK',text)
            self.assertNotIn('model_slot',text);self.assertNotIn('condition',text)
            mapping=json.loads((run/'runner_only/blind_map.json').read_text())
            conditions={c['call_id']:c['condition'] for c in calls}
            score_files=[]
            for reviewer in ['FIXTURE_REVIEW_A','FIXTURE_REVIEW_B']:
                p=base/(reviewer+'.csv');score_files.append(p)
                with p.open('w',newline='') as f:
                    w=csv.DictWriter(f,fieldnames=benchmark.REVIEW_FIELDS);w.writeheader()
                    for bid,entry in mapping.items():
                        cond=conditions[entry['call_id']]
                        row={'blind_id':bid,'reviewer_id':reviewer,**{k:2 for k in benchmark.RATING_FIELDS},
                             'distance':3 if cond=='B' else 1,'task_valid':1,'control_topology':'peer' if cond=='B' else 'central',
                             'memory_location':'external','adaptation_locus':'fixed','lifecycle':'persistent',
                             'resource_policy':'fixed','condition_guess':'unknown','rationale':'Synthetic rating for aggregation verification only.'}
                        w.writerow(row)
            report=benchmark.analyze(run,score_files)
            self.assertEqual(report['complete_triplets'],1)
            self.assertEqual(report['macro_B_minus_A'],2)
            self.assertEqual(report['macro_B_minus_C'],2)
            self.assertEqual(report['recorded_external_calls'],0)
            self.assertEqual(report['synthetic_fixture_calls'],3)
            self.assertEqual(report['status'],'TOOLING_TEST_ONLY')
            self.assertEqual(report['distribution'][0]['JSD_B_A'],1)
            self.assertIsNone(report['efficacy_conclusion'])

    def test_reused_context_detected_in_tooling_run(self):
        with tempfile.TemporaryDirectory(prefix='atlas_tooling_test_') as d:
            base=Path(d);run=self.make_run(base,True);calls=benchmark.manifest(run)['calls']
            atlas.write_json(base/'reply.json',self.reply());atlas.write_json(base/'meta.json',self.metadata(0))
            benchmark.import_reply(run,calls[0]['call_id'],base/'reply.json',base/'meta.json')
            with self.assertRaisesRegex(ValueError,'Session reused'):
                benchmark.import_reply(run,calls[1]['call_id'],base/'reply.json',base/'meta.json')

if __name__=='__main__':unittest.main()
