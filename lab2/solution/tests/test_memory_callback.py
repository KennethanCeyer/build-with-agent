import asyncio
from types import SimpleNamespace

from lab2_trip_agent.tools import auto_save_session_to_memory_callback


class RecordingMemoryService:
    def __init__(self):
        self.sessions = []

    async def add_session_to_memory(self, session):
        self.sessions.append(session)


def test_callback_saves_current_session_to_memory():
    memory_service = RecordingMemoryService()
    session = object()
    callback_context = SimpleNamespace(
        _invocation_context=SimpleNamespace(
            memory_service=memory_service,
            session=session,
        )
    )

    asyncio.run(auto_save_session_to_memory_callback(callback_context))

    assert memory_service.sessions == [session]


def test_callback_skips_when_memory_service_is_missing():
    callback_context = SimpleNamespace(
        _invocation_context=SimpleNamespace(
            memory_service=None,
            session=object(),
        )
    )

    asyncio.run(auto_save_session_to_memory_callback(callback_context))
