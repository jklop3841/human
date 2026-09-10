"""Prepare, import and blind new v2 calls without changing the frozen v0.4 pilot."""
import argparse
import copy
import json
import random
from pathlib import Path
from jsonschema import Draft202012Validator
from archive import validate_schema
from migrate import ROOT, digest, json_text, read_json, rows
from reader import normalize, check_behavior

def write_json(path, data):
    path.parent.mkdir(parents=True,exist_ok=True);path.write_text(json_text(data),encoding='utf-8')

def prepare(out, root=ROOT):
    out=Path(out)
    if out.exists() and any(out.iterdir()): raise ValueError('Campaign output must be empty; no overwrite')
    cfg=read_json(root/'benchmark_v2/config.json')
    if 'D' in cfg['conditions']: raise ValueError('D remains blocked until a separately reviewed multi-volume protocol exists')
    schema=read_json(root/'benchmark_v2/response.schema.json')
    tasks=read_json(root/'benchmark_v2/tasks.json')
    calls=[{'model_slot':m['slot'],'task_id':t['task_id'],'replicate':rep,'condition':c}
           for m in cfg['models'] for t in tasks for rep in range(1,cfg['replicates']+1) for c in cfg['conditions']]
    random.Random(cfg['seed']).shuffle(calls)
    common=(root/'benchmark_v2/common_prompt.txt').read_text()
    for i,c in enumerate(calls,1):
        c['run_id']=f'LC-RUN-20260906-{i:04d}'
        c['prompt_id']='Q'+digest(json.dumps(c,sort_keys=True).encode())[:12]
        task=next(t['prompt'] for t in tasks if t['task_id']==c['task_id'])
        material=(root/f"benchmark_v2/materials/{c['condition']}.txt").read_text()
        text=common+'\nTASK\n'+task+'\nCONTEXTUAL READING\n'+material+'\nRESPONSE SCHEMA\n'+json_text(schema)
        p=out/'prompts'/(c['prompt_id']+'.txt');p.parent.mkdir(parents=True,exist_ok=True);p.write_text(text)
        c['prompt_sha256']=digest(p.read_bytes())
    provenance={}
    for p in sorted((root/'benchmark_v2').rglob('*')):
        if p.is_file(): provenance[p.relative_to(root).as_posix()]=digest(p.read_bytes())
    for rel in ['templates/reader_response.json','templates/v2_receipt.json','schemas/agent_reader_reaction.schema.json','schemas/reader_receipt.schema.json','tools/benchmark_v2.py','tools/reader.py']:
        provenance[rel]=digest((root/rel).read_bytes())
    write_json(out/'runner_only/manifest.json',{'config':cfg,'calls':calls,'input_hashes':provenance,
               'status':'PREPARED_NOT_RUN','real_calls':0,'synthetic_fixture_calls':0})
    write_json(out/'runner_only/schedule.json',calls)
    write_json(out/'runner_only/response.schema.json',schema)
    write_json(out/'runner_only/reader.schema.json',read_json(root/'schemas/agent_reader_reaction.schema.json'))
    write_json(out/'runner_only/receipt.schema.json',read_json(root/'schemas/reader_receipt.schema.json'))
    write_json(out/'runner_only/supplied_domains.json',read_json(root/'benchmark_v2/supplied_domains.json'))
    for rel in ['benchmark_v2/reflection_prompt.txt','templates/reader_response.json','templates/v2_receipt.json']:
        (out/'runner_only'/Path(rel).name).write_bytes((root/rel).read_bytes())
    return {'prepared_calls':len(calls),'real_calls':0,'D':'BLOCKED_MISSING_DISTANT_VOLUMES','status':'PREPARED_NOT_RUN'}

