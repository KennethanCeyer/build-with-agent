from __future__ import annotations

from google.adk.agents import LlmAgent, SequentialAgent
from google.adk.agents.context import Context
from google.adk.models.llm_response import LlmResponse
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

# 1. 모임 기획 에이전트
meeting_planner = LlmAgent(
    name="meeting_planner",
    model="gemini-3.1-flash-lite-preview",
    instruction=(
        "당신은 모임을 기획하는 전문 매니저입니다. "
        "사용자의 요청에 따라 웹 검색과 과거 대화 기록을 참고하여 "
        "모임의 주제, 추천 시간, 최적의 장소를 상세히 정리하세요."
    ),
    tools=[google_search, *memory_retrieval_tools],
    generate_content_config=types.GenerateContentConfig(
        tool_config=types.ToolConfig(
            include_server_side_tool_invocations=True,
        ),
    ),
)

# 2. 디자인 전문가 에이전트
design_expert = LlmAgent(
    name="design_expert",
    model="gemini-3.1-flash-lite-preview",
    instruction=(
        "당신은 기획안에 시각적 영감을 더하는 디자인 전문가입니다.\n"
        "1. 반드시 generate_theme_image 도구를 호출하여 "
        "기획안의 컨셉에 어울리는 테마 이미지를 생성하세요.\n"
        "2. 이미지 생성이 완료된 후에는 어떤 느낌의 이미지가 생성되었는지 "
        "사용자에게 친절하게 설명하세요.\n"
        "3. 주의: 응답에 이미지 링크나 마크다운 이미지 태그(![]())를 직접 포함하지 마세요."
    ),
    tools=[generate_theme_image],
    generate_content_config=types.GenerateContentConfig(
        tool_config=types.ToolConfig(
            include_server_side_tool_invocations=True,
        ),
    ),
)


# 3. UI 카드 생성을 위한 콜백 함수
async def a2ui_builder_callback(
    context: Context,
    llm_response: LlmResponse,
) -> None:
    del context

    if not llm_response.content or not llm_response.content.parts:
        return None

    body = "\n".join(
        part.text for part in llm_response.content.parts if getattr(part, "text", None)
    )
    if not body:
        return None

    metadata = dict(llm_response.custom_metadata or {})
    metadata["a2ui"] = {
        "type": "meeting_plan_card",
        "title": "모임 기획안",
        "body": body,
    }
    llm_response.custom_metadata = metadata
    return None


# 4. 최종 결과 포매팅 에이전트
a2ui_formatter = LlmAgent(
    name="a2ui_formatter",
    model="gemini-3.1-flash-lite-preview",
    instruction=(
        "앞선 기획안과 디자인 결과를 종합하여 사용자에게 보여줄 최종 내용을 정리하세요. "
        "내용은 간결하고 매력적이어야 하며, 기획된 모임의 핵심 정보가 잘 드러나야 합니다."
    ),
    after_model_callback=a2ui_builder_callback,
)


# 5. 전체 협업 구조 정의 (SequentialAgent)
def build_meeting_manager() -> SequentialAgent:
    return SequentialAgent(
        name="lab3_meeting_agent",
        sub_agents=[
            meeting_planner,
            design_expert,
            a2ui_formatter,
        ],
    )


root_agent = build_meeting_manager()
