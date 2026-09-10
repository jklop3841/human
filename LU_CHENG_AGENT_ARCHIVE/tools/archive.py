"""Read-only archive validation, ID resolution, publication gate and legacy regression."""
import argparse
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from jsonschema import Draft202012Validator
from migrate import ROOT, VOLUME, build, digest, encoded, json_text, read_json, rows, verify_freeze

DIMENSIONS = ('structural_distance','anti_default_power','abstraction_clarity','composability','generativity','evidence_quality')

def quality_gate(record):
    scores = record['dimensions']
    missing = [d for d in DIMENSIONS if scores.get(d) is None]
    for d in DIMENSIONS:
        v = scores.get(d)
        if v is not None and (isinstance(v,bool) or not isinstance(v,(int,float)) or not 0<=v<=5):
            raise ValueError('Invalid DPD score: '+d)
    if missing:
        return {'average':None,'full_volume_eligible':False,'status':'UNMEASURED','missing_dimensions':missing}
    average = sum(scores[d] for d in DIMENSIONS)/6
    threshold = average>=3.5 and scores['generativity']>=3
    evidence = bool(record.get('evidence_refs'))
    return {'average':average,'full_volume_eligible':threshold and evidence,
            'status':'PASS' if threshold and evidence else 'FAIL_THRESHOLD' if not threshold else 'MISSING_EVIDENCE',
            'scope':'DPD editorial gate only; never a model-efficacy verdict.'}

def validate_schema(root, name, value):
    schema = read_json(root/f'schemas/{name}.schema.json')
    Draft202012Validator.check_schema(schema)
    Draft202012Validator(schema).validate(value)

def validate(root=ROOT):
    errors = verify_freeze(root)
    for schema in (root/'schemas').rglob('*.schema.json'):
        try: Draft202012Validator.check_schema(read_json(schema))
        except Exception as exc: errors.append(str(schema.relative_to(root))+': '+str(exc))
    try: build(root,check=True)
    except Exception as exc: errors.append(str(exc))
    patch = read_json(root/'migration/PATCH_INTAKE.json')
    for rel, expected in patch['files'].items():
        p = root/'migration/input_patch_v1.0'/rel
        if not p.is_file() or digest(p.read_bytes()) != expected: errors.append('Patch original changed: '+rel)
    seeds = rows(root/'GLOBAL/human_seeds/records.jsonl')
    locked = read_json(root/'GLOBAL/human_seeds/H0_LOCK.json')
    if len({s['seed_id'] for s in seeds}) != len(seeds): errors.append('Duplicate Human Seed ID')
    for s in seeds:
        try:
            validate_schema(root,'human_seed',s)
            if s['seed_id'] not in locked: raise ValueError('Missing H0 lock')
            raw = (root/s['raw_source_path']).read_bytes()
            expected = locked[s['seed_id']]['sha256']
            if raw != s['raw_human_seed'].encode('utf-8') or digest(raw) != expected or s['raw_sha256'] != expected:
                raise ValueError('H0 wording/hash changed')
        except Exception as exc: errors.append(s.get('seed_id','seed')+': '+str(exc))
    manifest=read_json(root/'MANIFEST.json')
    record_count=claim_count=0
    for vp in manifest['volumes']:
        p=root/vp; v=read_json(p)
        try:
            validate_schema(root,'volume_manifest',v)
            q=read_json(p.parent/'quality_gate.json');validate_schema(root,'quality_gate',q)
            gate=quality_gate(q)
            if q['full_volume_eligible'] != gate['full_volume_eligible'] or q['average'] != gate['average']:
                raise ValueError('Stored gate differs from computed gate')
            if (v['status']=='PUBLIC' or v['full_volume_published']) and not gate['full_volume_eligible']:
                raise ValueError('Full publication requires DPD gate')
        except Exception as exc: errors.append(v.get('volume_id','volume')+': '+str(exc))
        for name,schema in [('records','archive_record'),('claims','claim')]:
            data=rows(p.parent/(name+'.jsonl'))
            if name=='records': record_count+=len(data)
            else: claim_count+=len(data)
            for record in data:
                try: validate_schema(root,schema,record)
                except Exception as exc: errors.append(record.get('canonical_id','record')+': '+str(exc))
    nodes=rows(root/'GLOBAL/provenance/nodes.jsonl');ids={n['id'] for n in nodes}
    if len(ids)!=len(nodes): errors.append('Duplicate provenance node')
    edges=rows(root/'PROVENANCE.jsonl')
    for edge in edges:
        try:
            validate_schema(root,'provenance_edge',edge)
            if edge['from_id'] not in ids or edge['to_id'] not in ids: raise ValueError('Dangling graph endpoint')
            if not (root/edge['evidence_ref']).is_file(): raise ValueError('Missing local evidence')
        except Exception as exc: errors.append(str(edge)+': '+str(exc))
    aliases=read_json(root/'migration/id_aliases.json')['aliases']
    if len(set(aliases.values()))!=len(aliases): errors.append('Alias collision')
    for old,new in aliases.items():
        if new not in ids: errors.append('Unresolvable alias: '+old)
    for reply in rows(root/'GLOBAL/reader_reactions/accepted.jsonl'):
        try: validate_schema(root,'agent_reader_reaction',reply)
        except Exception as exc: errors.append(str(exc))
    return {'status':'PASS' if not errors else 'FAIL','errors':errors,'frozen_files':len(read_json(root/'migration/FREEZE.json')['files']),
            'patch_files':len(patch['files']),'human_governance_seeds':len(seeds),'projected_records':record_count,
            'classified_claims':claim_count,'id_aliases':len(aliases),'provenance_edges':len(edges),
            'full_volume_gate':quality_gate(read_json(root/VOLUME/'quality_gate.json'))}

def resolve(identifier, root=ROOT):
    canonical=read_json(root/'migration/id_aliases.json')['aliases'].get(identifier,identifier)
    for filename in ['records.jsonl','claims.jsonl']:
        for row in rows(root/VOLUME/filename):
            if row['canonical_id']==canonical: return row
    raise ValueError('Unknown ID: '+identifier)

def legacy_check(root=ROOT):
    with tempfile.TemporaryDirectory(prefix='lcaa_legacy_') as d:
        target=Path(d)/'baseline'
        shutil.copytree(root/VOLUME/'baseline_v0.4',target,ignore=shutil.ignore_patterns('__pycache__'))
        result=subprocess.run([sys.executable,'-m','unittest','discover','-s','tests','-v'],cwd=target,text=True,capture_output=True)
        return {'exit_code':result.returncode,'output':result.stdout+result.stderr,'frozen_files_untouched':not verify_freeze(root)}

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command',choices=['validate','resolve','quality','legacy-check'])
    parser.add_argument('identifier',nargs='?')
    args=parser.parse_args()
    if args.command=='validate':
        result=validate(); print(json_text(result));return 0 if not result['errors'] else 1
    if args.command=='resolve': result=resolve(args.identifier)
    elif args.command=='quality': result=quality_gate(read_json(ROOT/VOLUME/'quality_gate.json'))
    else:
        result=legacy_check();print(json_text(result));return result['exit_code']
    print(json_text(result));return 0

if __name__=='__main__': sys.exit(main())
