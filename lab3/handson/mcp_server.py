from __future__ import annotations

import os
from pathlib import Path

from mcp.server.fastmcp import FastMCP

from lab3_meeting_agent.adk_support import (
    expose_google_api_key,
    resolve_output_dir,
    save_backup_plan_payload,
    save_group_chat_update_payload,
)

PROJECT_ROOT = Path(__file__).resolve().parent

server = FastMCP(
    name="outing-deliverable-server",
    instructions="백업 모임 계획서와 단체 채팅 공지 마크다운 파일을 저장하는 MCP 서버입니다.",
)

expose_google_api_key(PROJECT_ROOT)


@server.tool(
    name="save_backup_plan",
    description="백업 모임 계획을 마크다운 파일로 저장합니다.",
)
def save_backup_plan(
    title: str, agenda: str, source_notes: str = ""
) -> dict[str, object]:
    return save_backup_plan_payload(
        title=title,
        agenda=agenda,
        source_notes=source_notes,
        output_dir=resolve_output_dir(PROJECT_ROOT),
    )


@server.tool(
    name="save_group_chat_update",
    description="친근한 단체 채팅 공지문을 마크다운 파일로 저장합니다.",
)
def save_group_chat_update(
    title: str, message: str, source_notes: str = ""
) -> dict[str, object]:
    return save_group_chat_update_payload(
        title=message,
        message=message,
        source_notes=source_notes,
        output_dir=resolve_output_dir(PROJECT_ROOT),
    )


if __name__ == "__main__":
    server.run(transport="stdio")
