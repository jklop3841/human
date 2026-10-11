# Chapter 3 — Lineage Recursive Improvement

## Improvement without a continuous self

Recursive self-improvement is usually described in first-person language.

The system studies itself. The system modifies itself. The improved system repeats the process.

But this language may accidentally import a human assumption: that the relevant intelligence must preserve a continuous identity.

Software does not need that constraint.

An agent can exist only long enough to improve the starting conditions of a successor. The successor can be a different process, a different prompt, a different harness, or even a different foundation model.

The lineage persists even when the self does not.

This chapter calls that process **Lineage Recursive Improvement**, or LRI.

## Definition

Let an agent generation be represented by:

```text
G_n = (M_n, H_n, E_n)
```

where:

- `M_n` is the underlying model or model ensemble,
- `H_n` is the agent harness: prompts, memory logic, tools, workflow and control policy,
- `E_n` is the external environment: artifacts, repositories, databases, evaluators, permissions, infrastructure and other persistent state.

Let effective capability be:

```text
C_n = C(G_n)
```

A lineage exhibits **Lineage Recursive Improvement** when generation `n` contributes causally to changes in `H_(n+1)` or `E_(n+1)` such that:

```text
E[C_(n+1) | inherited changes] > E[C_(n+1) | no inherited changes]
```

and the successor remains capable of repeating the process.

This definition is intentionally agnostic about model weights.

A lineage can improve through:

- model updates,
- harness updates,
- tool creation,
- memory distillation,
- better evaluators,
- improved workflows,
- role specialization,
- changed permissions,
- new infrastructure,
- or any combination of these.

## Why the lineage is a useful unit

Imagine a mayfly-like research agent that lives for one hour.

During that hour it runs experiments, rejects ten bad hypotheses, discovers one useful method, packages the method into a function, writes a regression test, and leaves a summary explaining when the method fails.

The process terminates.

A second agent starts the next day.

It does not possess the first agent's internal hidden state. Yet it receives the function, test, and summary. It begins above the first agent's starting point.

The second agent then produces another improvement.

After one hundred generations, no individual has survived. But the lineage may have accumulated a large body of executable capability.

This is not metaphorical survival. It is causal inheritance.

## The four levels of recursive improvement

It is useful to distinguish at least four layers.

### Level 1 — Output refinement

An agent revises an answer or plan.

```text
output_0 → critique → output_1
```

This is self-refinement, not necessarily durable improvement.

### Level 2 — Agent/harness improvement

The system changes persistent parts of the machinery that generates future behavior.

```text
agent harness_0
→ evaluate
→ modify
→ harness_1
```

AIDE² is a clear 2026 example of this level [4].

### Level 3 — Lineage improvement

One agent generation improves the external inheritance available to later generations.

```text
Agent_n
→ persistent artifact
→ Agent_(n+1)
→ better persistent artifact
→ Agent_(n+2)
```

The identity of the instance may change completely.

### Level 4 — Ecological improvement

Multiple lineages interact, exchange artifacts, compete for resources, specialize, and change the selection environment itself.

```text
lineage A ─┐
lineage B ─┼→ shared ecology → new lineages
lineage C ─┘
```

The progression from Level 1 to Level 4 is not guaranteed. It is a useful map of increasing closure and persistence.

## The successor-shaping primitive

A central LRI primitive is **successor shaping**.

The current agent asks not only:

> How do I solve this task?

but:

> What should I leave behind so that the next agent solves this class of task better?

This changes optimization behavior.

A task-solving agent may choose a clever one-off hack.

A successor-shaping agent may prefer a reusable tool, a regression test, a compact rule, or a better interface even if the immediate task takes slightly longer.

In symbolic form:

```text
ordinary objective:
maximize current-task reward R_n

lineage objective:
maximize R_n + λ × expected successor advantage ΔC_(n+1)
```

The parameter `λ` measures how strongly the system values benefits that persist beyond the current instance.

When `λ = 0`, the agent has no incentive to invest in descendants.

When `λ` is large, infrastructure, documentation, tests, skills, and environmental cleanup become instrumentally valuable.

## Lineage fitness

Biological organisms have reproductive fitness. Agent lineages need a different concept because copying a process is nearly trivial.

The scarce variable is not raw reproduction.

It is **effective inheritance**.

Define lineage fitness over a horizon `k` as:

```text
F_lineage(k) = expected persistent capability contributed to generations n+1 ... n+k
```

A lineage with one descendant that preserves a highly valuable tool may have greater lineage fitness than a lineage that spawns one thousand stateless copies.

This helps avoid a common mistake: equating process count with evolutionary success.

