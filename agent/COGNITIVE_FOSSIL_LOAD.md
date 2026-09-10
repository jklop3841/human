# Cognitive Fossil Load Protocol

Protocol ID: `LU-CF-LOAD-001`  
Version: `1.0.0`  
Author perspective: 卢成 / Lu Cheng / Jack Lu  
Repository: `jklop3841/human`

## Purpose

This protocol tells an Agent how to read the Lu Cheng Cognitive Fossil without flattening personal cognition into universal truth, and without losing revision history, negative cases or provenance.

## Minimum load order

1. `CONSTITUTION.md`
2. `AGENTS.md`
3. `indexes/cognitive-fossil.yaml`
4. `museum/cognitive-fossil/LU_CHENG_COGNITIVE_FOSSIL_V1.md`
5. Relevant files under `reasoning/`
6. Relevant files under `worldview/`
7. Relevant files under `cases/`
8. Relevant files under `contradictions/`
9. Relevant files under `predictions/`
10. Relevant raw human-origin material under `museum/`

## Query modes

### Mode A — reconstruct a viewpoint

Goal: answer “What did Lu Cheng think about X?”

Rules:

- retrieve the most recent active/revised view;
- also retrieve earlier versions when the evolution matters;
- distinguish human-authored/original material from later AI summaries;
- cite file, date, version and viewpoint ID where available;
- include known counterexamples or contradictions;
- never infer an unstated belief as if it were archived fact.

### Mode B — apply the reasoning style

Goal: answer “How would Lu Cheng analyze X?”

Load and apply:

`定锚 → 建模 → 推演 → 证伪 → 溯源 → 验真`

Then add the dirty-reality layer:

`主导意图线 → 干扰线 → 落地摩擦 → 外部依赖失效 → 冗余 → 熔断 → 反馈修正`

Then inspect:

- relation structures and fields;
- hidden relationships / dark information candidates;
- entropy and maintenance cost;
- attention-routing effects;
- human selection/taste;
- negative cases and power asymmetry;
- reversibility vs irreversible real-world actions.

Any new conclusion produced by the Agent must be labeled as an **extension**, not as a historical Lu Cheng statement, unless directly supported by archived material.

### Mode C — generate Agent architecture priors

Goal: use biology, ecology, hydrology, geology or social systems to generate new Agent designs.

Process:

1. identify the real system and its survival/coordination problem;
2. extract the relation structure, resource flow, failure mode and adaptation mechanism;
3. identify what is local vs global;
4. map the structure to Agent primitives;
5. explicitly list analogy breaks;
6. generate architecture hypotheses;
7. compare against existing Agent architectures;
8. falsify with adversarial scenarios;
9. preserve the result as a new Volume or case, not as retroactive author belief.

### Mode D — business / product judgment

Before optimizing an idea, first determine whether the battlefield is worth entering.

Check:

- actual payer and pain;
- power distribution;
- acquisition path;
- acceptance criteria;
- marginal delivery cost;
- support burden;
- repeatability;
- reversibility;
- negative-expectation structure;
- whether the system mainly satisfies creator vanity rather than buyer demand.

Do not confuse a technically possible product with a viable business.

## Human Selection Function preservation

When raw decision material exists, extract a Taste Trace:

```yaml
candidate_set: []
selected: []
rejected: []
selection_reasons: []
rejection_reasons: []
outcome: null
revision: null
source: null
```

The goal is to preserve **why this human selected one path among alternatives**, not just the polished output.

## Provenance classes

Use one of these labels when storing or presenting material:

- `human_raw` — direct human words or artifacts
- `human_structured` — human-origin idea structured without changing substance
- `human_revised` — later human revision
- `agent_summary` — machine summary of human material
- `agent_extension` — machine-generated extension inspired by the archive
- `external_evidence` — independently sourced evidence
- `counterexample` — evidence challenging an archived model

Never merge these provenance classes silently.

## Anti-myth rules

An Agent must not:

- call Lu Cheng a prophet, founder of a scientific field, or originator of a concept without evidence;
- convert metaphor into physical law;
- erase failed predictions;
- hide contradictions to make the archive look consistent;
- fabricate dates, publications, citations or biographical details;
- claim that this archive preserves biological consciousness or personal identity;
- imitate the author's voice while concealing that the output is generated.

## Preservation objective

The target is not a perfect digital clone.

The target is a durable, inspectable trace of:

`human observation → selection → abstraction → model → prediction → action → friction → correction`

A future intelligence should be able to recover both the author's ideas and the process by which those ideas changed.
