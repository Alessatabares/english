# -*- coding: utf-8 -*-
"""French deck — THE MOTOR (core engine of French).

NOT an immersion/reading deck (that's the sorcière tale). This is the FOUNDATION:
the structural skeleton + high-frequency motor that carries most of spoken/written
French — gender & articles, the pillar verbs and their conjugation, the everyday
tenses, two-part negation, pre-verbal object pronouns, questions, prepositions,
the impersonal frames (c'est / il y a / il faut) and basic connectors.

Deliberate exception to the repo's "never invent" rule: a foundation deck has no
source video, so the sentences are invented on purpose — short, funny and vivid
(vivid, absurd sentences are more memorable). Active recall via cloze; system
thinking via Intention (the job) + Pattern (the reusable frame) + note (the
contrast / the gender trap). English is the bridge language: each French item
carries an English gloss (meaning).

Study one plane at a time (tags), not the whole deck at once.

Run:  python3 tools/deck_french_motor.py   ->  french/motor/motor.apkg
"""

import deck_builder

LANGUAGE = "french"
SLUG = "motor"         # Anki deck name -> french::motor
DECK_ID = 1987452321   # stable: re-import updates instead of duplicating
LEVEL = "core"
SUBFOLDER = "motor"    # the .apkg lives in french/motor/

SOURCE_URL = ""  # curated foundation deck, no source video (legitimately empty)
DESCRIPTION = (
    "French · CORE MOTOR. The structural engine of French (A1 &rarr; B1 span): "
    "gender &amp; articles, the pillar verbs and conjugation, the everyday tenses "
    "(pass&eacute; compos&eacute;, imparfait, futur proche), two-part negation, "
    "pre-verbal object pronouns, questions, prepositions, the impersonal frames "
    "and basic connectors. Active recall (cloze) + system thinking (every back "
    "gives the job, the reusable pattern and the contrast). English is the bridge "
    "(each item has a gloss). Sentences invented on purpose — short and memorable. "
    "Study one plane (tag) at a time."
)

# PATTERN-CENTRIC design (hybrid), mirroring the English motor. The learning unit
# is the PATTERN, not the word:
#   FORK (the discriminator) -> VARIATION (several examples) -> COMPRESSION (the rule).
#
# Two card shapes, same note type:
#   1) CONTRAST SET — a fork with a confusable neighbour (le vs la, à vs de,
#      passé composé vs imparfait). Front = a <div class='title'> naming the fork +
#      3-6 varied example lines, EACH with its pivot in {{c1::...}}. All blanks are
#      c1 -> ONE card ("fill every blank"), answers differ line to line so you must
#      actually discriminate.
#   2) SIMPLE — an item with no obvious neighbour (chez, il faut). Front = 1-2
#      clozed lines; keep the English `meaning` gloss.
#
# Fields:
#   plane     : "grammar" | "verb-construction" | "connector" | "expression"
#   rule      : the discriminator headline, shown big/red first on the back (English)
#   text      : title (optional <div class='title'>) + example line(s), "\n"-joined,
#               pivots in {{c1::...}}  (invented on purpose — vivid & funny = memorable)
#   meaning   : English gloss (bridge) — for SIMPLE cards; omit on contrast sets
#   intention : the JOB the pattern does (English)
#   image / pattern / note : optional (picture, frame, gender trap / neighbour)

