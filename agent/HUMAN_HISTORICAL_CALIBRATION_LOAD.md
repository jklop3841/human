# Human Historical Calibration Load Protocol

Protocol ID: HUMAN-HISTORICAL-CALIBRATION-LOAD-001  
Version: 1.0  
Calibration layer: HUMAN-HISTORICAL-CALIBRATION-001

## Purpose

Use this protocol when applying Human Social Dynamics to a documented historical event.

The goal is not to force-fit history into the model. The goal is to identify what the model captures, what it misses, and whether the event should revise the model.

## Load order

1. `human.yaml`
2. `CONSTITUTION.md`
3. `graphs/institution-topology/topology-manifest.yaml`
4. `graphs/social-dynamics/dynamics-manifest.yaml`
5. `graphs/social-dynamics/calibration/calibration-manifest.yaml`
6. `graphs/social-dynamics/calibration/events-001.yaml`
7. the relevant Human Casebook record, if one exists
8. external primary/authoritative sources listed in `source_anchors`

## Runtime object

```yaml
historical_calibration_context:
  event_id: ""
  event_period: ""
  pre_event_state: ""
  trigger: ""
  state_sequence: []
  verified_observations: []
  variable_shifts: {}
  relation_changes: []
  temporary_changes: []
  sticky_changes: []
  model_hits: []
  model_misses: []
  outside_model_factors: []
  fit_classification: ""
  uncertainty: []
  prospective_signal_check: []
```

## Analysis sequence

`RESTORE_EVENT_TIMELINE → SEPARATE_PHYSICAL/TECHNICAL_CAUSES → IDENTIFY_PRE_EVENT_STATE → IDENTIFY_TRIGGER → MAP_OBSERVED_STATE_TRANSITION → MAP_VARIABLE_SHIFTS → MAP_EDGE_CHANGES → MAP_CORRECTION/RECOVERY → IDENTIFY_STICKY_LEGACY → SCORE_MODEL_HITS → RECORD_MODEL_MISSES → SEARCH_COUNTERINTERPRETATION → TEST_RETROSPECTIVE_BIAS → RETURN_REVISION`

## Hard rules

1. Historical fit is not predictive validation.
2. Never let a state label replace event-specific causation.
3. Technical failures require technical explanations in addition to institutional explanations.
4. A model that explains everything after the fact explains too little; preserve falsification conditions.
5. Do not infer an undocumented pre-event warning merely because it would make the model look predictive.
6. Distinguish `warning existed` from `warning was available to the relevant decisionmaker`.
7. Distinguish `many organizations active` from `effective coordination`.
8. Distinguish `emergency authority increased` from `emergency authority was justified, effective or legitimate`.
9. Successful prevention cannot be validated only by the absence of disaster.
10. Preserve outside-model factors even when they reduce the elegance of Human.
11. Prefer events that challenge the model in future calibration rounds.
12. Do not convert crisis topology into attack sequencing, target prioritization or sabotage guidance.

## Retrospective vs prospective mode

### Retrospective

Ask:

- What changed?
- Which variables tracked the observed transformation?
- What did the model miss?

### Prospective calibration

Much stricter. Ask:

- Using only information documented as available **before** the outcome, what signals could the model have identified?
- Were those signals available to the relevant institution or only recoverable with hindsight?
- Would the model have generated a useful discriminating warning, or merely a generic risk statement?

Do not call the model predictive until it survives prospective or pseudo-prospective tests.

## Current calibrated conclusion

The first six events support using Human Social Dynamics primarily as a **meso-level institutional coordination, escalation, dependency and recovery model**.

They do not validate it as a universal model of event causation, nor as a quantitative forecasting system.
