from __future__ import annotations

from google.adk.a2a.utils.agent_to_a2a import to_a2a
from google.adk.agents import LlmAgent
from google.genai import types

from ..tools import generate_theme_image

design_expert = LlmAgent(
    name="design_expert",
    model="gemini-3.1-flash-lite-preview",
    instruction=(
        "당신은 모임 디자인 전문가입니다. "
        "반드시 generate_theme_image 도구를 호출하여 기획안에 어울리는 이미지를 생성하세요. "
        "이미지 생성 후에는 이미지가 생성되었다는 내용을 친절하게 안내하세요. "
        "텍스트 응답에 이미지 링크나 마크다운 이미지 태그는 포함하지 마세요."
    ),
    tools=[generate_theme_image],
    generate_content_config=types.GenerateContentConfig(
        tool_config=types.ToolConfig(
            include_server_side_tool_invocations=True,
        ),
    ),
)

a2a_app = to_a2a(design_expert)
