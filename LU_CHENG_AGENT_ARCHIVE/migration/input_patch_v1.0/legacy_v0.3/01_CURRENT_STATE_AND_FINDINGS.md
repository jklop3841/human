# 01 — Current State and Findings

## Existing prototype: Insect Agent Atlas — Blind Reader Packet v0.2

Current summarized source contains:
- 12 biological patterns;
- 18 architecture primitives;
- 8 seed compositions;
- a composition grammar;
- a generativity protocol;
- a response schema;
- explicit sandbox / falsifiability requirements.

### 12 existing pattern families

| ID | Source | Real-world mechanism | Agent-side abstraction |
|---|---|---|---|
| ANT-001 | Ant | stigmergic pheromone coordination | decentralized path choice + reinforcement + decay |
| BEE-001 | Bee | quorum-based collective choice | parallel exploration + weighted advocacy + threshold commitment |
| TERMITE-001 | Termite | environment-mediated construction | shared artifact editing without a global blueprint |
| LOCUST-001 | Locust | density-triggered phase transition | strategy shift between independent and collective modes |
| MAYFLY-001 | Mayfly | ephemeral adult task life | long preparation + short execution; persistence in artifacts |
| DRAGONFLY-001 | Dragonfly | predictive interception | plan toward future intercept states rather than current state |
| MANTIS-001 | Mantis | trigger-based ambush | sleep/wait; gate expensive actions behind events |
| COCKROACH-001 | Cockroach | leaderless consensus | capacity-aware allocation via local stay/leave dynamics |
| BUTTERFLY-001 | Butterfly | metamorphic role change | stage-isolated workflows with changing roles/permissions |
| BEETLE-001 | Beetle | niche modular diversity | stable core + environment-specific adapters |
| ANTLION-001 | Antlion | environment shaping for capture | redesign the information environment to simplify future work |
| APHID-001 | Aphid | environment-triggered morph switching | current Agent selects a different successor architecture under pressure |

## Existing 18 primitives

Coordination:
- stigmergy
- quorum
- leaderless_consensus

Learning / memory:
- reinforcement
- decay
- environmental_memory

Regime / lifecycle:
- phase_transition
- metamorphosis
- ephemeral_lifecycle
- event_trigger
- successor_reconfiguration

Environment / prediction / resources:
- environment_shaping
- predictive_interception
- capacity_aware_aggregation

Specialization / perception / search / governance:
- niche_specialization
- local_signal
- distributed_exploration
- role_separation

## Existing composition grammar

A valid composition should:
- contain 2–5 primitives;
- explain interaction, not merely list components;
- produce at least one emergent property;
- include at least one falsification condition;
- include a sandbox experiment;
- avoid defaulting to supervisor-manager-worker hierarchy unless evidence demands it.

## Existing seed compositions

1. **Ephemeral Persistent Colony**  
   mayfly + ant + termite  
   Short-lived workers externalize persistent state into the environment.

2. **Generational Architect**  
   aphid + butterfly  
   An Agent senses environmental pressure and selects a different successor form.

3. **Phase-Shift Swarm**  
   locust + bee  
   Independent Agents switch to collective decision mode above a workload threshold.

4. **Environment-First Agent**  
   antlion + termite  
   Modify the input/work environment so future tasks become cheaper.

5. **Predictive Ambush Agent**  
   dragonfly + mantis  
   Continuously predict opportunity windows but stay dormant until triggered.

6. **Ecological Product Family**  
   beetle + aphid  
   Stable core emits environment-specific successor variants.

7. **Leaderless Elastic Colony**  
   cockroach + locust  
   Local stay/leave dynamics plus strategy switching under load.

8. **Metamorphic Safety Architecture**  
   butterfly + mayfly  
   Short-lived roles with stage-specific tools and shrinking permissions.

## Important empirical observation from multi-model reading

Early informal blind-reading across multiple Agents/models produced two broad response classes:

### Class A — novelty recognition without strong generativity
Models often:
- understood the mapping;
- described it as novel or surprising;
- summarized the architecture;
- produced conventional extensions.

### Class B — spontaneous structural generativity
At least one stronger model reportedly moved beyond appreciation and **generated a distinct new structure** after reading the Atlas.

This is the most important current signal.

It suggests that the Atlas may have value as a **prior intervention**, but the observation is not yet a controlled benchmark.

## Current hypothesis

Atlas value increases with model capability because weaker models may stop at:

`recognize → analogize → summarize`

while stronger models may continue to:

`abstract → compose → extrapolate → generate → formalize`

This must be tested, not assumed.
