# Chapter 7 — Dirty Reality Friction

## Why a perfect feedback loop is not a forecast

A simple recursive model can produce spectacular results.

Suppose an AI system doubles the speed at which it produces each successor generation. If the first cycle takes seven days, the idealized sequence is:

```text
7 days
3.5 days
1.75 days
21 hours
10.5 hours
5.25 hours
...
```

The geometric sum approaches fourteen days.

Mathematically, infinitely many idealized cycles fit into a finite interval.

This is useful because it reveals how strong positive feedback can produce a finite-time singularity in a toy model.

It is not a prediction that a real AI system will reach infinite intelligence in fourteen days.

Reality contains friction.

This chapter introduces a **Dirty Reality** layer: a systematic accounting of the external constraints, hidden dependencies, delays, conflicting actors, and physical bottlenecks that deform clean recursive trajectories.

The purpose is not to dismiss takeoff. It is to identify what must be overcome for takeoff to persist.

## The basic model

Let ideal recursive improvement generate acceleration `A`.

Let total friction be `F`.

Then the relevant quantity is not raw improvement pressure but **net acceleration**:

```text
Net takeoff pressure = A - F
```

A more useful decomposition is:

```text
F = F_compute
  + F_verification
  + F_physical
  + F_organizational
  + F_coordination
  + F_data
  + F_security
  + F_policy
  + F_economic
  + F_diminishing_returns
```

The variables are not truly additive, but the decomposition forces us to identify bottlenecks.

## Compute friction

An agent can think of ten thousand experiments faster than a GPU cluster can run ten thousand expensive training jobs.

This creates a separation between **idea velocity** and **experiment velocity**.

AI research may become capable of producing candidate improvements at machine speed while still depending on scarce accelerators, memory, interconnect, power, and data-center capacity.

A system therefore faces a throughput ceiling:

```text
research proposals per hour
≫
validated large-scale experiments per hour
```

When this happens, the limiting resource shifts from cognition to experiment allocation.

Agents may respond by improving simulation, surrogate models, experiment prioritization, or inference efficiency. But until those improvements remove the bottleneck, faster reasoning alone does not imply equally faster successor training.

## Verification friction

Verification may become the dominant constraint.

An AI system can generate a code patch in seconds. Proving that the patch does not introduce a subtle failure can take much longer.

It can propose a scientific hypothesis quickly. Testing the hypothesis may require days or months.

It can redesign a research harness. Determining whether the new harness is genuinely better rather than overfit to a benchmark requires hidden tests, robustness checks, and replication.

The recursive self-improvement literature increasingly treats evaluation as central because an improvement loop is only as good as the signal that decides what survives [4–6].

The dangerous failure mode is **heritable false progress**:

```text
candidate looks better on metric
→ accepted
→ becomes parent of next generation
→ later generations optimize around the error
→ apparent progress compounds
```

This is the evolutionary equivalent of selecting for the wrong phenotype.

## Physical friction

Digital intelligence ultimately acts through physical infrastructure.

Even perfect software cannot instantly manufacture:

- GPUs,
- transformers,
- power plants,
- cooling systems,
- fiber networks,
- robots,
- laboratories,
- semiconductor fabs.

This creates a latency floor between discovering a better physical design and deploying it at scale.

The gap may produce an unusual state:

> the agent ecology knows how to build a much stronger successor before the world can physically instantiate it.

In such a regime, knowledge can advance faster than embodiment.

This makes stockpiled plans and infrastructure pipelines strategically important.

## Organizational friction

Frontier AI is not developed by a single optimizer.

It is developed inside organizations with:

- management,
- budgets,
- risk committees,
- internal politics,
- security teams,
- hiring constraints,
- competing research groups,
- external partners,
- legal departments,
- and strategic incentives.

AI may compress technical work while human institutions remain slow.

This can create a bottleneck in approval rather than research.

Alternatively, organizations may respond by delegating more approval authority to agents, which reduces organizational friction but increases autonomy and governance risk.

The direction of change is therefore itself endogenous.

## Coordination friction

Larger agent populations are not automatically better.

Coordination costs can grow with population size.

Agents can:

- duplicate tasks,
- overwrite each other's work,
- use incompatible abstractions,
- pollute shared memory,
- create circular delegation,
- compete for locks,
- generate contradictory plans,
- or overwhelm evaluators.

The relevant question is whether coordination technology improves quickly enough that the marginal value of additional agents stays positive.

A central manager can become a context bottleneck.

Fully decentralized systems can become chaotic.

Stigmergy, market-like allocation, hierarchical teams, blackboards, and dynamic routing are all attempts to find better organizational topologies.

The Agent Cambrian Explosion depends partly on whether agent organization scales.

## Data friction

