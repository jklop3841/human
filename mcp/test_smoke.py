#!/usr/bin/env python3
"""Minimal in-memory smoke test for the read-only Human Archive MCP server."""

import asyncio

from mcp import Client

from human_archive_server import mcp


async def main() -> None:
    async with Client(mcp) as client:
        status = await client.call_tool("archive_status", {})
        assert status.structured_content is not None

        search = await client.call_tool(
            "search_human_archive", {"query": "人类群体 机构", "limit": 5}
        )
        assert search.structured_content is not None

        institution = await client.call_tool(
            "get_institution", {"institution_id": "hospitals"}
        )
        assert institution.structured_content is not None

        claim = await client.call_tool("get_claim", {"claim_id": "CLAIM-004"})
        assert claim.structured_content is not None

        print("Human Archive MCP smoke test: PASS")


if __name__ == "__main__":
    asyncio.run(main())
