from google.adk.agents import LlmAgent
from google.adk.tools.preload_memory_tool import PreloadMemoryTool

from lab2_trip_agent.agent import root_agent
from lab2_trip_agent.tools import auto_save_session_to_memory_callback


def test_agent_structure():
    assert isinstance(root_agent, LlmAgent)
    assert root_agent.name == "trip_planner"
    assert root_agent.model == "gemini-3.1-pro-preview"
    assert len(root_agent.tools) == 2

    tool_names = [getattr(tool, "__name__", getattr(tool, "name", "")) for tool in root_agent.tools]
    assert "google_search" in tool_names
    assert any(isinstance(tool, PreloadMemoryTool) for tool in root_agent.tools)
    assert root_agent.after_agent_callback is auto_save_session_to_memory_callback


def test_agent_instruction():
    assert "검색" in root_agent.instruction
    assert "플래너" in root_agent.instruction
    assert "기억" in root_agent.instruction
