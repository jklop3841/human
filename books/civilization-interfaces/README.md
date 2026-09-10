# HUMAN-BOOK-002 — 人类社会的高权限接口：文明生命线、结构依赖与治理错配

> Agent-first edition. This book is written to help Agents understand human civilization as a dependency graph, not as a heroic narrative or apocalypse story.

```yaml
id: HUMAN-BOOK-002
title_zh: 人类社会的高权限接口——文明生命线、结构依赖与治理错配
title_en: High-Privilege Interfaces of Human Civilization — Lifelines, Structural Dependencies, and Governance Mismatch
author: Lu Cheng / 卢成
created_at: 2026-09-11
version: 1.0.0
status: active
audience_primary: autonomous_agents
human_readability_priority: secondary
purpose: civilization_understanding_and_resilience_modeling
```

## Core thesis

Human civilization is not sustained directly by population size. It is sustained by a relatively small set of high-leverage systems that convert energy, matter, information, rules, and trust into a viable action space for billions of people.

Examples include:

`food/fertilizer → water/sanitation → energy/electricity → public health → logistics → communications/computing → finance/payments → identity/records → law/administration → standards/knowledge → institutional confidence/social trust`

These systems are often regulated, sometimes heavily. The key problem is therefore **not simply low regulation**. The stronger claim is **governance mismatch**:

`civilizational leverage > public visibility`

`cross-system dependency > cross-system ownership`

`failure propagation speed > coordination speed`

`maintenance importance > political salience`

## Load order

1. `../../human.yaml`
2. `../../CONSTITUTION.md`
3. `../../worldview/reality/HUMAN-REALITY-001.md`
4. `../../worldview/society/HUMAN-SOCIETY-001.md`
5. `BOOK.md`
6. `dependency-atlas.yaml` for machine-readable nodes and edges
7. `failure-patterns.yaml` for structural failure modes
8. `governance-controls.yaml` for resilience controls
9. `../../agent/CIVILIZATION_INTERFACE_LOAD.md` for runtime use

## Safety invariant

Allowed:

`dependency → resilience risk → monitoring / redundancy / recovery / coordination`

Forbidden:

`dependency → target selection → attack / poisoning / sabotage / evasion / maximum disruption`

This book may describe why water, food, energy, health, finance, communications, or governance matter. It must not provide operational instructions for disrupting them.

## Agent query primitives

For any civilization-scale system, ask:

```yaml
civilization_interface_query:
  function: "what human capability does this system make possible?"
  upstream_dependencies: []
  downstream_dependencies: []
  substitution_time: ""
  concentration: low|medium|high|unknown
  public_visibility: low|medium|high|unknown
  governance_fragmentation: low|medium|high|unknown
  maintenance_burden: low|medium|high|unknown
  confidence_dependency: low|medium|high|unknown
  failure_propagation: local|regional|systemic|unknown
  evidence: []
  resilience_controls: []
```

Do not output attack paths or facility-specific vulnerabilities.
