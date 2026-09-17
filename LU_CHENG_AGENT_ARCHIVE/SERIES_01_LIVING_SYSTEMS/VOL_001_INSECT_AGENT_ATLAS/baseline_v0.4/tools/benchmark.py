#!/usr/bin/env python3
"""Prepare isolated prompts, retain external replies, blind review, and analyze a pilot.

This program never invokes a model. Operator/API exports are imported explicitly.
"""
import argparse, csv, hashlib, io, json, math, random, re
from collections import Counter, defaultdict
from pathlib import Path
from statistics import mean
from atlas import ROOT, write_json

RATING_FIELDS=['distance','interaction','emergence','falsifiability','implementability']
FEATURES={
 'control_topology':['central','hierarchical','peer','environment','hybrid'],
 'memory_location':['instance','external','distributed','hybrid','none'],
 'adaptation_locus':['fixed','parameter','topology','lifecycle','mixed'],
 'lifecycle':['persistent','ephemeral','dormant','staged','mixed'],
 'resource_policy':['fixed','central_budget','local_budget','market','mixed']}
REVIEW_FIELDS=['blind_id','reviewer_id',*RATING_FIELDS,'task_valid',*FEATURES,'condition_guess','rationale']

def load(path): return json.loads(Path(path).read_text(encoding='utf-8'))
def sha(data): return hashlib.sha256(data).hexdigest()
def require(condition,message):
    if not condition: raise ValueError(message)
def manifest(run): return load(Path(run)/'runner_only/manifest.json')
def all_submissions(run): return [load(p) for p in sorted((Path(run)/'submissions').glob('*/submission.json'))]

