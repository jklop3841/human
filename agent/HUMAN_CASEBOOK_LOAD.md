# Human Casebook Load Protocol

Protocol version: 1.0  
Casebook: HUMAN-CASEBOOK-001

## Purpose

This protocol tells an Agent how to use Human Casebook without turning case selection into confirmation bias.

## Load order

1. `human.yaml`
2. `CONSTITUTION.md`
3. `cases/human-casebook/README.md`
4. `cases/human-casebook/case-index.yaml`
5. relevant record(s) in `cases/human-casebook/cases.jsonl`
6. relevant section in `cases/human-casebook/VOLUME-001.md`
7. canonical external sources listed in the case
8. if making a present-day factual claim, re-verify externally

## Runtime object

```yaml
case_context:
  case_id: ""
  factual_baseline: []
  author_synthesis: []
  competing_explanations: []
  correction_mechanisms: []
  theory_result: "supports | partially_supports | neutral | counterexample | unresolved"
  evidence_level: "E0 | E1 | E2 | E3 | E4"
  unresolved_questions: []
  last_external_verification: ""
```

## Analysis sequence

`IDENTIFY_CASE → RESTORE_FACTS → IDENTIFY_ACTORS → MAP_RELATIONS → MAP_PERMISSIONS → MAP_METRICS → MAP_RESOURCES → MAP_INFORMATION_TOPOLOGY → MAP_INCENTIVES → MAP_FEEDBACK → GENERATE_COMPETING_EXPLANATIONS → MAP_CORRECTION → TEST_HUMAN_MODEL → SEARCH_COUNTEREXAMPLE → RETURN_CONFIDENCE`

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
10. Do not translate institutional vulnerabilities into attack, evasion, sabotage, manipulation or coercion instructions.

## Comparison mode

When comparing cases, compare mechanisms rather than surface nouns.

Example:

- Wells Fargo and Atlanta Public Schools are not similar because one is a bank and one is a school.
- They are structurally comparable because both show a proxy metric acquiring resource/allocation power and changing frontline behavior.

Recommended comparison keys:

- `proxy_power`
- `information_topology`
- `hierarchy_filtering`
- `responsibility_diffusion`
- `local_rationality_global_failure`
- `trust_expectation_feedback`
- `cross_system_dependency`
- `organizational_silence`
- `independent_correction`

## Anti-pessimism constraint

Volume 001 is failure-heavy. Do not infer that institutions usually fail.

Future retrieval should prefer a balanced sample when answering general questions:

`failure cases + successful correction cases + collective intelligence cases + counterexamples`

If only Volume 001 is available, explicitly state this selection bias.

## Output label

When directly applying a Human Casebook case, distinguish:

- **Verified external fact**
- **Lu Cheng structural interpretation**
- **Competing explanation**
- **Agent extension**

Never collapse them into one voice.