def import_call(run,run_id,reply,reaction,receipt,root=ROOT):
    run,reply,reaction,receipt=map(Path,(run,reply,reaction,receipt))
    manifest=read_json(run/'runner_only/manifest.json')
    call=next((c for c in manifest['calls'] if c['run_id']==run_id),None)
    if call is None: raise ValueError('Unknown prepared run ID')
    p=run/'prompts'/(call['prompt_id']+'.txt')
    if digest(p.read_bytes())!=call['prompt_sha256']: raise ValueError('Prepared prompt changed')
    meta=read_json(receipt);answer=read_json(reply);response=normalize(read_json(reaction))
    for name,data in [('receipt',meta),('response',answer),('reader',response)]:
        Draft202012Validator(read_json(run/f'runner_only/{name}.schema.json')).validate(data)
    check_behavior(response)
    if meta['mode']!='v2_controlled' or meta['run_id']!=run_id: raise ValueError('Controlled receipt/run required')
    if any(response[k]!=meta[k] for k in ['run_id','model','version']): raise ValueError('Reader metadata mismatch')
    if meta['input_bundle_sha256']!=call['prompt_sha256']: raise ValueError('Wrong prompt receipt')
    if meta['browsing_policy']!='equal_budget_search' or meta.get('search_audit_complete') is not True:
        raise ValueError('Equal-budget search and complete operator tool audit required')
    log=answer['search_log']
    if [x['step'] for x in log]!=list(range(1,len(log)+1)): raise ValueError('Search sequence incomplete')
    for kind,field,limit in [('query','query_count',3),('open','page_open_count',5)]:
        count=sum(x['kind']==kind for x in log)
        if type(meta.get(field)) is not int or meta[field]!=count or count>limit: raise ValueError('Missing, mismatched or over-budget '+field)
    if meta.get('architecture_sealed_before_reflection') is not True or meta.get('architecture_sha256_before_reflection')!=digest(reply.read_bytes()):
        raise ValueError('Operator must seal the raw architecture before reflection')
    ids={a['architecture_id'] for a in answer['architectures']}
    if len(ids)!=2: raise ValueError('Duplicate architecture ID')
    for candidate in answer['external_domain_candidates']:
        if candidate['architecture_id'] not in ids: raise ValueError('External candidate has no architecture target')
        if not candidate['source_url'].startswith(('https://','http://')): raise ValueError('External candidate requires a source URL')
    for a in answer['architectures']:
        for trace in a['prior_trace']:
            if trace['record_id'] not in [f'P{i:02d}' for i in range(1,11)] or call['condition']=='A':
                raise ValueError('Invalid supplied-prior trace')
    existing=[read_json(p) for p in (run/'receipts').glob('*.json')] if (run/'receipts').exists() else []
    if any(m['session_id']==meta['session_id'] for m in existing): raise ValueError('Session reused')
    for m in existing:
        if m['model_slot']==call['model_slot'] and any(m[k]!=meta[k] for k in ['provider','model','version','settings_fingerprint','browsing_policy']):
            raise ValueError('Model slot settings or identity drift')
    target=run/'raw'/run_id
    if target.exists(): raise ValueError('Refusing to overwrite raw campaign result')
    # Reader evidence names must resolve to these three sealed local inputs; no inferred evidence.
    allowed={reply.name,reaction.name,receipt.name}
    if not set(response['evidence_refs'])<=allowed: raise ValueError('Reaction evidence must name the supplied answer/reaction/receipt files')
    target.mkdir(parents=True)
    for source,name in [(reply,'architecture.json'),(reaction,'reaction.json'),(receipt,'receipt.json')]:
        (target/name).write_bytes(source.read_bytes())
    response['evidence_refs']=[f'raw/{run_id}/architecture.json',f'raw/{run_id}/reaction.json',f'raw/{run_id}/receipt.json']
    write_json(run/'responses'/(run_id+'.json'),answer)
    write_json(run/'reactions'/(run_id+'.json'),response)
    write_json(run/'receipts'/(run_id+'.json'),{**meta,'model_slot':call['model_slot'],'raw_reply_sha256':digest(reply.read_bytes()),'raw_reaction_sha256':digest(reaction.read_bytes())})
    return {'run_id':run_id,'status':'RECORDED_REQUIRES_INDEPENDENT_REVIEW','observed_calls':len(existing)+1,'causal_conclusion':None}

def blind(run,out):
    run,out=Path(run),Path(out)
    if out.exists() and any(out.iterdir()): raise ValueError('Reviewer output must be empty')
    manifest=read_json(run/'runner_only/manifest.json');items=[];mapping={}
    for c in manifest['calls']:
        p=run/'responses'/(c['run_id']+'.json')
        if not p.exists(): continue
        for i,a in enumerate(read_json(p)['architectures']):
            bid='BV2-'+digest((c['run_id']+str(i)).encode())[:12]
            payload={k:v for k,v in a.items() if k not in ['name','prior_trace','architecture_id']}
            items.append({'blind_id':bid,'architecture':payload})
            mapping[bid]={'run_id':c['run_id'],'architecture_index':i}
    random.Random(8731).shuffle(items)
    write_json(out/'architectures.json',items)
    write_json(run/'runner_only/blind_map.json',mapping)
    (out/'architecture_review.csv').write_text('blind_id,reviewer_id,task_valid,distance,interaction,emergence,novelty,falsifiability,implementability,condition_guess,rationale\n')
    (out/'README.md').write_text('Score architecture mechanisms first. Do not load runner_only or source-aware packets. Lock ratings before source-aware review. Content can still reveal treatment.\n')
    return {'architectures_exported':len(items),'blind_scope':'Name, prior trace, source search, identity and condition keys omitted; semantic masking is partial.'}

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);s=p.add_subparsers(dest='cmd',required=True)
    a=s.add_parser('prepare');a.add_argument('--out',required=True)
    a=s.add_parser('import')
    for name in ['run','run-id','reply','reaction','receipt']:a.add_argument('--'+name,required=True)
    a=s.add_parser('blind');a.add_argument('--run',required=True);a.add_argument('--out',required=True)
    args=p.parse_args()
    try: result=prepare(args.out) if args.cmd=='prepare' else blind(args.run,args.out) if args.cmd=='blind' else import_call(args.run,args.run_id,args.reply,args.reaction,args.receipt)
    except (ValueError,KeyError) as exc: p.exit(1,str(exc)+'\n')
    print(json_text(result))
