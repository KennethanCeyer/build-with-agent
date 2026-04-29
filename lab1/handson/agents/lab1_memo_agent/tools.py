from __future__ import annotations

from pathlib import Path


def read_trip_notes() -> str:
    """기존에 작성된 여행 메모 파일(data/trip-note.md)을 읽어옵니다."""
    note_path = Path("data/trip-note.md")
    if note_path.exists():
        return note_path.read_text(encoding="utf-8")
    return "여행 메모 파일이 존재하지 않습니다."


def save_itinerary(content: str) -> str:
    """에이전트가 정리한 최종 일정을 파일로 저장합니다."""
    output_path = Path("outputs/trip-plan.md")
    output_path.parent.mkdir(exist_ok=True)
    output_path.write_text(content, encoding="utf-8")
    return f"{output_path}에 일정이 저장되었습니다."
