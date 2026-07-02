# french · motor

The **structural engine** of French: the high-frequency core that carries most of
everyday French. This is the foundation deck — the layer to make automatic before
the reading decks (e.g. the sorcière tale).

- **File:** `motor.apkg` → imports as the Anki deck `french::motor`
- **Source script:** `../../tools/deck_french_motor.py`
- **Cards:** 29 · French target, English gloss (bridge language) · Cloze
- **Stable `DECK_ID`** → re-importing updates the cards, never duplicates.

## Card design — pattern-centric

Same model as the English motor. The learning unit is the **pattern**, not the word:

```
FORK (the discriminator) → VARIATION (several examples) → COMPRESSION (the rule)
```

Two card shapes, same Cloze note:

1. **Contrast set** — a fork with a confusable neighbour (`le` vs `la`, `à` vs
   `de`, `passé composé` vs `imparfait`). Front = a **title** naming the fork +
   3–6 varied example lines, each with its pivot in `{{c1::…}}`. Every blank is
   `c1`, so it's **one card** ("fill every blank"), and the answers differ line
   to line — you have to actually discriminate.
2. **Simple** — an item with no obvious neighbour (`chez`, `il faut`). Front =
   1–2 clozed lines; keeps the English `meaning` gloss.

Back, in English (the bridge):

- **Rule** — the discriminator headline (red, on top): the one line to compress.
- **Meaning** — the English gloss (simple cards).
- **Intention** — the job the pattern does.
- **Pattern** / **note** — the reusable frame, or the gender trap / neighbour.

Sentences are **invented on purpose** (a foundation deck has no source video):
the declared exception to the repo's "harvest from source" rule, which is why
`SOURCE_URL` is empty.

## What it covers — structural map (and how it differs from English)

French has load-bearing structures English lacks; the motor is built around them.
Most rows are **contrast sets** — the fork is right there in the title.

| Tag (`plane`) | Subsystem | Forks & items |
|---|---|---|
| `grammar` | Gender & articles | `le` vs `la` vs `les`, `un/une/des`, partitive `du/de la/des`, contractions `au/du` |
| `grammar` | Subject pronouns | `on` vs `nous`, `tu` vs `vous`, gendered `il/elle` for objects |
| `verb-construction` | Pillar verbs | `être / avoir / aller / faire`, plus être/avoir plural forms |
| `grammar` | Present tense | regular `-ER` vs `-IR` endings |
| `grammar` | Past | `passé composé` vs `imparfait`; auxiliary `avoir` vs `être` + agreement |
| `grammar` | Future & politeness | `je veux` vs `je voudrais`, futur proche (`aller` + inf) |
| `grammar` | Negation | two-part `ne … pas / jamais / rien / personne` |
| `grammar` | Pre-verbal pronouns | `le/la/les` vs `y` vs `en` |
| `grammar` | Questions | 3 ways to ask (`est-ce que` / inversion / intonation), question words |
| `grammar` | Prepositions | `à` vs `de` (+ contractions), `chez`, `en` |
| `expression` | Impersonal frames | `c'est` vs `il est`, `il y a`, `il faut` |
| `connector` | Connectors | `et/mais/ou`, `parce que` vs `donc`, `si` vs `quand` |
| `grammar` | Adjectives | position (after vs BAGS before) + gender/number agreement |
| `verb-construction` | Reflexive verbs | `je me lève`, `je m'appelle` |

**Out of scope (by design):** topical vocabulary, advanced lexis, the subjunctive,
literary tenses — those belong to the reading/elevation decks.

## Workflow

```
# 1. Build the deck (from repo root, venv active)
source .venv/bin/activate
python3 tools/deck_french_motor.py        # -> french/motor/motor.apkg

# 2. Import
#    double-click french/motor/motor.apkg  -> deck "french::motor" in Anki

# 3. Study one subsystem at a time, by tag, e.g.
#    tag:verb-construction   (the pillar verbs + reflexives)
#    tag:expression          (c'est / il y a / il faut)

# 4. Sync (local + GitHub)
git add tools/deck_french_motor.py french/motor/
git commit -m "french/motor: <change>"
git push origin main
```

To edit cards: change `CARDS` in `tools/deck_french_motor.py`, re-run the build,
re-import. The stable `DECK_ID` makes Anki update the existing cards in place.

## Architecture

```
elevation decks  → real French sources (tales, talks), harvested verbatim
─────────────────────────────────────────────────────────────────────────
motor (this deck) → gender, articles, conjugation, frames (automaticity)
```
