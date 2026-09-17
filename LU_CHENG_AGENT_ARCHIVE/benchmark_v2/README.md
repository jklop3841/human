# Generativity Benchmark v2 — runnable research pilot

This is a new protocol, not a retrospective relabeling of BENCH-04-PILOT.
The full inherited pilot remains frozen, with browsing disabled and zero real model calls.
V2 prepares 54 isolated A/B/C calls: 3 model slots × 2 tasks × 3 replicates.
B uses a ten-item excerpt from Volume 001; the result can support only that intervention scope.
C matches 365 whitespace words. Provider token equality is unverified; record counts and apply a preregistered tokenizer before a confirmatory study.
D remains blocked until at least two real, distant, qualifying volumes and balanced materials exist.

## Run

1. `python tools/benchmark_v2.py prepare --out work_runs/v2`
2. Use runner_only/schedule.json to open a fresh isolated session for each prompt. Keep the generator away from this repository, answers and condition key.
3. Record actual provider/model/version, route, settings, session and tool-call audit using templates/v2_receipt.json. A model name in a filename is not identity evidence. Record query_count, page_open_count, search_audit_complete, architecture_sealed_before_reflection and architecture_sha256_before_reflection.
4. Save the raw architecture response first, then ask benchmark_v2/reflection_prompt.txt with templates/reader_response.json. No answer edits after reflection.
5. `python tools/benchmark_v2.py import --run work_runs/v2 --run-id LC-RUN-20260906-0001 --reply answer.json --reaction reaction.json --receipt receipt.json`
6. `python tools/benchmark_v2.py blind --run work_runs/v2 --out work_runs/v2_review`
7. Independent reviewers score architecture-only exports first, lock them, then inspect source/search evidence separately. Names, prior_trace and treatment keys are omitted from the architecture export. Mechanism content can still reveal treatment.

## Scoring and inference

Use frozen v0.4 benchmark/RUBRIC.md for architecture distance, trace, interaction, emergence, novelty, falsification and implementability.
The statistical unit is a generation call; average its two architectures first. Pair B−A and B−C within model/task/replicate,
then average by model; do not treat the two architectures as independent observations. D is a separate future comparison.
R0–R5 and HPC must retain rationale, raw answer and operator receipt. A reader's causal counterfactual is introspection, not causal identification.
Independent novelty requires a nearest-neighbor check. No automatic score turns model agreement into verification.

External Search Escape requires a logged self-selected search, a concrete task-useful mechanism and a domain outside supplied_domains.json.
Reviewers consider all supplied stimulus ancestry, aliases, retrieved suggestions and source chains; fungi is already present and is not escape.
A source suggested by a search engine is downstream search evidence, not proof of a spontaneous human-prior effect.
Compute escape only after two independent source-aware reviews; disagreement remains unresolved. Report per-condition denominators, unknowns and B−A/B−C.
Architecture reviewers remain separate from source-aware reviewers. Missing or over-budget tool logs exclude a call from controlled comparisons.
The local importer checks declared receipts, not provider server logs; actual origin must still be audited by the operator.

This release prepares/imports/blinds v2 records; no campaign or adjudicated effect estimate has been completed.
Use structured review tables and the explicit aggregation rules above; automatic v2 efficacy scoring is intentionally not implemented without reviewer data.
