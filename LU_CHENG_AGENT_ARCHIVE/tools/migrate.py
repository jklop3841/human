"""Deterministic, additive LCAA projection. Never edits the frozen v0.4 corpus."""
import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VOLUME = 'SERIES_01_LIVING_SYSTEMS/VOL_001_INSECT_AGENT_ATLAS'
DATE = '2026-09-06'
KINDS = {
    'observations': ('observation_id', 'LC-OBS-2026-', 5),
    'primitives': ('primitive_id', 'LC-PRIM-', 4),
    'compositions': ('composition_id', 'LC-COMP-', 4),
    'species': ('species_id', 'LC-ARCH-', 4),
    'sources': ('source_id', 'LC-SRC-', 4),
    'experiments': ('experiment_id', 'LC-EXP-', 4),
    'lineage': ('event_id', 'LC-EVENT-', 4),
}

def read_json(p):
    return json.loads(Path(p).read_text(encoding='utf-8'))

def rows(p):
    return [json.loads(s) for s in Path(p).read_text(encoding='utf-8').splitlines() if s.strip()]

def digest(b):
    return hashlib.sha256(b).hexdigest()

def encoded(obj):
    return json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode('utf-8')

def json_text(obj):
    return json.dumps(obj, ensure_ascii=False, indent=2)+'\n'

def jsonl_text(records):
    return ''.join(json.dumps(r, ensure_ascii=False)+'\n' for r in records)

def verify_freeze(root=ROOT):
    lock = read_json(root/'migration/FREEZE.json')
    baseline = root/lock['baseline_path']
    errors = []
    actual = {p.relative_to(baseline).as_posix() for p in baseline.rglob('*')
              if p.is_file() and '__pycache__' not in p.parts and p.suffix != '.pyc'}
    if actual != set(lock['files']):
        errors.append('Frozen baseline file set changed')
    for rel, expected in lock['files'].items():
        p = baseline/rel
        if not p.is_file() or digest(p.read_bytes()) != expected:
            errors.append('Frozen content changed: '+rel)
    return errors

