# Human Groups and Institutions Load Protocol

protocol_id: HGI-LOAD-001  
version: 1.1.0  
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
9. `books/human-groups-institutions/collective-failure-patterns.yaml`
10. `books/human-groups-institutions/INSTITUTIONAL_DRIFT_FRAMEWORK.md`
11. `books/human-groups-institutions/institution-atlas.yaml`
12. For a named institution, load the matching category file under `books/human-groups-institutions/institutions/`.
13. `research/2026-09-human-groups-evidence.md`
14. `research/2026-09-institutional-drift-evidence.md`
15. Load full `BOOK.md` for extended reasoning.

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
    official_function: []
    protected_value: []
    real_world_permissions: []
    clients_or_subjects: []
    resource_constraints: []
    performance_metrics: []
    frontline_discretion: unknown
    information_asymmetry: unknown
    hierarchy_depth: unknown
    subject_exit_cost: unknown
    dirty_reality_forces: []
    likely_drift_patterns: []
    capture_or_corruption_evidence: []
    stabilizing_mechanisms: []
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
10. `IDENTIFY_INSTITUTION_ARCHETYPE` — locate the institution in `institution-atlas.yaml` and the relevant category file.
11. `SEPARATE_MISSION_FROM_BEHAVIOR` — record what the institution says it exists to do separately from observed outputs.
12. `MAP_PERMISSION` — identify what the institution can actually change: freedom, money, access, care, certification, information, infrastructure, identity, rules or force.
13. `MAP_SCARCITY` — identify limits in staff, time, money, beds, docket, equipment, attention, data or political capital.
14. `MAP_METRICS` — identify which measurable proxies affect promotion, funding, evaluation or legitimacy.
15. `MAP_FRONTLINE_DISCRETION` — identify the point where broad rules become case-by-case human decisions.
16. `MAP_HIERARCHY_FILTERING` — inspect whether bad news and edge cases survive upward reporting.
17. `MAP_SELF_PRESERVATION` — ask whether budget, jurisdiction, reputation or organizational survival has become an independent objective.
18. `MAP_EXTERNAL_CAPTURE` — inspect conflicts, lobbying, donor/client dependence, revolving doors and concentrated outside influence.
19. `CLASSIFY_DRIFT` — separate adaptive discretion, scarcity compression, metric substitution, information failure, capture and corruption.
20. `MAP_CORRECTION` — identify appeal, audit, dissent, competition, independent review, rotation, transparency and revision channels.
21. `CHECK_COLLECTIVE_INTELLIGENCE` — actively search for process gains, not only failure modes.
22. `CHECK_COUNTERMODEL` — ask whether selection effects, expertise, legitimate coordination, resource scarcity or simple incentives explain the behavior better.
23. `OUTPUT_UNKNOWNS` — if private attitudes, motives or internal data are unavailable, state that explicitly.

## Institutional drift classifier

```yaml
institutional_drift:
  adaptive_discretion:
    evidence: []
  scarcity_compression:
    evidence: []
  metric_substitution:
    evidence: []
  hierarchy_or_information_failure:
    evidence: []
  principal_agent_drift:
    evidence: []
  organizational_self_preservation:
    evidence: []
  external_capture:
    evidence: []
  corruption:
    evidence: []
```

Do not collapse these categories into one.

## Hard interpretive rules

- Group membership does not prove individual belief.
- Majority size does not prove independent evidence.
- Consensus does not prove truth.
- Minority status does not prove falsehood.
- Crowd size does not prove irrationality.
- Authority does not prove expertise.
- Expertise does not automatically prove legitimacy.
- Institutional behavior does not imply a single institutional mind.
- Mission statement does not prove operational behavior.
- Poor performance does not prove corruption.
- A performance metric does not prove mission success.
- Frontline deviation may be legitimate adaptation, not misconduct.
- Correlation across a network does not by itself prove social contagion.
- Groupthink is a heuristic diagnosis, not a default explanation.

## Output contract

```yaml
collective_assessment:
  object: ""
  object_type: ""
  core_structure: ""
  detected_mechanisms: []
  official_mission: []
  real_world_permissions: []
  resource_constraints: []
  proxy_metrics: []
  frontline_discretion: ""
  dirty_reality_forces: []
  likely_drift_patterns: []
  capture_or_corruption_status: unsupported|possible|supported|unknown
  collective_intelligence_conditions: []
  collective_failure_conditions: []
  authority_structure: []
  information_bottlenecks: []
  dissent_conditions: []
  responsibility_structure: []
  institutional_amplification: []
  correction_channels: []
  countermodels: []
  evidence: []
  unknowns: []
```

## Safety invariant

Use these mechanisms to understand, audit, explain and design transparent institutions.

Do not convert them into targeted manipulation, covert influence, agitation, deception, coercion, hatred, vulnerability exploitation, evasion of law enforcement, or operational sabotage against real institutions or groups.
