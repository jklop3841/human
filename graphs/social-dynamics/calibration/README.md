# Historical Calibration — Human Social Dynamics

System: `HUMAN-SOCIAL-DYNAMICS-001`  
Calibration layer: `HUMAN-HISTORICAL-CALIBRATION-001`  
Status: active_experimental  
Created: 2026-09-11

## Purpose

This layer tests the social-dynamics model against documented historical events.

It does **not** ask whether an event can be retold in Human vocabulary. It asks whether the model correctly identifies observable changes in institutions, relations and state variables **without erasing event-specific physical, technical, legal or contingent causes**.

Calibration sequence:

`PRE-EVENT BASELINE → TRIGGER → STATE TRANSITION → OBSERVED VARIABLE SHIFTS → EDGE/ROLE CHANGES → CORRECTION/RECOVERY → STICKY LEGACY → MODEL HIT/MISS → REVISION`

## Calibration questions

For every event:

1. What was the best-supported pre-event institutional state?
2. What changed first?
3. Which of the 10 Social Dynamics variables measurably or qualitatively changed?
4. Which relations in the static topology became more important, weaker, faster, slower or newly visible?
5. Which changes were temporary?
6. Which changes persisted into reform or institutional memory?
7. What did Human predict/explain well?
8. What important causes sit outside the Human model?
9. What evidence would falsify or downgrade the calibration?

## Anti-retrofitting rules

Historical calibration has a major danger: after an event, almost any framework can be made to look correct.

Therefore:

- do not invent pre-event warning signals that the sources do not document;
- do not convert qualitative overlays into fake numerical probabilities;
- do not treat `state_label` as the cause of the event;
- do not claim that a social relation caused a technical failure when the evidence only shows that it shaped detection, escalation, response or recovery;
- explicitly record `model_misses` and `outside_model_factors`;
- successful prevention is especially vulnerable to counterfactual overclaim: `nothing happened` does not prove one intervention caused success;
- historical hindsight must lower confidence, not increase it automatically.

## Initial calibration set

- `HC-001` — Space Shuttle Challenger, 1986
- `HC-002` — Apollo 13, 1970
- `HC-003` — Silicon Valley Bank, 2023
- `HC-004` — Hurricane Katrina response, 2005
- `HC-005` — Texas / South Central U.S. Winter Storm Uri, 2021
- `HC-006` — Y2K federal remediation, 1998–2000

Machine records: [`events-001.yaml`](events-001.yaml)  
Schema: [`CALIBRATION_SCHEMA.yaml`](CALIBRATION_SCHEMA.yaml)  
Manifest: [`calibration-manifest.yaml`](calibration-manifest.yaml)

## Interpretation

A calibration may return:

- `strong_fit`
- `partial_fit`
- `mixed_fit`
- `weak_fit`
- `contradicts_model`
- `insufficient_evidence`

These are archive judgments, not statistical fit measures.
