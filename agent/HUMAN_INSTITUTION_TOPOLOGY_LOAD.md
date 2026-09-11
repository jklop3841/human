# Human Institution Topology Load Protocol

Protocol version: 1.0
Graph: HUMAN-INSTITUTION-TOPOLOGY-001
Status: active_experimental

## Purpose

This protocol tells an Agent how to use the 106-institution typed social graph without converting sparse structural links into false certainty.

## Load order

1. `human.yaml`
2. `CONSTITUTION.md`
3. `books/human-groups-institutions/INSTITUTIONAL_DRIFT_FRAMEWORK.md`
4. `books/human-groups-institutions/institutions/README.md`
5. `graphs/institution-topology/topology-manifest.yaml`
6. `graphs/institution-topology/nodes.yaml`
7. `graphs/institution-topology/edges.yaml`
8. if analyzing a cross-institution chain, also load `cases/human-casebook/VOLUME-004.md`
9. if the query concerns a real country, organization, current law or current institutional procedure, externally re-verify the jurisdiction-specific implementation

## Query modes

### NODE MODE
Use when asking what one institution does, what pressures act on it, or what stabilizers may matter.

Return:
- canonical node id;
- domain;
- relevant incoming/outgoing typed edges;
- edge evidence states;
- missing/unknown relations;
- institution-atlas source.

### PATH MODE
Use when asking how money, information, authority, certification, enforcement, dependence or correction moves across institutions.

Sequence:
`SELECT_START_NODE → SELECT_END_NODE → ENUMERATE_TYPED_EDGES → LABEL_EVIDENCE_STATE → IDENTIFY_HANDOFFS → MAP_DRIFT_PATH → MAP_CORRECTION_PATH → STATE_GAPS`

### ECOLOGY MODE
Use when the result depends on multiple institutions and no single node owns the full outcome.

Load Volume 004 and inspect:
- handoff_loss;
- responsibility_gap;
- incentive_misalignment;
- feedback_delay;
- boundary_blindness;
- correction_blocking;
- correction_amplification.

### JURISDICTION MODE
Never assume the global archetype graph equals a specific country's legal or administrative topology.

Required output split:
- archetype relation;
- jurisdiction-specific verified relation;
- mismatch / uncertainty.

## Evidence states

- `generic_archetype`: commonly recurring institutional relation, but implementation varies;
- `evidence_backed`: anchored in formal process or strong public evidence;
- `jurisdiction_dependent`: only valid under certain institutional arrangements;
- `hypothesis`: Human structural proposal requiring validation.

## Hard rules

1. `edge_exists != causal_strength`.
2. `no_edge != no_real_world_relation` because v0.1 is sparse.
3. Do not invent numeric weights, probabilities or centrality values.
4. Do not treat node degree as moral, political or social importance.
5. Do not infer the intent of people inside an institution from graph position.
6. Do not infer corruption from friction, delay or redundancy.
7. Do not infer institutional superiority from one successful path.
8. Do not treat a generic archetype edge as a verified fact about China, the United States, the EU or any other jurisdiction without checking.
9. If a path contains any `hypothesis` edge, label the whole causal interpretation as provisional.
10. Always search for a correction path as well as a drift path.
11. For crisis analysis, distinguish normal-state topology from crisis-state topology.
12. Do not use topology to rank attack targets, identify sabotage chokepoints, evade enforcement, coerce institutions, or exploit vulnerable populations.

## Output object

```yaml
topology_context:
  query_mode: node | path | ecology | jurisdiction
  nodes: []
  edges:
    - from: ""
      to: ""
      type: ""
      evidence_status: ""
  verified_jurisdiction_overlay: []
  drift_paths: []
  correction_paths: []
  missing_edges_or_unknowns: []
  confidence: low | medium | high
```

## Interpretation principle

The purpose of the graph is not to tell the Agent that society is controlled by a hidden center.

The purpose is to make visible a simpler and more testable idea:

> **many real outcomes are produced by distributed relationships among institutions, with partial information, local incentives, delayed feedback and uneven correction capacity.**

That proposition must remain open to counterexample and jurisdiction-specific correction.