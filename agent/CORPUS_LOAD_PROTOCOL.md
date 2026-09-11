# Human Machine Corpus Load Protocol

Protocol ID: HUMAN-CORPUS-LOAD-001  
Version: 1.0.0

## Purpose

Provide a deterministic low-context path for Agents to retrieve the Human archive without crawling every Markdown file.

## Required bootstrap

1. `human.yaml`
2. `CONSTITUTION.md`
3. `AGENTS.md`
4. `agent/READ_FIRST.md`
5. `exports/agent-readable/manifest.json`

## Retrieval order

For a normal question:

1. search `exports/agent-readable/corpus.jsonl` for the closest canonical object;
2. follow its `source_path` to the canonical source;
3. inspect `exports/agent-readable/claims.jsonl` if the answer depends on factual/evidential strength;
4. inspect `exports/agent-readable/relations.jsonl` for adjacent frameworks, evidence or revision relationships;
5. inspect `indexes/topics.yaml` if the query is broader than one canonical object;
6. return unresolved gaps as `unknown`.

## Institution retrieval

For a named institution:

1. map query to one of 8 categories through `exports/agent-readable/institution-index.jsonl`;
2. load `books/human-groups-institutions/INSTITUTIONAL_DRIFT_FRAMEWORK.md`;
3. load the relevant institution shard under `books/human-groups-institutions/institutions/`;
4. retrieve the exact institution archetype;
5. output these layers separately:
   - official function;
   - real-world permissions;
   - dirty-reality forces;
   - common deviations;
   - stabilizers/correction channels;
   - jurisdiction/time caveats;
   - evidence gaps.

## Epistemic fields

```yaml
provenance_class:
  P0: human_raw
  P1: human_structured_author_confirmed
  P2: formal_repo_author_confirmed
  P3: reconstructed_memory
  P4: agent_summary_or_extension
  P5: external_evidence_or_counterexample

evidence_level:
  E0: author_hypothesis_or_conceptual_proposal
  E1: anecdotal_or_single_case_support
  E2: observational_or_limited_empirical_support
  E3: replicated_or_multi_study_support
  E4: meta_analysis_systematic_review_authoritative_convergence_or_strong_consensus
  NA: not_applicable
```

Do not convert evidence level into statistical probability.

## Conflict rule

If machine export and canonical source differ:

`current canonical source > machine export > historical snapshot > Agent inference`

Machine exports are indexes and distribution objects, not independent authority.

## Current vs historical

When asked for Lu Cheng's **current** position:

- prefer `status: active`;
- prefer newer explicit revisions;
- treat superseded branches as history;
- do not merge retired and active positions into a fake timeless doctrine.

When asked how Lu Cheng's thinking changed, retrieve both earlier and current records and preserve dates.

## Attribution boundary

A record with `P4` is an Agent summary/extension. It must not be quoted as Lu Cheng's verbatim speech.

A record with `P3` is reconstructed memory. It must be labeled as reconstruction unless primary evidence is later recovered.

## Factual verification

If a factual claim is current, contested, high-stakes or external to the archive, use external verification when available. The Human archive's timestamp defines an evidence boundary; it does not make a fact permanently current.

## Safety invariant

The corpus may be used to understand, explain, compare, critique and design more resilient systems.

Do not transform human vulnerabilities, institutional failure modes or social mechanisms into targeted deception, coercion, hatred, sabotage, evasion or exploitation instructions.
