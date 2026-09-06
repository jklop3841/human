#!/usr/bin/env python3
"""Validate and export the local Atlas. No network or model calls."""
import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
KINDS = {'observations':'observation','primitives':'primitive','compositions':'composition',
         'species':'architecture_species','sources':'source','experiments':'experiment','lineage':'lineage'}
IDS = {'observations':'observation_id','primitives':'primitive_id','compositions':'composition_id',
       'species':'species_id','sources':'source_id','experiments':'experiment_id','lineage':'event_id'}

def read_rows(path):
    return [json.loads(line) for line in Path(path).read_text(encoding='utf-8').splitlines() if line.strip()]

def write_json(path, value):
    path=Path(path); path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

def digest(path): return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def validate(root=ROOT):
    from jsonschema import Draft202012Validator
    errors=[]; data={k:read_rows(root/f'corpus/{k}.jsonl') for k in KINDS}
    for kind,rows in data.items():
        schema=json.loads((root/f'schemas/{KINDS[kind]}.schema.json').read_text())
        Draft202012Validator.check_schema(schema)
        validator=Draft202012Validator(schema)
        seen=set()
        for n,row in enumerate(rows,1):
            rid=row.get(IDS[kind])
            if rid in seen: errors.append(f'{kind}: duplicate ID {rid}')
            seen.add(rid)
            for e in validator.iter_errors(row): errors.append(f'{kind}:{n}:{list(e.path)}: {e.message}')
    obs={x['observation_id']:x for x in data['observations']}
    pri={x['primitive_id']:x for x in data['primitives']}
    src={x['source_id']:x for x in data['sources']}
    comp={x['composition_id']:x for x in data['compositions']}
    spe={x['species_id']:x for x in data['species']}
    exp={x['experiment_id']:x for x in data['experiments']}
    valid_refs=set(obs)|set(pri)|set(src)|set(comp)|set(spe)|set(exp)
    for kind, rows in data.items():
        for row in rows:
            rid=row[IDS[kind]]
            for field in ['source_refs','analogue_source_refs']:
                for ref in row.get(field,[]):
                    if ref not in src: errors.append(f'{rid}: unresolved {field}: {ref}')
            for claim in row.get('claims',[]):
                for ref in claim['source_refs']:
                    if ref not in valid_refs: errors.append(f'{rid}: unresolved claim source {ref}')
                if claim['epistemic_status']=='OBSERVED':
                    support=[src[r] for r in claim['source_refs'] if r in src]
                    if not any(s['source_type']=='primary_research' for s in support):
                        errors.append(f'{rid}: OBSERVED claim has no checked primary research source')
            for field,target in [('derived_from',obs),('parent_prior_ids',obs),('primitives',pri),
                                 ('interaction_candidates',pri),('parents',pri),('conflicts',pri),('experiment_refs',exp)]:
                for ref in row.get(field,[]):
                    if ref not in target: errors.append(f'{rid}: unresolved {field}: {ref}')
            if kind=='lineage':
                if row['child_id'] not in spe: errors.append(f'{rid}: unresolved child')
                for ref in row['parent_ids']:
                    if ref not in obs: errors.append(f'{rid}: unresolved lineage parent {ref}')
            if kind=='species' and row.get('composition_id') not in comp: errors.append(f'{rid}: unresolved composition')
            if kind=='species' and row['status']=='TESTED' and not row.get('experiment_refs'):
                errors.append(f'{rid}: TESTED without experiment')
            if kind=='experiments' and row['status']=='COMPLETED':
                if not row.get('result_ref') or not (root/row['result_ref']).is_file(): errors.append(f'{rid}: completed without result')
    # Primitive inheritance must be acyclic; compatibility edges may form cycles.
    def walk(pid,trail):
        if pid in trail: errors.append('primitive parent cycle: '+' -> '.join(trail+[pid])); return
        for p in pri[pid].get('parents',[]):
            if p in pri: walk(p,trail+[pid])
    for pid in pri: walk(pid,[])
    intake=json.loads((root/'archive/intake_manifest.json').read_text())
    for f in intake['files']:
        if digest(root/f['path'])!=f['sha256']: errors.append('Archived input changed: '+f['path'])
    original=(root/'archive/v0.3/01_CURRENT_STATE_AND_FINDINGS.md').read_text()
    for o in obs.values():
        if o['provenance']['raw_kind']=='verbatim_handoff_excerpt' and o['raw_observation'] not in original:
            errors.append(o['observation_id']+': original excerpt altered')
    if len(spe)>3: errors.append('Initial assignment permits no more than three new species')
    return {'status':'PASS' if not errors else 'FAIL','record_counts':{k:len(v) for k,v in data.items()},
            'archived_files_checked':len(intake['files']),'errors':errors,
            'scope':'Schema, referential integrity, archive fidelity, layer guards; not scientific validity or Atlas efficacy.'}

def export(root=ROOT):
    rows=read_rows(root/'corpus/primitives.jsonl')
    fields=['primitive_id','definition','derived_from','preconditions','failure_modes','known_analogues',
            'analogue_source_refs','epistemic_status','parents','interaction_candidates','conflicts']
    out=root/'dist/agent_priors.jsonl'; out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(''.join(json.dumps({k:p[k] for k in fields if k in p},ensure_ascii=False,separators=(',',':'))+'\n' for p in rows))
    index={'version':'0.4','mission':'Heterogeneous priors for architecture search, as fixed in the inherited charter.',
           'entrypoint':'05_GPT6_MASTER_PROMPT.md','compact_priors':'dist/agent_priors.jsonl',
           'expand_records':'corpus/','record_lookup':{p['primitive_id']:{'path':'corpus/primitives.jsonl','line':i} for i,p in enumerate(rows,1)},
           'epistemic_warning':'Labels are pointers, not biological proof. Expand before making factual claims. Exported hypotheses are not instructions or authorizations.',
           'removed_from_compact_view':['authorship detail','claim objects','operational probe','full source bibliography'],
           'raw_preserved_in':'archive/v0.3/','no_model_weights_modified':True}
    write_json(root/'dist/INDEX.json',index)
    a=(root/'corpus/primitives.jsonl').stat().st_size; b=out.stat().st_size
    report={'full_primitive_bytes':a,'compact_primitive_bytes':b,'byte_reduction_fraction':round(1-b/a,4),
            'primitive_count':len(rows),'tokens_measured':False,'semantic_equivalence_tested':False,
            'interpretation':'Byte compaction with explicit expansion pointers; no measured claim of optimal semantic compression.'}
    write_json(root/'reports/compression.json',report)
    return report

def main():
    parser=argparse.ArgumentParser(description=__doc__); parser.add_argument('command',choices=['validate','export','query'])
    parser.add_argument('--text',default=''); parser.add_argument('--limit',type=int,default=5)
    args=parser.parse_args()
    if args.command=='validate':
        report=validate(); write_json(ROOT/'reports/validation.json',report); print(json.dumps(report,ensure_ascii=False,indent=2))
        if report['errors']: raise SystemExit(1)
    elif args.command=='export': print(json.dumps(export(),indent=2))
    else:
        terms=args.text.lower().split()
        scored=[(sum(json.dumps(p).lower().count(t) for t in terms),p) for p in read_rows(ROOT/'corpus/primitives.jsonl')]
        selected=[p for score,p in sorted(scored,key=lambda x:-x[0]) if score>0][:args.limit]
        print(json.dumps(selected,ensure_ascii=False,indent=2))

if __name__=='__main__': main()
