#!/usr/bin/env python3
"""Synthetic capsule-residency cost model. No LLM, biology, or service performance claims."""
import json, random, hashlib
from collections import OrderedDict
from pathlib import Path
from statistics import mean
from atlas import ROOT, write_json, read_rows

def trace(scenario,seed,steps):
    rng=random.Random(seed)
    if scenario=='recurring_long':
        result=[]; previous=None
        while len(result)<steps:
            family=rng.choice([k for k in range(4) if k!=previous]); previous=family
            result.extend([family]*rng.randint(20,40))
        return result[:steps]
    if scenario=='rapid_switch':
        result=[]; previous=None
        for _ in range(steps):
            family=rng.choice([k for k in range(4) if k!=previous]); previous=family; result.append(family)
        return result
    if scenario=='one_shot': return list(range(steps))
    raise ValueError(scenario)

def simulate(requests,policy,cfg):
    cache=OrderedDict(); active=None; cost=0.; builds=restores=suspends=0; peaks=0
    cap=cfg['capacity']
    for key in requests:
        if policy=='rebuild':
            builds+=1; cost+=cfg['build_cost']+cfg['execution_cost']; continue
        # No future access: cache lookup uses only the current exact family key.
        if policy in ['dormant_pool','cold_lru_transient'] and active!=key:
            if active is not None:
                suspends+=1; cost+=cfg['suspend_cost']
            active=None
        if key not in cache:
            builds+=1; cost+=cfg['build_cost']
            if len(cache)>=cap: cache.popitem(last=False)
            cache[key]=True
        else:
            cache.move_to_end(key)
            if policy!='warm_lru' and active!=key:
                restores+=1; cost+=cfg['restore_cost']
        active=key
        cost+=cfg['execution_cost']
        if policy=='warm_lru': cost+=len(cache)*cfg['active_maintenance_per_step']
        else: cost+=cfg['active_maintenance_per_step']+(len(cache)-1)*cfg['dormant_maintenance_per_step']
        peaks=max(peaks,len(cache))
    return {'total_cost':round(cost,8),'builds':builds,'restores':restores,'suspends':suspends,'peak_stored_capsules':peaks}

def main():
    p=ROOT/'experiments/cost_config.json'; cfg=json.loads(p.read_text()); raw=[]
    for scenario in cfg['scenarios']:
        for seed in cfg['seeds']:
            requests=trace(scenario,seed,cfg['steps'])
            h=hashlib.sha256(json.dumps(requests).encode()).hexdigest()
            for policy in cfg['policies']:
                raw.append({'scenario':scenario,'seed':seed,'policy':policy,'trace_sha256':h,**simulate(requests,policy,cfg)})
    out=ROOT/'reports/cost_sandbox_raw.jsonl'; out.parent.mkdir(exist_ok=True)
    out.write_text(''.join(json.dumps(r)+'\n' for r in raw))
    means={s:{p:mean(r['total_cost'] for r in raw if r['scenario']==s and r['policy']==p) for p in cfg['policies']} for s in cfg['scenarios']}
    recurring=means['recurring_long']['dormant_pool']<means['recurring_long']['warm_lru']
    broad=all(means[s]['dormant_pool']<min(v for p,v in means[s].items() if p!='dormant_pool') for s in means)
    matched=all(abs(r['total_cost']-next(x['total_cost'] for x in raw if x['scenario']==r['scenario'] and x['seed']==r['seed'] and x['policy']=='cold_lru_transient'))<1e-9 for r in raw if r['policy']=='dormant_pool')
    report={'experiment_id':cfg['experiment_id'],'status':'COMPLETED','epistemic_status':'TESTED',
      'scope':'synthetic_cost_accounting_only','real_model_calls':0,'config_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
      'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'simulations':len(raw),'seeds':len(cfg['seeds']),
      'mean_total_cost':means,'recurring_vs_warm_supported_under_assumptions':recurring,
      'broad_superiority_supported':broad,'matches_conventional_cold_cache':matched,
      'interpretation':'The residency rule can change assumed cost, but an explicitly equivalent ordinary cache ties it. This is a prior-art/abstraction calibration, not evidence of Atlas generativity or a new algorithm.',
      'limitations':[cfg['key_assumption'],'Cost constants were assumed; they are not empirical token, latency or energy measurements.',
                    'The conventional matched policy shares the same executable transition rules by design; its equivalence is an analytical negative control.',
                    'No semantic validity decay, erroneous matching, network faults, concurrency or permission transitions were simulated.']}
    write_json(ROOT/'reports/cost_sandbox_summary.json',report)
    experiments=read_rows(ROOT/'corpus/experiments.jsonl')
    for r in experiments:
        if r['experiment_id']==cfg['experiment_id']:
            r.update(status='COMPLETED',epistemic_status='TESTED',result_ref='reports/cost_sandbox_summary.json')
    (ROOT/'corpus/experiments.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in experiments))
    # Keep the whole species hypothetical. Add scoped tested/rejected claims instead of laundering evidence upwards.
    species=read_rows(ROOT/'corpus/species.jsonl')
    for s in species:
        if s['species_id']=='AA04-S001':
            s['experiment_refs']=['EXP-S001-COST']
            s['claims']=[c for c in s['claims'] if c['claim_id'] not in ['AA04-S001-C2','AA04-S001-C3']]
            s['claims'].extend([
             {'claim_id':'AA04-S001-C2','text':'Synthetic cost results are stored in EXP-S001-COST; scope does not extend to real Agents.','epistemic_status':'TESTED','source_refs':['EXP-S001-COST'],'validation_status':'synthetic_only'},
             {'claim_id':'AA04-S001-C3','text':'Broad superiority over the matched ordinary cache is rejected in this simulation.','epistemic_status':'REJECTED','source_refs':['EXP-S001-COST'],'validation_status':'rejected_under_declared_model'}])
    (ROOT/'corpus/species.jsonl').write_text(''.join(json.dumps(s,ensure_ascii=False)+'\n' for s in species))
    lineage=read_rows(ROOT/'corpus/lineage.jsonl')
    lineage=[e for e in lineage if e['event_id']!='EV04-S001-NEGCTRL']
    lineage.append({'event_id':'EV04-S001-NEGCTRL','child_id':'AA04-S001',
      'parent_ids':['FOREST-001','IMMUNE-001','MAYFLY-001'],'event':'scoped_claim_rejected',
      'epistemic_status':'REJECTED','experiment_refs':['EXP-S001-COST'],'claim_ids':['AA04-S001-C3'],
      'reason':'An explicitly matched conventional cold cache ties the proposed mechanism; broad superiority is not supported. Other untested claims retain their own status.'})
    (ROOT/'corpus/lineage.jsonl').write_text(''.join(json.dumps(e,ensure_ascii=False)+'\n' for e in lineage))
    print(json.dumps(report,ensure_ascii=False,indent=2))

if __name__=='__main__': main()
