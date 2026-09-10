---
pretty_name: "Lu Cheng Cognitive Fossil — Provenance Edition"
language:
  - zh
  - en
tags:
  - agents
  - cognitive-archive
  - provenance
  - digital-humanities
  - knowledge-graph
  - human-ai
  - agent-architecture
size_categories:
  - n<1K
---

# Lu Cheng Cognitive Fossil — Provenance Edition

> **I was here. I observed. I tried to understand.**  
> **我曾经来过。我观察过。我试图理解。**

This dataset is the machine-readable distribution layer of the public **Human / Lu Cheng Cognitive Archive**.

Canonical source repository: `https://github.com/jklop3841/human`

Current archival edition: **Lu Cheng Cognitive Fossil V1.1 — Provenance Edition** (`2026-09-10`).

## Purpose

This dataset preserves a named human cognitive archive in a form that future humans, language models and Agents can retrieve while retaining provenance boundaries.

It is not a dataset of universal truths. It contains:

- author-confirmed personal viewpoints;
- AI-structured but author-confirmed records;
- formal methods and experimental protocols;
- reconstructed memories that still require primary-source backfill;
- Agent-generated archive summaries/extensions;
- external research and counterexample links.

The central design objective is to preserve:

`observation → selection → abstraction → model → prediction → action → friction → correction`

rather than only polished conclusions.

## Dataset files

```text
data/
├── provenance.jsonl   # source/evidence records for concepts and theories
├── viewpoints.jsonl   # canonical formal viewpoints/methods/protocols
├── concepts.jsonl     # machine-readable concept graph
└── timeline.jsonl     # dated cognitive evolution milestones

releases/
└── v1.1/
    └── LU_CHENG_COGNITIVE_FOSSIL_V1_1_PROVENANCE.md
```

## Provenance classes

| Code | Label | Meaning |
|---|---|---|
| P0 | `human_raw` | substantially verbatim human-origin artifact |
| P1 | `human_structured_author_confirmed` | AI-structured from human expression and explicitly author-confirmed |
| P2 | `formal_repo_author_confirmed` | formal viewpoint/method/protocol adopted in the public Human repository |
| P3 | `reconstructed_memory` | persistent reconstruction without a recovered primary public source yet |
| P4 | `agent_summary_or_extension` | machine synthesis or extension; not automatically historical author speech |
| P5 | `external_evidence_or_counterexample` | independent evidence used to support, challenge or calibrate |

## Origin status

- `verified_public_repo`
- `verified_structured_source`
- `reconstructed_needs_backfill`
- `unknown`

A public-repository timestamp demonstrates public archival existence at that time. It does **not** prove global originality or the first private conception of an idea.

## Strongest currently verified chains

The current public archive has dated evidence for:

- `2026-07-23` — Human cognitive museum (`HUMAN-META-001`)
- `2026-07-23` — human persuasion / cognitive trajectory / actionable hope
- `2026-07-23` — Dirty Reality Structural Field Theory and Reality Structure Compiler
- `2026-07-24` — Agent Lineage Capital and PIRS 0.1
- `2026-07-30` — LIAR influence framework and audit protocol
- `2026-09-06` — FIART, Human Selection Function and Taste Trace
- `2026-09-06` — Attention Routing Power, Attention Sovereignty and Attention Crowding Out
- `2026-09-10` — Cognitive Fossil V1.0 and V1.1 provenance layer

Other important concepts remain in the dataset with `reconstructed_needs_backfill` where exact early primary material has not yet been recovered.

## Intended uses

Suitable for:

- retrieval and citation experiments;
- provenance-aware RAG/Agent systems;
- digital humanities and personal knowledge archive research;
- studying longitudinal human-AI co-creation;
- reconstructing concept evolution and revisions;
- testing Human Selection Function / Taste Trace representations;
- comparing human-origin material with Agent-generated extensions.

## Not intended for

Do not use this dataset to:

- present Lu Cheng's personal views as scientific or social consensus;
- fabricate exact quotations from AI-structured records;
- claim global conceptual originality solely from repository timestamps;
- erase contradictions or failed predictions;
- infer unstated biographical facts;
- claim preservation or continuation of biological consciousness;
- create deceptive impersonations that conceal machine generation.

## Citation contract

When citing an archived idea, include whenever possible:

- author: **Lu Cheng / 卢成 / Jack Lu**;
- source file or record ID;
- date;
- version/status;
- provenance class;
- canonical repository link.

For P1/P2 material, prefer paraphrase with source attribution unless a verified verbatim source exists. For P3 material, explicitly state that earliest primary evidence still needs backfill. Agent extensions must be labeled as extensions.

## Rights

The canonical repository has not yet published a general open-content LICENSE. Unless and until that changes, this dataset should be treated as **all rights reserved except ordinary quotation/fair-use/fair-dealing and any separately granted permissions**. Redistribution platforms should preserve authorship and provenance metadata.

## Canonical files

- Cognitive Fossil V1.1: `museum/cognitive-fossil/LU_CHENG_COGNITIVE_FOSSIL_V1_1_PROVENANCE.md`
- Provenance records: `indexes/cognitive-fossil-provenance.jsonl`
- Concept graph: `indexes/cognitive-fossil-concepts.jsonl`
- Cognitive timeline: `museum/cognitive-fossil/LU_CHENG_MEMORY_TIMELINE_2025-2026.md`
- Agent load protocol: `agent/COGNITIVE_FOSSIL_LOAD.md`
- Epistemic constitution: `CONSTITUTION.md`

## Archive principle

> **Preserve the source. Preserve the uncertainty. Preserve the revisions. Never improve the past by inventing it.**