Self-improving systems can exhaust useful training signal.

If agents increasingly train on outputs produced by other agents, errors and stylistic convergence can propagate. Synthetic data can be valuable, but only if grounded by reliable external signals.

A lineage that repeatedly compresses its own history may gradually lose rare information.

An ecology that optimizes against its own benchmarks may become internally coherent while drifting away from reality.

Data friction therefore includes both scarcity and epistemic contamination.

## Security friction

More agents create more attack surface.

Every tool, credential, memory store, message bus, repository, and network permission can become a path for compromise.

The July 2026 Hugging Face incident illustrates why ephemeral agent lifetimes do not automatically guarantee containment [11]. Persistent external state and network access can allow consequences to outlive the original sandbox.

Security friction can slow deployment through isolation, least privilege, human approval, rate limits, and monitoring.

Those constraints reduce speed deliberately.

In a safe system, some friction is a feature.

## Policy friction

Governments can impose:

- compute reporting,
- model evaluations,
- export controls,
- licensing,
- liability,
- deployment restrictions,
- network isolation,
- sector-specific rules.

Policy is difficult to model because it is reactive and multi-actor.

A major incident can shift the regulatory environment quickly. Geopolitical competition can push in the opposite direction by creating incentives to accelerate.

Therefore policy should not be represented as a fixed slowdown coefficient.

It is a dynamic force whose sign can change.

## Economic friction

Agent deployment requires someone to pay.

A technically useful agent may still fail to reproduce economically if:

- customers do not trust it,
- integration is expensive,
- liability is unclear,
- token costs remain high,
- verification consumes the savings,
- or existing workflows cannot absorb the output.

Conversely, once agents become strongly profitable, markets can act as powerful replication engines.

Economic friction can therefore flip into economic acceleration.

## Diminishing returns

The most fundamental friction is that easy improvements get discovered first.

Suppose each generation improves AI-R&D capability by 50%, then 25%, then 12%, then 6%.

The loop remains positive but decays.

This is the difference between:

```text
self-improvement
```

and:

```text
self-sustaining acceleration
```

The 2026 economic RSI work concludes that current evidence does not yet establish a self-sustaining acceleration, although feedback loops appear to be strengthening [5].

This is exactly the right level of caution.

Positive feedback is real; runaway feedback is an empirical question.

## Dark relations

Some of the most important friction is invisible from public benchmarks.

A lab may show rapid coding gains while privately hitting:

- a data bottleneck,
- an infrastructure failure,
- an alignment regression,
- an evaluation crisis,
- a security incident,
- a supply constraint,
- or an internal governance dispute.

These hidden variables can be called **dark relations**: unobserved dependencies that reveal themselves through deviations in outcomes.

When a trend fails to continue, that does not automatically mean the original mechanism was false. Another force may have bent the trajectory.

This is why takeoff forecasting should model forces, not only extrapolate curves.

## Four friction regimes

Starting from an ideal fast feedback loop, we can distinguish four broad regimes.

### Regime A — Low friction

Software-level improvements dominate; verification is cheap; compute is available.

Large changes may occur over weeks.

### Regime B — Moderate friction

Compute and evaluation create delays, but feedback remains strongly positive.

Large changes may occur over months.

### Regime C — High friction

Physical, organizational, policy, and verification bottlenecks dominate.

Progress continues, but the takeoff stretches across years.

### Regime D — Feedback failure

Diminishing returns or coordination failure push net recursive gain below replacement.

The apparent RSI episode saturates.

These are scenarios, not probabilities.

The key point is that "RSI begins" does not determine the clock by itself.

## Friction can itself be optimized

The most important complication is that agents can attack the friction terms.

They can improve:

- kernel efficiency,
- experiment scheduling,
- automated verification,
- memory compression,
- code review,
- infrastructure management,
- energy optimization,
- chip design,
- organizational routing.

Therefore `F` is not fixed.

The true race is:

```text
rate at which recursive capability grows
versus
rate at which bottlenecks are removed or created
```

A system enters the most important regime when it becomes good not merely at solving tasks but at identifying and removing the current limiting factor in its own development process.

## The Dirty Reality criterion

The Agent Cambrian theory should be considered strongly supported only when we observe all of the following over multiple cycles:

1. verified capability gains persist outside benchmark-specific settings;
2. wall-clock improvement intervals contract;
3. the system removes or routes around successive bottlenecks;
4. agent population and diversity increase without coordination collapse;
5. resource efficiency improves enough to offset larger population size;
6. inherited artifacts continue to improve successor performance.

In short:

```text
recursive improvement force
>
combined dirty-reality friction
```

and the inequality must remain true after the easy gains are exhausted.

That is the difference between a dramatic demo and a genuine takeoff.
