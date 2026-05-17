---
name: english-session
description: Run one English immersion session for Alessa. Creates a Jupyter notebook with audio + text from the next block of her current book, waits for her to listen and stop, then runs the 8-step workflow (harvest → selection → perception → writing → naming → corrections → Anki). Use when she says "let's do an English session" or names a book she's already started.
---

# english-session

The full session workflow lives in this project's `CLAUDE.md` — read it first if you have not in this conversation. Below is just the operational checklist.

## Steps

1. Ask which book (or read default from latest `library/*/progress.json` modified). Read its `progress.json` to get `last_block` and `last_paragraph_in_block`. The next session resumes at the next block (`last_block + 1`) unless she says otherwise.

2. Create `sessions/<slug>/YYYY-MM-DD_NN.ipynb` from the template below. Fill in:
   - the audio path: `../../library/<slug>/audio/NN.mp3` (two levels up because of subfolder)
   - the full text of that block: `library/<slug>/chunks/NN.txt`, paragraph-numbered

3. Tell her the notebook path and tell her: "open it, press play, run the `stop_session(...)` cell when you stop."

4. **Wait.** When she comes back, she will tell you she stopped at paragraph X. Read `library/<slug>/chunks/NN.txt` and consider only paragraphs 1..X as the session's listened text.

5. **Harvest** (your work). Scan the listened text through three planes. Real phrases from the text only, never invented:
   - Framings — the 6 lenses (I–VI). One row per real occurrence. Empty row if a lens did not appear.
   - Verbs / dense constructions
   - Tenses / aspect

   Present as 3 markdown tables in a new notebook cell.

6. Ask her to pick **4–6 phrases**.

7. **Perception**: pick 1–2 of her chosen phrases. Ask only perceptual questions (function, register, implication). **No correction.**

8. **Written exercise**: give her one creative prompt derived from the *theme of what she listened to* (not academic). 5–6 lines. Constraint: use phrases from **≥3 of the 6 lenses**. Tell her not to edit while writing.

9. After she writes: **naming + 1–2 surgical corrections**. Light register/stance/function naming. Each correction with a one-line "why".

10. **Anki staging**: generate **≤8 cards**, mixing the three card types (book phrase cloze, her own use cloze, correction basic). Tag every card by plane (`lente::II-distance`, `verb::phrasal`, `tense::future-perfect`, `correction`, etc.) plus `libro::<slug>` and `source::book` or `source::own-writing`. Append cell that calls `phrase_bank.stage_cards(cards, session_id=...)`.

11. Closing question: *"En qué situaciones de tu semana esta lengua te serviría?"* — do not answer for her.

## Notebook template

Each session notebook has these cells in order:

```
# (markdown) Header — session metadata table
# (code) Audio player: Audio('../library/<slug>/audio/NN.mp3')
# (markdown) Text of block, paragraph-numbered as a blockquote
# (code) stop_session(book='<slug>', block=NN, last_paragraph=?, elapsed_min=?)
# --- below are added BY YOU after she stops ---
# (markdown) Harvest tables (3 planes)
# (markdown) Her selection (she fills)
# (markdown) Perception questions + her answer
# (markdown) Written exercise prompt + her writing
# (markdown) Naming + corrections
# (code) cards list + phrase_bank.stage_cards(cards)
# (markdown) Closing question + state-at-close table
```

## Hard rules (mirror of CLAUDE.md)

- No corrections in steps 1–8.
- Harvest only what the text actually contains.
- Max 8 cards per session.
- Prompts are creative, derived from the block's theme.
- Speaking practice is done outside Claude Code; if she pastes a voice transcript, treat it like writing.
