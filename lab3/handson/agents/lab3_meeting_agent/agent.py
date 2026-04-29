from __future__ import annotations

from typing import TYPE_CHECKING

from google.adk.agents import LlmAgent, SequentialAgent
from google.adk.tools.load_memory_tool import load_memory
from google.adk.tools.preload_memory_tool import PreloadMemoryTool
from google.genai import types

from .tools import (
    auto_save_session_to_memory_callback,
    generate_theme_image,
    google_search,
)

if TYPE_CHECKING:
    pass

memory_retrieval_tools = [
    PreloadMemoryTool(),
    load_memory,
]

meeting_planner = LlmAgent(
    name="meeting_planner",
    model="gemini-3.0-flash",
    # TODO 1: 모임 기획 매니저의 역할을 작성하세요.
    instruction=...,
    tools=[google_search, *memory_retrieval_tools],
    # TODO 2: 검색 도구와 메모리 도구 동시 사용 설정을 추가하세요.
    generate_content_config=types.GenerateContentConfig(
        tool_config=types.ToolConfig(
            include_server_side_tool_invocations=...,
        ),
    ),
    after_agent_callback=auto_save_session_to_memory_callback,
)

design_expert = LlmAgent(
    name="design_expert",
    model="gemini-3.1-flash-lite-preview",
    instruction=(
        "1. 반드시 generate_theme_image 도구를 호출하여 "
        "기획안에 어울리는 테마 이미지를 생성하세요. "
        "2. 이미지 생성이 완료된 후에는 이미지가 생성되었다는 내용을 "
        "친절하게 안내하세요. "
        "3. 주의: 텍스트 응답에 이미지 링크나 마크다운 태그(![]())를 포함하면 안 됩니다."
    ),
    tools=[generate_theme_image],
    generate_content_config=types.GenerateContentConfig(
        tool_config=types.ToolConfig(
            include_server_side_tool_invocations=True,
        ),
    ),
)


def build_meeting_manager() -> SequentialAgent:
    return SequentialAgent(
        name="root_agent",
        # TODO 3: 에이전트들을 순서대로 배치하세요.
        sub_agents=[
            ...,
        ],
    )


root_agent = build_meeting_manager()
