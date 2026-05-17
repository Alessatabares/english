"""Chunk a cleaned source.txt into ~10-min blocks and generate one mp3 per block with edge-tts."""
from __future__ import annotations
import asyncio
import re
import subprocess
from pathlib import Path

import edge_tts

ROOT = Path(__file__).resolve().parent.parent
LIBRARY = ROOT / "library"

DEFAULT_VOICE = "en-US-AriaNeural"
WORDS_PER_BLOCK = 1500  # ~10 min at 150 wpm TTS


def _split_paragraphs(text: str) -> list[str]:
    text = re.sub(r"\n{3,}", "\n\n", text.strip())
    parts = [p.strip() for p in text.split("\n\n") if p.strip()]
    return parts


def chunk_text(source_text: str, words_per_block: int = WORDS_PER_BLOCK) -> list[list[str]]:
    """Group paragraphs into blocks of approximately words_per_block words.

    Returns a list of blocks; each block is a list of paragraphs.
    """
    paragraphs = _split_paragraphs(source_text)
    blocks: list[list[str]] = []
    current: list[str] = []
    current_words = 0
    for p in paragraphs:
        w = len(p.split())
        if current_words + w > words_per_block and current:
            blocks.append(current)
            current, current_words = [], 0
        current.append(p)
        current_words += w
    if current:
        blocks.append(current)
    return blocks


async def _tts_one(text: str, out_path: Path, voice: str) -> None:
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(str(out_path))


def prep_book(book_slug: str, voice: str = DEFAULT_VOICE) -> dict:
    """Read library/<slug>/source.txt, chunk it, write chunks/NN.txt + audio/NN.mp3.

    Returns a summary dict.
    """
    book_dir = LIBRARY / book_slug
    src = book_dir / "source.txt"
    if not src.exists():
        raise FileNotFoundError(f"Missing {src}")

    chunks_dir = book_dir / "chunks"
    audio_dir = book_dir / "audio"
    chunks_dir.mkdir(parents=True, exist_ok=True)
    audio_dir.mkdir(parents=True, exist_ok=True)

    blocks = chunk_text(src.read_text())
    summary = {"book": book_slug, "blocks": []}

    for i, paragraphs in enumerate(blocks, start=1):
        text = "\n\n".join(paragraphs)
        chunk_path = chunks_dir / f"{i:02d}.txt"
        audio_path = audio_dir / f"{i:02d}.mp3"
        chunk_path.write_text(text)
        asyncio.run(_tts_one(text, audio_path, voice))
        summary["blocks"].append({
            "index": i,
            "paragraphs": len(paragraphs),
            "words": sum(len(p.split()) for p in paragraphs),
            "chunk_path": str(chunk_path.relative_to(ROOT)),
            "audio_path": str(audio_path.relative_to(ROOT)),
        })
        print(f"  block {i:02d}: {summary['blocks'][-1]['words']} words → {audio_path.name}")

    return summary


if __name__ == "__main__":
    import sys
    slug = sys.argv[1] if len(sys.argv) > 1 else "nietzsche-truth-lies"
    result = prep_book(slug)
    print(f"\n✓ {len(result['blocks'])} blocks generated for {slug}")