CARDS = [
    # ============ A. GENDER & ARTICLES (every noun is M or F) ============
    dict(plane="grammar",
         rule="le → M · la → F · les → plural (the)",
         text=("<div class='title'>le / la / les</div>"
               "① {{c1::La}} lune surveille tout le quartier. (F)\n"
               "② {{c1::Le}} chat juge mes décisions. (M)\n"
               "③ {{c1::Les}} voisins écoutent aux murs. (pl)\n"
               "④ {{c1::La}} vérité est dans le frigo. (F)"),
         intention="The definite article marks gender (le/la) and number (les).",
         note="Gender is rarely logical — always learn it WITH the noun."),
    dict(plane="grammar",
         rule="un → M · une → F · des → plural (a / some)",
         text=("<div class='title'>un / une / des</div>"
               "① J'ai adopté {{c1::une}} licorne au supermarché. (F)\n"
               "② Il y a {{c1::un}} problème avec ton plan. (M)\n"
               "③ Elle collectionne {{c1::des}} chaussettes tristes. (pl)"),
         intention="Indefinite article: new to the listener; agrees in gender/number.",
         note="des (indefinite plural, 'some') vs les (definite plural, 'the')."),
    dict(plane="grammar",
         rule="du → M mass · de la → F mass · des → plural (partitive 'some')",
         text=("<div class='title'>du / de la / des (partitif)</div>"
               "① Je veux {{c1::du}} pain, pas tout le pain du monde. (M)\n"
               "② Tu bois {{c1::de la}} tisane à minuit ? (F)\n"
               "③ On mange {{c1::des}} frites en cachette. (pl)"),
         intention="Partitive = 'some / an amount of' an uncountable. French REQUIRES it.",
         note="'I want bread' -> 'je veux du pain' (never 'je veux pain')."),
    dict(plane="grammar",
         rule="à+le=au · à+les=aux · de+le=du · de+les=des (mandatory)",
         text=("<div class='title'>contractions : à+le, de+le</div>"
               "① Je vais {{c1::au}} marché acheter du courage. (à+le)\n"
               "② Elle parle {{c1::aux}} pigeons du parc. (à+les)\n"
               "③ C'est la fin {{c1::du}} film. (de+le)\n"
               "④ Le prix {{c1::des}} billets est absurde. (de+les)"),
         intention="These fusions are obligatory — the raw words can't sit side by side.",
         note="Never write 'à le' or 'de le'."),

    # ============ B. SUBJECT PRONOUNS (on / nous, tu / vous) ============
    dict(plane="grammar",
         rule="on → spoken 'we' (+ il/elle verb form) · nous → written/formal 'we'",
         text=("<div class='title'>on vs nous</div>"
               "① {{c1::On}} mange à huit heures, comme des gens civilisés. (spoken)\n"
               "② {{c1::Nous}} mangeons à huit heures. (written)\n"
               "③ {{c1::On}} y va ? (let's go?)"),
         intention="In speech 'on' replaces 'nous' almost always; it takes the 3rd-singular verb.",
         note="'on' also = generic 'one / people'."),
    dict(plane="grammar",
         rule="tu → informal singular · vous → formal, OR plural",
         text=("<div class='title'>tu vs vous</div>"
               "① {{c1::Tu}} peux arrêter de juger mon café ? (a friend)\n"
               "② {{c1::Vous}} pouvez patienter, madame ? (polite)\n"
               "③ {{c1::Vous}} êtes en retard, tous les trois. (plural)"),
         intention="Same 'you', two social settings — and vous doubles as the plural.",
         note="Picking the wrong one is a social mistake, not just grammar."),
    dict(plane="grammar",
         rule="the pronoun agrees with the noun's GENDER — even for objects",
         text="Où est la clé ? {{c1::Elle}} est dans le frigo, évidemment.",
         meaning="it / she (agrees with the gendered noun)",
         intention="Objects are he/she in French, following the noun's gender.",
         note="la table -> elle · le livre -> il."),

    # ============ C. THE PILLAR VERBS (être / avoir / aller / faire) ============
    dict(plane="verb-construction",
         rule="être=be · avoir=have · aller=go · faire=do/make",
         text=("<div class='title'>les 4 verbes piliers</div>"
               "① Je {{c1::suis}} fatiguée mais élégante. (être)\n"
               "② J'{{c1::ai}} faim et zéro patience. (avoir)\n"
               "③ Je {{c1::vais}} regretter cette crêpe. (aller)\n"
               "④ Qu'est-ce que tu {{c1::fais}} avec ce poulet ? (faire)"),
         intention="The four most-used, most-irregular verbs; they also build other tenses.",
         note="avoir for age/hunger (j'ai faim); aller + inf = near future; faire = weather."),
    dict(plane="verb-construction",
         rule="être: suis/es/est/sommes/êtes/sont · avoir: ai/as/a/avons/avez/ont",
         text=("<div class='title'>être &amp; avoir — pluriel</div>"
               "① Nous {{c1::sommes}} en retard, comme toujours. (être)\n"
               "② Vous {{c1::avez}} raison, hélas. (avoir)\n"
               "③ Ils {{c1::sont}} bizarres mais gentils. (être)\n"
               "④ Elles {{c1::ont}} un plan douteux. (avoir)"),
         intention="Drill the plural forms of the two auxiliaries — they build every compound tense.",
         note="These two carry the whole passé composé."),

    # ============ D. PRESENT TENSE (regular endings) ============
    dict(plane="grammar",
         rule="-ER: -e/-es/-e/-ons/-ez/-ent · -IR: adds -iss- in the plural",
         text=("<div class='title'>présent : -ER vs -IR</div>"
               "① Nous {{c1::parlons}} aux plantes, et elles répondent. (-er)\n"
               "② Je {{c1::finis}} toujours par manger le dernier biscuit. (-ir)\n"
               "③ Ils {{c1::finissent}} tard. (-ir, -iss-)\n"
               "④ Vous {{c1::parlez}} trop vite. (-er)"),
         intention="The two big regular groups; -ER endings mostly SOUND alike, only spelling changes.",
         note="-IR verbs grow the -iss- block in the plural: finissons, finissent."),

    # ============ E. THE PAST (passé composé vs imparfait; avoir vs être) ============
    dict(plane="grammar",
         rule="passé composé → the event that happens · imparfait → scenery / habit",
         text=("<div class='title'>passé composé vs imparfait</div>"
               "① Quand j'{{c1::étais}} petite, je parlais aux escargots. (background)\n"
               "② Hier j'{{c1::ai mangé}} toute la tarte. (event)\n"
               "③ Il {{c1::pleuvait}} quand le train est parti. (scenery)\n"
               "④ Soudain, elle {{c1::a crié}}. (event)"),
         intention="Same past, two jobs: the ongoing backdrop vs the punctual thing that happens.",
         note="imparfait = 'was -ing / used to'; passé composé = the completed event."),
    dict(plane="grammar",
         rule="most verbs → avoir · motion/change + reflexives → être (participle agrees)",
         text=("<div class='title'>passé composé : avoir vs être</div>"
               "① J'{{c1::ai}} mangé toute la tarte. (avoir)\n"
               "② Elle est {{c1::partie}} sans dire au revoir. (être + accord: partie)\n"
               "③ Nous {{c1::avons}} fini le travail. (avoir)\n"
               "④ Ils {{c1::sont}} arrivés en retard. (être, arrivés)"),
         intention="Pick the auxiliary; with être the participle agrees with the subject.",
         note="House of être: aller, venir, partir, naître, mourir... + all reflexives."),

    # ============ F. FUTURE & POLITENESS ============
    dict(plane="grammar",
         rule="je veux → blunt 'I want' · je voudrais → polite 'I would like'",
         text=("<div class='title'>je veux vs je voudrais</div>"
               "① {{c1::Je voudrais}} un café et une nouvelle personnalité. (polite)\n"
               "② {{c1::Je veux}} tout, tout de suite. (blunt)\n"
               "③ {{c1::Je voudrais}} réserver une table. (polite request)"),
         intention="The conditional 'voudrais' softens a demand — the default with strangers.",
         note="'je veux' can sound rude; reach for 'je voudrais'."),
    dict(plane="grammar",
         rule="aller (present) + infinitive = the everyday spoken future",
         text="Je {{c1::vais commencer}} demain. Probablement.",
         meaning="I'm going to start (near future)",
         intention="Near future: no new endings, just aller + the infinitive.",
         pattern="aller + infinitive (je vais partir, on va voir)"),

    # ============ G. NEGATION (the two-part wrap) ============
    dict(plane="grammar",
         rule="ne wraps the verb; swap 'pas' → jamais / plus / rien / personne",
         text=("<div class='title'>ne … pas / jamais / rien / personne</div>"
               "① Je {{c1::ne}} comprends pas, et j'aime ça. (first half)\n"
               "② Je ne mange {{c1::jamais}} de coriandre. (never)\n"
               "③ Il n'y a {{c1::rien}} dans le frigo. (nothing)\n"
               "④ Je ne vois {{c1::personne}}. (nobody)"),
         intention="French negation is two pieces around the verb; the second piece sets the meaning.",
         note="In speech the 'ne' is often dropped: 'je sais pas'."),

    # ============ H. PRE-VERBAL PRONOUNS (le/la/les · y · en) ============
    dict(plane="grammar",
         rule="le/la/les → the thing · y → à+place · en → de+thing ('some'). All BEFORE the verb.",
         text=("<div class='title'>pronoms pré-verbaux</div>"
               "① Tu vois la lune ? Je {{c1::la}} vois aussi. (direct object)\n"
               "② Tu vas à Paris ? J'{{c1::y}} vais aussi ! (à + lieu)\n"
               "③ Du gâteau ? J'{{c1::en}} veux trois parts. (de + chose)\n"
               "④ Tes clés ? Je {{c1::les}} ai. (plural object)"),
         intention="These pronouns replace whole phrases and sit BEFORE the verb — opposite to English.",
         note="English: 'I see it' (after). French: 'je la vois' (before)."),

    # ============ I. QUESTIONS ============
    dict(plane="grammar",
         rule="intonation (Tu viens ?) · est-ce que (neutral) · inversion (Viens-tu ? formal)",
         text=("<div class='title'>poser une question : 3 façons</div>"
               "① {{c1::Est-ce que}} tu as vraiment lu le contrat ? (neutral)\n"
               "② {{c1::Qu'est-ce que}} tu fais ce week-end ? (what + statement)\n"
               "③ As-{{c1::tu}} tout mangé ? (inversion, formal)"),
         intention="Three registers of the same question; est-ce que needs no inversion.",
         note="Qu'est-ce que = the default spoken 'what'."),
    dict(plane="grammar",
         rule="où=where · quand=when · pourquoi=why · comment=how · combien=how much · qui=who",
         text=("<div class='title'>les mots interrogatifs</div>"
               "① {{c1::Pourquoi}} le chat me regarde comme ça ? (why)\n"
               "② {{c1::Où}} sont mes clés ? (where)\n"
               "③ {{c1::Combien}} ça coûte ? (how much)\n"
               "④ {{c1::Comment}} tu fais ça ? (how)"),
         intention="The info-question words open a specific gap; the frame after stays the same.",
         pattern="[mot] + est-ce que + statement ?"),

    # ============ J. PREPOSITIONS (à / de pillars + chez / en) ============
    dict(plane="grammar",
         rule="à → to/at a point (place/time) · de → of/from (possession/origin)",
         text=("<div class='title'>à vs de</div>"
               "① On se voit {{c1::à}} la gare à midi ? (a point)\n"
               "② C'est le chien {{c1::de}} ma voisine bizarre. (possession)\n"
               "③ Je viens {{c1::de}} Paris. (origin)\n"
               "④ Je pense {{c1::à}} toi. (à + person)"),
         intention="The two pillar prepositions; they also drive the contractions (au, du).",
         note="Possession = 'de': 'Marie's book' = le livre de Marie."),
    dict(plane="grammar",
         rule="chez + person = at/to their home or business",
         text="On va {{c1::chez}} moi ou chez le dragon ?",
         meaning="at / to someone's place",
         intention="No one-word English equivalent — 'chez' points at a person's place.",
         pattern="chez moi, chez le médecin, chez Renault."),
    dict(plane="grammar",
         rule="en → by (transport), in (months, feminine countries)",
         text="Je voyage {{c1::en}} train, jamais en retard (mensonge).",
         meaning="by / in",
         intention="Preposition 'en' for means and enclosed time/place.",
         pattern="en mai · en France · en bus."),

    # ============ K. IMPERSONAL FRAMES (c'est / il y a / il faut) ============
    dict(plane="expression",
         rule="c'est + noun/adj (identify) · il/elle est + profession/adjective (describe)",
         text=("<div class='title'>c'est vs il est</div>"
               "① {{c1::C'est}} compliqué, mais pas impossible. (identify)\n"
               "② {{c1::Il est}} médecin, paraît-il. (profession, no article)\n"
               "③ {{c1::Ce sont}} des menteurs. (plural)\n"
               "④ {{c1::Elle est}} fatiguée. (describe)"),
         intention="Both mean 'it/he is', but c'est points at a thing and il est describes.",
         note="c'est UN médecin (with article) vs il est médecin (no article)."),
    dict(plane="expression",
         rule="il y a → there is/are (invariable) · also 'ago'",
         text="{{c1::Il y a}} un problème avec ton plan génial.",
         meaning="there is / there are",
         intention="One frame for existence, singular OR plural.",
         note="il y a deux ans = two years ago."),
    dict(plane="expression",
         rule="il faut + infinitive = must / need to (impersonal)",
         text="{{c1::Il faut}} dormir, pas acheter un kayak à 3h du matin.",
         meaning="one must / it's necessary to",
         intention="Impersonal obligation — no real subject.",
         note="il faut que + subjunctive comes later — start with the infinitive."),

    # ============ L. CONNECTORS ============
    dict(plane="connector",
         rule="et → add · mais → contrast · ou → choice",
         text=("<div class='title'>et / mais / ou</div>"
               "① Je suis venue pour le fromage, {{c1::mais}} je reste pour le vin. (contrast)\n"
               "② J'aime le thé {{c1::et}} le silence. (add)\n"
               "③ C'est ton café {{c1::ou}} le mien ? (choice)"),
         intention="The three basic joins: pile on, turn against, offer a fork.",
         pattern="X et Y · X mais Y · X ou Y"),
    dict(plane="connector",
         rule="parce que → the cause (why) · donc → the result (so)",
         text=("<div class='title'>parce que vs donc</div>"
               "① Je chuchote {{c1::parce que}} le bébé dort enfin. (cause)\n"
               "② Le sol était mouillé, {{c1::donc}} j'ai dansé sans le vouloir. (result)\n"
               "③ Il est tard, {{c1::donc}} je pars. (result)\n"
               "④ Je pars {{c1::parce que}} il est tard. (cause)"),
         intention="Same causal link, opposite order: effect ← parce que ← cause · cause → donc → effect.",
         note="parce que answers 'pourquoi'; car = more formal/written."),
    dict(plane="connector",
         rule="si → if (condition) · quand → when (time)",
         text=("<div class='title'>si vs quand</div>"
               "① {{c1::Si}} tu nourris le chat, il habite ici maintenant. (condition)\n"
               "② {{c1::Quand}} le train arrive, tout le monde court. (time)\n"
               "③ {{c1::Si}} j'ai le temps, je viendrai. (condition)"),
         intention="si opens a hypothesis; quand marks the moment something happens.",
         pattern="Si + présent, ... futur (si tu viens, on mangera)."),

    # ============ M. ADJECTIVES (position + agreement) ============
    dict(plane="grammar",
         rule="most adjectives → AFTER the noun (+e F, +s pl) · BAGS → BEFORE",
         text=("<div class='title'>adjectifs : position + accord</div>"
               "① Une idée {{c1::géniale}} et absurde. (after, F agreement)\n"
               "② Un {{c1::beau}} désastre, vraiment. (BAGS, before)\n"
               "③ Des voitures {{c1::rouges}}. (after, plural)\n"
               "④ Une {{c1::jeune}} femme pressée. (BAGS age, before)"),
         intention="Position is the fork: default after (agreeing), but BAGS adjectives jump before.",
         note="BAGS = Beauty/Age/Goodness/Size: beau, joli, jeune, vieux, bon, mauvais, grand, petit, nouveau."),

    # ============ N. REFLEXIVE VERBS (the action returns to you) ============
    dict(plane="verb-construction",
         rule="reflexive pronoun (me/te/se/nous/vous/se): the action returns to the subject",
         text="Je {{c1::me}} réveille déjà fatiguée.",
         meaning="myself (reflexive pronoun)",
         intention="Reflexive verbs carry a pronoun — far more common than in English.",
         pattern="je me · tu te · il se · nous nous · vous vous · ils se + verb",
         note="se lever, s'appeler: 'je m'appelle' = I'm called."),
]

if __name__ == "__main__":
    import shutil

    path = deck_builder.build(LANGUAGE, SLUG, DECK_ID, CARDS, LEVEL, DESCRIPTION)
    # Relocate the .apkg into the french/motor/ subfolder.
    sub = path.parent / SUBFOLDER
    sub.mkdir(exist_ok=True)
    dest = sub / f"{SLUG}.apkg"
    shutil.move(str(path), str(dest))
    print(f"Moved -> {dest.relative_to(path.parent.parent)}")
