from google.adk.agents import SequentialAgent
from google.adk.tools.load_memory_tool import load_memory
from google.adk.tools.preload_memory_tool import PreloadMemoryTool

from lab3_meeting_agent.agent import (
    meeting_planner,
    root_agent,
)
from lab3_meeting_agent.tools import auto_save_session_to_memory_callback


def test_agent_structure():
    assert isinstance(root_agent, SequentialAgent)
    assert root_agent.name == "root_agent"
    assert len(root_agent.sub_agents) == 3

    sub_agent_names = [agent.name for agent in root_agent.sub_agents]
    assert sub_agent_names == [
        "meeting_planner",
        "design_expert",
        "a2ui_formatter",
    ]


def test_meeting_planner_uses_search_memory_and_callback():
    tool_names = [
        getattr(tool, "__name__", getattr(tool, "name", "")) for tool in meeting_planner.tools
    ]
    assert "google_search" in tool_names
    assert any(isinstance(tool, PreloadMemoryTool) for tool in meeting_planner.tools)
    assert any(tool is load_memory for tool in meeting_planner.tools)
    assert meeting_planner.after_agent_callback is auto_save_session_to_memory_callback


def test_design_expert_is_local_and_has_image_tool():
    """design_expert가 원격이 아닌 로컬 에이전트이며
    이미지 생성 도구를 가지고 있는지 확인합니다."""
    expert = root_agent.sub_agents[1]
    assert expert.name == "design_expert"
    tool_names = [getattr(t, "__name__", getattr(t, "name", "")) for t in expert.tools]
    assert "generate_theme_image" in tool_names


def test_a2ui_formatter_has_builder_callback():
    formatter = root_agent.sub_agents[2]
    assert formatter.name == "a2ui_formatter"
    assert formatter.after_model_callback.__name__ == "a2ui_builder_callback"
