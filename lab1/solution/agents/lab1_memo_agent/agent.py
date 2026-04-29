from __future__ import annotations

from google.adk.agents import Agent

from .tools import read_trip_notes, save_itinerary


def build_travel_agent() -> Agent:
    return Agent(
        name="trip_memo_agent",
        model="gemini-3.1-flash-lite-preview",
        instruction="당신은 여행 메모를 읽고 일정을 정리하여 저장하는 비서입니다.",
        tools=[
            read_trip_notes,
            save_itinerary,
        ],
    )


root_agent = build_travel_agent()
