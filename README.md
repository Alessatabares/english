# languages

Anki decks for learning languages, built from YouTube videos. One folder per
language. Each deck targets the **B2/C1 → C2** jump: advanced lexis, dense
verb/grammar constructions, and connectors that elevate writing.

## Structure

```
languages/
├── english/
│   └── nietzsche-truth-lies.apkg      # C2
├── french/
│   └── sorciere-rue-mouftard.apkg     # A1 -> A2
└── tools/
    ├── deck_builder.py                # shared .apkg builder
    ├── deck_english_nietzsche.py      # one script per deck = its card list
    └── deck_french_sorciere.py
```

## Each deck = one `.apkg`

**Download and double-click** → imports straight into Anki. That's it.

## Card design

Cloze note type. Front = a real sentence from the video with the term hidden.
Back (all in English, on purpose — monolingual = transfer):

- **Intention** — when you reach for the word / the job it does
- **Image** (lexis) or **Pattern** (verbs, grammar, connectors → a template you can reuse when *you* write)
- **Synonyms** — alternatives and register equivalents

## Workflow (per video)

1. Pick a YouTube video and grab its transcript.
2. Curate the C1→C2 items across three planes: advanced lexis · verbs &
   grammar · connectors. Skip what's already B2, plus proper nouns and Latin.
3. Add them to a `CARDS` list and run the generator.
4. Commit the `.apkg` into the language folder.

The back is written in the strongest bridge language: **English** for both decks
(for French, English carries the gloss + when-to-use). The level is per deck
(English = C2, French = A1→A2), so "advanced" vs "everyday" is chosen to match.

```bash
pip install -r requirements.txt
python tools/deck_english_nietzsche.py   # -> english/nietzsche-truth-lies.apkg
python tools/deck_french_sorciere.py     # -> french/sorciere-rue-mouftard.apkg
```
