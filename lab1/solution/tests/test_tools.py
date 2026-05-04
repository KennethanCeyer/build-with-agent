from pathlib import Path

from lab1_trip_agent.tools import read_trip_notes, save_itinerary


def test_read_trip_notes_reads_existing_note(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    note_path = Path("data/trip-note.md")
    note_path.parent.mkdir()
    note_path.write_text("서울숲 산책\n성수 카페", encoding="utf-8")

    assert read_trip_notes() == "서울숲 산책\n성수 카페"


def test_read_trip_notes_handles_missing_note(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    assert "존재하지 않습니다" in read_trip_notes()


def test_save_itinerary_creates_output_file(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    result = save_itinerary("1일차 일정")

    assert result == "outputs/trip-plan.md에 일정이 저장되었습니다."
    assert Path("outputs/trip-plan.md").read_text(encoding="utf-8") == "1일차 일정"
