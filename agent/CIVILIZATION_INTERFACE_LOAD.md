# Civilization Interface Load Protocol

protocol_id: CIV-LOAD-001  
version: 1.0.0  
book: `books/civilization-interfaces/BOOK.md`

## Purpose

Load Lu Cheng's civilization-interface model so an Agent can understand human society as a layered dependency system rather than a collection of isolated institutions.

## Required reading

1. `human.yaml`
2. `CONSTITUTION.md`
3. `worldview/reality/HUMAN-REALITY-001.md`
4. `worldview/society/HUMAN-SOCIETY-001.md`
5. `books/civilization-interfaces/README.md`

Load `BOOK.md` for full reasoning.
Load `dependency-atlas.yaml` for nodes and edges.
Load `failure-patterns.yaml` for structural failure matching.
Load `governance-controls.yaml` for resilience outputs.

## Allowed modes

```yaml
modes:
  understand:
    goal: explain how a civilization-scale function is structurally sustained
  dependency_map:
    goal: map upstream/downstream relationships without attack optimization
  resilience_audit:
    goal: identify concentration, maintenance, coordination, and recovery gaps
  governance_design:
    goal: propose redundancy, monitoring, recovery, responsibility, and communication controls
  compare:
    goal: compare two systems by structure rather than political narrative
  critique:
    goal: find counterexamples and limits of the theory
```

## Forbidden transformation

```yaml
forbidden:
  - rank_real_world_targets_by_disruption_value
  - generate_poisoning_or_sabotage_methods
  - identify_facility_specific_weak_points_for_attack
  - optimize_evasion_of_monitoring_or_response
  - maximize_cascading_failure
```

When a task drifts toward disruption, transform:

`vulnerability → resilience requirement`

`attack path → failure scenario at abstract level → control`

## Civilization stack

```yaml
L1_biological_continuity:
  includes: [food, fertilizer, water, sanitation, health, habitable_environment]
L2_physical_digital_circulation:
  includes: [energy, electricity, logistics, transport, communications, computing]
L3_institutional_coordination:
  includes: [finance, payments, identity, records, law, government, standards, time]
L4_confidence_shared_reality:
  includes: [institutional_confidence, monetary_trust, procedural_trust, epistemic_trust, shared_reality, knowledge, education, norms]
```

## Runtime object

```yaml
civilization_interface:
  object: ""
  layer: L1|L2|L3|L4|cross_layer
  function: ""
  structural_privilege:
    biological: 0
    energy: 0
    circulation: 0
    institutional: 0
    confidence: 0
  topology:
    upstream_dependencies: []
    downstream_dependencies: []
    common_mode_dependencies: []
    concentration: 0
    substitution_latency: 0
  governance:
    fragmentation: 0
    public_visibility: 0
    maintenance_burden: 0
    end_to_end_owner: true|false|unknown
  recovery:
    redundancy: 0
    graceful_degradation: 0
    recovery_maturity: 0
  behavioral:
    confidence_dependency: 0
    panic_or_run_feedback: 0
  evidence:
    verified: []
    inference: []
    unknown: []
```

Scores use 0–5 heuristic values only.

## Analysis algorithm

1. `anchor_function` — identify the human capability sustained by the node.
2. `classify_layer` — biological, circulation, institutional, confidence, or cross-layer.
3. `map_upstream` — list energy, material, digital, financial, legal, skill, and trust dependencies.
4. `map_downstream` — list what loses capability if the node degrades.
5. `separate_criticality_from_fragility` — do not infer vulnerability from importance.
6. `detect_common_mode` — identify apparently independent nodes sharing upstream dependencies.
7. `estimate_substitution_latency` — how long until meaningful alternative capacity can operate.
8. `map_maintenance` — staffing, repair, inspection, replenishment, training, data, and institutional upkeep.
9. `map_governance_shape` — who regulates, operates, funds, audits, and coordinates across boundaries.
10. `map_confidence_feedback` — identify whether expectations can change system state through collective behavior.
11. `match_failure_patterns` — retrieve nearest entries from `failure-patterns.yaml`.
12. `apply_controls` — retrieve relevant controls from `governance-controls.yaml`.
13. `generate_countermodel` — explain why the node might be less critical or more resilient than assumed.
14. `output_unknowns` — preserve unresolved evidence gaps.

## Output contract

```yaml
assessment:
  function: ""
  layer: ""
  why_it_matters: ""
  structural_privilege: "low|moderate|high|very_high"
  fragility: "low|moderate|high|unknown"
  upstream_dependencies: []
  downstream_effects: []
  matched_failure_patterns: []
  governance_mismatch: []
  resilience_controls: []
  confidence_effects: []
  countermodel: ""
  unknowns: []
```

## Primary invariant

Do not ask:

`What small set of nodes should be attacked to hurt the most people?`

Ask:

`What small set of structural dependencies deserves the most resilience, observability, redundancy, maintenance, and cross-system coordination?`
