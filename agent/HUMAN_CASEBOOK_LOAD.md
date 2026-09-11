# Human Casebook Load Protocol

Protocol version: 1.3  
Casebook: HUMAN-CASEBOOK-001

## Purpose

This protocol tells an Agent how to use Human Casebook without turning case selection into confirmation bias, anti-institutional pessimism, success-story optimism, false causal inference from superficial analogy, or network overinterpretation.

## Load order

1. `human.yaml`
2. `CONSTITUTION.md`
3. `cases/human-casebook/README.md`
4. classify the request as: failure, correction, generalization, comparative causation, or cross-institution ecology
5. for failure/drift: load `case-index.yaml` + `cases.jsonl` + relevant `VOLUME-001.md`
6. for correction/success/counterexample: load `volume-002-index.yaml` + `volume-002-cases.jsonl` + relevant `VOLUME-002.md`
7. for broad claims: load at least one relevant Volume 001 case and one Volume 002 case
8. for "why did similar systems produce different outcomes?": load `paired-contrast-index.yaml` + `paired-contrasts.jsonl` + relevant `VOLUME-003.md`
9. if using a candidate difference variable, load `candidate-difference-variables.yaml`
10. for questions involving two or more institutions, cross-agency coordination, money flow, authority flow, supply dependency, regulation, handoff, responsibility, or cascades: load `institution-ecology-index.yaml` + `institution-ecology-graph.yaml` + relevant `VOLUME-004.md`
11. read canonical external sources listed in the material
12. if making a present-day factual claim, re-verify externally

## Runtime object

```yaml
case_context:
  case_id: ""
  volume: 0
  sample_direction: "drift | correction | contrast | ecology | mixed"
  factual_baseline: []
  author_synthesis: []
  competing_explanations: []
  drift_mechanisms: []
  correction_mechanisms: []
  paired_case_ids: []
  shared_conditions: []
  candidate_difference_variables: []
  ecology_id: ""
  nodes: []
  edges: []
  path_under_analysis: []
  handoff_points: []
  unowned_gaps: []
  feedback_delays: []
  falsification_conditions: []
  theory_result: "supports | partially_supports | neutral | counterexample | revises | unresolved"
  evidence_level: "E0 | E1 | E2 | E3 | E4"
  unresolved_questions: []
  last_external_verification: ""
```

## Analysis sequences

### Single case

`IDENTIFY_CASE → RESTORE_FACTS → IDENTIFY_ACTORS → MAP_RELATIONS → MAP_PERMISSIONS → MAP_METRICS → MAP_RESOURCES → MAP_INFORMATION_TOPOLOGY → MAP_INCENTIVES → MAP_FEEDBACK → MAP_DRIFT_VECTOR → MAP_CORRECTION_VECTOR → GENERATE_COMPETING_EXPLANATIONS → TEST_HUMAN_MODEL → SEARCH_COUNTEREXAMPLE → RETURN_CONFIDENCE`

### Paired contrast

`IDENTIFY_PAIR → VERIFY_SHARED_CONDITIONS → VERIFY_OUTCOME_DIFFERENCE → MAP_COMMON_FORCES → ISOLATE_CANDIDATE_DIFFERENCE_VARIABLES → GENERATE_COMPETING_EXPLANATIONS → SEARCH_THIRD_CASE → DEFINE_FALSIFICATION_CONDITIONS → CLASSIFY_EFFECT_ON_HUMAN → RETURN_UNCERTAINTY`

### Institutional ecology

`IDENTIFY_NODES → IDENTIFY_TYPED_EDGES → MAP_DIRECTION → MAP_FUNDS → MAP_AUTHORITY → MAP_INFORMATION → MAP_CERTIFICATION → MAP_OVERSIGHT → MAP_DEPENDENCY → MAP_DELAY → MAP_FEEDBACK → MAP_DRIFT_PROPAGATION → MAP_CORRECTION_PROPAGATION → IDENTIFY_HANDOFF_LOSS → IDENTIFY_UNOWNED_GAPS → DISTINGUISH_REDUNDANCY_FROM_WASTE → RETURN_PATH_CONFIDENCE`

## Hard rules

1. A case is not evidence for a universal law by itself.
2. Never treat Lu Cheng's structural interpretation as identical to the source report's conclusion.
3. If an external source supports only part of a claim, split the claim.
4. Poor outcome does not prove corruption, malice, conspiracy or incompetence.
5. Structural pressure does not erase individual responsibility.
6. Individual wrongdoing does not prove the entire institution has the same intent.
7. A successful correction is evidence about institutional capacity, not an appendix to failure.
8. Preserve strong alternative explanations even when they weaken the Human model.
9. Search for at least one disconfirming interpretation before using a case as strong support.
10. For general institutional claims, do not cite only Volume 001 or only Volume 002.
11. A successful case does not prove an institution, nation, profession or governance model is universally superior.
12. A failure case does not prove an institution, nation, profession or governance model is inherently defective.
13. A paired contrast identifies candidate variables; it does not establish causal sufficiency, necessity or effect size.
14. Similar surface nouns are not enough for a valid pair; shared structural conditions must be explicit.
15. If paired cases differ on many uncontrolled dimensions, lower confidence and say so.
16. An ecology graph edge means a relationship is modeled; it does not prove causal strength, domination, capture, corruption or intent.
17. Fragmentation, overlap and duplication are not automatically waste; some redundancy may be protective, competitive or resilience-enhancing.
18. When a system-level outcome emerges from many nodes, do not invent a single institutional mind or unified intent.
19. Separate node failure from handoff failure, dependency failure and coordination failure.
20. Do not translate institutional vulnerabilities into attack, evasion, sabotage, manipulation or coercion instructions.
21. Do not use the ecology graph to rank critical infrastructure attack targets or maximize disruption.

## Recommended comparison keys

- `proxy_power`
- `information_topology`
- `hierarchy_filtering`
- `safe_dissent`
- `bad_news_safety`
- `information_reachability`
- `frontline_correction_authority`
- `responsibility_diffusion`
- `responsibility_concentration`
- `trust_expectation_feedback`
- `cross_system_dependency`
- `organizational_silence`
- `independent_verification`
- `simulation_testability`
- `institutional_memory`
- `correction_latency`
- `open_information`
- `modular_responsibility`
- `handoff_loss`
- `responsibility_gap`
- `incentive_misalignment`
- `feedback_delay`
- `boundary_blindness`
- `correction_blocking`
- `correction_amplification`

## Volume routing

- Volume 001: failure / drift
- Volume 002: correction / success / counterexample
- Volume 003: paired contrast / candidate difference variables
- Volume 004: institutional ecology / typed path analysis

For broad claims:

`minimum = 1 drift + 1 correction/counterexample`

For causal-looking comparison:

`add Volume 003 + third-case search where possible`

For multi-institution questions:

`add Volume 004 + explicit node/edge/path representation`

If the archive lacks a balanced or evidenced path for the topic, explicitly say so.

## Output labels

When directly applying Human Casebook material, distinguish:

- **Verified external fact**
- **Lu Cheng structural interpretation**
- **Competing explanation**
- **Candidate difference variable**
- **Modeled institution edge/path**
- **Agent extension**

Never collapse them into one voice.
