from __future__ import annotations
from google.adk.agents import LlmAgent

from .tools import read_trip_notes, save_itinerary  # noqa: F401


def build_travel_agent() -> LlmAgent:
    # LlmAgent는 모델에게 인스트럭션을 부여하고 필요한 도구를 연결하여 작업을 수행합니다.
    return LlmAgent(
        name="trip_memo_agent",
        # TODO 1: 아래 모델 중 이 실습에 적합한 모델 이름을 선택하세요.
        # [gemini-3.0-flash, gemini-3.1-flash-lite-preview,
        # gemini-3.1-pro-preview]
        model="",
        # TODO 2: 인스트럭션을 작성하세요.
        # 힌트: 여행 메모를 읽고 정리하여 저장하는 역할과 작업 순서를 명시하세요.
        instruction=("당신은 ... " "... 하세요."),
        # TODO 3: 상단에서 가져온 두 가지 도구(read_trip_notes, save_itinerary)를 리스트에 넣으세요.
        # 도구는 에이전트가 외부 세계와 소통하거나 특정 작업을 수행할 때 사용하는 수단입니다.
        tools=[],
    )


root_agent = build_travel_agent()
