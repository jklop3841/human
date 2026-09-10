# Cross-platform Preservation Roadmap / 跨平台存续路线

Archive: `Human / Lu Cheng Cognitive Fossil`  
Snapshot: `2026-09-10`

## Objective

Do not let a single platform become the only surviving copy or the only discovery path.

The archive should optimize for four properties:

1. **discoverability** — humans and Agents can find it;
2. **machine readability** — structured text and metadata can be parsed without proprietary UI;
3. **provenance** — versions, dates and authorship remain verifiable;
4. **redundancy** — loss of one platform does not erase the archive.

---

## Layer 0 — Canonical living source: GitHub

Canonical repository:

`https://github.com/jklop3841/human`

Role:

- active development;
- commit history;
- version control;
- issue/PR discussion;
- Markdown/YAML/JSONL machine-readable source;
- public canonical reference.

Required files:

- `README.md`
- `CONSTITUTION.md`
- `AGENTS.md`
- `CITATION.cff`
- `human.yaml`
- `indexes/cognitive-fossil.yaml`
- `indexes/cognitive-fossil-concepts.jsonl`
- `agent/COGNITIVE_FOSSIL_LOAD.md`
- `museum/cognitive-fossil/LU_CHENG_COGNITIVE_FOSSIL_V1.md`
- `museum/cognitive-fossil/LU_CHENG_MEMORY_TIMELINE_2025-2026.md`

Release rule:

- create a signed/versioned release for important milestones;
- never rewrite historical releases to make the author appear consistently correct;
- preserve contradictions and retired views.

---

## Layer 1 — Persistent DOI snapshots: Zenodo

Role:

- freeze important releases;
- obtain persistent DOI identifiers;
- improve scholarly/research discovery;
- create immutable citation targets for specific versions.

Recommended deposited object per major version:

`human-cognitive-fossil-vX.Y.Z.zip`

Include:

- complete repository snapshot;
- PDF export of the main fossil;
- JSONL concept graph;
- SHA256SUMS.txt;
- release notes;
- citation metadata.

Do not upload secrets, credentials or unnecessary private identifiers.

---

## Layer 2 — Source-history preservation: Software Heritage

Role:

- archive the public Git repository and its development history;
- provide an archive independent from GitHub;
- preserve source artifacts even if the original hosting location disappears.

Action:

- submit the canonical GitHub repository through Software Heritage “Save Code Now”;
- repeat after major releases if the latest snapshot is not yet captured.

---

## Layer 3 — AI-native corpus distribution: Hugging Face Datasets

Recommended dataset name:

`lu-cheng-cognitive-fossil`

Role:

- make the cognitive archive directly consumable as a dataset;
- expose structured records to researchers, LLM tooling and Agent pipelines;
- support dataset card metadata and machine querying.

Recommended structure:

```text
README.md                  # dataset card
concepts.jsonl             # one concept per line
viewpoints.jsonl           # one viewpoint/version per line
timeline.jsonl             # dated belief evolution
cases.jsonl                # cases and counterexamples
taste_traces.jsonl         # candidate/selected/rejected/outcome/revision
raw_transcripts/           # only public-safe, consented raw material
releases/                  # frozen archive versions
```

Minimum record schema:

```json
{
  "id": "...",
  "date": "YYYY-MM-DD",
  "author": "Lu Cheng / 卢成",
  "provenance": "human_raw | human_structured | human_revised | agent_summary | agent_extension | external_evidence | counterexample",
  "topic": "...",
  "text": "...",
  "source": "...",
  "version": "...",
  "confidence": null,
  "supersedes": null,
  "contradicted_by": []
}
```

---

## Layer 4 — Long-form and media preservation: Internet Archive

Role:

- preserve ZIP/PDF/HTML snapshots;
- preserve audio/video/public raw human material that does not fit neatly in Git;
- provide another independently hosted copy.

Recommended item family:

- `lu-cheng-cognitive-fossil-v1`
- `lu-cheng-human-voice-archive-2026`
- `lu-cheng-agent-archive-series-01`

Every item should contain strong metadata:

- creator: Lu Cheng / 卢成 / Jack Lu;
- date;
- description;
- source GitHub repository;
- canonical website;
- version;
- SHA256 checksums;
- provenance statement.

---

## Layer 5 — Canonical public web layer: agentarchitect.me

Role:

- human-facing discovery;
- machine-facing canonical identity;
- stable semantic entry point linking every archival copy.

Recommended routes:

```text
/human
/cognitive-fossil
/cognitive-fossil/timeline
/cognitive-fossil/concepts
/cognitive-fossil/agent-load
/agent-archive
```

Machine discovery files should link the archive:

```text
/llms.txt
/agents.txt
/.well-known/agent.json
/schema.json
/sitemap.xml
```

The website should not be the sole source of truth; it should point back to versioned archival objects.

---

## Layer 6 — Offline survival copies

Maintain at least:

- two offline storage devices in different physical locations;
- repository bundle/ZIP;
- plain Markdown/JSONL exports;
- PDF/A or ordinary PDF reading copy;
- SHA256 checksums;
- a short `START_HERE.txt` explaining identity, version and how to verify files.

Plain text formats are preferred because they remain interpretable without the original application.

---

## Release package standard

Each major release should produce:

```text
lu-cheng-cognitive-fossil-vX.Y.Z/
├── START_HERE.md
├── README.md
├── CITATION.cff
├── SHA256SUMS.txt
├── cognitive_fossil.md
├── cognitive_fossil.pdf
├── timeline.md
├── concepts.jsonl
├── viewpoints.jsonl
├── contradictions.jsonl
├── predictions.jsonl
├── taste_traces.jsonl
├── agent_load_protocol.md
└── source-repository.txt
```

---

## Preservation principle

Do not optimize only for “being online.”

Optimize for:

> **findable + parseable + attributable + versioned + redundant + criticizable**

The archive should remain useful even to a future intelligence that knows nothing about the author in advance.
