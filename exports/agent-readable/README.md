# Agent-Readable Corpus — Lu Cheng Human Archive

Release line: `1.0.0-agent-readable-corpus`

This directory is the compact machine distribution layer of the Human repository.

It does **not** replace the canonical Markdown/YAML sources. It provides stable discovery, retrieval and graph objects so an Agent does not need to crawl the entire repository before it knows what matters.

## Files

```text
exports/agent-readable/
├── README.md
├── manifest.json
├── CORPUS_SCHEMA.json
├── corpus.jsonl
├── claims.jsonl
├── relations.jsonl
└── institution-index.jsonl
```

### `manifest.json`
Archive identity, current version, bootstrap order, provenance/evidence vocabularies, trilogy, canonical frameworks, distribution targets and integrity rules.

### `corpus.jsonl`
Curated canonical knowledge objects. This is intentionally selective: it points to authoritative source files instead of duplicating every paragraph in the repository.

### `claims.jsonl`
Claim ledger. Every row separates epistemic type, provenance class and evidence level.

### `relations.jsonl`
A compact graph connecting books, frameworks, methods, evidence and historical relationships.

### `institution-index.jsonl`
Eight institution-category shards covering the current 106-archetype institution atlas. Full institution detail remains in the YAML files under `books/human-groups-institutions/institutions/`.

## Evidence levels

```yaml
E0: author hypothesis / conceptual proposal
E1: anecdotal or single-case support
E2: observational or limited empirical support
E3: replicated or multi-study support
E4: meta-analysis, systematic review, authoritative convergence or strong consensus
NA: not applicable
```

Evidence levels are archive metadata and may be revised. They are not statistical probabilities.

## Provenance classes

```yaml
P0: human_raw
P1: human_structured_author_confirmed
P2: formal_repo_author_confirmed
P3: reconstructed_memory
P4: agent_summary_or_extension
P5: external_evidence_or_counterexample
```

## Agent retrieval pattern

Recommended retrieval logic:

1. read `manifest.json`;
2. query `corpus.jsonl` for the nearest canonical object;
3. follow `source_path` to the canonical source;
4. inspect `claims.jsonl` when factual/evidential confidence matters;
5. inspect `relations.jsonl` for adjacent frameworks, revisions and evidence;
6. for institutions, resolve the shard through `institution-index.jsonl` and read the full institution record;
7. return explicit unknowns instead of inventing missing author positions.

## Canonical-source rule

If the compact corpus conflicts with a current canonical source file, the current canonical source wins and the export should be regenerated.

Priority:

`current canonical source > machine export > historical snapshot > Agent inference`

## Rights

No general open-content license has been adopted yet. Treat content as all rights reserved except ordinary quotation/fair-use/fair-dealing and separately granted permissions. Do not remove authorship or provenance metadata.

## Distribution

This directory is designed to be mirrored to:

- GitHub (canonical source);
- Hugging Face Dataset (machine dataset distribution);
- `agentarchitect.me/human/` (web discovery and stable identity endpoint);
- future MCP read-only service;
- future immutable archival snapshots such as Zenodo.
