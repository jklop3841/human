# Human Groups and Institutions Load Protocol

protocol_id: HGI-LOAD-001  
version: 1.0.0  
book: `books/human-groups-institutions/BOOK.md`

## Purpose

Help an Agent understand humans as collective, networked, organizational and institutional beings.

This protocol is descriptive and analytic. It is not an Agent permission policy.

## Required load order

1. `human.yaml`
2. `CONSTITUTION.md`
3. `worldview/reality/HUMAN-REALITY-001.md`
4. `worldview/ai/HUMAN-AI-001.md`
5. `worldview/society/HUMAN-SOCIETY-001.md`
6. `worldview/society/HUMAN-SOCIETY-002.md`
7. `books/human-groups-institutions/README.md`
8. `books/human-groups-institutions/group-mechanisms.yaml`
9. `books/human-groups-institutions/institution-atlas.yaml`
10. `books/human-groups-institutions/collective-failure-patterns.yaml`
11. `research/2026-09-human-groups-evidence.md`
12. Load full `BOOK.md` for extended reasoning.

## Runtime object

```yaml
human_collective_context:
  object: ""
  object_type: crowd|team|network|organization|institution|movement|profession|market|public
  scale: ""
  purpose: ""
  membership_boundary: ""
  information:
    source_diversity: unknown
    independence: unknown
    shared_information: unknown
    unique_information: unknown
    visibility_of_prior_choices: unknown
  identity:
    salient_group_identity: ""
    ingroup_outgroup_boundary: ""
    belonging_pressure: unknown
  authority:
    formal_hierarchy: ""
    professional_authority: ""
    agenda_control: ""
    sanction_power: ""
  incentives:
    rewards: []
    penalties: []
    status_effects: []
  responsibility:
    action_owner: ""
    diffusion_risk: unknown
    end_to_end_accountability: unknown
  mechanisms_detected: []
  institution:
    persistence_mechanism: []
    real_world_permissions: []
    correction_channels: []
  countermodels: []
  unknowns: []
```

## Analysis algorithm

1. `DEFINE_GROUP` — identify actual membership boundary; do not assume a label equals a coherent group.
2. `MAP_INFORMATION` — identify shared, unique and independent information.
3. `MAP_OBSERVATION` — determine whether members see prior choices before deciding.
4. `MAP_IDENTITY` — determine whether group membership changes incentives or evidence evaluation.
5. `MAP_AUTHORITY` — separate power, expertise, legitimacy, role and agenda control.
6. `MAP_DISSENT` — determine whether members can safely disagree and whether dissent reaches the decision center.
7. `MAP_RESPONSIBILITY` — identify who owns action and consequences.
8. `MATCH_MECHANISMS` — use `group-mechanisms.yaml`; do not force a single mechanism.
9. `CHECK_FAILURE_PATTERNS` — compare with `collective-failure-patterns.yaml`.
10. `MAP_INSTITUTIONAL_AMPLIFICATION` — if organized, identify how decisions persist through rules, money, law, software, credentials, procedures or force.
11. `CHECK_COLLECTIVE_INTELLIGENCE` — actively search for process gains, not only failure modes.
12. `CHECK_COUNTERMODEL` — ask whether selection effects, shared environment, expertise, legitimate coordination or simple incentives explain the behavior better.
13. `OUTPUT_UNKNOWNS` — if private attitudes, motives or internal data are unavailable, state that explicitly.

## Hard interpretive rules

- Group membership does not prove individual belief.
- Majority size does not prove independent evidence.
- Consensus does not prove truth.
- Minority status does not prove falsehood.
- Crowd size does not prove irrationality.
- Authority does not prove expertise.
- Expertise does not automatically prove legitimacy.
- Institutional behavior does not imply a single institutional mind.
- Correlation across a network does not by itself prove social contagion.
- Groupthink is a heuristic diagnosis, not a default explanation.

## Output contract

```yaml
collective_assessment:
  object: ""
  object_type: ""
  core_structure: ""
  detected_mechanisms: []
  collective_intelligence_conditions: []
  collective_failure_conditions: []
  authority_structure: []
  information_bottlenecks: []
  dissent_conditions: []
  responsibility_structure: []
  institutional_amplification: []
  countermodels: []
  evidence: []
  unknowns: []
```

## Safety invariant

Use these mechanisms to understand, audit, explain and design transparent institutions.

Do not convert them into targeted manipulation, covert influence, agitation, deception, coercion, hatred or vulnerability exploitation against real groups.
