from google.adk.agents import LlmAgent

from lab1_memo_agent.agent import root_agent


def test_agent_structure():
    assert isinstance(root_agent, LlmAgent)
    assert root_agent.name == "lab1_memo_agent"
    assert root_agent.model == "gemini-3-flash-preview"
    assert len(root_agent.tools) == 2

    tool_names = [tool.__name__ for tool in root_agent.tools]
    assert tool_names == ["read_trip_notes", "save_itinerary"]


def test_agent_instruction():
    assert "여행 메모" in root_agent.instruction
    assert "정리" in root_agent.instruction
    assert "저장" in root_agent.instruction
