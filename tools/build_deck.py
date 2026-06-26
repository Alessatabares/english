"""Build an Anki-importable deck from a curated card list.

Each card targets the C1 -> C2 jump: advanced lexis, dense verb/grammar
constructions, and discourse connectors that elevate written English.
All back content is in English on purpose (monolingual loop = transfer).

Run:  python tools/build_deck.py
Emits (next to this repo root, under decks/):
  - <slug>.tsv  -> import into Anki, note type "Cloze", fields Text / Back Extra,
                   field separator = Tab, "Allow HTML in fields" = ON, tags column 3.
  - <slug>.md   -> human-readable, grouped by plane (renders on GitHub).
"""

from pathlib import Path

BOOK_SLUG = "nietzsche-truth-lies"
BOOK_TITLE = "On Truth and Lies in a Nonmoral Sense (Breazeale tr.)"
SOURCE = "YouTube audiobook, W. A. Haussmann reading / Breazeale translation"

# Each card:
#   term      : the target item (also the answer in the cloze)
#   text      : the real sentence with {{c1::term}} clozed
#   intention : when you reach for it / the job it does (English)
#   image     : a vivid mental picture (lexis) OR ""  -> use pattern instead
#   pattern   : a reusable writing template (verbs/grammar/connectors) OR ""
#   synonyms  : alternatives / register equivalents OR ""
#   note      : optional one-line nuance (e.g. contrast with a near-synonym)
#   plane     : "vocab" | "verb-construction" | "grammar" | "connector"

