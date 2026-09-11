# Lu Cheng Human Archive MCP — Read-Only Baseline

This is a local read-only MCP interface over the Human repository.

It exists so an MCP-capable Agent can query the archive without scraping the entire repository.

## Current SDK target

The baseline targets the official MCP Python SDK **v2 stable line** and Python 3.10+.

Install:

```bash
python -m venv .venv
# activate the environment
pip install -r mcp/requirements.txt
```

Run through the MCP Inspector:

```bash
mcp dev mcp/human_archive_server.py
```

Or run directly over stdio:

```bash
python mcp/human_archive_server.py
```

The server is intentionally read-only.

## Tools

### `archive_status()`
Returns current repository/archive version, featured entrypoints and distribution state.

### `search_human_archive(query, limit=8)`
Searches the curated canonical machine corpus.

### `get_canonical_object(object_id)`
Retrieves one compact canonical object and its `source_path`.

### `search_claims(query, limit=10)` / `get_claim(claim_id)`
Retrieves claim, provenance and evidence metadata.

### `get_relation_neighbors(node_id)`
Returns incoming/outgoing knowledge-graph edges.

### `search_institutions(query, limit=10)` / `get_institution(institution_id)`
Searches the full institution YAML shards and returns:

- official function;
- high permissions;
- dirty-reality forces;
- common deviations;
- stabilizers.

Institution deviations are hypotheses to inspect, not accusations against every institution or employee.

### `read_source(source_path, max_chars=20000)`
Reads a canonical text source inside the repository with path-traversal and file-type restrictions.

## Resources

- `human://manifest`
- `human://llms`

## Example Agent workflow

Question: `卢成如何理解医院？`

1. call `search_institutions("医院 hospital")`;
2. choose `hospitals`;
3. call `get_institution("hospitals")`;
4. if deeper theory is needed, call `search_human_archive("institutional drift hospital")`;
5. follow `source_path` through `read_source(...)`;
6. keep external fact, Lu Cheng viewpoint and Agent inference separate.

## Security / integrity

This server does not expose filesystem write, shell execution, network access or repository mutation tools.

`read_source` only resolves files beneath repository root and only permits text-like archive file types.

Do not extend this MCP server with mutation actions unless a separate authorization, audit and rollback model is explicitly designed.

## Canonical-source rule

`current canonical source > machine export > historical snapshot > Agent inference`

The MCP server is an access layer. It is not a new source of truth.
