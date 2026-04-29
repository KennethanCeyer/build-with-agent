from google.adk.a2a.utils.agent_to_a2a import to_a2a
from google.adk.agents import LlmAgent
from google.adk.cli.utils.envs import load_dotenv

from ..tools import generate_theme_image

load_dotenv()

design_expert = LlmAgent(
    name="design_expert",
    model="gemini-3.1-flash-lite-preview",
    instruction=(
        "당신은 수석 UI/UX 디자이너입니다. "
        "사용자가 요청하는 모임 테마와 어울리는 디자인 방향을 제안하세요. "
        "모임의 분위기를 잘 나타낼 수 있는 테마 이미지를 "
        "'generate_theme_image' 도구를 사용하여 반드시 생성해야 합니다. "
        "도구가 반환한 image_data_url 값은 최종 답변의 마지막 줄에 "
        "'image_data_url: <값>' 형식으로 그대로 포함하세요."
    ),
    tools=[generate_theme_image],
)

a2a_app = to_a2a(design_expert, port=8001)
