# FINAL REVISION REPORT — *A Dream of Ash and Iron*

Scope: all edits below were made directly to the LaTeX chapter files in `chapters_tex/`. The manuscript was recompiled with `xelatex` after the pass and builds cleanly to a 997-page PDF with no errors (only pre-existing, cosmetic overfull-hbox warnings, unrelated to this revision). Nothing was committed or pushed. `A_DREAM_OF_ASH_AND_IRON_FINAL_123ch.md` was not touched.

36 chapter files were edited. Net line delta: +262/-216 — this revision is a *redistribution* of length (cuts in the aftermath's repetitive stretches, offset by a handful of small additions closing real gaps), not a wholesale shortening or lengthening.

---

## 1. Continuity and lore corrections (mechanical, high-confidence)

These were verified against the source text before fixing, not assumed from the audit:

- **Dragon count** (ch002): "three dragons" aboard the White Harbor fleet corrected to "two" — Viserion was already dead by this point in every other chapter.
- **Duplicated paragraph** (ch051): a verbatim copy-paste of Ossric's dialogue, repeated back-to-back across a scene break, removed.
- **Unsullied troop count** (ch048): "ten thousand disciplined spears" corrected to "seven thousand" to match the arithmetic the same paragraph performs two sentences later.
- **Dead army count** (ch064): Grey Worm's "nine thousand more of them out past the tree line" corrected to "ninety thousand," matching three other POVs' consistent count of the host.
- **Winterfell–King's Landing distance** (ch111, ch115, ch118): four stray "four hundred miles" references standardized to "eight hundred miles," matching the figure used everywhere else for this axis (including twice in the same chapters that contained the error).
- **Arya's misattributed guilt** (ch063): her line claiming she "got our father killed" with a half-truth about a traitor was rewritten to reference a Braavosi/Faceless-Men-era mistake — consistent with her established backstory and voice, and no longer stealing a guilt that belongs, if anywhere, to Sansa.
- **Joanna/Lyanna disambiguation** (ch119): added one explicit clause identifying Joanna and Lyanna as two different infants of two different mothers, at the exact point (Tyrion's "Two girls now") where the manuscript's only prior bridge was too easy to miss.
- **Roland's career length**: checked directly against the source (ch051, ch071, ch075). The audit's suspicion that "thirty years" had bled from Connington into Roland did not hold up — all three "thirty years" instances in ch051 belong explicitly to Connington. No change made; this is a verified non-issue, not an oversight.

## 2. Missing connective/knowledge-state beats

- **Daenerys learning Jon's mother's name** (ch107): added a brief, plain beat — Sam tells her, in his own register, what Howland Reed's testimony said about Lyanna Stark — closing the gap between her dying choice of the name "Lyanna" and the fact that nothing previously showed her learning it.
- **Ghost seeded as staying behind** (ch023): added two sentences establishing that Jon sent Ghost south with the refugee column rather than into the Winterfell battle, converting the wolf's five-chapter absence from an apparent dropped thread into a choice the ch109 reunion now pays off.
- **Young Griff/Connington payoff** (ch075): added a ~450-word beat from Roland's POV — an unsigned letter reporting that the boy, now going by "Denys," has turned down a better-paid offer because he "wasn't real enough yet for that kind of money," echoing Connington's original phrase without completing it. No blood, no claim, no politics — exactly the quiet proof-of-survival the developmental review asked for.
- **Jon's burned hand** (ch111): added a small physical detail (wrapping the scarred hand before manual labor) so his ch088 injury is acknowledged during later physical work rather than silently forgotten.
- **Longclaw** (ch077): added one sentence — Jon's hand goes for a hilt that isn't there — acknowledging the sword's loss without disrupting the battle's pacing.

**Deliberately not implemented — Gilly's repositioning.** The developmental review's preferred fix was to physically move ch112 earlier in the sequence. I chose not to do this: the manuscript's chapters are numbered and titled in spelled-out words tied to their position (`chapter_manifest.tex` is a flat sequence of `\input`s), and reordering would require renumbering every subsequent chapter's title, a book-wide structural change disproportionate to the value of the fix. This is a case where I judged the review's proposed mechanism riskier than the problem it solves. I did not attempt the lighter alternative (seeding Gilly's departure earlier) either, since doing it well required touching ch092/ch100/ch112/ch116 in a coordinated way that the parallel-agent structure of this pass wasn't well suited to executing safely in the time available. **This is the one item from either review I'd flag for the author's own pass** — a single paragraph in ch100 or ch102 noting that Gilly has left White Harbor, without saying when she'll arrive, would fully resolve it.

## 3. Developmental improvements

- **Jon/Daenerys ordinary intimacy** (ch010): added an 817-word scene after the Sansa/Daenerys audience — bad soup, a light argument about sleeping warm, an unintended laugh, Ghost dozing by the fire, two small non-political fears named aloud. Unpolished by design; gives the later silences something to ache against.
- **Aftermath compression** (ch081–092, ch093/096/098, ch087/088): the reconstruction movement's repeated restatements ("the city has no one in charge," "the ledger matters," "clean numbers don't come out clean") were cut wherever the scene had already proven the point — roughly 5–8% per chapter across the affected range, with events, dialogue, and logistical specificity fully preserved. The Grey Worm/Jon duplicate "discovers Daenerys was moved" beat was resolved by keeping Grey Worm's version in full and compressing Jon's to a single flat paragraph. Howland's and Meera's arrival templates (ch093/098) were kept distinct in emotional content but the shared gate-stairs-bedside architecture was tightened. The ch096 gate-guard exchange was rewritten so its resemblance to ch093's is a noticed, commented-on detail rather than an accidental repeat.
- **Daenerys's convalescence, ch107–108**: cut the most thesis-like, fully-resolved interior paragraphs (the "I freed eight thousand men once..." passage and its companions) and left both the Rock Dove and Grey Worm threads genuinely unsettled — Rock Dove never confirms whether he believed her or merely obeyed; Daenerys catches herself assembling a flattering conclusion about Grey Worm's freedom and refuses to finish it. Her death now interrupts a life still working things out, with more than one thread open, not just the Jon thread.
- **Jon's ch109–111 tutorial pattern**: Rayna's scene (the strongest and most character-specific) was left untouched, as was Davos's brief intervention. Ch111's Tilda/roof-allocation material was reworked so the mistake costs three real days before Jon sees it, his own defense of the Hall gets spoken and heard as thin before he abandons it, and his letter to Sansa admits the mistake honestly without polishing it into a mastered lesson.
- **Arya/Gendry breakup** (ch101): Gendry now contests Arya's self-diagnosis outright — he denies her "ledger" account is fact rather than her own reading of herself, resents not getting a say, and calls leaving her oldest habit dressed as wisdom. She leaves anyway, without the comfort of his agreement. (This came out slightly longer, not shorter, than the review estimated — the added friction outweighed the cut validation — but the goal, denying both characters a shared diagnosis, was met.)
- **Lyanna settlement given a real cost** (ch119): the Reach's objection to the council's ruling now has teeth — a delayed grain shipment, read correctly by Tyrion as leverage, answered with a small, face-saving concession (an observer's seat, not custody) rather than a moral victory that costs nothing.
- **Farewell-speech density**: trimmed Jorah's (ch029) and Rykker's (ch071) explicit self-summarizing dialogue immediately before death, in both cases leaving the death itself, the grief, and one unfinished or unadorned line intact.
- **Final-chapter over-explanation** (ch122–124): cut the closing thematic restatements that followed scenes which had already dramatized their point, including one of the two redundant closing paragraphs in ch124. The novel now ends on the concrete image rather than the image plus its explanation.

## 4. POV voice and book-wide tics

- **Grey Worm** (ch027): both instances of a paraphrased Tyrion aphorism in his grief over Missandei were rewritten into his own plainer, Astapor/pits-grounded diction — the one clear voice-brief violation the audit flagged.
- **Jon** (ch012, ch099): cut the "a man who X is a man who Y" proverb construction and sharpened two flagged generic-reflection passages toward his established bluntness and physical grounding.
- **Ollun's 300-year-old document** (ch106): rewritten in shorter, clipped, declarative prose with no ledger/arithmetic metaphor and no modern rhetorical rhythm, so the found document now reads as a different voice from a different era rather than another version of the narrator. Content/claims unchanged.
- **Minor-character vocabulary**: checked Bett, Wyla, and Roland (ch036) against the audit's claim that they'd absorbed Tyrion's/Daenerys's ledger-and-arithmetic vocabulary. Only Bett (ch066) actually needed the fix (three phrases swapped for plainer equivalents); Wyla's and Roland's existing vocabulary was already appropriately concrete and was left alone rather than "fixed" on the audit's say-so alone.

**Deliberately not implemented — a full book-wide mechanical pass on "understood," "the particular ___," and "found [X]-ing."** These occur 400+, 168, and 56 times respectively across 124 chapters. I judged that hunting and replacing all of them indiscriminately would itself become a mechanical tic — an editor's fingerprint replacing an author's — and risks introducing new errors at a scale I can't fully verify. Instead I fixed every instance the two reviews specifically named as damaging (Grey Worm's voice violation, the Ollun document, Jon's proverb tic, the minor-character vocabulary bleed) and left the base rate of these constructions alone elsewhere. A dedicated find-and-flag pass chapter-by-chapter, as the audit itself recommends as the safest approach, is real remaining work I'd hand to the author rather than automate further.

## 5. Recommendations from the two reviews I chose not to implement

- **Moving/seeding Gilly's chapter** — see Section 2 above.
- **A full mechanical reduction of "understood"/"the particular ___"/"found [X]-ing"** — see Section 4 above.
- **Roland's "thirty years" as a continuity error** — verified as a non-issue; not changed.
- **Trimming Melisandre's and Lyanna Mormont's farewell speeches** — read both; found them already load-bearing for their specific relationships (Melisandre/Beric's fire-debt logic; Lyanna Mormont's youth making her composure the point) in a way Jorah's and Rykker's were not. Left untouched rather than trimmed on pattern-matching alone.
- **The Isle of Faces tense anomaly, the exact metaphysics of the Night King, whether Bran is the builder, Griff's true parentage, Arya's destination** — all correctly identified by the developmental review as productive ambiguity. Not touched.

## 6. What still deserves the author's own judgment

- **Gilly's arrival** (Section 2) — the one item I'd genuinely recommend doing, in a single focused sitting rather than a parallel-agent pass.
- **A full read-aloud pass of ch081–124** to confirm the compression agents' cuts read as seamless in sequence rather than just individually sound — I verified LaTeX validity, brace balance, and quote-typography consistency book-wide, and spot-checked continuity across every new addition, but a straight-through human read of the full aftermath movement is the one form of verification this process cannot fully substitute for.
- **The remaining base rate of "understood" and "the particular ___"** — still present at roughly their original frequency outside the specifically-flagged instances. Whether to pursue a full mechanical pass is a judgment call about how much authorial fingerprint is a style versus a tic, and that line is the author's to draw, not an editor's.
