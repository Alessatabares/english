# english · motor

The **structural engine** of English: the high-frequency, closed-class core that
carries 70%+ of everything spoken and written. This is the foundation deck — the
layer you want automatic before the advanced reading decks (e.g. Nietzsche C2).

- **File:** `motor.apkg` → imports as the Anki deck `english::motor`
- **Source script:** `../../tools/deck_english_motor.py`
- **Cards:** 75 · monolingual English · Cloze
- **Stable `DECK_ID`** → re-importing updates the cards, never duplicates.

## Card design

Cloze note. Front = a short, vivid sentence with the key piece hidden in
`{{c1::…}}` (active recall). Back, all in English:

- **Intention** — the job the word does in the sentence.
- **Pattern** — the reusable, generative frame (one card → many sentences).
- **Image** — a concrete mental picture (only for concrete words).
- **note** — the contrast with its confusable neighbour.

Sentences are **invented on purpose** (a foundation deck has no source video):
this is the declared exception to the repo's "harvest from source" rule, which is
why `SOURCE_URL` is empty.

## What it covers — structural map

8 subsystems (= tags / `plane`). Study one subsystem at a time.

| Tag (`plane`) | Subsystem | Covers |
|---|---|---|
| `grammar` | Pronouns & determiners | `it`/`they`, `this/that`, relative `who/which`, `a/the`, `some/any`, `many/much` — subjecthood, definiteness, count vs mass |
| `grammar` | Prepositions | `in/on/at`, `to/from`, `of`, `with/for/by/about`, `between`, `through` — space/time/logic, passive agent |
| `grammar` | Auxiliaries & modals | do-support, `be+ing`, passive, present perfect, `going to`, `will` + `can/could/would/should/must/might` — the whole finite-verb engine |
| `expression` | Generative frames | `there is/are`, the three conditionals, `the more…the more`, `used to`, `would rather`, `had better` |
| `connector` | Basic connectors | `and/but/or/so` + `because/although/when/while/that` |
| `verb-construction` | Light verbs | `get/make/take/do/go/have/give/keep/let/want` + collocations & catenatives |
| `grammar` | Negation, quantity, frequency | `not`, `nothing/never`, frequency-adverb position, `very/too/so`, `already/yet/still`, `just` |
| `grammar` | Wh- questions | `what/why/how/where/when/who/whose/which` + subject-aux inversion |

**Out of scope (by design):** topical vocabulary, C1→C2 lexis, high-register
discourse connectors, rhetorical moves — those belong to the elevation decks
built from real sources.

## Workflow

```
# 1. Build the deck (from repo root, venv active)
source .venv/bin/activate
python tools/deck_english_motor.py        # -> english/motor/motor.apkg

# 2. Import
#    double-click english/motor/motor.apkg  -> deck "english::motor" in Anki

# 3. Study one subsystem at a time, by tag, e.g.
#    tag:expression          (the generative frames)
#    tag:verb-construction   (the light verbs)

# 4. Sync (local + GitHub)
git add tools/deck_english_motor.py english/motor/
git commit -m "english/motor: <change>"
git push origin main
```

To edit cards: change `CARDS` in `tools/deck_english_motor.py`, re-run the build,
re-import. The stable `DECK_ID` makes Anki update the existing cards in place.

## Architecture

```
elevation decks  → essays + deep conversation (C2), harvested from real sources
─────────────────────────────────────────────────────────────────────────────
motor (this deck) → structural skeleton + light verbs + frames (automaticity)
```
