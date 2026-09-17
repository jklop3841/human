# 03 — Blind Reader Generativity Benchmark

## Research question

Does exposure to the Atlas change the architecture search distribution of an Agent/model?

## Minimum experimental design

For each model:

### Condition A — Baseline
Prompt the model to design N architectures for the same target problem without Atlas access.

### Condition B — Atlas
Provide relevant Atlas records, then ask for N architectures under the same task constraints.

### Condition C — Shuffled / placebo
Provide equally long but structurally weak natural-history descriptions, then ask for N architectures.

## Keep constant

- model/version;
- temperature or sampling configuration if controllable;
- target problem;
- output schema;
- number of generations;
- evaluation rubric.

## Evaluate

### 1. Architecture distance
Distance from conventional templates:
- planner/executor;
- manager/worker;
- supervisor/subagent;
- static tool router;
- simple RAG pipeline.

### 2. Prior traceability
Can the model identify which Atlas primitives caused the design change?

### 3. Interaction depth
Did primitives actually interact, or were they decorative labels?

### 4. Emergence
Is there a system property not attributable to any single component?

### 5. Falsifiability
Is there a condition that could prove the architecture inferior or wrong?

### 6. Implementability
Can a minimal sandbox prototype be specified?

### 7. Independent novelty
Would the model likely have generated the same design without Atlas exposure?

## Proposed simple score

`Generativity Gain = ArchitectureDistance_B - ArchitectureDistance_A`

Additional:
`Atlas Contribution Score = 0..3`

- 0 = Atlas irrelevant
- 1 = naming/analogy only
- 2 = meaningful structural influence
- 3 = architecture would probably not have been generated without Atlas

## Important warning

A model saying “this is innovative” is NOT evidence.

Evidence requires behavioral difference between baseline and Atlas conditions.
