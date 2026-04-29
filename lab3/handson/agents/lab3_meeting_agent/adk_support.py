from __future__ import annotations

import os
from pathlib import Path


def expose_google_api_key(base_dir: Path) -> None:
    env_path = _find_env_file(base_dir)
    if env_path is None:
        return

    for line in env_path.read_text(encoding="utf-8").splitlines():
        if not line.startswith("GOOGLE_API_KEY="):
            continue
        value = line.split("=", 1)[1].strip()
        if value and value != "본인_API_키":
            os.environ.setdefault("GOOGLE_API_KEY", value)


def resolve_output_dir(project_root: Path) -> Path:
    output_dir = project_root / "outputs"
    output_dir.mkdir(exist_ok=True)
    return output_dir


def save_backup_plan_payload(
    title: str,
    agenda: str,
    source_notes: str,
    output_dir: Path,
) -> dict[str, object]:
    output_path = output_dir / "backup-meetup-plan.md"
    output_path.write_text(
        f"# {title}\n\n## 진행 계획\n{agenda}\n\n## 참고 메모\n{source_notes}\n",
        encoding="utf-8",
    )
    return {"ok": True, "path": str(output_path)}


def save_group_chat_update_payload(
    title: str,
    message: str,
    source_notes: str,
    output_dir: Path,
) -> dict[str, object]:
    output_path = output_dir / "group-chat-update.md"
    output_path.write_text(
        f"# {title}\n\n{message}\n\n## 참고 메모\n{source_notes}\n",
        encoding="utf-8",
    )
    return {"ok": True, "path": str(output_path)}


def _find_env_file(base_dir: Path) -> Path | None:
    for candidate_base in [base_dir, *base_dir.parents]:
        candidate = candidate_base / ".env"
        if candidate.exists():
            return candidate
    return None
