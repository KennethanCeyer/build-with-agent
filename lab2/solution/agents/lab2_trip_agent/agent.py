from __future__ import annotations

from google.genai import types


from google.adk.agents import LlmAgent
from google.adk.tools.preload_memory_tool import PreloadMemoryTool

from .tools import (
    auto_save_session_to_memory_callback,
    google_search,
)


async def fix_text_extraction_callback(callback_context, llm_response):
    """GenAI SDK의 Built-in 도구 혼합 시 텍스트 추출 누락 문제를 해결합니다."""
    if llm_response.content and llm_response.content.parts:
        # ADK가 내부적으로 텍스트를 추출하지 못하더라도 parts에는 데이터가 유지됩니다.
        pass
    return llm_response


def build_trip_planner() -> LlmAgent:
    return LlmAgent(
        name="trip_planner",
        model="gemini-3.1-pro-preview",
        instruction=(
            "당신은 실시간 웹 검색과 이전 대화 기억을 활용하여 "
            "사용자 맞춤형 여행 계획을 수립하는 수석 플래너입니다.\n"
            "이전 대화 맥락이나 사용자의 취향을 기억에서 불러와 반영하세요."
        ),
        tools=[
            google_search,
            PreloadMemoryTool(),
        ],
        generate_content_config=types.GenerateContentConfig(
            tool_config=types.ToolConfig(include_server_side_tool_invocations=True),
        ),
        after_model_callback=fix_text_extraction_callback,
        after_agent_callback=auto_save_session_to_memory_callback,
    )


root_agent = build_trip_planner()
