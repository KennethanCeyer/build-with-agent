from __future__ import annotations

from google.adk.agents import LlmAgent, SequentialAgent
from google.adk.tools.load_memory_tool import load_memory
from google.adk.tools.preload_memory_tool import PreloadMemoryTool
from google.genai import types

from .tools import (
    generate_theme_image,
    google_search,
)

memory_retrieval_tools = [
    PreloadMemoryTool(),
    load_memory,
]

meeting_planner = LlmAgent(
    name="meeting_planner",
    model="gemini-3.1-flash-lite-preview",
    instruction=(
        "당신은 모임을 기획하는 매니저입니다. "
        "웹 검색과 기억을 활용해 모임의 주제, 시간, 장소를 정리하세요."
    ),
    tools=[google_search, *memory_retrieval_tools],
    generate_content_config=types.GenerateContentConfig(
        tool_config=types.ToolConfig(
            include_server_side_tool_invocations=True,
        ),
    ),
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
        name="lab3_meeting_agent",
        sub_agents=[
            meeting_planner,
            design_expert,
        ],
    )


root_agent = build_meeting_manager()
