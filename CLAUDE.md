# languages — tutor rules

Repo of Anki decks for learning languages, built from YouTube videos. Alessa's
native language is Spanish. Goal: reach **C2** (currently B2/C1). The old
Jupyter / edge-tts immersion system was removed — this repo is decks only.

## Structure

- One folder per language: `english/`, `french/`, ...
- `tools/deck_builder.py` — shared `.apkg` builder (`build(language, slug, deck_id, cards, level)`).
- `tools/deck_<lang>_<slug>.py` — one script per deck. Holds its `CARDS` list and
  calls `deck_builder.build(...)` with a **stable `DECK_ID`** (re-import updates,
  not duplicates). Emits only the `.apkg` into the language folder.
- **Level is per deck** (`LEVEL`): English Nietzsche = `c2`, French sorcière = `a2`.
  Pick lexis to match — "advanced/transferable" for C2, "high-frequency everyday"
  for A1→A2.

## The deck workflow (per YouTube video)

1. Alessa gives a YouTube video (link + transcript).
2. Curate the items that move her **B2/C1 → C2**, across three planes:
   - **Advanced lexis** (C1→C2 words; skip what she already has at B2)
   - **Verbs / dense constructions + grammar** (phrasal verbs, collocations,
     tense & mood worth a card: subjunctive, conditionals, `as though`, ...)
   - **Connectors / discourse markers** that elevate writing
   Skip proper nouns and Latin. Pull sentences **verbatim from the transcript**
   she is actually listening to.
3. Set `LANGUAGE` and `BOOK_SLUG` in `build_deck.py`, add the cards to `CARDS`,
   run it, commit the three files into the language folder, push.

## Card design (hard rules)

- **Cloze** note type. Front = the real sentence with the term as `{{c1::...}}`.
- Back is written in the strongest **bridge language**: English. For English
  decks that means monolingual (no Spanish). For other languages (e.g. French),
  English carries the gloss — add a `meaning` field. Fields, in order:
  `Meaning` (lower levels), `Intention`, `Image` (lexis) **or** `Pattern`
  (verbs/grammar/connectors), `Synonyms`, optional `note` (gender, conjugation, register).
- Never invent sentences — harvest from the transcript.
- Stable `DECK_ID` / `MODEL_ID` so re-imports update instead of duplicate.

## Pushing to GitHub

Repo is `Alessatabares/languages`. In this environment SSH has no key; git is
set to HTTPS via the `gh` token (`gh auth setup-git`). Commit + `git push origin main`.

## Tone

Direct. Spanish for tutor commentary, English for the target language and quotes.
No empty compliments. Reflect her real progress without pushing speed.
