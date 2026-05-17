# english

Sistema personal de inmersión en inglés a partir de libros que me importan. Lectura + audio sincronizado + ejercicio escrito creativo + Anki, todo orquestado desde Claude Code sobre notebooks de Jupyter.

## Filosofía

El libro es un **pozo de lengua**, no una línea de tiempo. Cada sesión avanza solo cuando el material está exprimido. Comprensión primero, después activación, después memoria.

> *I'm not learning English. I'm learning how English places ideas, distance, and responsibility.*

## Cómo funciona una sesión

```
1. Audio + texto sincronizado en un notebook → escuchas hasta que te cansas
2. Corres stop_session() → se guarda dónde paraste
3. Yo (Claude) cosecho del tramo escuchado:
     • framings  (las 6 lentes cognitivas)
     • verbos / construcciones densas
     • tiempos / aspecto
4. Eliges 4-6 frases para trabajar
5. 1-2 preguntas perceptuales (sin corrección)
6. Ejercicio escrito creativo basado en el tema del tramo
7. 1-2 correcciones quirúrgicas + naming ligero
8. ≤8 cards a Anki (deck: english), tagged por plano
9. Pregunta de cierre — no la respondo yo
```

Siguiente día: abro nuevo notebook, sigo desde donde paraste. Cuando termina un libro, eliges otro y vuelve a empezar.

## Las 6 lentes (framings)

| Lente | Función |
|---|---|
| I. Focus & Reframing | entra a la idea de lado, no de frente |
| II. Distance & Safety | baja riesgo epistémico; posición antes que contenido |
| III. Positioning & Consequence | idea → implicación; corta el rambling |
| IV. Soft Assertion | existir sin declarar guerra a la realidad |
| V. Interaction & Flow | gestión de tiempo bajo carga (no significado) |
| VI. Limits & Openness | pensamiento inacabado; postura sin cierre |

## Estructura

```
english/
├── CLAUDE.md                       # reglas del tutor
├── tools/
│   ├── book_prep.py                # libro → chunks + mp3 (edge-tts)
│   ├── session.py                  # progress tracking + stop_session()
│   └── phrase_bank.py              # staging de cards para Anki
├── library/
│   └── <libro-slug>/
│       ├── source.txt              # texto limpio completo
│       ├── chunks/NN.txt           # texto por bloque
│       ├── audio/NN.mp3            # audio por bloque
│       └── progress.json           # estado del libro
├── sessions/
│   └── <libro-slug>/
│       └── YYYY-MM-DD_NN.ipynb     # un notebook por sesión
├── anki-pending/
│   └── YYYY-MM-DD.json             # cards en cola antes de empujar a Anki
└── .claude/skills/
    ├── book-prep/SKILL.md          # preparar un libro nuevo
    └── english-session/SKILL.md    # correr una sesión
```

## Requisitos

- Python 3.10+
- `edge-tts` (instalado con `pip install --user edge-tts`)
- Claude Code con el MCP `anki` configurado
- Anki Desktop abierto con AnkiConnect cuando se hacen los push de cards
- Un deck en Anki llamado `english`

## Empezar un libro nuevo

Dile a Claude: *"empecemos un libro nuevo: [título]"* → invoca el skill `book-prep`:
1. Busca el texto en dominio público (Gutenberg, Standard Ebooks, Wikisource)
2. Lo limpia y guarda en `library/<slug>/source.txt`
3. Corre `python3 -m tools.book_prep <slug>` → genera chunks + audio
4. Inicializa `progress.json`

## Empezar una sesión

Dile a Claude: *"sesión de [libro]"* → invoca el skill `english-session`:
1. Lee `progress.json` para saber dónde resumir
2. Crea el notebook con el siguiente bloque
3. Tú escuchas + paras cuando quieres
4. Claude cosecha → tú eliges → escribes → correcciones → Anki

## Libros

- **Nietzsche — On Truth and Falsity in their Ultramoral Sense** (Mügge tr., 1911) — 5 bloques, ~36 min audio total

---

Proyecto personal de Alessa. Sin pretensión de generalidad — diseñado para una sola cabeza y una sola forma de aprender.
