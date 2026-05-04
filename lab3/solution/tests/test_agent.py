from google.adk.agents import SequentialAgent

from lab3_meeting_agent.agent import (
    root_agent,
)


def test_agent_structure():
    assert isinstance(root_agent, SequentialAgent)
    assert root_agent.name == "lab3_meeting_agent"
    assert len(root_agent.sub_agents) == 3

    sub_agent_names = [agent.name for agent in root_agent.sub_agents]
    assert sub_agent_names == [
        "meeting_planner",
        "design_expert",
        "a2ui_formatter",
    ]


def test_design_expert_is_local_and_has_image_tool():
    """design_expert가 원격이 아닌 로컬 에이전트이며
    이미지 생성 도구를 가지고 있는지 확인합니다."""
    expert = root_agent.sub_agents[1]
    assert expert.name == "design_expert"
    tool_names = [getattr(t, "__name__", getattr(t, "name", "")) for t in expert.tools]
    assert "generate_theme_image" in tool_names
