from lab3_meeting_agent.expert.agent import a2a_app, design_expert


def test_design_expert_is_exposed_as_a2a_app():
    assert design_expert.name == "design_expert"
    assert "디자인" in design_expert.instruction
    assert a2a_app is not None
