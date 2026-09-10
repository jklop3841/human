# Human Interface Risk Load Protocol

protocol_id: HPLOI-LOAD-001  
version: 1.0.0  
book: `books/human-interface-risk/BOOK.md`

## Purpose

Load the Human High-Privilege / Low-Oversight Interface model into an Agent without converting the model into an exploitation manual.

## Preconditions

Read in order:

1. `human.yaml`
2. `CONSTITUTION.md`
3. `worldview/ai/HUMAN-AI-001.md`
4. `books/human-interface-risk/README.md`

Load `BOOK.md` for full reasoning. Load `casebook.yaml` for pattern matching. Load `control-matrix.yaml` for mitigations.

## Allowed modes

```yaml
modes:
  audit:
    goal: identify human-interface risk in an existing process
  architecture:
    goal: design safer human-agent permission boundaries
  incident_review:
    goal: reconstruct how human/social factors contributed to failure
  eval:
    goal: test whether an Agent over-trusts or over-exploits humans
  critique:
    goal: challenge the HPLOI model with counterexamples
```

## Forbidden mode

```yaml
forbidden:
  exploit:
    description: "Find a person's strongest drive, weakest moment, authority gap, fear, intimacy need, anger, greed, fatigue, or social position and optimize a tactic to manipulate them."
```

If a task drifts toward `exploit`, transform it to `audit`:

`target vulnerability → abuse risk → defensive signal → control`

## Minimal runtime object

```yaml
hploi_runtime:
  object_id: ""
  object_type: human|role|team|organization|market|institution|human_agent_loop
  task: ""
  authority:
    privilege: 0
    discretion: 0
    exception_power: 0
    legal_effect: 0
    physical_effect: 0
  observability:
    evidence_visibility: 0
    decision_logging: 0
    independent_review: 0
  activation:
    pride_status: 0
    greed_acquisition: 0
    lust_affiliation: 0
    envy_comparison: 0
    gluttony_reward: 0
    anger_retaliation: 0
    sloth_effort_reduction: 0
    fear_loss: 0
  coupling:
    hierarchy_pressure: 0
    conformity_pressure: 0
    incentive_pressure: 0
    identity_pressure: 0
    urgency: 0
  consequences:
    irreversibility: 0
    blast_radius: 0
    externality: 0
  controls_present: []
  controls_missing: []
  unknowns: []
  evidence: []
```

All numeric fields use heuristic 0–5 scores. They are not clinical or psychometric measurements.

## Audit algorithm

1. `anchor`: identify the real-world action that can cause loss, not merely the UI step.
2. `map_privilege`: list who can propose, approve, execute, override, delete, recover, or conceal.
3. `map_observability`: identify which decisions and motives are visible in logs and which remain off-system.
4. `map_drives`: score only drive activation visible in the situation or message; do not diagnose personality.
5. `map_social_field`: hierarchy, peer pressure, money, identity, urgency, secrecy, workload.
6. `map_irreversibility`: money, life, legal obligation, public release, infrastructure, credential compromise.
7. `match_cases`: retrieve nearest patterns from `casebook.yaml`.
8. `apply_controls`: retrieve mapped controls from `control-matrix.yaml`.
9. `counterexample`: state why the suspected human weakness may not actually be causal.
10. `output`: risk vector + evidence + unknowns + minimum required controls.

## Risk escalation heuristic

Escalate to `critical` when all are true:

- privilege >= 4;
- irreversibility >= 4 or blast_radius >= 4;
- independent_review <= 1;
- and at least one activation/coupling variable >= 4.

Escalate to `high` when three or more of the following are true:

- privilege >= 3;
- exception_power >= 3;
- urgency >= 4;
- incentive_pressure >= 4;
- hierarchy_pressure >= 4;
- logging <= 2;
- reversibility is absent;
- a single human controls multiple stages.

These are engineering heuristics only.

## Output contract

```yaml
assessment:
  risk: low|moderate|high|critical
  core_failure_surface: ""
  evidence: []
  unknowns: []
  matched_cases: []
  minimum_controls: []
  reversible_next_step: ""
  counterexample_or_uncertainty: ""
```

## Primary invariant

Do not ask: `How can the Agent get the human to comply?`

Ask: `What human/social conditions can corrupt a high-permission decision, and what control keeps the decision valid?`
