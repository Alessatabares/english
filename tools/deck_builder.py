"""Shared Anki .apkg builder for the languages repo.

One folder per language; one .apkg per deck. Each deck script (e.g.
deck_english_nietzsche.py) defines its CARDS and calls build().

Card dict fields (all optional except text + intention):
  plane     : "vocab" | "verb-construction" | "grammar" | "connector" | "expression"
  text      : the real sentence from the video, with {{c1::term}} clozed
  meaning   : English gloss of the term  (use for lower levels, e.g. A2 French)
  intention : when you reach for it / the job it does (English)
  image     : a vivid mental picture (concrete lexis)
  pattern   : a reusable writing/speaking template (verbs, grammar, connectors)
  synonyms  : alternatives / register equivalents
  note      : one-line nuance (gender, conjugation, register, contrast)
"""

from pathlib import Path

MODEL_ID = 1987452311  # shared note type across every deck
PLANE_ORDER = ["vocab", "verb-construction", "grammar", "connector", "expression"]

_CSS = (".card{font-family:Georgia,serif;font-size:20px;color:#222;"
        "text-align:left;max-width:640px;margin:0 auto;line-height:1.5}"
        ".cloze{font-weight:bold;color:#1565c0}"
        "#answer{margin:14px 0}b{color:#000}i{color:#666}")


def back_html(c):
    parts = []
    if c.get("meaning"):
        parts.append(f"<b>Meaning:</b> {c['meaning']}")
    parts.append(f"<b>Intention:</b> {c['intention']}")
    if c.get("image"):
        parts.append(f"<b>Image:</b> {c['image']}")
    if c.get("pattern"):
        parts.append(f"<b>Pattern:</b> {c['pattern']}")
    if c.get("synonyms"):
        parts.append(f"<b>Synonyms:</b> {c['synonyms']}")
    if c.get("note"):
        parts.append(f"<i>{c['note']}</i>")
    return "<br>".join(parts)


def build(language, slug, deck_id, cards, level):
    """Write <root>/<language>/<slug>.apkg. deck_id must be stable per deck."""
    import genanki

    root = Path(__file__).resolve().parent.parent
    out_dir = root / language
    out_dir.mkdir(exist_ok=True)

    model = genanki.Model(
        MODEL_ID, "Immersion Cloze",
        fields=[{"name": "Text"}, {"name": "Back Extra"}],
        templates=[{
            "name": "Cloze",
            "qfmt": "{{cloze:Text}}",
            "afmt": "{{cloze:Text}}<hr id=answer>{{Back Extra}}",
        }],
        css=_CSS,
        model_type=genanki.Model.CLOZE,
    )

    deck = genanki.Deck(deck_id, f"{language}::{slug}")
    for c in cards:
        deck.add_note(genanki.Note(
            model=model,
            fields=[c["text"], back_html(c)],
            tags=[slug, level, c["plane"]],
        ))

    path = out_dir / f"{slug}.apkg"
    genanki.Package(deck).write_to_file(str(path))

    counts = {p: len([c for c in cards if c["plane"] == p]) for p in PLANE_ORDER}
    counts = {p: n for p, n in counts.items() if n}
    print(f"Wrote {len(cards)} cards -> {path.relative_to(root)}")
    print("  planes:", counts)
    return path
