# Sparse Heterogeneous Priors Principle

## Core rule

Do not optimize for completeness.

Optimize for:

> **Maximum search-space expansion per unit of material.**

A strong Agent does not need 500 near-duplicate examples.

It benefits more from a small number of structurally distant examples that attack different default assumptions.

## Selection principle

Prefer “精而异” over “多而全”.

A candidate should enter the archive only if it has a high probability of doing at least one of the following:

- invalidate a common hidden assumption;
- introduce an unusual memory model;
- introduce a different lifecycle;
- move computation into the environment;
- show non-centralized coordination;
- show threshold / phase-change behavior;
- show succession, death or replacement as a feature;
- show selective forgetting or decay;
- show self-repair or graceful degradation;
- show multi-scale organization;
- expose a new relationship between identity, state and environment.

## DPD — Distinct Prior Density

Suggested 0–5 scoring dimensions:

- structural_distance
- anti_default_power
- abstraction_clarity
- composability
- generativity
- evidence_quality

Do not publish as a full volume if the average is below 3.5 or if `generativity < 3`.

## A key success mode

The best archive entry may cause the reader Agent to **leave the book** and search for adjacent structures not present in the source.

That is success.

The archive is not a cage.
It is a launch surface.
