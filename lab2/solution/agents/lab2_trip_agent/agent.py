from __future__ import annotations

from google.genai import types

from google.adk.agents import LlmAgent
from google.adk.agents.callback_context import CallbackContext
from google.adk.tools.load_memory_tool import LoadMemoryTool
from google.adk.tools.preload_memory_tool import PreloadMemoryTool

from .tools import google_search


async def auto_save_session_to_memory_callback(callback_context: CallbackContext):
    await callback_context.add_session_to_memory()


def build_trip_planner() -> LlmAgent:
    return LlmAgent(
        name="lab2_trip_agent",
        model="gemini-3-flash-preview",
        instruction=(
            "당신은 실시간 웹 검색과 이전 대화 기억을 활용하여 "
            "사용자 맞춤형 여행 계획을 수립하는 수석 플래너입니다.\n"
            "이전 대화 맥락이나 사용자의 취향을 기억에서 불러와 답변에 반영하세요."
        ),
        tools=[
            google_search,
            # LoadMemoryTool은 에이전트가 메모리에서 정보를 검색할 때 사용할 수 있는 도구입니다.
            # 명시적인 호출이 없는 한 이 도구는 사용되지 않습니다.
            LoadMemoryTool(),
            # PreloadMemoryTool은 시작과 매번 대화 과정에 자동으로 실행하여 메모리에서 정보를 불러옵니다.
            PreloadMemoryTool(),
        ],
        after_agent_callback=auto_save_session_to_memory_callback,
        generate_content_config=types.GenerateContentConfig(
            tool_config=types.ToolConfig(include_server_side_tool_invocations=True),
        ),
    )


root_agent = build_trip_planner()
