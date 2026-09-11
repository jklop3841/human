# Human Social Dynamics Load Protocol

Protocol version: 1.0  
System: HUMAN-SOCIAL-DYNAMICS-001

## Purpose

This protocol tells an Agent how to reason about time/state changes without treating the static institution graph as timeless.

## Load order

1. `human.yaml`
2. `CONSTITUTION.md`
3. `graphs/institution-topology/topology-manifest.yaml`
4. `graphs/institution-topology/nodes.yaml`
5. relevant static edges
6. `graphs/social-dynamics/dynamics-manifest.yaml`
7. `graphs/social-dynamics/state-types.yaml`
8. relevant domain overlay
9. relevant Human Casebook cases for calibration
10. current external evidence if making a real-world or present-day claim

## Runtime object

```yaml
social_dynamics_context:
  domain: ""
  jurisdiction: "generic | specific"
  time_window: ""
  inferred_state: []
  state_confidence: "low | medium | high | unknown"
  baseline_topology: []
  node_changes: []
  edge_changes: []
  drift_risks: []
  correction_opportunities: []
  reversible_changes: []
  sticky_changes: []
  exit_conditions: []
  unresolved_questions: []
```

## Analysis sequence

`ANCHOR_TIME → LOAD_STATIC_TOPOLOGY → CLASSIFY_STATE_OR_MIXED_STATE → MAP_STATE_VARIABLES → MAP_NODE_CHANGES → MAP_EDGE_CHANGES → MAP_DRIFT_VECTOR → MAP_CORRECTION_VECTOR → IDENTIFY_TEMPORARY_VS_STICKY_CHANGES → DEFINE_EXIT_CONDITIONS → CHECK_CASEBOOK → CHECK_JURISDICTION → RETURN_UNCERTAINTY`

## State classification rule

Never force a system into exactly one state.

Allowed outputs include:

- `NORMAL`
- `CRISIS`
- `CRISIS + REFORM`
- `EMERGENCY transitioning to RECOVERY`
- `unknown / insufficient evidence`

## Hard rules

1. Static topology is the baseline, not the current state.
2. State overlays are priors and question templates, not predictions.
3. Do not assign numeric transition probabilities unless externally supported.
4. `CRISIS` does not imply collapse.
5. `EMERGENCY` does not imply abuse or authoritarianism.
6. Expanded authority must be paired with exit conditions and review paths.
7. Faster information may reduce verification depth; treat speed and accuracy separately.
8. Recovery is not necessarily a return to the prior topology.
9. Crisis can amplify both failure and collective intelligence.
10. Temporary mechanisms may become sticky; identify which ones and why.
11. Specific legal/administrative claims require jurisdiction-specific evidence.
12. Do not translate dependency changes into attack sequencing, sabotage targets or coercive tactics.

## Historical calibration

Use existing Human Casebook material as calibration examples rather than universal templates:

- healthcare: Mid Staffordshire / Keystone ICU / public-health cases
- finance: SVB and other confidence/liquidity cases
- infrastructure: Texas 2021 / Katrina / Y2K contrast
- information: engagement ranking and crisis-information cases
- science: Publish or Perish / Human Genome Project
- high-risk coordination: Challenger / Apollo 13 / ASRS

The Agent must state whether it is using a case as:

- analogy
- partial structural match
- counterexample
- evidence-backed mechanism

Never collapse analogy into causation.

## Output format

For a dynamic-system answer, prefer:

1. **Baseline topology**
2. **Current/inferred state**
3. **What changed in nodes**
4. **What changed in edges**
5. **Drift risks**
6. **Correction opportunities**
7. **Exit conditions / recovery logic**
8. **Uncertainty and missing evidence**

## Constitutional constraint

The Human archive studies how societies operate and adapt. It must not be used to rank critical targets, optimize disruption, evade safeguards, or exploit emergency conditions.
