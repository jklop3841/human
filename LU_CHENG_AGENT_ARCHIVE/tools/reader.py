"""Normalize and append evidence-backed reader reports. No model calls or automatic causal scoring."""
import argparse
import copy
import json
import re
import sys
from pathlib import Path
from archive import validate_schema
from migrate import ROOT, digest, json_text, rows

def normalize(raw):
    r=copy.deepcopy(raw)
    nested=r.pop('reader',{})
    for key in ['run_id','model','version']:
        value=nested.get(key,nested.get('model_name') if key=='model' else None)
        if value is not None:
            if key in r and r[key]!=value: raise ValueError('Conflicting flat/nested '+key)
            r[key]=value
    for old,new in [('counterfactual_without_atlas','counterfactual_without_archive'),
                    ('external_domain_discovered','external_domains_discovered'),('criticism','criticisms')]:
        if old in r:
            v=r.pop(old)
            if new in r and r[new]!=v: raise ValueError('Conflicting field alias: '+old)
            r[new]=v
    for field in ['external_domains_discovered','criticisms']:
        if isinstance(r.get(field),str): r[field]=[r[field]]
    if r.get('reaction_class') not in ('R0','R1','R2','R3','R4','R5'):
        raise ValueError('Template or invalid reaction class is not a measured response')
    score=r.get('hpc_score')
    if isinstance(score,bool) or not isinstance(score,int) or not 0<=score<=5:
        raise ValueError('HPC must be an explicit integer 0–5, never an unfilled/null template')
    r['schema_version']='1.0'
    r['hpc_basis']='READER_SELF_REPORT_NOT_CAUSAL_ESTIMATE'
    return r

def check_behavior(r):
    if r.get('synthetic_fixture') is True:
        raise ValueError('Synthetic reader fixture cannot enter a real-results ledger')
    for field in ['hpc_rationale','human_contribution','model_contribution','counterfactual_without_archive']:
        if not r.get(field,'').strip(): raise ValueError('Missing substantive '+field)
    if r['prior_changed'] and not r.get('prior_change_description','').strip():
        raise ValueError('Changed prior requires description')
    if r['reaction_class'] in ('R3','R5') and not r['search_changed']:
        raise ValueError('R3/R5 requires changed search')
    if r['reaction_class']=='R4' and not r['generated_beyond_source']:
        raise ValueError('R4 requires a generated composition reference/description')
    if r['reaction_class']=='R5' and not r['external_domains_discovered']:
        raise ValueError('R5 requires an external-domain candidate; independent escape adjudication remains separate')

def safe_evidence(base, ref):
    p=(base/ref).resolve()
    if not p.is_relative_to(base.resolve()) or not p.is_file():
        raise ValueError('Evidence must be a real file inside the reply directory: '+ref)
    return p

def import_reaction(reply_path, receipt_path, input_path, out, root=ROOT):
    reply_path, receipt_path, input_path, out = map(Path,(reply_path,receipt_path,input_path,out))
    raw_bytes=reply_path.read_bytes();r=normalize(json.loads(raw_bytes))
    meta=json.loads(receipt_path.read_bytes())
    validate_schema(root,'agent_reader_reaction',r);validate_schema(root,'reader_receipt',meta)
    check_behavior(r)
    if meta['mode']!='observational_reader':
        raise ValueError('Use benchmark_v2.py import for controlled campaign records')
    if any(r[k]!=meta[k] for k in ['run_id','model','version']):
        raise ValueError('Reader identity/run differs from operator metadata')
    if digest(input_path.read_bytes())!=meta['input_bundle_sha256']:
        raise ValueError('Input bundle hash mismatch')
    if not re.fullmatch(r'LC-RUN-\d{8}-\d{4}',r['run_id']): raise ValueError('Invalid run ID')
    evidence=[safe_evidence(reply_path.parent,x) for x in r['evidence_refs']]
    out.mkdir(parents=True,exist_ok=True)
    accepted=out/'accepted.jsonl';receipts=out/'receipts.jsonl'
    old=rows(accepted) if accepted.exists() else []
    old_meta=rows(receipts) if receipts.exists() else []
    if any(x['run_id']==r['run_id'] for x in old): raise ValueError('Refusing to overwrite existing reader run')
    if any(x['session_id']==meta['session_id'] for x in old_meta): raise ValueError('Session reused')
    target=out/'raw'/r['run_id']
    if target.exists(): raise ValueError('Raw run directory already exists')
    target.mkdir(parents=True)
    (target/'reply.json').write_bytes(raw_bytes)
    (target/'receipt.json').write_bytes(receipt_path.read_bytes())
    (target/'input.txt').write_bytes(input_path.read_bytes())
    copied=[]
    for i,source in enumerate(evidence,1):
        path=target/f'evidence_{i:03d}{source.suffix}'
        path.write_bytes(source.read_bytes());copied.append(path.relative_to(out).as_posix())
    r['evidence_refs']=copied
    r['recorded_mode']='observational_reader'
    r['raw_reply_sha256']=digest(raw_bytes)
    # Single-writer local ledger. Concurrent imports are intentionally unsupported.
    accepted.write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in old+[r]))
    receipts.write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in old_meta+[meta]))
    return {'run_id':r['run_id'],'status':'RECORDED_OBSERVATIONAL','controlled_calls_added':0,
            'causal_conclusion':None,'hpc_basis':r['hpc_basis']}

def summary(out):
    p=Path(out)/'accepted.jsonl';data=rows(p) if p.exists() else []
    counts={k:sum(r['reaction_class']==k for r in data) for k in ['R0','R1','R2','R3','R4','R5']}
    return {'reader_reports':len(data),'status':'DESCRIPTIVE_SELF_REPORTS' if data else 'NO_REAL_RESULTS',
            'reaction_counts':counts,'hpc_self_report_mean':sum(r['hpc_score'] for r in data)/len(data) if data else None,
            'controlled_calls':0,'causal_conclusion':None,'escape_rate':None}

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);s=p.add_subparsers(dest='cmd',required=True)
    n=s.add_parser('normalize');n.add_argument('reply')
    i=s.add_parser('import');i.add_argument('--reply',required=True);i.add_argument('--receipt',required=True);i.add_argument('--input',required=True);i.add_argument('--out',required=True)
    a=s.add_parser('summary');a.add_argument('--out',default=str(ROOT/'GLOBAL/reader_reactions'))
    args=p.parse_args()
    try:
        result=normalize(json.loads(Path(args.reply).read_text())) if args.cmd=='normalize' else import_reaction(args.reply,args.receipt,args.input,args.out) if args.cmd=='import' else summary(args.out)
        print(json_text(result))
    except (ValueError,KeyError) as exc: p.exit(1,str(exc)+'\n')
