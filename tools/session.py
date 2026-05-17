"""Session state: progress tracking per book + stop_session hook for notebooks."""
from __future__ import annotations
import json
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LIBRARY = ROOT / "library"


def _progress_path(book: str) -> Path:
    return LIBRARY / book / "progress.json"


def load_progress(book: str) -> dict:
    p = _progress_path(book)
    if not p.exists():
        return {"book": book, "last_block": 0, "last_paragraph_in_block": 0, "sessions": []}
    return json.loads(p.read_text())


def stop_session(book: str, block: int, last_paragraph: int, elapsed_min: float | int = 0) -> dict:
    """Called from the notebook when the user stops listening.

    Updates progress.json with where the user stopped and appends a session record.
    Returns the updated progress dict.
    """
    progress = load_progress(book)
    progress["last_block"] = block
    progress["last_paragraph_in_block"] = last_paragraph
    progress["sessions"].append({
        "date": str(date.today()),
        "block": block,
        "last_paragraph": last_paragraph,
        "elapsed_min": elapsed_min,
    })
    _progress_path(book).write_text(json.dumps(progress, indent=2, ensure_ascii=False))
    print(f"✓ Progress saved. Next session resumes at block {block}, paragraph {last_paragraph + 1}.")
    return progress