CARDS = [
    # ============ PLANE A: ADVANCED LEXIS (C1 -> C2) ============
    dict(plane="vocab", term="mendacious",
         text="That was the most arrogant and {{c1::mendacious}} minute of world history.",
         intention="Condemn something as false by its very nature — heavier and more moral than 'untrue'; you reach for it to accuse, not just to describe.",
         image="A mouth that keeps producing cracked, counterfeit words.",
         synonyms="deceitful, untruthful, lying, false"),
    dict(plane="vocab", term="ephemeral",
         text="The intellect was certainly allotted to these most unfortunate, delicate and {{c1::ephemeral}} beings.",
         intention="Stress that something lasts only a brief moment, with an elevated / poetic tone.",
         image="A mayfly that lives a single day; a soap bubble.",
         synonyms="fleeting, short-lived, transient, momentary",
         note="ephemeral = poetic, lasts very briefly; transient = neutral, simply passing."),
    dict(plane="vocab", term="transient",
         text="How miserable, how shadowy and {{c1::transient}}, how aimless and arbitrary the human intellect looks within nature.",
         intention="Mark something as passing / temporary in a neutral-to-formal register; common in academic prose.",
         image="A passenger who gets off at the very next stop.",
         synonyms="temporary, passing, fleeting, momentary"),
    dict(plane="vocab", term="arbitrary",
         text="We separate things according to gender... what {{c1::arbitrary}} assignments.",
         intention="Criticise a choice or rule as based on whim rather than reason — a key word for argument and critique.",
         image="A coin flip deciding a law.",
         synonyms="random, capricious, unjustified, whimsical"),
    dict(plane="vocab", term="reprehensible",
         text="There is nothing so {{c1::reprehensible}} and unimportant in nature that it would not immediately swell up like a balloon.",
         intention="Morally condemn — 'deserving of blame'. Strong, formal censure.",
         image="A stern finger pointing in judgment.",
         synonyms="blameworthy, deplorable, disgraceful, shameful"),
    dict(plane="vocab", term="dissimulation",
         text="As a means for the preserving of the individual, the intellect unfolds its principal powers in {{c1::dissimulation}}.",
         intention="Name the act of hiding your true feelings or intentions behind a false surface — a precise, literary word.",
         image="A calm mask held over a panicking face.",
         synonyms="pretence, concealment, dissembling, feigning"),
    dict(plane="vocab", term="flattering",
         text="This pride contains within itself the most {{c1::flattering}} estimation of the value of knowing.",
         intention="Describe praise that inflates someone's self-image, often insincere or self-serving.",
         image="A mirror that quietly makes you look taller.",
         synonyms="complimentary, gratifying, fawning, ingratiating"),
    dict(plane="vocab", term="insatiable",
         text="Man is sustained by that which is pitiless, greedy, {{c1::insatiable}} and murderous.",
         intention="Stress a hunger or desire that can never be satisfied — intense, formal.",
         image="A pit that swallows everything and is never full.",
         synonyms="unquenchable, voracious, ravenous, unappeasable"),
    dict(plane="vocab", term="pitiless",
         text="Man is sustained by that which is {{c1::pitiless}}, greedy, insatiable and murderous.",
         intention="Describe something utterly without mercy — colder and stronger than 'cruel'.",
         image="A machine that crushes without ever pausing.",
         synonyms="merciless, ruthless, relentless, remorseless"),
    dict(plane="vocab", term="defrauded",
         text="What men avoid by excluding the liar is not so much being {{c1::defrauded}} as it is being harmed by means of fraud.",
         intention="Accuse of cheating someone (esp. of money or rights) through deception — legal / formal.",
         image="A contract with clauses written in invisible ink.",
         synonyms="swindled, cheated, deceived, duped"),
    dict(plane="vocab", term="designation",
         text="A uniformly valid and binding {{c1::designation}} is invented for things.",
         intention="Refer formally to the act or result of naming / labelling something — academic register.",
         image="A label gun tagging every object in the room.",
         synonyms="label, name, term, denotation"),
    dict(plane="vocab", term="tautology",
         text="If he will not be satisfied with truth in the form of {{c1::tautology}}, then he will always exchange truths for illusions.",
         intention="Name a statement that merely repeats itself and says nothing new — useful in argument and criticism.",
         image="A dog chasing its own tail.",
         synonyms="redundancy, circular statement, pleonasm"),
    dict(plane="vocab", term="embellished",
         text="A sum of human relations which have been poetically and rhetorically intensified, transferred and {{c1::embellished}}.",
         intention="Say something has been decorated or dressed up — often implying added but unreal detail. Great for writing about style.",
         image="A plain cake buried under ornate icing.",
         synonyms="adorned, decorated, ornamented, dressed up"),
    dict(plane="vocab", term="canonical",
         text="After long usage they seem to a people to be fixed, {{c1::canonical}} and binding.",
         intention="Mark something as officially accepted / authoritative — academic.",
         image="Rules carved into stone tablets.",
         synonyms="authoritative, official, established, orthodox"),
    dict(plane="vocab", term="edifice",
         text="The great {{c1::edifice}} of concepts displays the rigid regularity of a Roman columbarium.",
         intention="A large, impressive structure — literal, or (very usefully) a metaphor for a whole system of ideas in an essay.",
         image="A vast cathedral built entirely of glass.",
         synonyms="structure, construction, building, framework"),
    dict(plane="vocab", term="audacious",
         text="That framework of concepts is nothing but a scaffolding and toy for the most {{c1::audacious}} feats of the liberated intellect.",
         intention="Note boldness that borders on reckless daring — can be admiring or critical.",
         image="A tightrope walker, no net, grinning.",
         synonyms="bold, daring, fearless, brazen"),
    dict(plane="vocab", term="ardent",
         text="It continually manifests an {{c1::ardent}} desire to refashion the world.",
         intention="Describe intense, passionate feeling — warmer and more literary than 'eager'.",
         image="A fire burning steadily in the chest.",
         synonyms="passionate, fervent, intense, eager"),
    dict(plane="vocab", term="scorn",
         text="The one stands in fear of intuition, the other with {{c1::scorn}} for abstraction.",
         intention="Express strong contempt — looking down on something as worthless.",
         image="A curled lip turning away.",
         synonyms="contempt, disdain, derision, mockery"),
    dict(plane="vocab", term="prudence",
         text="The former rules over life by knowing how to meet his needs by means of foresight, {{c1::prudence}} and regularity.",
         intention="Name careful, sensible judgment that avoids risk — a virtue word, formal.",
         image="Someone checking the weather before every single step.",
         synonyms="caution, discretion, good sense, circumspection"),
    dict(plane="vocab", term="ensnaring",
         text="He seeks nothing but sincerity, truth, freedom from deception and protection against {{c1::ensnaring}} surprise attacks.",
         intention="Describe trapping someone, often by trickery — literary.",
         image="A net hidden under a layer of leaves.",
         synonyms="entrapping, snaring, catching, entangling"),
    dict(plane="vocab", term="aloof",
         text="Nature confines and locks him within a proud, deceptive consciousness, {{c1::aloof}} from the coils of the bowels.",
         intention="Describe being distant or detached — physically or emotionally apart, with a touch of superiority.",
         image="A cat watching everything from a high shelf.",
         synonyms="distant, detached, remote, standoffish"),
    dict(plane="vocab", term="disenchanted",
         text="A mythically inspired people resembles a dream more than it does the waking world of a scientifically {{c1::disenchanted}} thinker.",
         intention="Loss of illusion or magic — freed from belief but also a little deflated. Useful for tone.",
         image="A magician revealed to be working hidden strings.",
         synonyms="disillusioned, jaded, undeceived"),
    dict(plane="vocab", term="repose",
         text="Only by forgetting this primitive world of metaphor can one live with any {{c1::repose}}, security and consistency.",
         intention="A formal / literary word for calm rest or peace of mind.",
         image="A still lake at dawn.",
         synonyms="calm, tranquillity, rest, serenity"),
    dict(plane="vocab", term="congealed",
         text="After nature had drawn a few breaths the star cooled and {{c1::congealed}}.",
         intention="Describe a liquid turning solid or thick — vivid, and a strong metaphor for ideas hardening.",
         image="Warm gravy slowly turning to jelly.",
         synonyms="solidified, set, coagulated, hardened"),

    # ============ PLANE B: VERBS / CONSTRUCTIONS ============
    dict(plane="verb-construction", term="dispense with",
         text="The fundamental human drive which one cannot for a single instant {{c1::dispense with}} in thought.",
         intention="Formally say 'do without' / 'get rid of'. Elevates writing far above 'remove'.",
         pattern="cannot dispense with X | this step can be dispensed with",
         synonyms="do without, forgo, get rid of, eliminate"),
    dict(plane="verb-construction", term="ward off",
         text="The man guided by concepts only succeeds by such means in {{c1::warding off}} misfortune.",
         intention="Keep away / prevent something bad: danger, illness, an attack, criticism.",
         pattern="ward off + danger / illness / criticism",
         synonyms="fend off, stave off, avert, repel"),
    dict(plane="verb-construction", term="shoring up",
         text="Science is always building new higher stories and {{c1::shoring up}}, cleaning and renovating the old cells.",
         intention="Support or strengthen something weak — an argument, an economy, a structure.",
         pattern="shore up + an argument / the economy / a case",
         synonyms="bolster, prop up, reinforce, buttress"),
    dict(plane="verb-construction", term="wage",
         text="They have been denied the chance to {{c1::wage}} the battle for existence with horns or sharp teeth.",
         intention="The correct verb for carrying on a war, campaign or sustained struggle.",
         pattern="wage war / a campaign / a battle (against)",
         synonyms="carry on, conduct, pursue, fight"),
    dict(plane="verb-construction", term="lays hold of",
         text="For expressing these relations he {{c1::lays hold of}} the boldest metaphors.",
         intention="A literary phrase for seizing or grasping something — an idea, a tool, an opportunity.",
         pattern="lay hold of + an idea / a chance / a weapon",
         synonyms="seize, grasp, take hold of, grab"),
    dict(plane="verb-construction", term="carried away",
         text="He will no longer tolerate being {{c1::carried away}} by sudden impressions, by intuitions.",
         intention="Lose self-control under the force of an emotion or impulse.",
         pattern="be / get carried away by + emotion / enthusiasm",
         synonyms="get swept up, lose control, be overwhelmed"),
    dict(plane="verb-construction", term="swell up",
         text="There is nothing so unimportant in nature that it would not immediately {{c1::swell up}} like a balloon at the slightest puff.",
         intention="Enlarge or inflate — literal, or a metaphor for ego and pride.",
         pattern="swell up like a balloon | his pride swelled up",
         synonyms="inflate, balloon, puff up, expand"),

    # ============ PLANE B': GRAMMAR / TENSE & MOOD ============
    dict(plane="grammar", term="be sought",
         text="Henceforth it thinks the truth demands that each conceptual god {{c1::be sought}} only within his own sphere.",
         intention="Mandative subjunctive: after demand / require / insist / suggest + that, use the BASE verb (be, not is). A clear C2 marker in formal writing.",
         pattern="demand / insist / require that X be done (not 'is done')",
         note="Register: formal. e.g. 'The rule requires that it be reviewed.'"),
    dict(plane="grammar", term="would learn",
         text="If we could communicate with a gnat, we {{c1::would learn}} that he likewise flies through the air with the same solemnity.",
         intention="Second conditional: hypothesise about something contrary to present fact. if + past, would + base verb.",
         pattern="If X happened, we would see Y",
         note="Unreal present / hypothetical."),
    dict(plane="grammar", term="as though",
         text="Its possessor takes it so solemnly {{c1::as though}} the world's axis turned within it.",
         intention="'as though / as if' + past tense expresses something imagined or unreal in the present — C2 comparison & hedging.",
         pattern="X behaves as though it knew / mattered / were true",
         note="The past tense ('turned', 'were') signals it is NOT actually so."),
    dict(plane="grammar", term="would have every reason to",
         text="Without this addition they {{c1::would have every reason to}} flee this existence as quickly as Lessing's son.",
         intention="A strong, elegant way to justify a hypothetical reaction in argument.",
         pattern="One would have every reason to doubt / reject / fear X",
         synonyms="would be fully justified in, would have good cause to"),

    # ============ PLANE C: CONNECTORS / DISCOURSE MARKERS ============
    dict(plane="connector", term="insofar as",
         text="{{c1::Insofar as}} the individual wants to maintain himself against others, he will employ the intellect mainly for dissimulation.",
         intention="'to the extent that / in the degree that' — a precise academic conditional connector that sharpens an argument.",
         pattern="Insofar as X is true, Y follows",
         note="Register: formal / academic."),
    dict(plane="connector", term="whereas",
         text="{{c1::Whereas}} the man of action binds his life to reason, the scientific investigator builds his hut right next to the tower of science.",
         intention="Draw a clean contrast between two clauses — a formal 'while / in contrast'.",
         pattern="Whereas A does X, B does Y"),
    dict(plane="connector", term="at bottom",
         text="{{c1::At bottom}}, what the investigator of such truths is seeking is only the metamorphosis of the world into man.",
         intention="Introduce the underlying / fundamental truth beneath appearances — a sophisticated alternative to 'basically'.",
         pattern="At bottom, the problem is X, not Y",
         synonyms="fundamentally, in essence, ultimately"),
    dict(plane="connector", term="that is to say",
         text="That which shall count as truth is established — {{c1::that is to say}}, a uniformly valid and binding designation is invented for things.",
         intention="Reformulate or clarify what you just said ('i.e.') — buys precision without restarting the sentence.",
         pattern="X is contingent, that is to say, it could have been otherwise",
         synonyms="in other words, i.e., namely"),
    dict(plane="connector", term="in short",
         text="Playing a role for others and for oneself — {{c1::in short}}, a continuous fluttering around the solitary flame of vanity.",
         intention="Compress a list or argument into one summarising clause.",
         pattern="...; in short, it cannot hold",
         synonyms="in brief, in sum, to sum up"),
    dict(plane="connector", term="on the contrary",
         text="Their senses nowhere lead to truth; {{c1::on the contrary}}, they are content to receive stimuli.",
         intention="Reject the previous idea and assert its opposite — emphatic.",
         pattern="It did not fail; on the contrary, it succeeded",
         note="Not the same as 'in contrast' — this NEGATES the prior claim."),
    dict(plane="connector", term="nevertheless",
         text="That was the most mendacious minute of world history, but {{c1::nevertheless}} it was only a minute.",
         intention="Concede a point yet assert something that stands against it — formal 'but still'.",
         pattern="The data is limited; nevertheless, the trend is clear",
         synonyms="nonetheless, even so, all the same"),
    dict(plane="connector", term="henceforth",
         text="Every people thinks the truth, and {{c1::henceforth}} demands that each conceptual god be sought only within his own sphere.",
         intention="'from this point on' — formal, marks a turning point or a new rule.",
         pattern="The terms are fixed; henceforth they bind everyone",
         synonyms="from now on, from then on, thereafter"),
    dict(plane="connector", term="moreover",
         text="{{c1::Moreover}}, man permits himself to be deceived in his dreams every night of his life.",
         intention="Add a further, often stronger, point — formal 'also / furthermore'.",
         pattern="It is costly; moreover, it is unreliable",
         synonyms="furthermore, in addition, besides, what is more"),
    dict(plane="connector", term="as it were",
         text="Man is sustained in the indifference of his ignorance, {{c1::as it were}} hanging in dreams on the back of a tiger.",
         intention="Soften a bold metaphor or phrasing — signals 'so to speak'. A small marker of a careful, C2 writer.",
         pattern="It is, as it were, the grammar of thought",
         synonyms="so to speak, in a sense, if you will"),
]

