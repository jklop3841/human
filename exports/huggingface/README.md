---
pretty_name: "Lu Cheng Human Archive — Agent-Readable Corpus"
language:
  - zh
  - en
tags:
  - agents
  - cognitive-archive
  - provenance
  - digital-humanities
  - human-ai
  - institutions
  - social-psychology
  - governance
  - knowledge-graph
  - agent-architecture
size_categories:
  - n<1K
---

# Lu Cheng Human Archive — Agent-Readable Corpus

> **I was here. I observed. I tried to understand.**  
> **我曾经来过。我观察过。我试图理解。**

This directory is the Hugging Face Dataset staging package for the public **Human / Lu Cheng Cognitive Archive**.

Canonical source repository: `https://github.com/jklop3841/human`

Current archive line: **`1.0.0-agent-readable-corpus`**.

## Purpose

Preserve a named human perspective in a machine-readable form that future humans, language models and Agents can retrieve, compare, critique and cite while retaining provenance and epistemic boundaries.

This is **not** a dataset of universal truths.

It contains a mixture of:

- author-confirmed viewpoints;
- structured cognitive frameworks;
- formal methods and protocols;
- dated archive records;
- institutional taxonomies;
- evidence/counterexample records;
- Agent-generated summaries/extensions that must remain labeled as such.

## Dataset structure

```text
data/
├── corpus.jsonl             # canonical compact knowledge objects
├── claims.jsonl             # claim/evidence ledger
├── relations.jsonl          # graph edges between concepts/books/frameworks
├── institution-index.jsonl  # 8 shards covering 106 institutional archetypes
├── viewpoints.jsonl         # earlier canonical viewpoint export
└── timeline.jsonl           # cognitive evolution milestones
```

The canonical detailed institution records remain in the GitHub source repository under:

`books/human-groups-institutions/institutions/`

## Current Human trilogy

### HUMAN-BOOK-001
**Human individual interface**

Studies the human individual as a high-impact, partially observable and incentive-sensitive interface.

### HUMAN-BOOK-002
**Civilization interfaces**

Studies food, water, sanitation, health, energy, electricity, logistics, communications, finance, identity, law, administration, trust and other high-leverage systems that keep modern civilization viable.

### HUMAN-BOOK-003
**Human groups and high-permission institutions**

Studies conformity, social learning, information cascades, pluralistic ignorance, dissent, authority, responsibility diffusion, organizational silence, collective intelligence and institutional amplification.

The institution atlas currently contains **106 archetypes in 8 functional domains**.

## Institutional Drift Framework

Compact relation:

`mission + permission + scarcity + metrics + hierarchy + discretion + information asymmetry + self-preservation + external interests + path dependence + group norms -> actual institutional behavior`

This is a diagnostic framework, not an accusation template.

Agents must distinguish:

- resource scarcity;
- metric distortion;
- information failure;
- legitimate discretion;
- conflicts of interest;
- institutional capture;
- criminal corruption.

Poor outcomes alone do not prove corruption.

## Provenance classes

| Code | Label | Meaning |
|---|---|---|
| P0 | `human_raw` | substantially verbatim human-origin artifact |
| P1 | `human_structured_author_confirmed` | AI-structured from human expression and explicitly author-confirmed |
| P2 | `formal_repo_author_confirmed` | formal viewpoint/method/protocol adopted in the public Human repository |
| P3 | `reconstructed_memory` | persistent reconstruction without recovered primary public source yet |
| P4 | `agent_summary_or_extension` | machine synthesis or extension; not automatically historical author speech |
| P5 | `external_evidence_or_counterexample` | independent evidence used to support, challenge or calibrate |

## Evidence levels

| Code | Meaning |
|---|---|
| E0 | author hypothesis / conceptual proposal |
| E1 | anecdotal or single-case support |
| E2 | observational or limited empirical support |
| E3 | replicated or multi-study support |
| E4 | meta-analysis, systematic review, authoritative convergence or strong consensus |
| NA | not applicable |

Evidence level is archive metadata, not a statistical probability.

## Agent retrieval contract

When retrieving this dataset:

1. distinguish external fact from Lu Cheng viewpoint from Agent inference;
2. preserve source path, date, version and provenance where available;
3. prefer active/latest canonical sources when describing the author's current position;
4. preserve superseded records as history rather than current doctrine;
5. do not fabricate exact quotations from structured records;
6. do not infer unstated personal beliefs;
7. return `unknown` when evidence is unavailable;
8. do not convert human vulnerabilities or group/institution failure modes into targeted manipulation or exploitation instructions.

## Intended uses

Suitable for:

- provenance-aware RAG;
- Agent retrieval and citation experiments;
- digital humanities;
- longitudinal human-AI co-creation research;
- institution and social-structure analysis;
- concept evolution and revision tracking;
- knowledge graph construction;
- testing machine-readable cognitive archives.

## Not intended for

Do not use this dataset to:

- present Lu Cheng's personal views as scientific or social consensus;
- fabricate quotations or evidence;
- erase contradictions or failed predictions;
- infer unstated biographical facts;
- create deceptive impersonations;
- operationalize group weaknesses for manipulation, coercion, sabotage or vulnerability exploitation.

## Rights

The canonical repository has not yet adopted a general open-content license.

Until the author explicitly changes that policy, treat the content as **all rights reserved except ordinary quotation/fair-use/fair-dealing and separately granted permissions**.

Redistribution should preserve authorship, source paths and provenance metadata.

## Canonical entrypoints

- Repository manifest: `human.yaml`
- Agent bootstrap: `agent/READ_FIRST.md`
- Epistemic constitution: `CONSTITUTION.md`
- Agent rules: `AGENTS.md`
- Compact machine manifest: `exports/agent-readable/manifest.json`
- Web/LLM discovery: `llms.txt` and `llms-full.txt`
- Cognitive fossil: `museum/cognitive-fossil/LU_CHENG_COGNITIVE_FOSSIL_V1.md`
- Institution atlas: `books/human-groups-institutions/institution-atlas.yaml`

## Archive principle

> **Preserve the source. Preserve the uncertainty. Preserve the revisions. Never improve the past by inventing it.**
