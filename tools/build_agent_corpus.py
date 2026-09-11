#!/usr/bin/env python3
"""Build deterministic machine-readable exports for the Human archive.

Outputs are derived indexes. Canonical Markdown/YAML sources remain authoritative.

Requires: PyYAML >= 6
Usage:
    python tools/build_agent_corpus.py
"""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "exports" / "agent-readable"
HF_OUT = ROOT / "exports" / "huggingface" / "data"

TEXT_SUFFIXES = {".md", ".yaml", ".yml", ".json", ".jsonl", ".txt"}
EXCLUDE_PARTS = {".git", "node_modules", ".venv", "__pycache__"}


def dump_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def parse_frontmatter(path: Path) -> tuple[dict[str, Any], str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}, text
    raw = text[4:end]
    body = text[end + 5 :]
    meta = yaml.safe_load(raw) or {}
    return meta if isinstance(meta, dict) else {}, body


def first_heading(body: str) -> str | None:
    for line in body.splitlines():
        m = re.match(r"^#\s+(.+?)\s*$", line)
        if m:
            return m.group(1).strip()
    return None


def build_institutions() -> list[dict[str, Any]]:
    base = ROOT / "books" / "human-groups-institutions" / "institutions"
    rows: list[dict[str, Any]] = []
    for path in sorted(base.glob("*.yaml")):
        doc = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        category = doc.get("category")
        institutions = doc.get("institutions") or {}
        if not isinstance(institutions, dict):
            continue
        for key in sorted(institutions):
            item = institutions[key] or {}
            if not isinstance(item, dict):
                continue
            rows.append(
                {
                    "id": f"INST::{key}",
                    "object_type": "institution",
                    "title": key,
                    "author": "Lu Cheng / 卢成",
                    "status": "active",
                    "category": category,
                    "source_path": rel(path),
                    "provenance_class": "P2",
                    "epistemic_type": "method",
                    "evidence_level": "NA",
                    "official_function": item.get("official_function", []),
                    "high_permissions": item.get("high_permissions", []),
                    "dirty_reality_forces": item.get("dirty_reality_forces", []),
                    "common_deviations": item.get("common_deviations", []),
                    "stabilizers": item.get("stabilizers", []),
                }
            )
    return rows


def build_viewpoints() -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for path in sorted((ROOT / "worldview").rglob("*.md")):
        meta, body = parse_frontmatter(path)
        if not meta.get("id"):
            continue
        rows.append(
            {
                "id": meta.get("id"),
                "object_type": "viewpoint",
                "title": meta.get("title") or first_heading(body) or path.stem,
                "author": meta.get("author") or "Lu Cheng / 卢成",
                "created_at": meta.get("created_at") or meta.get("date"),
                "updated_at": meta.get("updated_at"),
                "version": str(meta.get("version")) if meta.get("version") is not None else None,
                "status": meta.get("status") or "reference",
                "topics": meta.get("topics") or [],
                "claim": meta.get("claim"),
                "confidence": meta.get("confidence"),
                "source_path": rel(path),
                "provenance_class": "P2" if meta.get("author_confirmed") else "P4",
                "epistemic_type": "viewpoint",
            }
        )
    return rows


def build_file_manifest() -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file():
            continue
        if any(part in EXCLUDE_PARTS for part in path.parts):
            continue
        if path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        rp = rel(path)
        if rp == "exports/agent-readable/checksums.sha256":
            continue
        rows.append(
            {
                "path": rp,
                "bytes": path.stat().st_size,
                "sha256": sha256_file(path),
            }
        )
    return rows


def write_checksums(file_rows: list[dict[str, Any]]) -> None:
    path = OUT / "checksums.sha256"
    with path.open("w", encoding="utf-8", newline="\n") as f:
        for row in file_rows:
            f.write(f"{row['sha256']}  {row['path']}\n")


def mirror_for_hf(source: Path, name: str | None = None) -> None:
    HF_OUT.mkdir(parents=True, exist_ok=True)
    target = HF_OUT / (name or source.name)
    target.write_bytes(source.read_bytes())


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    HF_OUT.mkdir(parents=True, exist_ok=True)

    institutions = build_institutions()
    viewpoints = build_viewpoints()

    dump_jsonl(OUT / "institutions.jsonl", institutions)
    dump_jsonl(OUT / "generated-viewpoints.jsonl", viewpoints)

    # Generate manifest after derived JSONL exists so those files are hashed too.
    file_rows = build_file_manifest()
    dump_jsonl(OUT / "file-manifest.jsonl", file_rows)
    write_checksums(file_rows)

    mirror_for_hf(OUT / "institutions.jsonl")
    mirror_for_hf(OUT / "generated-viewpoints.jsonl")

    print(
        json.dumps(
            {
                "institutions": len(institutions),
                "viewpoints": len(viewpoints),
                "files_hashed": len(file_rows),
                "output": rel(OUT),
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
