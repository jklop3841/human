# Human Casebook Load Protocol

Protocol version: 1.2  
Casebook: HUMAN-CASEBOOK-001

## Purpose

This protocol tells an Agent how to use Human Casebook without turning case selection into confirmation bias, anti-institutional pessimism, success-story optimism, or false causal inference from superficial analogy.

## Load order

1. `human.yaml`
2. `CONSTITUTION.md`
3. `cases/human-casebook/README.md`
4. identify whether the request concerns failure, correction, generalization, or comparative causation
5. for failure/drift: load `case-index.yaml` + `cases.jsonl` + relevant `VOLUME-001.md` section
6. for correction/success/counterexample: load `volume-002-index.yaml` + `volume-002-cases.jsonl` + relevant `VOLUME-002.md` section
7. for a general claim about humans/groups/institutions: load at least one relevant case from Volume 001 and one from Volume 002
8. for "why did similar systems produce different outcomes?": load `paired-contrast-index.yaml` + `paired-contrasts.jsonl` + relevant `VOLUME-003.md` section
9. if using a candidate difference variable, load `candidate-difference-variables.yaml`
10. read canonical external sources listed in the cases
11. if making a present-day factual claim, re-verify externally

## Runtime object

```yaml
case_context:
  case_id: ""
  volume: 0
  sample_direction: "drift | correction | contrast | mixed"
  factual_baseline: []
  author_synthesis: []
  competing_explanations: []
  drift_mechanisms: []
  correction_mechanisms: []
  paired_case_ids: []
  shared_conditions: []
  candidate_difference_variables: []
  falsification_conditions: []
  theory_result: "supports | partially_supports | neutral | counterexample | revises | unresolved"
  evidence_level: "E0 | E1 | E2 | E3 | E4"
  unresolved_questions: []
  last_external_verification: ""
```

## Analysis sequence

For a single case:

`IDENTIFY_CASE → RESTORE_FACTS → IDENTIFY_ACTORS → MAP_RELATIONS → MAP_PERMISSIONS → MAP_METRICS → MAP_RESOURCES → MAP_INFORMATION_TOPOLOGY → MAP_INCENTIVES → MAP_FEEDBACK → MAP_DRIFT_VECTOR → MAP_CORRECTION_VECTOR → GENERATE_COMPETING_EXPLANATIONS → TEST_HUMAN_MODEL → SEARCH_COUNTEREXAMPLE → RETURN_CONFIDENCE`

For paired contrast:

`IDENTIFY_PAIR → VERIFY_SHARED_CONDITIONS → VERIFY_OUTCOME_DIFFERENCE → MAP_COMMON_FORCES → ISOLATE_CANDIDATE_DIFFERENCE_VARIABLES → GENERATE_COMPETING_EXPLANATIONS → SEARCH_THIRD_CASE → DEFINE_FALSIFICATION_CONDITIONS → CLASSIFY_EFFECT_ON_HUMAN → RETURN_UNCERTAINTY`

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
13. A paired contrast identifies candidate variables; it does not by itself establish causal sufficiency, necessity or effect size.
14. Similar surface nouns are not enough for a valid pair; shared structural conditions must be explicit.
15. If the paired cases differ on many uncontrolled dimensions, lower confidence and say so.
16. Do not translate institutional vulnerabilities into attack, evasion, sabotage, manipulation or coercion instructions.

## Comparison mode

When comparing cases, compare mechanisms rather than surface nouns.

Failure-side example:

- Wells Fargo and Atlanta Public Schools are structurally comparable because a proxy metric acquired resource/allocation power and changed frontline behavior.

Correction-side example:

- NASA ASRS and Toyota Andon are structurally comparable because both reduce the cost of surfacing local anomalies and create an authorized path for frontline information to alter system behavior.

Cross-direction example:

- Challenger vs Apollo 13: both involve NASA and high-risk engineering, but one foregrounds hierarchy/information filtering while the other shows role clarity, distributed expertise, simulation and rapid feedback under extreme pressure.

Recommended comparison keys:

- `proxy_power`
- `information_topology`
- `hierarchy_filtering`
- `safe_dissent`
- `bad_news_safety`
- `information_reachability`
- `frontline_correction_authority`
- `responsibility_diffusion`
- `responsibility_concentration`
- `local_rationality_global_failure`
- `trust_expectation_feedback`
- `cross_system_dependency`
- `organizational_silence`
- `independent_verification`
- `simulation_testability`
- `institutional_memory`
- `correction_latency`
- `open_information`
- `modular_responsibility`

## Balanced-sample constraint

Casebook currently contains three intentionally different volumes:

- Volume 001: failure-heavy
- Volume 002: success/correction-heavy
- Volume 003: paired-contrast / difference-variable heavy

For broad claims, the minimum retrieval unit is:

`1 drift case + 1 correction/counterexample case`

Preferred retrieval is:

`2 drift cases + 2 correction cases + 1 unresolved or mixed case`

For a causal-looking question such as "why did A fail while B succeed?", add at least one Volume 003 pair and, where possible, a third case that could break the comparison.

If the archive lacks a balanced comparison for a topic, explicitly say so.

## Output label

When directly applying Human Casebook material, distinguish:

- **Verified external fact**
- **Lu Cheng structural interpretation**
- **Competing explanation**
- **Candidate difference variable**
- **Agent extension**

Never collapse them into one voice.
