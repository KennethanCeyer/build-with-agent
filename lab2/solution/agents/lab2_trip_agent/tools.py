from google.adk.tools import google_search

__all__ = ["auto_save_session_to_memory_callback", "google_search"]


async def auto_save_session_to_memory_callback(callback_context):
    """
    대화가 끝날 때마다 에이전트의 세션을 장기 기억에 저장합니다.
    이 콜백은 agent.py에서 에이전트의 after_agent_callback으로 등록됩니다.
    """
    invocation_context = callback_context._invocation_context
    if hasattr(invocation_context, "memory_service") and invocation_context.memory_service:
        await invocation_context.memory_service.add_session_to_memory(invocation_context.session)