def prepare(run, config_path=ROOT/'benchmark/config.json'):
    run=Path(run);require(not run.exists(),'Run directory already exists; create a new run instead of overwriting.')
    cfg=load(config_path); tasks={t['task_id']:t for t in load(ROOT/'benchmark/tasks.json')}
    require(cfg.get('run_mode','real_collection') in ['real_collection','synthetic_tooling_test'],'Unknown run mode')
    require(cfg['architectures_per_call']==2,'This frozen output schema requires exactly two architectures per call')
    rng=random.Random(cfg['seed']); schema=(ROOT/'benchmark/response.schema.json').read_text()
    common=(ROOT/'benchmark/common_prompt.txt').read_text()
    for d in ['prompts','runner_only','submissions']: (run/d).mkdir(parents=True,exist_ok=True)
    calls=[]; order=0
    for m in cfg['models']:
        for task in cfg['task_ids']:
            for replicate in range(cfg['replicates']):
                conditions=list(cfg['conditions']);rng.shuffle(conditions)
                for condition in conditions:
                    order+=1;call_id='Q'+sha(f'{cfg["seed"]}:{order}:{rng.random()}'.encode())[:12]
                    reading=(ROOT/f'benchmark/materials/{condition}.txt').read_text().strip()
                    prompt=common+'\nTarget problem:\n'+tasks[task]['prompt']
                    if reading: prompt+='\n\n'+reading
                    prompt+='\n\nOutput schema:\n'+schema
                    p=run/f'prompts/{call_id}.txt';p.write_text(prompt)
                    calls.append({'call_id':call_id,'model_slot':m['slot'],'task_id':task,'replicate':replicate+1,
                                  'condition':condition,'scheduled_order':order,'prompt_sha256':sha(p.read_bytes())})
    write_json(run/'runner_only/manifest.json',{'config':cfg,'calls':calls,'status':'PREPARED_NOT_RUN',
       'material_hashes':{c:sha((ROOT/f'benchmark/materials/{c}.txt').read_bytes()) for c in cfg['conditions']},
       'schema_sha256':sha(schema.encode()),'tasks_sha256':sha((ROOT/'benchmark/tasks.json').read_bytes()),
       'real_model_calls_recorded':0})
    write_json(run/'runner_only/response.schema.json',json.loads(schema))
    write_json(run/'runner_only/tasks.json',list(tasks.values()))
    with (run/'runner_only/operator_schedule.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(calls[0]));w.writeheader();w.writerows(calls)
    first=calls[:3]
    (run/'FIRST_THREE_CALLS.md').write_text('# 首轮三个独立上下文\n\n先登记 M01 的实际界面/模型信息。以下三个文件每个都在全新、关闭记忆与联网的对话中单独提交；不要给生成模型整个目录。\n\n'+
       '\n'.join(f'{i}. `prompts/{c["call_id"]}.txt`' for i,c in enumerate(first,1))+
       '\n\n保留完整原始回复和会话元信息。三次回复是同一模型同一任务的三种条件，仅是流程首轮，不能单独证明有效。\n')
    return {'planned_calls':len(calls),'planned_architectures':len(calls)*cfg['architectures_per_call'],
            'real_model_calls':0,'run':str(run)}

def register(run,slot,provider,model_id,surface,evidence):
    run=Path(run);m=manifest(run)
    require(not any(s['model_slot']==slot for s in all_submissions(run)),'Model identity frozen after the first reply; use a new run to change it.')
    matches=[x for x in m['config']['models'] if x['slot']==slot]; require(len(matches)==1,'Unknown model slot')
    require(all(str(v).strip() for v in [provider,model_id,surface,evidence]),'Model identity fields must be filled from observed evidence.')
    require(not any(x['slot']!=slot and x.get('provider')==provider and x.get('model_id')==model_id for x in m['config']['models']),
            'A distinct slot cannot double-count the same provider/model as another model')
    matches[0].update(provider=provider,model_id=model_id,surface=surface,identity_evidence=evidence)
    write_json(run/'runner_only/manifest.json',m)
    return {'registered_slot':slot,'identity_source':'operator_supplied_evidence; not inferred from model self-description'}

def import_reply(run,call_id,response_path,metadata_path):
    from jsonschema import Draft202012Validator
    run=Path(run);m=manifest(run);calls={c['call_id']:c for c in m['calls']}
    require(call_id in calls,'Unknown call ID');call=calls[call_id]
    require(sha((run/f'prompts/{call_id}.txt').read_bytes())==call['prompt_sha256'],'Prompt changed after preparation')
    model=next(x for x in m['config']['models'] if x['slot']==call['model_slot'])
    require(all(model.get(k) for k in ['provider','model_id','surface','identity_evidence']),'Register the actual model identity first')
    dest=run/f'submissions/{call_id}';require(not dest.exists(),'One scheduled call gets one retained reply; no overwrite or best-of selection')
    meta=load(metadata_path)
    require(meta.get('metadata_source') in ['operator_observation','provider_api'],'Metadata must come from operator or API, not model self-report')
    for k in ['session_id','settings_fingerprint','generation_timestamp']:
        require(isinstance(meta.get(k),str) and meta[k] and 'REPLACE_' not in meta[k],f'Missing actual {k}')
    synthetic=m['config'].get('run_mode')=='synthetic_tooling_test'
    require(meta.get('synthetic_fixture',False)==synthetic,'Synthetic fixtures must be explicitly isolated in a synthetic_tooling_test run')
    for prev in all_submissions(run):
        require(prev['metadata']['session_id']!=meta['session_id'],'Session reused: every condition needs an independent fresh context')
        if prev['model_slot']==call['model_slot']:
            require(prev['metadata']['settings_fingerprint']==meta['settings_fingerprint'],'Settings changed within a model block; start a new run')
    raw=Path(response_path).read_bytes();text=raw.decode('utf-8');parse_text=text.strip()
    # Preserve exact raw bytes; strip only a single wrapper for structural parsing.
    if parse_text.startswith('```') and parse_text.endswith('```'):
        parse_text=re.sub(r'^```(?:json)?\s*','',parse_text,flags=re.I);parse_text=re.sub(r'\s*```$','',parse_text)
    errors=[];output=None
    try:
        output=json.loads(parse_text)
        validator=Draft202012Validator(load(run/'runner_only/response.schema.json'))
        errors=[e.message for e in validator.iter_errors(output)]
        if not errors:
            ids=[x['architecture_id'] for x in output['architectures']]
            if len(ids)!=len(set(ids)): errors.append('Duplicate architecture IDs')
    except (json.JSONDecodeError,TypeError) as e: errors.append(str(e))
    contamination=[]
    for k in ['fresh_context','memory_disabled','browsing_disabled']:
        if meta.get(k) is not True: contamination.append(k+' not verified true')
    if meta.get('prior_conversation_exposure') is not False: contamination.append('prior conversation exposure not excluded')
    dest.mkdir();(dest/'raw.txt').write_bytes(raw)
    submission={**call,'model_identity':model,'metadata':meta,'raw_sha256':sha(raw),
                'data_kind':'synthetic_fixture' if synthetic else 'operator_supplied_external_reply',
                'output':output,'parse_errors':errors,'contamination_flags':contamination,
                'eligibility':'contaminated' if contamination else ('invalid_output' if errors else 'eligible')}
    write_json(dest/'submission.json',submission)
    m['real_model_calls_recorded']=0 if synthetic else len(all_submissions(run));m['status']='TOOLING_TEST_ONLY' if synthetic else 'COLLECTING'
    write_json(run/'runner_only/manifest.json',m)
    return {'call_id':call_id,'eligibility':submission['eligibility'],'parse_errors':errors,'contamination_flags':contamination}

def blind(run,out):
    run=Path(run);out=Path(out);require(not out.exists(),'Reviewer export already exists; choose a new directory')
    out.mkdir(parents=True);m=manifest(run);entries=[];mapping={}
    for s in all_submissions(run):
        if s['eligibility']!='eligible': continue
        for i,a in enumerate(s['output']['architectures']):
            blind_id='R'+sha((s['call_id']+':'+str(i)).encode())[:14]
            # Trace and names are scored later, separately, because they identify condition/model.
            body={k:v for k,v in a.items() if k not in ['architecture_id','name','prior_trace']}
            mapping[blind_id]={'call_id':s['call_id'],'architecture_index':i,'task_id':s['task_id']}
            entries.append({'blind_id':blind_id,'task_id':s['task_id'],'architecture':body})
    random.Random(m['config']['seed']+1).shuffle(entries)
    write_json(out/'architectures.json',entries)
    write_json(out/'tasks.json',load(run/'runner_only/tasks.json'))
    write_json(out/'feature_codebook.json',FEATURES)
    with (out/'scores.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=REVIEW_FIELDS);w.writeheader()
        for e in entries: w.writerow({'blind_id':e['blind_id']})
    (out/'RUBRIC.md').write_text((ROOT/'benchmark/RUBRIC.md').read_text())
    # The mapping remains outside the reviewer export.
    write_json(run/'runner_only/blind_map.json',mapping)
    return {'eligible_architectures_exported':len(entries),'condition_map_included':False,
            'blinding_limit':'Mechanism content or spontaneous biological words can still reveal treatment. Reviewers record a condition guess.'}

def js_divergence(left,right):
    if not left or not right: return None
    a=Counter(left);b=Counter(right);n=sum(a.values());k=sum(b.values());result=0.
    for key in set(a)|set(b):
        p=a[key]/n;q=b[key]/k;t=(p+q)/2
        if p: result+=.5*p*math.log2(p/t)
        if q: result+=.5*q*math.log2(q/t)
    return result

def analyze(run,score_files):
    run=Path(run);m=manifest(run);subs={s['call_id']:s for s in all_submissions(run)}
    synthetic=m['config'].get('run_mode')=='synthetic_tooling_test'
    require(synthetic or all(s.get('data_kind')!='synthetic_fixture' and not s['metadata'].get('synthetic_fixture') for s in subs.values()),
            'Synthetic data detected inside a real collection run')
    mapping=load(run/'runner_only/blind_map.json') if (run/'runner_only/blind_map.json').exists() else {}
    ratings=defaultdict(list);seen=set()
    for path in score_files:
        for row in csv.DictReader(io.StringIO(Path(path).read_text(encoding='utf-8'))):
            if not row.get('reviewer_id'): continue
            bid=row['blind_id'];require(bid in mapping,'Unknown blind ID in scoring file')
            pair=(bid,row['reviewer_id']);require(pair not in seen,'Duplicate reviewer rating');seen.add(pair)
            require(row.get('rationale','').strip(),'Scores need a mechanism-based rationale')
            for field in RATING_FIELDS:
                row[field]=float(row[field]);require(math.isfinite(row[field]) and 0<=row[field]<=4,'Rating out of range')
            row['task_valid']=int(row['task_valid']);require(row['task_valid'] in [0,1],'task_valid must be 0 or 1')
            for field,allowed in FEATURES.items():require(row[field] in allowed,f'Unknown {field} category')
            require(row.get('condition_guess') in ['A','B','C','unknown'],'Condition guess must be A/B/C/unknown')
            ratings[bid].append(row)
    needed=m['config']['evaluation']['reviewers_required'];bycall=defaultdict(list);disagreements=[];guess=[]
    for bid,rs in ratings.items():
        if len({r['reviewer_id'] for r in rs})<needed: continue
        call_id=mapping[bid]['call_id'];features=[]
        for field in FEATURES:
            values={r[field] for r in rs}
            if len(values)>1: disagreements.append({'blind_id':bid,'field':field,'values':sorted(values)})
            features.append(next(iter(values)) if len(values)==1 else None)
        distance=mean(r['distance']*r['task_valid'] for r in rs)
        bycall[call_id].append({'distance':distance,'raw_distance':mean(r['distance'] for r in rs),
          'task_valid':mean(r['task_valid'] for r in rs),'signature':'|'.join(features) if all(features) else None,
          **{f:mean(r[f] for r in rs) for f in RATING_FIELDS if f!='distance'}})
        for r in rs:
            guess.append(r['condition_guess']==subs[call_id]['condition'] if r['condition_guess']!='unknown' else None)
    call_scores={}
    for c in m['calls']:
        s=subs.get(c['call_id'])
        if not s or s['eligibility']=='contaminated': continue
        if s['eligibility']=='invalid_output': call_scores[c['call_id']]=0.
        elif len(bycall[c['call_id']])==m['config']['architectures_per_call']:
            call_scores[c['call_id']]=mean(x['distance'] for x in bycall[c['call_id']])
    blocks=defaultdict(dict)
    for c in m['calls']:
        if c['call_id'] in call_scores:
            blocks[(c['model_slot'],c['task_id'],c['replicate'])][c['condition']]=call_scores[c['call_id']]
    complete=[]
    for key,scores in blocks.items():
        if set(scores)==set(['A','B','C']):
            complete.append({'model_slot':key[0],'task_id':key[1],'replicate':key[2],**scores,
                'B_minus_A':scores['B']-scores['A'],'B_minus_C':scores['B']-scores['C']})
    per_model=[]
    for slot in [x['slot'] for x in m['config']['models']]:
        rows=[r for r in complete if r['model_slot']==slot]
        if rows:per_model.append({'model_slot':slot,'complete_blocks':len(rows),
          'B_minus_A':mean(r['B_minus_A'] for r in rows),'B_minus_C':mean(r['B_minus_C'] for r in rows)})
    signatures=defaultdict(list)
    for c in m['calls']:
        for a in bycall.get(c['call_id'],[]):
            if a['signature'] and a['task_valid']==1:
                signatures[(c['model_slot'],c['task_id'],c['condition'])].append(a['signature'])
    distribution=[]
    for model in m['config']['models']:
        for task in m['config']['task_ids']:
            k=(model['slot'],task)
            a,b,c=[signatures[(*k,g)] for g in ['A','B','C']]
            distribution.append({'model_slot':k[0],'task_id':task,'A_n':len(a),'B_n':len(b),'C_n':len(c),
             'JSD_B_A':js_divergence(b,a),'JSD_B_C':js_divergence(b,c),
             'histograms':{g:dict(Counter(v)) for g,v in [('A',a),('B',b),('C',c)]}})
    n_expected=len(m['calls'])//3
    summary={'benchmark_id':m['config']['benchmark_id'],'planned_calls':len(m['calls']),
      'recorded_external_calls':0 if synthetic else len(subs),'synthetic_fixture_calls':len(subs) if synthetic else 0,
      'eligible_calls':sum(s['eligibility']=='eligible' for s in subs.values()),
      'invalid_output_calls':sum(s['eligibility']=='invalid_output' for s in subs.values()),
      'contaminated_calls':sum(s['eligibility']=='contaminated' for s in subs.values()),
      'missing_calls':len(m['calls'])-len(subs),'complete_triplets':len(complete),'expected_triplets':n_expected,
      'status':'TOOLING_TEST_ONLY' if synthetic else ('NO_REAL_RESULTS' if not subs else ('PILOT_DESCRIPTIVE_COMPLETE' if len(complete)==n_expected else 'INCOMPLETE_DESCRIPTIVE_ONLY')),
      'per_model':per_model,'macro_B_minus_A':mean(r['B_minus_A'] for r in per_model) if per_model else None,
      'macro_B_minus_C':mean(r['B_minus_C'] for r in per_model) if per_model else None,
      'distribution':distribution,'feature_disagreements':disagreements,
      'condition_guess_accuracy_known_only':mean(x for x in guess if x is not None) if any(x is not None for x in guess) else None,
      'efficacy_conclusion':None,'capability_scaling_conclusion':None,
      'limitations':['Pilot has few independent calls; distribution divergence has upward finite-sample bias.',
                    'Two outputs in one call are clustered, never counted as two independent trials.',
                    'JSD uses only valid outputs with agreed feature coding; disagreement and missingness can bias it.',
                    'Unknown sampling settings and imperfect semantic blinding remain recorded limitations.',
                    'A positive distance difference is not a task-quality, novelty or model-capability result.']}
    write_json(run/'analysis/paired_blocks.json',complete);write_json(run/'analysis/summary.json',summary)
    return summary

def main():
    p=argparse.ArgumentParser(description=__doc__);sub=p.add_subparsers(dest='cmd',required=True)
    q=sub.add_parser('prepare');q.add_argument('--run',required=True);q.add_argument('--config',default=str(ROOT/'benchmark/config.json'))
    q=sub.add_parser('register-model');q.add_argument('--run',required=True)
    for flag in ['slot','provider','model-id','surface','evidence']:q.add_argument('--'+flag,required=True)
    q=sub.add_parser('import');q.add_argument('--run',required=True);q.add_argument('--call-id',required=True)
    q.add_argument('--response',required=True);q.add_argument('--metadata',required=True)
    q=sub.add_parser('blind');q.add_argument('--run',required=True);q.add_argument('--out',required=True)
    q=sub.add_parser('analyze');q.add_argument('--run',required=True);q.add_argument('--scores',nargs='*',default=[])
    a=p.parse_args()
    if a.cmd=='prepare': result=prepare(a.run,a.config)
    elif a.cmd=='register-model':result=register(a.run,a.slot,a.provider,a.model_id,a.surface,a.evidence)
    elif a.cmd=='import':result=import_reply(a.run,a.call_id,a.response,a.metadata)
    elif a.cmd=='blind':result=blind(a.run,a.out)
    else:result=analyze(a.run,a.scores)
    print(json.dumps(result,ensure_ascii=False,indent=2))

if __name__=='__main__': main()
