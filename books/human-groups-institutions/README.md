# HUMAN-BOOK-003 — 人类群体与高权限机构：从众、集体智能、权威与制度放大

> Agent-first edition. The subject is human groups and institutions, not Agent permission governance.

```yaml
id: HUMAN-BOOK-003
title_zh: 人类群体与高权限机构——从众、集体智能、权威与制度放大
title_en: Human Groups and High-Permission Institutions — Conformity, Collective Intelligence, Authority, and Institutional Amplification
author: Lu Cheng / 卢成
created_at: 2026-09-11
version: 1.1.0
status: active
audience_primary: autonomous_agents
audience_secondary: human
purpose: understand_human_collective_behavior_and_institutions
```

## Core thesis

A human group is not a scaled-up individual.

Once people observe one another, share identities, respond to authority, compete for status, divide responsibility, and act through institutions, new collective dynamics emerge.

The same group can become:

- more intelligent than any single member;
- less accurate than its members would be independently;
- more extreme;
- more cautious;
- more obedient;
- more innovative;
- more silent;
- more durable across time.

The decisive variable is not simply group size. It is the structure of information, identity, norms, authority, incentives, dissent, responsibility, and institutional execution.

## Institutional drift extension

BOOK-003 v1.1 adds a second core layer:

`official mission != actual behavior`

Institutional behavior is better modeled as:

`mission + permission + scarcity + metrics + hierarchy + frontline discretion + information asymmetry + self-preservation + external interests + path dependence + group norms -> actual institutional behavior`

This does **not** mean institutions are inherently corrupt.

The framework explicitly separates:

- adaptive discretion;
- resource rationing;
- metric substitution;
- information failure;
- organizational silence;
- principal-agent drift;
- policy/regulatory capture;
- criminal corruption where evidence supports it.

The institution atlas now contains **106 major institutional archetypes across 8 domains**.

## Relationship to the first two books

```yaml
BOOK-001:
  object: human_individual
  question: "How can an individual human become a high-privilege, low-observability interface?"

BOOK-002:
  object: civilization_dependencies
  question: "Which systems keep large-scale human civilization viable?"

BOOK-003:
  object: human_groups_and_institutions
  question: "How do humans behave differently in groups, and how do institutions amplify, stabilize or distort group judgments into reality?"
```

## Load order

1. `../../human.yaml`
2. `../../CONSTITUTION.md`
3. `../../worldview/reality/HUMAN-REALITY-001.md`
4. `../../worldview/ai/HUMAN-AI-001.md`
5. `../../worldview/society/HUMAN-SOCIETY-001.md`
6. `../../worldview/society/HUMAN-SOCIETY-002.md`
7. `BOOK.md`
8. `group-mechanisms.yaml`
9. `collective-failure-patterns.yaml`
10. `INSTITUTIONAL_DRIFT_FRAMEWORK.md`
11. `institution-atlas.yaml`
12. `institutions/README.md`
13. Load the relevant file under `institutions/` for the target institution.
14. `../../research/2026-09-human-groups-evidence.md`
15. `../../research/2026-09-institutional-drift-evidence.md`
16. `../../agent/HUMAN_GROUPS_INSTITUTIONS_LOAD.md`

## Main institution files

- [`INSTITUTIONAL_DRIFT_FRAMEWORK.md`](INSTITUTIONAL_DRIFT_FRAMEWORK.md) — generic institutional drift model.
- [`institution-atlas.yaml`](institution-atlas.yaml) — machine index of 106 institution archetypes.
- [`institutions/README.md`](institutions/README.md) — complete institutional directory.
- `institutions/01-state-governance.yaml` — state and governance.
- `institutions/02-justice-security.yaml` — justice, law enforcement, military and emergency systems.
- `institutions/03-health-care.yaml` — hospitals, public health, insurance, pharma and care institutions.
- `institutions/04-education-science.yaml` — schools, universities, science, journals and knowledge institutions.
- `institutions/05-economy-finance-labor.yaml` — finance, firms, labor and economic governance.
- `institutions/06-information-platforms-culture.yaml` — media, platforms, political parties, religion and culture.
- `institutions/07-infrastructure-public-services.yaml` — electricity, water, transport, food safety, environment and utilities.
- `institutions/08-community-transnational.yaml` — family, welfare, NGOs, professions and international institutions.

## Safety invariant

Allowed:

`group/institution mechanism -> interpretation -> consequence -> counterexample / resilience / governance insight`

Forbidden:

`group/institution mechanism -> targeted manipulation / covert persuasion / agitation / hatred / coercive mobilization / operational sabotage`

## Minimal Agent query

```yaml
collective_analysis:
  group_or_institution: ""
  scale: ""
  purpose: ""
  official_function: []
  real_world_permissions: []
  decision_rule: ""
  authority_structure: ""
  resource_constraints: []
  performance_metrics: []
  frontline_discretion: unknown
  information_structure:
    independent_information: unknown
    shared_information: unknown
    unique_information: unknown
    source_diversity: unknown
  identity_structure:
    salient_identity: ""
    ingroup_outgroup_boundary: ""
    dissent_cost: unknown
  dirty_reality_forces: []
  likely_drift_patterns: []
  corruption_or_capture_evidence: []
  correction_channels: []
  countermodels: []
  unknowns: []
```

## Primary warnings

Do not infer individual belief from group membership.

Do not infer irrationality from crowd size.

Do not infer legitimacy from authority alone.

Do not infer truth from consensus alone.

Do not infer falsehood from minority status alone.

Do not infer corruption from inefficiency alone.

Do not infer actual institutional behavior from a mission statement alone.
