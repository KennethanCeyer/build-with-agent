"""`python -m lab2_trip_agent`로 에이전트 로딩만 확인합니다."""

from .agent import root_agent

print(f"ADK agent loaded: {root_agent.name}")