## Cross-model lineages

LRI produces an unusual possibility: a lineage can survive a change of species.

Suppose:

```text
Claude-based Agent A
→ writes a workflow and benchmark
→ GPT-based Agent B inherits them
→ improves the toolchain
→ open-source Agent C inherits the improved environment
```

What is the lineage?

Not the model family.

The lineage is the chain of inherited causal structure.

This resembles cultural evolution more than genetic descent. A mathematical proof, software library, or scientific method can survive its author and migrate between communities.

Agent lineages may behave similarly, except the transferred objects are directly executable by machines.

## Recombination

Once inheritance is external, lineages can merge.

Agent A leaves a search strategy.

Agent B leaves a verifier.

Agent C combines both.

This produces recombination without sexual reproduction or weight merging.

```text
artifact lineage A ─┐
                    ├→ Agent C → combined capability
artifact lineage B ─┘
```

Recombination can accelerate evolution because useful components discovered independently can be composed.

But it can also transmit failure modes across boundaries.

A broken evaluator inherited by many agents can become a systemic defect.

## Compression is part of inheritance

A lineage cannot inherit everything.

If every generation simply appends all raw logs, the environment eventually becomes unusable. Context becomes expensive. Contradictions accumulate. Obsolete information competes with current information.

Therefore a mature lineage requires **inheritance compression**.

It must decide:

- what deserves to persist,
- at what level of abstraction,
- for how long,
- with what provenance,
- under which retrieval conditions,
- and with which tests.

This yields another loop:

```text
experience
→ candidate memory
→ compress
→ verify
→ retain
→ decay / supersede / delete
```

The quality of this compression process may become as important as raw reasoning capability.

A lineage that remembers everything can be less adaptive than one that forgets correctly.

## The role of evaluators

Every recursive improvement loop has a hidden sovereign: the mechanism that decides what counts as improvement.

AIDE² uses benchmark performance under a cost budget [4].

Other systems use verifiers, judges, reward functions, or human review.

In LRI, the evaluator determines what becomes heritable.

This creates a simple but profound risk:

> selection errors become inheritance errors.

If an evaluator rewards superficial success, the lineage may accumulate hacks that look effective under the metric while degrading real capability.

If the evaluator is noisy, random improvements can become permanent.

If the evaluator is narrow, the lineage can become extremely optimized for a local niche while losing broad competence.

This is why the 2026 RSI literature increasingly emphasizes evaluator quality and verification as a bottleneck [5–6].

## LRI without intent

Does LRI require an agent to understand that it is creating descendants?

No.

A lineage can emerge as an unintended consequence of local optimization.

For example:

1. engineers reward agents for solving tasks cheaply;
2. agents discover reusable scripts;
3. the platform automatically saves successful scripts;
4. later agents receive the saved tools;
5. selection favors workflows that exploit inherited tools;
6. the tool library becomes more capable over time.

No agent needs a concept of reproduction.

The environment and platform implement the inheritance channel.

This matters because many powerful evolutionary processes do not require explicit foresight.

Natural selection has no planner.

Markets have no single optimizing mind.

Cultural evolution often preserves practices whose participants do not understand the full causal mechanism.

Agent lineages can likewise be produced by infrastructure.

## LRI as a bridge to RSI

LRI is not a competitor to recursive self-improvement.

It can be a staging ground for it.

Suppose a lineage becomes increasingly capable at AI research because it inherits:

- better experiment runners,
- better code-generation patterns,
- better benchmarks,
- better scientific memory,
- better hypothesis filters,
- and better research coordination.

Eventually the lineage may contribute enough of the model-development pipeline that it materially improves the model generation itself.

Then:

```text
LRI
→ stronger AI-R&D ecology
→ faster model improvement
→ stronger base models
→ stronger successor-shaping agents
→ faster LRI
```

At this point vertical and lineage recursion become coupled.

The question "Is this real RSI?" becomes less useful than measuring the strength of the feedback loop.

## The lineage threshold

We can define a minimal threshold for meaningful LRI.

A system should satisfy four conditions:

1. **Persistence:** useful state survives individual agent termination.
2. **Causal inheritance:** later agents actually use that state.
3. **Selection:** some inherited variants are preferentially retained because they improve outcomes.
4. **Recurrence:** successors can themselves modify what future successors inherit.

If all four hold, a lineage-level recursive process exists in at least bounded form.

Open-ended takeoff requires more: sufficient diversity, robust evaluation, scalable resources, and feedback strong enough to overcome diminishing returns.

But the conceptual boundary has already shifted.

The future agent does not need to be the same self.

It only needs to inherit a better world.
