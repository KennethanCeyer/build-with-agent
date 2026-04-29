from google.adk.a2a.utils.agent_to_a2a import to_a2a  # noqa: F401
from google.adk.agents import LlmAgent
from google.adk.cli.utils.envs import load_dotenv

from ..tools import generate_theme_image  # noqa: F401

load_dotenv()

design_expert = LlmAgent(
    name="design_expert",
    model="gemini-3.1-flash-lite-preview",
    # TODO 5: 디자인 전문가의 역할과 generate_theme_image 도구 사용 지침을 작성하세요.
    # 힌트: 도구가 반환한 image_data_url을 최종 답변 마지막 줄에 보존하게 하세요.
    instruction=...,
    # TODO 6: 디자인 전문가가 사용할 도구를 등록하세요.
    tools=[...],
)

# TODO 7: 디자인 전문가 에이전트를 8001 포트의 A2A 앱으로 노출하세요.
a2a_app = ...
