from google.adk.tools import google_search

__all__ = ["auto_save_session_to_memory_callback", "google_search"]


# TODO 1: session을 장기 기억에 저장하는 콜백을 완성하세요.
async def auto_save_session_to_memory_callback(callback_context):
    invocation_context = callback_context._invocation_context
    has_memory_attribute = hasattr(invocation_context, "memory_service")
    memory_service = invocation_context.memory_service if has_memory_attribute else None
    if memory_service:
        # 이 시점의 invocation_context에는 지금까지의 모든 session이 담겨 있습니다.
        # 메모리 서비스의 add_session_to_memory 함수는 이 session 객체를 통째로 받아
        # 데이터베이스나 파일 등 장기 저장소에 보관하는 역할을 합니다.

        # TODO: 현재 session을 장기 저장소에 저장하도록 코드를 완성하세요.
        # 힌트: invocation_context 안에는 session, 에이전트 이름인 name 등이 있습니다.
        await memory_service.add_session_to_memory(
            # invocation_context.xxxx (xxxx 부분을 알맞게 채우세요)
        )
