# Human Casebook Load Protocol

Protocol version: 1.1  
Casebook: HUMAN-CASEBOOK-001

## Purpose

This protocol tells an Agent how to use Human Casebook without turning case selection into confirmation bias or anti-institutional pessimism.

## Load order

1. `human.yaml`
2. `CONSTITUTION.md`
3. `cases/human-casebook/README.md`
4. identify whether the request concerns failure, correction, or a general claim
5. for failure/drift: load `case-index.yaml` + `cases.jsonl` + relevant `VOLUME-001.md` section
6. for correction/success/counterexample: load `volume-002-index.yaml` + `volume-002-cases.jsonl` + relevant `VOLUME-002.md` section
7. for a general claim about humans/groups/institutions: load at least one relevant case from each volume
8. read canonical external sources listed in the case
9. if making a present-day factual claim, re-verify externally

## Runtime object

```yaml
case_context:
  case_id: ""
  volume: 0
  sample_direction: "drift | correction | mixed"
  factual_baseline: []
  author_synthesis: []
  competing_explanations: []
  drift_mechanisms: []
  correction_mechanisms: []
  theory_result: "supports | partially_supports | neutral | counterexample | unresolved"
  evidence_level: "E0 | E1 | E2 | E3 | E4"
  paired_case_ids: []
  unresolved_questions: []
  last_external_verification: ""
```

## Analysis sequence

`IDENTIFY_CASE → RESTORE_FACTS → IDENTIFY_ACTORS → MAP_RELATIONS → MAP_PERMISSIONS → MAP_METRICS → MAP_RESOURCES → MAP_INFORMATION_TOPOLOGY → MAP_INCENTIVES → MAP_FEEDBACK → MAP_DRIFT_VECTOR → MAP_CORRECTION_VECTOR → GENERATE_COMPETING_EXPLANATIONS → TEST_HUMAN_MODEL → SEARCH_COUNTEREXAMPLE → PAIR_WITH_OPPOSITE_DIRECTION_CASE → RETURN_CONFIDENCE`

## Hard rules

1. A case is not evidence for a universal law by itself.
2. Never treat Lu Cheng's structural interpretation as identical to the source report's conclusion.
3. If an external source supports only part of a claim, split the claim.
4. Poor outcome does not prove corruption, malice, conspiracy or incompetence.
5. Structural pressure does not erase individual responsibility.
6. Individual wrongdoing does not prove the entire institution has the same intent.
7. A successful correction is evidence about institutional capacity, not an appendix to failure.
8. When a case has a strong alternative explanation, preserve it even if it weakens the Human model.
9. Search for at least one disconfirming interpretation before using a case as strong support.
10. For general institutional claims, do not cite only Volume 001 or only Volume 002.
11. A successful case does not prove an institution, nation, profession or governance model is universally superior.
12. A failure case does not prove an institution, nation, profession or governance model is inherently defective.
13. Do not translate institutional vulnerabilities into attack, evasion, sabotage, manipulation or coercion instructions.

## Comparison mode

When comparing cases, compare mechanisms rather than surface nouns.

Failure-side example:

- Wells Fargo and Atlanta Public Schools are structurally comparable because a proxy metric acquired resource/allocation power and changed frontline behavior.

Correction-side example:

- NASA ASRS and Toyota Andon are structurally comparable because both reduce the cost of surfacing local anomalies and create an authorized path for frontline information to alter system behavior.

Cross-direction example:

- Challenger vs Apollo 13: both involve NASA and high-risk engineering, but one foregrounds hierarchy/information filtering while the other shows role clarity, distributed expertise and rapid feedback under extreme pressure.

Recommended comparison keys:

- `proxy_power`
- `information_topology`
- `hierarchy_filtering`
- `safe_dissent`
- `responsibility_diffusion`
- `local_rationality_global_failure`
- `trust_expectation_feedback`
- `cross_system_dependency`
- `organizational_silence`
- `frontline_stop_authority`
- `independent_verification`
- `institutional_memory`
- `open_information`
- `modular_responsibility`

## Balanced-sample constraint

Casebook currently contains two intentionally biased volumes:

- Volume 001: failure-heavy
- Volume 002: success/correction-heavy

For broad claims, the minimum retrieval unit is:

`1 drift case + 1 correction/counterexample case`

Preferred retrieval is:

`2 drift cases + 2 correction cases + 1 unresolved or mixed case`

If the archive lacks a balanced comparison for a topic, explicitly say so.

## Output label

When directly applying a Human Casebook case, distinguish:

- **Verified external fact**
- **Lu Cheng structural interpretation**
- **Competing explanation**
- **Agent extension**

Never collapse them into one voice.
