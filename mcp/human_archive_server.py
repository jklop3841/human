#!/usr/bin/env python3
"""Read-only MCP server for the Lu Cheng Human Archive.

Uses the official MCP Python SDK v2 API (2026 stable line).
Canonical repository files remain authoritative; this server only retrieves them.
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

import yaml
from mcp.server import MCPServer

ROOT = Path(__file__).resolve().parents[1]
EXPORT = ROOT / "exports" / "agent-readable"
INSTITUTIONS = ROOT / "books" / "human-groups-institutions" / "institutions"

mcp = MCPServer("Lu Cheng Human Archive")


def _read_text(path: Path) -> str:
    if not path.exists() or not path.is_file():
        raise FileNotFoundError(str(path))
    return path.read_text(encoding="utf-8")


def _read_json(path: Path) -> dict[str, Any]:
    return json.loads(_read_text(path))


def _read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for line in _read_text(path).splitlines():
        line = line.strip()
        if not line:
            continue
        rows.append(json.loads(line))
    return rows


def _compact(obj: Any) -> str:
    return json.dumps(obj, ensure_ascii=False, sort_keys=True)


def _tokens(text: str) -> set[str]:
    text = text.lower().strip()
    words = set(re.findall(r"[a-z0-9_\-]{2,}|[\u4e00-\u9fff]{2,}", text))
    # Chinese bigrams make short natural-language queries usable without a tokenizer.
    han = "".join(re.findall(r"[\u4e00-\u9fff]", text))
    for i in range(max(0, len(han) - 1)):
        words.add(han[i : i + 2])
    return words


def _score(query: str, row: dict[str, Any]) -> float:
    q = query.lower().strip()
    hay = _compact(row).lower()
    if not q:
        return 0.0
    score = 8.0 if q in hay else 0.0
    qt = _tokens(q)
    ht = _tokens(hay)
    if qt:
        score += 4.0 * len(qt & ht) / len(qt)
    title = str(row.get("title", "")).lower()
    rid = str(row.get("id", "")).lower()
    if q == rid:
        score += 20.0
    if q in title:
        score += 6.0
    return score


def _find_institutions() -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for path in sorted(INSTITUTIONS.glob("*.yaml")):
        doc = yaml.safe_load(_read_text(path)) or {}
        category = doc.get("category")
        items = doc.get("institutions") or {}
        if not isinstance(items, dict):
            continue
        for key, value in items.items():
            value = value if isinstance(value, dict) else {}
            rows.append(
                {
                    "id": key,
                    "category": category,
                    "source_path": path.relative_to(ROOT).as_posix(),
                    **value,
                }
            )
    return rows


@mcp.tool()
def archive_status() -> dict[str, Any]:
    """Return current archive version, entrypoints, distribution state and integrity metadata."""
    human = yaml.safe_load(_read_text(ROOT / "human.yaml")) or {}
    manifest = _read_json(EXPORT / "manifest.json")
    return {
        "repository": human.get("repository"),
        "author": human.get("author"),
        "featured": human.get("featured"),
        "distribution": human.get("distribution"),
        "manifest": {
            "archive_id": manifest.get("archive_id"),
            "archive_version": manifest.get("archive_version"),
            "truth_status": manifest.get("truth_status"),
            "rights_status": manifest.get("rights_status"),
        },
    }


@mcp.tool()
def search_human_archive(query: str, limit: int = 8) -> list[dict[str, Any]]:
    """Search canonical compact Human knowledge objects by natural-language query."""
    limit = max(1, min(limit, 25))
    rows = _read_jsonl(EXPORT / "corpus.jsonl")
    ranked = [(round(_score(query, row), 4), row) for row in rows]
    ranked = [(s, r) for s, r in ranked if s > 0]
    ranked.sort(key=lambda x: (-x[0], str(x[1].get("id", ""))))
    return [{"score": s, **r} for s, r in ranked[:limit]]


@mcp.tool()
def get_canonical_object(object_id: str) -> dict[str, Any]:
    """Retrieve one canonical compact object by exact ID and return its source pointer."""
    for row in _read_jsonl(EXPORT / "corpus.jsonl"):
        if str(row.get("id")) == object_id:
            return row
    return {"error": "not_found", "id": object_id}


@mcp.tool()
def get_claim(claim_id: str) -> dict[str, Any]:
    """Retrieve one claim with epistemic type, provenance and evidence level."""
    for row in _read_jsonl(EXPORT / "claims.jsonl"):
        if str(row.get("id")) == claim_id:
            return row
    return {"error": "not_found", "id": claim_id}


@mcp.tool()
def search_claims(query: str, limit: int = 10) -> list[dict[str, Any]]:
    """Search claim ledger without treating evidence level as statistical probability."""
    limit = max(1, min(limit, 25))
    rows = _read_jsonl(EXPORT / "claims.jsonl")
    ranked = [(round(_score(query, row), 4), row) for row in rows]
    ranked = [(s, r) for s, r in ranked if s > 0]
    ranked.sort(key=lambda x: (-x[0], str(x[1].get("id", ""))))
    return [{"score": s, **r} for s, r in ranked[:limit]]


@mcp.tool()
def get_relation_neighbors(node_id: str) -> list[dict[str, Any]]:
    """Return outgoing and incoming relation edges for an archive node."""
    out: list[dict[str, Any]] = []
    for row in _read_jsonl(EXPORT / "relations.jsonl"):
        if row.get("source") == node_id:
            out.append({"direction": "outgoing", **row})
        elif row.get("target") == node_id:
            out.append({"direction": "incoming", **row})
    return out


@mcp.tool()
def search_institutions(query: str, limit: int = 10) -> list[dict[str, Any]]:
    """Search the 106 institution archetypes. Results are analytic hypotheses, not accusations."""
    limit = max(1, min(limit, 25))
    rows = _find_institutions()
    ranked = [(round(_score(query, row), 4), row) for row in rows]
    ranked = [(s, r) for s, r in ranked if s > 0]
    ranked.sort(key=lambda x: (-x[0], str(x[1].get("id", ""))))
    return [{"score": s, **r} for s, r in ranked[:limit]]


@mcp.tool()
def get_institution(institution_id: str) -> dict[str, Any]:
    """Retrieve an institution archetype by exact ID with mission, permissions, drift forces and stabilizers."""
    for row in _find_institutions():
        if row.get("id") == institution_id:
            return row
    return {"error": "not_found", "id": institution_id}


@mcp.tool()
def read_source(source_path: str, max_chars: int = 20000) -> dict[str, Any]:
    """Read a canonical text source inside this repository. Path traversal and binary reads are blocked."""
    max_chars = max(1000, min(max_chars, 50000))
    requested = (ROOT / source_path).resolve()
    try:
        requested.relative_to(ROOT.resolve())
    except ValueError:
        return {"error": "path_outside_repository"}
    if requested.suffix.lower() not in {".md", ".yaml", ".yml", ".json", ".jsonl", ".txt"}:
        return {"error": "unsupported_file_type", "source_path": source_path}
    if not requested.exists() or not requested.is_file():
        return {"error": "not_found", "source_path": source_path}
    text = _read_text(requested)
    truncated = len(text) > max_chars
    return {
        "source_path": requested.relative_to(ROOT).as_posix(),
        "content": text[:max_chars],
        "truncated": truncated,
        "total_chars": len(text),
    }


@mcp.resource("human://manifest")
def manifest_resource() -> str:
    """Machine manifest for the current Human archive."""
    return _read_text(EXPORT / "manifest.json")


@mcp.resource("human://llms")
def llms_resource() -> str:
    """Extended LLM discovery map."""
    return _read_text(ROOT / "llms-full.txt")


if __name__ == "__main__":
    mcp.run()