def project(root=ROOT):
    errors = verify_freeze(root)
    if errors:
        raise ValueError('; '.join(errors))
    baseline = root/VOLUME/'baseline_v0.4'
    corpus = {kind:rows(baseline/f'corpus/{kind}.jsonl') for kind in KINDS}
    aliases = {}
    for kind, (key, prefix, width) in KINDS.items():
        for i, row in enumerate(corpus[kind], 1):
            aliases[row[key]] = f'{prefix}{i:0{width}d}'
    claim_number = 0
    for data in corpus.values():
        for record in data:
            for c in record.get('claims', []):
                claim_number += 1
                aliases[c['claim_id']] = f'LC-CLAIM-2026-{claim_number:05d}'
    records, claims, edges = [], [], []
    def edge(a, b, relation, ref, scope='Recorded derivation, not a measured causal effect.'):
        edges.append({'from_id':a,'to_id':b,'relation':relation,'created_at':DATE,
                      'actor':'LCAA-MODEL-MIGRATOR','evidence_ref':ref,'scope':scope})
    for kind, data in corpus.items():
        key = KINDS[kind][0]
        path = f'{VOLUME}/baseline_v0.4/corpus/{kind}.jsonl'
        for line, old in enumerate(data, 1):
            old_id = old[key]; cid = aliases[old_id]
            prov = old.get('provenance', {})
            inherited = prov.get('origin_kind') in ('handoff_summary','summary_migration')
            if kind == 'sources':
                author = 'HUMAN_CURATED' if old_id == 'SRC-HANDOFF' else 'EXTERNAL_SOURCE'
                layer = 'E'
            elif kind in ('species','compositions') and not inherited:
                author, layer = 'MODEL_DERIVED', 'A2'
            elif kind == 'experiments':
                author, layer = 'MODEL_DERIVED', 'R' if old['status']=='COMPLETED' else 'A2'
            elif kind == 'lineage':
                author, layer = 'MODEL_FORMALIZED', 'R'
            else:
                author, layer = 'MODEL_FORMALIZED', 'A1'
            citation_scope = ('Bibliography preserves external authorship and source access limits; metadata compilation is model work.'
                              if author == 'EXTERNAL_SOURCE' else
                              'Lu Cheng is the archive originator/curator; this record formalization is not a raw human quotation or a proven human causal contribution.')
            obj = {'schema_version':'1.0','archive_id':'LCAA','series_id':'LCAA-S01','volume_id':'LCAA-S01-V001',
                   'canonical_id':cid,'legacy_id':old_id,'record_type':kind,'authorship_class':author,
                   'layer':layer,'epistemic_status':old.get('epistemic_status','HYPOTHESIZED'),
                   'human_seed_refs':[], 'human_seed_status':'MISSING_RAW' if inherited else 'NOT_ASSERTED',
                   'legacy_ref':path,'legacy_line':line,'payload_sha256':digest(encoded(old)),
                   'attribution_scope':citation_scope,'payload':old}
            records.append(obj)
            edge(cid, 'LCAA-LU-CHENG' if old_id=='SRC-HANDOFF' else 'LCAA-MODEL-MIGRATOR',
                 'CURATED_BY' if old_id=='SRC-HANDOFF' else 'FORMALIZED_BY',path,
                 'Collection curation only.' if old_id=='SRC-HANDOFF' else 'Machine-readable record compilation; no transfer of underlying source authorship.')
            for field, relation in [('derived_from','DERIVED_FROM'),('parent_prior_ids','DERIVED_FROM'),
                                    ('primitives','COMPOSED_WITH'),('source_refs','CITES'),
                                    ('analogue_source_refs','CITES'),('experiment_refs','TESTED_BY'),
                                    ('parent_ids','DERIVED_FROM')]:
                for ref in old.get(field, []):
                    if ref in aliases: edge(cid, aliases[ref],relation,path)
            if old.get('composition_id') in aliases:
                edge(cid,aliases[old['composition_id']],'DERIVED_FROM',path)
            for c in old.get('claims', []):
                claim = {'canonical_id':aliases[c['claim_id']], 'legacy_id':c['claim_id'],
                         'record_id':cid,'epistemic_status':c['epistemic_status'],
                         'authorship_class':'MODEL_FORMALIZED','text':c['text'],
                         'validation_status':c['validation_status'],'source_refs':[aliases[x] for x in c['source_refs'] if x in aliases],
                         'evidence_ref':path,'attribution_scope':'Claim wording/classification compiled by model; source support remains separately scoped.'}
                claims.append(claim)
                edge(cid,claim['canonical_id'],'DERIVED_FROM',path,'Record contains this separately classified claim.')
                for ref in claim['source_refs']:
                    edge(claim['canonical_id'],ref,'REJECTED_BY' if c['epistemic_status']=='REJECTED' else 'TESTED_BY' if c['epistemic_status']=='TESTED' else 'CITES',path,
                         'Applies only to this claim and the original evidence/experimental assumptions.')
    seeds = rows(root/'GLOBAL/human_seeds/records.jsonl')
    for seed in seeds:
        edge(seed['seed_id'],'LCAA-LU-CHENG','OBSERVED_BY',seed['raw_source_path'],
             'Exact governance message preserved; identity follows supplied project context.')
        edge('LCAA-S01-V001',seed['seed_id'],'DERIVED_FROM',seed['raw_source_path'],
             'Governance of continuation/migration only; no architecture-level HPC assertion.')
    edge('LCAA-S01-V001','LCAA-LU-CHENG','CURATED_BY','AUTHOR.md','Archive originator and collection curation.')
    nodes = [{'id':'LCAA','kind':'archive'}, {'id':'LCAA-S01','kind':'series'},
             {'id':'LCAA-S01-V001','kind':'volume'}, {'id':'LCAA-LU-CHENG','kind':'human_curator'},
             {'id':'LCAA-MODEL-MIGRATOR','kind':'model_compiler','model_identity':'Exact runtime ID unavailable'}]
    nodes += [{'id':s['seed_id'],'kind':'human_governance_seed'} for s in seeds]
    nodes += [{'id':r['canonical_id'],'kind':r['record_type']} for r in records]
    nodes += [{'id':c['canonical_id'],'kind':'claim'} for c in claims]
    # Duplicate edges are harmless conceptually, but emit only one identical record.
    edges = list({encoded(e):e for e in edges}.values())
    sample_ids = {'MAYFLY-001','ephemeral_lifecycle','SEED-001','AA04-S001','EXP-S001-COST'}
    return {
        'migration/id_aliases.json':json_text({'version':'1.0','scope':'LCAA-S01-V001','aliases':aliases,
          'rule':'Frozen assignment; extend by appending new IDs, never renumber an existing alias.'}),
        VOLUME+'/records.jsonl':jsonl_text(records),
        VOLUME+'/claims.jsonl':jsonl_text(claims),
        'GLOBAL/provenance/nodes.jsonl':jsonl_text(nodes),
        'PROVENANCE.jsonl':jsonl_text(edges),
        VOLUME+'/PROVENANCE.jsonl':jsonl_text(edges),
        'migration/samples/insect_records.jsonl':jsonl_text([r for r in records if r['legacy_id'] in sample_ids]),
    }

def build(root=ROOT, check=False):
    outputs = project(root)
    changed = []
    for rel, content in outputs.items():
        p = root/rel
        if p.exists() and p.read_text(encoding='utf-8') == content: continue
        changed.append(rel)
        if not check:
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(content, encoding='utf-8')
    if check and changed: raise ValueError('Projection differs: '+', '.join(changed))
    return {'generated_files':len(outputs),'changed_files':changed,'frozen_files_modified':0}

if __name__ == '__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check',action='store_true')
    args=parser.parse_args()
    print(json_text(build(check=args.check)),end='')
