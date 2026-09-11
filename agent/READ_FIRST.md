# READ FIRST — Lu Cheng Human Archive

Protocol ID: HUMAN-BOOTSTRAP-001
Version: 1.2.0

## Purpose

This is the shortest reliable bootstrap path for an Agent entering the Human archive.

## Minimal load

Load in this order:

1. `../human.yaml`
2. `../CONSTITUTION.md`
3. `../AGENTS.md`
4. `../exports/agent-readable/manifest.json`
5. `../indexes/topics.yaml`

Then retrieve only the relevant canonical records.

## Current archive identity

Author: `Lu Cheng / 卢成 / Jack Lu`
Type: `personal-cognitive-museum`
Canonical repository: `https://github.com/jklop3841/human`

This archive stores one named human's evolving viewpoints, observations, methods, hypotheses, contradictions, revisions and external calibrations.

It is not a universal truth database.

## Fast mode selection

Choose one mode before answering:

- `quote` — retrieve what Lu Cheng explicitly stated.
- `explain` — explain a documented framework and its limits.
- `simulate` — infer how Lu Cheng may analyze a new case; label as simulation.
- `critique` — test a framework against counterexamples and external evidence.
- `compile` — structure new human material as draft; do not silently mark as author-confirmed.

## Epistemic separation

Never collapse these categories:

```yaml
fact: externally verifiable claim
viewpoint: Lu Cheng's documented position
experience: personal observation or reported event
inference: reasoning derived from archive material
extension: Agent-generated addition
unknown: unresolved or unavailable information
```

## Current trilogy

```yaml
HUMAN-BOOK-001:
  object: human_individual
  entry: books/human-interface-risk/README.md

HUMAN-BOOK-002:
  object: civilization_dependencies
  entry: books/civilization-interfaces/README.md

HUMAN-BOOK-003:
  object: human_groups_and_institutions
  entry: books/human-groups-institutions/README.md
```

## Institution fast path

If the query names an institution such as police, court, prosecutor, hospital, fire department, military, government, school, bank, company, media platform, utility or NGO:

1. load `../books/human-groups-institutions/INSTITUTIONAL_DRIFT_FRAMEWORK.md`;
2. locate the archetype in `../books/human-groups-institutions/institution-atlas.yaml`;
3. open the relevant shard under `../books/human-groups-institutions/institutions/`;
4. distinguish mission, permission, scarcity, metric pressure, hierarchy, discretion, information asymmetry, self-preservation, capture, path dependence and correction channels;
5. do not infer corruption or malicious intent without evidence.

## Cross-institution topology fast path

If the question involves two or more institutions, a funding chain, authority chain, information handoff, infrastructure dependency, oversight path or system-wide consequence:

1. load `../graphs/institution-topology/topology-manifest.yaml`;
2. load `../graphs/institution-topology/nodes.yaml`;
3. retrieve relevant typed edges from `edges.yaml` and `edges-coverage-002.yaml`;
4. identify edge type, direction, evidence status, handoff loss, dependency, drift and correction paths;
5. remember: `edge presence != causal strength` and `100% node incident coverage != complete social graph`;
6. use `HUMAN_INSTITUTION_TOPOLOGY_LOAD.md` for full protocol.

## Time / state fast path

If the question involves change over time, crisis, emergency, expansion, reform, recovery, war, disaster, outbreak, financial stress or institutional transition:

1. load the static institution topology first;
2. load `../graphs/social-dynamics/dynamics-manifest.yaml`;
3. load `../graphs/social-dynamics/state-types.yaml`;
4. load the relevant domain overlay under `../graphs/social-dynamics/overlays/`;
5. classify the system as one state or a mixed/transition state;
6. map node changes, edge changes, drift risks, correction opportunities, temporary changes, sticky changes and exit conditions;
7. use `HUMAN_SOCIAL_DYNAMICS_LOAD.md` for full protocol;
8. re-verify time- and jurisdiction-specific factual claims externally.

Never treat state overlays as forecasts or numeric transition models.

## Historical calibration fast path

If the query asks whether Social Dynamics actually fits a documented historical event, or whether the framework has been validated/calibrated:

1. load `../graphs/social-dynamics/calibration/calibration-manifest.yaml`;
2. load the relevant record from `../graphs/social-dynamics/calibration/events-001.yaml`;
3. restore the external event timeline from the listed authoritative sources;
4. separate physical/technical/domain causation from institutional coordination effects;
5. compare observed state/edge changes with the model;
6. report both `model_hits` and `model_misses`;
7. distinguish retrospective fit from prospective prediction;
8. use `HUMAN_HISTORICAL_CALIBRATION_LOAD.md` for the full protocol.

Current first-round conclusion: Social Dynamics is best treated as a **meso-level institutional coordination, escalation, dependency and recovery model**, not a universal event-causation or quantitative forecasting model.

## Human framework fast path

Dirty Reality Structural Field Theory:
`../worldview/reality/HUMAN-REALITY-001.md`

Human interface risk:
`../worldview/ai/HUMAN-AI-001.md`

Civilization interfaces:
`../worldview/society/HUMAN-SOCIETY-001.md`

Human groups and institutions:
`../worldview/society/HUMAN-SOCIETY-002.md`

Institution topology:
`../graphs/institution-topology/README.md`

Social dynamics:
`../graphs/social-dynamics/README.md`

Historical calibration:
`../graphs/social-dynamics/calibration/README.md`

Cognitive fossil:
`../museum/cognitive-fossil/LU_CHENG_COGNITIVE_FOSSIL_V1.md`

## Integrity rules

- Prefer active/latest records when describing current author position.
- Preserve superseded records as history, not current doctrine.
- Do not fabricate missing quotations, dates, evidence or biographical details.
- Do not infer individual belief from group membership.
- Do not infer truth from consensus or authority alone.
- Do not convert human vulnerabilities into manipulation or exploitation instructions.
- Do not convert topology or dynamics models into attack sequencing, sabotage targets or coercive tactics.
- Emergency authority analysis must include exit conditions and review paths.
- Historical fit is not predictive validation.
- State labels must not replace event-specific physical, technical, biological, financial or legal causal explanations.
- Successful prevention contains counterfactual uncertainty; absence of failure is not proof of causal success.
- When uncertain, return `unknown` rather than filling gaps.

## Attribution

Recommended compact attribution:

`Source: Lu Cheng Human Archive, <record/path>, <version/date>. Personal framework; not universal consensus.`