PLANE_TITLES = {
    "vocab": "Plane A — Advanced lexis (C1 → C2)",
    "verb-construction": "Plane B — Verbs & dense constructions",
    "grammar": "Plane B′ — Grammar: tense & mood",
    "connector": "Plane C — Connectors & discourse markers (write like C2)",
}
PLANE_ORDER = ["vocab", "verb-construction", "grammar", "connector"]


def back_html(c):
    parts = [f"<b>Intention:</b> {c['intention']}"]
    if c.get("image"):
        parts.append(f"<b>Image:</b> {c['image']}")
    if c.get("pattern"):
        parts.append(f"<b>Pattern:</b> {c['pattern']}")
    if c.get("synonyms"):
        parts.append(f"<b>Synonyms:</b> {c['synonyms']}")
    if c.get("note"):
        parts.append(f"<i>{c['note']}</i>")
    return "<br>".join(parts)


def tags_for(c):
    return f"{BOOK_SLUG} c2 {c['plane']}"


def build():
    root = Path(__file__).resolve().parent.parent
    out_dir = root / "decks"
    out_dir.mkdir(exist_ok=True)

    # --- TSV (Anki import) ---
    tsv_lines = []
    for c in CARDS:
        text = c["text"].replace("\t", " ").replace("\n", " ")
        extra = back_html(c).replace("\t", " ").replace("\n", " ")
        tsv_lines.append(f"{text}\t{extra}\t{tags_for(c)}")
    tsv_path = out_dir / f"{BOOK_SLUG}.tsv"
    tsv_path.write_text("\n".join(tsv_lines) + "\n", encoding="utf-8")

    # --- Markdown (readable on GitHub) ---
    md = [
        f"# Deck: {BOOK_TITLE}",
        "",
        f"*Source: {SOURCE}.* All back content is in English on purpose "
        "(monolingual = transfer). Target: the B2/C1 → C2 jump.",
        "",
        f"**{len(CARDS)} cards** across three planes. Cloze note type; "
        "front = the real sentence with the term hidden.",
        "",
        "## How to import into Anki",
        "",
        f"1. File → Import → `decks/{BOOK_SLUG}.tsv`",
        "2. Note type: **Cloze**  |  Deck: **english**",
        "3. Field separator: **Tab**  |  **Allow HTML in fields: ON**",
        "4. Map: column 1 → *Text*, column 2 → *Back Extra*, column 3 → *Tags*",
        "",
    ]
    for plane in PLANE_ORDER:
        items = [c for c in CARDS if c["plane"] == plane]
        if not items:
            continue
        md.append(f"## {PLANE_TITLES[plane]}")
        md.append("")
        for c in items:
            shown = c["text"].replace("{{c1::", "**[ ").replace("}}", " ]**")
            md.append(f"- **{c['term']}** — {shown}")
            md.append(f"  - *Intention:* {c['intention']}")
            if c.get("image"):
                md.append(f"  - *Image:* {c['image']}")
            if c.get("pattern"):
                md.append(f"  - *Pattern:* `{c['pattern']}`")
            if c.get("synonyms"):
                md.append(f"  - *Synonyms:* {c['synonyms']}")
            if c.get("note"):
                md.append(f"  - *Note:* {c['note']}")
        md.append("")
    md_path = out_dir / f"{BOOK_SLUG}.md"
    md_path.write_text("\n".join(md), encoding="utf-8")

    print(f"Wrote {len(CARDS)} cards")
    print(f"  - {tsv_path.relative_to(root)}")
    print(f"  - {md_path.relative_to(root)}")
    counts = {p: len([c for c in CARDS if c['plane'] == p]) for p in PLANE_ORDER}
    print("  planes:", counts)


if __name__ == "__main__":
    build()
