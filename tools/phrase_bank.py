"""Stage Anki cards from a session for later push via the anki MCP."""
from __future__ import annotations
import csv
import json
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PENDING = ROOT / "anki-pending"


def stage_cards(cards: list[dict], session_id: str | None = None) -> Path:
    """Write cards to anki-pending/<date>_<session>.json so Claude can push them via MCP.

    Each card should have: type ('cloze' | 'basic'), front, (back for basic), tags (list).
    """
    PENDING.mkdir(parents=True, exist_ok=True)
    sid = session_id or str(date.today())
    out = PENDING / f"{sid}.json"
    payload = {"session_id": sid, "count": len(cards), "cards": cards}
    out.write_text(json.dumps(payload, indent=2, ensure_ascii=False))
    print(f"✓ {len(cards)} cards staged at {out.relative_to(ROOT)}")
    print("  → ask Claude to push them: 'push pending cards to Anki'")
    return out
