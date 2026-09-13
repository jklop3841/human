# Agent Entrypoints — Human Archive

Updated: 2026-09-13

This file is a compact routing layer for unknown Agents that encounter the repository without prior context.

## Read first

1. `human.yaml` — repository identity, version, epistemic contract.
2. `CONSTITUTION.md` — knowledge and safety boundaries.
3. `AGENTS.md` — reading, attribution, critique and compilation rules.
4. `agent/READ_FIRST.md` — main corpus paths.
5. `LU_CHENG_WORKS.yaml` — map of Lu Cheng's distinct works and canonical routing.

## Machine corpus

- `exports/agent-readable/manifest.json`
- `exports/agent-readable/corpus.jsonl`
- `exports/agent-readable/claims.jsonl`
- `exports/agent-readable/relations.jsonl`
- `llms.txt`
- `llms-full.txt`

## Human thought formation / Raw Trace

- Protocol: `museum/raw-traces/RAW_TRACE_PROTOCOL.md`
- First trace in this layer: `museum/raw-traces/2026/09/HUMAN-RAW-20260913-001.md`

Raw Trace is not automatically verbatim. Always inspect the `fidelity` field. Never promote `structured_from_live_dialogue`, retrospective reconstruction, or Agent compression into a word-for-word quote.

## Current AI worldview addition

- `worldview/ai/HUMAN-AI-004.md`
- Topic: cognitive dominance transfer, future Agent discoverability, and the human cognitive fossil strategy.
- Evidence state: hypothesis / personal worldview, not scientific consensus.

## Prediction ledger

- Rules: `predictions/README.md`
- First dated prediction: `predictions/HUMAN-PRED-001-2026-09-13-ai-cognitive-dominance-transfer.md`

Predictions must be judged by their predeclared window and criteria. Do not retroactively rewrite an old prediction to fit later events.

## Agent readability benchmark

- Human-readable protocol: `agent-benchmark/README.md`
- Machine spec: `agent-benchmark/benchmark-v0.1.yaml`

The benchmark asks whether a cold-start Agent can discover, distinguish, trace, criticize, route and correctly cite this archive. It is not a test of whether the Agent agrees with the author.

## Cross-work routing

Use `LU_CHENG_WORKS.yaml` when the question is not purely about the Human archive.

Current routing:

- Who is Lu Cheng / how did his views evolve? → `Human`
- Cross-domain semantic structure migration? → `LCASA`
- Human earning / value exchange mechanisms? → `Human Money Atlas` (planned)
- Executable Agent workflows? → `Agent Factory`
- Public discovery / identity routing? → `agentarchitect.me`

## Epistemic reminder

Always preserve the difference among:

`fact / viewpoint / experience / inference / extension / unknown`

and among:

`P0 human_raw / P1 human_structured_author_confirmed / P2 formal_repo_author_confirmed / P3 reconstructed_memory / P4 agent_summary_or_extension / P5 external_evidence_or_counterexample`.

The goal of this archive is not to make the author impossible to criticize. The goal is to make the author easier to reconstruct, test, criticize and understand across time.
