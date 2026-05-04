from __future__ import annotations

from google.genai import types

from google.adk.agents import LlmAgent
from google.adk.tools.load_memory_tool import LoadMemoryTool  # noqa: F401
from google.adk.tools.preload_memory_tool import PreloadMemoryTool  # noqa: F401

from .tools import (  # noqa: F401
    google_search,  # noqa: F401
)


def build_trip_planner() -> LlmAgent:
    return LlmAgent(
        name="lab2_trip_agent",
        model="gemini-3-flash-preview",
        # TODO 1: 지침을 작성하세요.
        # 힌트: 웹 검색과 기억을 활용해 여행 계획을 세우는 플래너의 역할과 지침을 명시하세요.
        instruction=("당신은 ... 입니다. ... 하세요."),
        # TODO 2: 실시간 웹 검색과 매 턴 시작 시 기억을 불러올 도구를 리스트에 넣으세요.
        # 구글 검색, 메모리 불러오기 도구들을 사용해야 합니다.
        tools=[],
        generate_content_config=types.GenerateContentConfig(
            tool_config=types.ToolConfig(include_server_side_tool_invocations=True),
        ),
    )


root_agent = build_trip_planner()
