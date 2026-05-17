---
name: book-prep
description: Prepare a new book for English immersion sessions. Downloads/cleans the text, splits it into ~10-min audio blocks, generates one mp3 per block with edge-tts, and initializes progress.json. Use when Alessa says "let's start a new book" or names a new title.
---

# book-prep

Triggered when Alessa wants to start a new book.

## Steps

1. Ask her for the book title and (optionally) preferred voice. Confirm the slug you will use (kebab-case, e.g. `nietzsche-truth-lies`).
2. Find a public-domain English text. Preferred sources: Project Gutenberg, Standard Ebooks, Wikisource. If only a copyrighted edition exists, ask her whether she has a legal copy to provide.
3. Download the raw text. Save the cleaned essay/book body (strip Gutenberg headers/footers, license, ToC) to `library/<slug>/source.txt`.
4. Run the chunker + TTS:

   ```bash
   cd /home/alessa/projects/english-immersion
   python3 -m tools.book_prep <slug>
   ```

   This creates `library/<slug>/chunks/NN.txt` and `library/<slug>/audio/NN.mp3` (one per ~10-min block).

5. Initialize `library/<slug>/progress.json`:

   ```json
   {"book": "<slug>", "last_block": 0, "last_paragraph_in_block": 0, "sessions": []}
   ```

6. Confirm to Alessa: book title, slug, number of blocks, total estimated minutes. Ask if she wants to start the first session now (→ invoke `english-session`).

## Voice choice

Default: `en-US-AriaNeural`. Other good options:
- `en-US-GuyNeural` — neutral male
- `en-GB-RyanNeural` — British male
- `en-GB-SoniaNeural` — British female

To list all voices: `edge-tts --list-voices | grep en-`.

## Rules

- Never use copyrighted translations unless Alessa provides them legally.
- Save raw download to `/tmp/<slug>_raw.txt` so you can re-extract if cleaning was wrong.
- If the work is very long (>3h audio), warn her — she may want to pick a section/chapter rather than the whole thing.
