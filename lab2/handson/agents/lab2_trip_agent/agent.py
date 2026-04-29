from __future__ import annotations

from google.genai import types  # noqa: F401

from google.adk.agents import LlmAgent
from google.adk.tools.preload_memory_tool import PreloadMemoryTool  # noqa: F401

from .tools import auto_save_session_to_memory_callback, google_search  # noqa: F401


def build_trip_planner() -> LlmAgent:
    return LlmAgent(
        name="trip_planner",
        model="gemini-3.1-pro-preview",
        # TODO 1: 인스트럭션을 작성하세요.
        # 힌트: 웹 검색과 기억을 활용해 여행 계획을 세우는 플래너의 역할과 지침을 명시하세요.
        instruction=("당신은 ... " "... 반영하세요."),
        # TODO 2: 실시간 웹 검색과 매 턴 시작 시 기억을 불러올 도구를 리스트에 넣으세요.
        # [google_search, PreloadMemoryTool, LoadMemoryTool, save_itinerary]
        tools=[],
        # TODO 3: 내장 검색 도구와 함수 호출 방식의 메모리 도구를 함께 쓰도록 설정하세요.
        # 힌트: Gemini API에서 검색과 함수 호출을 혼합하려면 전용 설정이 필요합니다.
        # generate_content_config=types.GenerateContentConfig(
        #     tool_config=types.ToolConfig(include_server_side_tool_invocations=True),
        # ),
        generate_content_config=None,
        # TODO 4: 답변 직후 대화를 자동 저장할 콜백 함수를 연결하세요.
        # [auto_save_session_to_memory_callback, read_trip_notes, None]
        after_agent_callback=None,
    )


root_agent = build_trip_planner()
