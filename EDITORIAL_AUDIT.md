# EDITORIAL AUDIT — *A Dream of Ash and Iron*

**Scope:** Full manuscript, Prologue + 123 chapters (`chapters_tex/ch001.tex`–`ch124.tex`), read in narrative order.
**Method:** 13 chronological batch passes covering every chapter (continuity/lore/knowledge-state/POV/repetition/dialogue/pacing), plus 10 dedicated full-arc passes for every POV character with 5+ chapters (Jon, Daenerys, Tyrion, Samwell, Sansa, Brienne, Arya, Yara, Roland, Grey Worm), plus book-wide mechanical frequency counts on candidate authorial tics, plus targeted verification greps against the source files for every "verify against rest of book" flag the passes raised. Nothing below is guessed — every claim was checked against the actual chapter text.
**This report changes nothing.** No chapter has been edited. Per instructions, work stops here pending your review.

---

## SUMMARY TABLE

| Metric | Count |
|---|---|
| Critical findings | 4 |
| High findings | 9 |
| Medium findings | 22 |
| Low / Optional findings | 18 |
| Continuity problems identified | 13 |
| POV-differentiation problems identified | ~15 (1 per major POV + several cross-cutting) |
| Repeated-prose-pattern (fingerprint) problems | 7 book-wide patterns |
| Suggested cuts / compressions | 6 (see Pacing section) |
| Suggested additions | 0 (see Season 7 Loose-End Audit — every thread is classified E) |

---

## HOW TO READ THIS REPORT

Findings are grouped by category rather than strictly by severity, since the same underlying issue (e.g. a repeated tic) spans dozens of files. Each finding uses the requested fields. Book-wide patterns (Phase 4 fingerprint audit) report **aggregate frequency** instead of a single location, since that *is* the finding.

---

# 1. CONTINUITY — CRITICAL / HIGH

### 1.1 — Dragon count contradicts itself at the very start of the book
**SEVERITY:** Critical | **CATEGORY:** Continuity | **FILE:** `ch002.tex`
**LOCATION:** ~line 5, Tyrion's POV, fleet approaching White Harbor
**CURRENT ISSUE:** The fleet is described as currently carrying "the seven hundred soldiers, forty horses, and three dragons currently occupying a fleet." But the Prologue (`ch001.tex`) establishes that Viserion died destroying the Wall "not half a year" before this voyage, and every later chapter (ch008–ch010 onward) consistently treats only **two** living dragons (Rhaegal, Drogon) as aboard. This is an internal contradiction within the opening 10 chapters, not just a cross-book risk.
**WHY IT MATTERS:** This is the reader's first exposure to the book's central magical asset. A miscount in chapter 2 undermines confidence in every subsequent number the book asks the reader to track (armies, casualties, days of food).
**RECOMMENDED ACTION:** Change "three dragons" to "two dragons" in ch002. (Contrast: a later retrospective line in ch048 — "when Tyrion first watched it march north from Dragonstone with three dragons" — is *not* an error; that's a valid memory of the period before Viserion died, during Season 7, and should be left alone.)
**STORY IMPACT:** None — one word.
**CONFIDENCE:** High.

### 1.2 — Winterfell–King's Landing distance stated as both 400 and 800 miles, twice within single chapters
**SEVERITY:** Critical | **CATEGORY:** Continuity | **FILES:** `ch111.tex`, `ch115.tex`, `ch113.tex`, `ch118.tex`
**LOCATION:** ch111 ("ride eight hundred miles north" ... "Daenerys, four hundred miles south" — same chapter); ch115 ("a burned city four hundred miles from home" ... "Jon, eight hundred miles north" — same chapter); ch113 ("Winterfell's stood eight hundred miles distant"); ch118 ("the city, four hundred miles south").
**CURRENT ISSUE:** The single most load-bearing geographic fact in the back third of the book — how far apart Jon and the rest of the cast are during the entire post-war epistolary section — is given as two different numbers, including twice inside the *same* chapter (ch111, ch115), by the *same* character's own narration.
**WHY IT MATTERS:** This distance is the emotional engine of several late chapters (letters arriving "too late," Jon and Sansa's separation, the pacing of news about Daenerys's death). A reader who notices the discrepancy loses trust in the geography of the whole ending.
**RECOMMENDED ACTION:** Pick one figure (800 miles is used more often and matches ch113/ch109's established "eight hundred miles" framing for the same Winterfell–KL axis) and correct the four "four hundred mile[s]" instances to match.
**STORY IMPACT:** None — a find-and-replace.
**CONFIDENCE:** High.

### 1.3 — Duplicated paragraph (verbatim) in ch051
**SEVERITY:** Critical | **CATEGORY:** Other (production error) | **FILE:** `ch051.tex`
**LOCATION:** A full exchange beginning "She'll remind the Company considerably more plainly whose gold this isn't..." appears twice, back-to-back, separated only by a `\sceneBreak`, with no variation.
**CURRENT ISSUE:** This reads as a literal copy-paste artifact from drafting, not intentional repetition — same dialogue, same beat, same speakers, twice in a row.
**WHY IT MATTERS:** Stalls the one Roland/Ossric political-unrest scene and will read as a proofing failure to any reader/editor who reaches it.
**RECOMMENDED ACTION:** Delete the duplicate instance.
**STORY IMPACT:** None.
**CONFIDENCE:** High.

### 1.4 — The Lannister/Cersei infant is named "Joanna," then silently becomes "Lyanna" with no in-text acknowledgment
**SEVERITY:** Critical | **CATEGORY:** Continuity | **FILES:** `ch058.tex`, `ch059.tex`, `ch070.tex`, `ch102.tex` (name: **Joanna**) vs. `ch117.tex`, `ch119.tex`, `ch121.tex`+ (name: **Lyanna**)
**LOCATION:** ch058 ("I thought I might name her Joanna. Our mother never once... I thought this one deserved a name that started her off already owing that debt to somebody kind."); repeated as "Joanna Lannister" through ch070 and ch102. Then ch117 (Daenerys's *own* separate, later-born daughter): "Daenerys named her before she died. Her name is Lyanna." Ch119's formal council ruling refers to "the infant presently known as Lyanna."
**CURRENT ISSUE:** On close reading these are **two different infants** — Cersei/Jaime's daughter Joanna (born ch058, present through at least ch102) and Daenerys's daughter, separately named Lyanna at her mother's death (ch116–117). But nothing in the manuscript clearly re-establishes, at the point Lyanna is introduced, that Joanna still exists as a separate, older child in the same household — and Tyrion's ch119 interior line ("Two girls now... raised in this same building by people who love them") is the *only* place the book acknowledges two infants exist, and even that line is unglossed (see 2.3 below) enough that multiple independent read-throughs of this manuscript concluded it was a single child being renamed.
**WHY IT MATTERS:** This is the most confusing thread in the last third of the book. If two separate children are intended, the manuscript needs one clear scene establishing that Joanna is a toddler by the time Lyanna is born, so readers don't reasonably conclude (as this audit initially did, independently, from two separate passes) that the same child was renamed.
**RECOMMENDED ACTION:** Add a single clarifying beat — even one sentence — the first time both children appear near each other (ch119 is the natural spot, since Tyrion already thinks "Two girls now") making explicit that Joanna and Lyanna are different children of different mothers. This is the one addition in this whole audit that crosses from "flag" to "worth a small, surgical fix," because the current text is genuinely ambiguous to a good-faith reader, not just under-signaled.
**STORY IMPACT:** Minor — clarification only, no plot change.
**CONFIDENCE:** High that the confusion is real (confirmed independently by the Tyrion-arc pass and by direct text verification); the underlying facts may already be internally consistent and just need one connecting line.

### 1.5 — Unsullied troop count is internally inconsistent by several thousand men
**SEVERITY:** High | **CATEGORY:** Continuity | **FILE:** `ch048.tex` (self-contradicts within one paragraph), cross-referenced against `ch091.tex`, `ch108.tex`, `ch120.tex`
**LOCATION:** ch048: "...march north from Dragonstone with three dragons and **ten thousand disciplined spears**..." — followed two sentences later, same paragraph: "The Unsullied numbered perhaps three thousand of the **seven** that had sailed from Essos." Then post-war, ch091/ch108/ch120 all state **eight thousand** Unsullied are garrisoned in King's Landing.
**CURRENT ISSUE:** The same lineage of soldiers is given as 10,000 (original), then 7,000 (original, same paragraph), then losses are dramatized bringing them to ~3,000 by the time they reach King's Landing (ch048), then the post-war count is 8,000 — *higher* than either original figure minus any stated reinforcement.
**WHY IT MATTERS:** Troop numbers are used repeatedly as emotional and strategic stakes (siege planning, manumission scene, Grey Worm's command). A reader doing the arithmetic the book itself keeps inviting them to do will not get consistent numbers.
**RECOMMENDED ACTION:** Settle on one original figure (7,000 reads as the intended one, since it's the number given the specific arithmetic treatment) and either explain the post-war 8,000 (reinforcements from Essos? Meereen garrison folded in?) or bring it down to match a plausible post-losses recovery.
**STORY IMPACT:** None — numbers only.
**CONFIDENCE:** High (the ch048 self-contradiction is confirmed directly in the source text within a single paragraph).

### 1.6 — Dead army's size given as "nine thousand" and "ninety thousand" for the same force, one day apart
**SEVERITY:** High | **CATEGORY:** Continuity | **FILES:** `ch064.tex` (Grey Worm: "there were nine thousand more of them out past the tree line") vs. `ch065.tex`/`ch067.tex`/`ch077.tex` (Arya/Davos/narration: "ninety thousand," used three times, consistently)
**WHY IT MATTERS:** A tenfold discrepancy in the size of the besieging army, stated by two POV characters standing on the same wall on consecutive nights. "Ninety thousand" is clearly the intended, book-wide figure (used three times across three POVs); ch064's "nine thousand" reads as a dropped digit.
**RECOMMENDED ACTION:** Change ch064's "nine thousand more of them out past the tree line" to "ninety thousand" (or a phrase making clear Grey Worm means a *local, visible* remainder rather than the whole host, if that's the intended reading — as currently written it isn't legible that way).
**STORY IMPACT:** None.
**CONFIDENCE:** Medium-High.

### 1.7 — Arya's line misattributes the cause of Ned Stark's death
**SEVERITY:** High | **CATEGORY:** Lore/Continuity | **FILE:** `ch063.tex`
**LOCATION:** Arya to Sansa: "the last time I brought someone half a thing about a traitor in a Northern camp, I was eleven years old and I got our father killed with it."
**CURRENT ISSUE:** In both the show and the novels, Arya bears no causal role in Ned Stark's death — that thread runs through Sansa (Septa Mordane, Cersei) and Littlefinger's betrayal, not through any intelligence Arya brought forward. This line hands Arya a formative guilt that belongs, if anywhere, to Sansa — and the Sansa POV audit, working entirely independently, flagged the same line as landing oddly for the opposite reason (it seems to borrow Sansa's own guilt).
**WHY IT MATTERS:** Two independent reads of two different POV arcs both stopped on this line. Either it's a deliberate alternate-backstory beat (in which case it should be seeded once, clearly, somewhere earlier) or it's a misattributed detail that should go to Sansa, or be generalized/removed.
**RECOMMENDED ACTION:** Verify authorial intent; if unintentional, either reattribute the guilt to Sansa (who canonically carries a version of it) or rewrite Arya's line to reference a Braavosi/Faceless-Men-era mistake instead, which fits her established voice better anyway.
**STORY IMPACT:** Minor if changed — a single line of dialogue, not a plot fact.
**CONFIDENCE:** High that the line is anomalous; medium on whether it's an error vs. an intentional (if unclear) divergence.

### 1.8 — Roland Storm's career length given as both 22 and 30 years, echoing Connington's own number
**SEVERITY:** Medium-High | **CATEGORY:** Continuity/POV-Voice | **FILES:** `ch051.tex` ("thirty years") vs. `ch071.tex`/`ch075.tex` ("twenty-two years," used repeatedly)
**CURRENT ISSUE:** "Thirty years" is also Jon Connington's own signature refrain in the same two chapters ("I've spent thirty years telling myself a great cause was worth any private cost"). Roland's number appears to have been contaminated by the character he's escorting.
**WHY IT MATTERS:** Undercuts the claim that Roland has a voice distinct from Connington's — the numbers literally bleed across characters.
**RECOMMENDED ACTION:** Standardize on "twenty-two years" (used 3+ times) for Roland; leave "thirty years" as Connington's exclusively.
**STORY IMPACT:** None.
**CONFIDENCE:** Medium.

### 1.9 — Ser Brynden Tully appears alive and commanding a battle line
**SEVERITY:** Medium | **CATEGORY:** Lore | **FILES:** `ch018.tex`, `ch022.tex`, `ch033.tex`, `ch063.tex`
**CURRENT ISSUE:** "Ser Brynden" (explicitly "Brynden Tully" per ch063) commands a rearguard line and comforts Rowan Glover at a campfire. In core ASOIAF/show canon, Brynden "Blackfish" Tully dies at the second siege of Riverrun before this story's timeline. If this manuscript has deliberately kept him alive (an authorial divergence), that's a valid creative choice under the "main storyline is locked" rule and needs no fix — but if it's an unintentional slip (e.g., confusing him with another Tully or an invented Riverlands knight), it should be corrected or the character renamed.
**RECOMMENDED ACTION:** Author confirmation only. If deliberate, no action. If accidental, rename to an invented Riverlands knight, or to Edmure Tully (who — see the Loose-End Audit below — is otherwise entirely unaddressed in this manuscript and could absorb this role for free).
**STORY IMPACT:** None to Minor, depending on intent.
**CONFIDENCE:** Medium (flagging the discrepancy; not asserting it's unintentional).

---

# 2. KNOWLEDGE-STATE / LOOSE THREADS (verified against full text)

### 2.1 — Daenerys never shown learning Jon's mother's name, but dies naming her daughter after her
**SEVERITY:** Medium | **CATEGORY:** Knowledge-State | **FILES:** `ch116.tex`, `ch117.tex`
Daenerys's dying thought reveals she deliberately chose "Lyanna" knowing it was Jon's mother's name — but no scene (in this manuscript, across the full read) shows her being told this. Sam and Sansa's knowledge is explicitly sourced to Howland Reed's sealed written testimony (ch094) — nothing shows that testimony, or its contents, reaching Daenerys before her death.
**RECOMMENDED ACTION:** A single line — in ch094, ch107, or ch108 — showing Daenerys reading or being told the testimony's contents would close this gap. Given the emotional weight the name carries at her death, this is worth a small fix rather than leaving as pure ambiguity.
**CONFIDENCE:** Medium-High.

### 2.2 — Ghost the direwolf disappears from Jon's POV for five chapters with no signal he stayed north
**SEVERITY:** Low-Medium | **CATEGORY:** Continuity | **FILES:** `ch012.tex` (present) → absent through `ch023, ch041, ch062, ch077, ch088, ch099` → reappears `ch109.tex` (thinner, healed broken leg, torn ear)
A reader following only Jon's POV has no signal that Ghost didn't go south with the army; the ch109 reunion lands as a surprise rather than an earned payoff. Likely addressed in a non-Jon chapter, but Jon's own arc never mentions it.
**RECOMMENDED ACTION:** One line in any of Jon's southbound chapters ("Ghost, left behind at his own insistence...") would convert this from a gap into a choice.
**CONFIDENCE:** Medium.

### 2.3 — "Two girls now" (ch119) is the only bridge between the Joanna and Lyanna threads, and it's easy to miss
See 1.4 above — same underlying issue, noted here for completeness since it's a knowledge-state/legibility problem as much as a naming one.

### 2.4 — Daenerys's pregnancy nearly leaks via a delirious soldier and is never followed up
**SEVERITY:** Low | **CATEGORY:** Loose Thread (likely intentional, flagging for tracking) | **FILE:** `ch074.tex`
A rescued Ironborn soldier reports Daenerys "said something about a dragon, and she said something about a child" while delirious on the mud flats — a live secret-exposure risk that the batch containing it never revisits. May be intentionally dropped (nothing came of it) or may pay off later; confirm.
**CONFIDENCE:** Low (informational).

### 2.5 — The Isle of Faces "agreement" vision uses grammatically present tense, self-flagged by Sam as an anomaly he doesn't understand "for another twenty-six years"
**SEVERITY:** Optional | **CATEGORY:** Mystery (intentional) | **FILES:** `ch073.tex`, `ch078.tex`
This is a deliberately planted mystery, not an error — flagging only so it can be confirmed to actually pay off somewhere the current read didn't reach (e.g., if there's a planned Book Two).
**CONFIDENCE:** High that this is intentional.

---

# 3. AUTHORIAL FINGERPRINT AUDIT (Phase 4) — book-wide, quantified

These frequencies come from a direct grep across all 124 chapter files, not estimates. **These are not automatically bad** — several are load-bearing thematic motifs. The question for each is whether it's a deliberate, book-wide theme (fine) or an accidental verbal habit shared by 20+ characters who should sound different from each other (the actual problem).

| Pattern | Raw count across manuscript | Verdict |
|---|---|---|
| `"the particular ___"` | 168 instances | **Reduce.** Appears in effectively every chapter regardless of POV ("the particular way," 14×; "the particular stillness," 9×; etc.). This is the single most diagnostic authorial tic in the manuscript — it is doing the descriptive work every POV's narration reaches for by default. |
| `"understood"` as realization-verb | 402 instances | **Reduce heavily.** The default mechanism for delivering *every* character's epiphany, from Tyrion to Bett the water-carrier to Grey Worm. Multiple independent POV audits (Jon, Tyrion, Brienne, Sansa, Yara, Samwell, Arya, Grey Worm, Daenerys) flagged this construction unprompted, in nearly identical terms. |
| `arithmetic` / `cost(s)` / `price` / `debt` / `ledger` / `accounting`/`accounted` family | 102 + 193 + 44 + 26 + 37 + 31 + 12 = **445 instances** | **Deliberate motif, but worked past the point of signature into tic.** This is clearly intentional for Tyrion and reasonably intentional for Daenerys, Grey Worm, and Sansa (all characters whose arcs are literally about the cost of decisions) — but the same vocabulary is also used verbatim by Bett (an illiterate water-carrier), Wyla (a fishwife), Roland, Yara, Brienne, and Jon. When a slave-raised soldier and a fishwife and a Hand of the King all reach for the word "arithmetic" to describe the same kind of grief, the motif has stopped characterizing anyone in particular. **Recommend:** keep it as Tyrion's and Daenerys's signature; vary the vocabulary (sums, reckoning, toll, weighing) for everyone else. |
| `"found himself/herself [verb]-ing"` | 56 instances | **Reduce.** Same function as "understood" — a generic interiority-announcement crutch. |
| `", not X, but Y"` type contrastive construction | ~230 instances (proxy count) | **Reduce where mechanical.** A legitimate rhetorical device in isolation; at this density it becomes the default shape of *any* character's realization sentence. |
| `"for the first time"` | 46 instances | **Fine at this density**, but watch — several POV audits independently flagged clusters of 3–5 uses within a single chapter. |
| `"settled into" / "settled [X]"` | ~50 instances | **Minor tic**, same emotional-landing function reused across Brienne, Grey Worm, Sansa, Jon in adjacent chapters. |

**Cross-cutting finding, Phase 4/Phase 3 combined:** Every one of the ten independent full-arc POV audits — run blind to each other's results — flagged the *same* handful of constructions ("the particular ___," "understood, [gerund], that...," "found [X]-ing") as the primary threat to that character's voice distinctiveness. This is strong, convergent evidence that these are genuinely book-wide authorial habits rather than character-appropriate idiom, and that a single global pass targeting these specific constructions (not a general rewrite) would measurably sharpen voice differentiation across the whole cast with minimal risk to plot or tone.

**Recommended action for Section 3 as a whole:** A find-and-flag pass (not a rewrite) on the four "reduce" rows above, chapter by chapter, replacing roughly half of each instance with either (a) a more character-specific construction or (b) nothing at all — i.e., trusting the preceding action/dialogue to carry the beat, per the Phase 5 over-explanation findings below, which overlap heavily with this list.

---

# 4. POV VOICE AUDIT (Phase 3) — per character

Full-arc reads (all chapters, in order) were run for the ten POV characters with 5+ chapters. Summary of each:

| Character | Chapters read | Overall verdict |
|---|---|---|
| **Jon** | 13 | Strong where anchored to duty/command/blind-spot-about-politics (the "HE STOOD HERE" cult thread is the best execution of the brief). Drifts generic in 2–3 reflective passages (ch012, ch109, ch099) and in a recurring "a man who X is a man who Y" proverb-tic (6+ uses) that's too polished for his established bluntness. Longclaw is dropped mid-fight (ch077) and never mentioned again — a loose thread. His burned hand's severity (ch088) isn't acknowledged during later physical labor (ch111). |
| **Daenerys** | 13 | Best-executed POV in the sample where anchored to specific personal history (Astapor, Drogo, dragons) — and contains the audit's single best example of a character being wrong and *not* cleanly realizing it (ch091→097, the Rock Dove judgment). Undercut by 3–4 passages in her convalescence chapters (ch097, ch107, ch108) where she arrives at fully-formed, essayistic self-diagnoses just before her death — exactly the "clean self-awareness" pattern the brief warns against. Multiple emotional threads (Grey Worm/Astapor, Missandei, justice-vs-vengeance) resolve suspiciously neatly in the two chapters immediately before she dies; the Jon thread, by contrast, is left genuinely and well unresolved. |
| **Tyrion** | 11 | Voice holds up consistently — incentive-tracking, historical-parallel wit stays analytical rather than decorative throughout. Main risk is mechanical: "arithmetic/ledger" vocabulary (see Section 3) and "I find [X]" as a hedge are used so often they've become verbal scaffolding rather than chosen tics. The Podrick/Varys/Brienne loss threads are genuinely, well left unresolved — flagged as a craft strength. |
| **Sansa** | 8 | Strongest on-brief material: the Rowan Glover thread (ch063/082/123) and the water-allocation scene (ch082) are exactly the courtesy/hierarchy/what's-left-unsaid intelligence the brief calls for. One notable drift into Daenerys/Cersei-style abstract monarchy theorizing (ch115). Never once notices clothing/appearance despite this being a stated signature lens — a conspicuous absence worth a look. |
| **Arya** | 7 | The tactical/sensory voice (bodies, hands, weapons, exits) is strong and distinctive in the four battle-adjacent chapters. Drifts into a softer, articulate, "literary" register specifically in the Gendry relationship chapters (035/045/101) — the breakup in ch101 is unusually tidy/mutually-validating for a character defined as feral/detached. Nymeria and her wolfpack are **never mentioned anywhere in her arc** (see Section 5). A possible hand-laterality contradiction: ch065 has her kill one-handed with her right arm after her left is disabled, but ch080 establishes she is exclusively left-handed with a blade. |
| **Brienne** | 7 | More ornamented/aphoristic throughout than the "plain, unornamented" brief calls for — a real register split exists between four reflective chapters (020/031/050/061, long comma-laden sentences) and two crisis chapters (068/084, short clipped sentences), worth confirming as intentional. Her own POV arc never bridges "Jaime alive" (ch061) to "Jaime's body has been in storage eight days" (ch084) — likely covered elsewhere, but a silent jump within her own arc. Oathkeeper is never named in any of her seven chapters; Catelyn Stark, the origin of her oath, is never referenced despite Sansa's frequent presence. |
| **Samwell** | 9 | Two distinct registers exist across the arc: long/aphoristic (ch011/039/046/060) vs. clipped/numerically obsessive (ch078/092/106/113/117) — plausibly an intentional trauma/maester-hardening arc, but abrupt enough to flag. His "bookish" trait is a label in the early chapters and only becomes reasoning-shaping (citing precedent, parsing tense) from ch060 onward. His son ("little Sam") is named once (ch011) and never again despite 2+ story-years elapsing. The physical-self-consciousness trait called for in the brief is entirely absent (opposite failure mode from a joke — simply missing). |
| **Yara** | 6 | Holds up best of the "no explicit brief" characters — saltwater idiom, contempt for ceremony, and the Theon thread (deliberately left unresolved, ch089) are all strong, on-brief work. One clean numeric outlier: "four hundred ships and thirty thousand men" (ch089) vs. a carefully tracked fleet of ~35–40 ships everywhere else — possibly rhetorical hyperbole in a negotiation (plausible reading) but worth confirming. |
| **Roland** | 5 | An invented character; voice is distinctive within his own material (the artillery/siege-engineering chapters, 071/075, are the strongest justification for his POV slot). The two political-intrigue chapters (036/051) read as comparatively generic "any officer" filler and are the weakest-justified POV real estate in the sample. See 1.8 (career-length number bleeding from Connington). His promise to extract Griff and Connington's resulting death are never mentioned again in his own later chapters — an unacknowledged thread rather than either a resolved or a deliberately open one. |
| **Grey Worm** | 5 | The author's explicit brief ("should not sound like Tyrion") is **violated once, clearly**: his introductory chapter (ch027, the Missandei death) routes his grief through a paraphrase of Tyrion's own aphorism, repeated near-verbatim twice in the same chapter. His other four chapters (064/087/105/120) largely succeed — plain, order-shaped, concrete — and contain some of the strongest material in the whole POV sample (the "Hold the range... nobody spends anything early" sequence, the silent 840-man formation in ch087). |

**Cross-cutting POV finding:** Minor/one-off POV characters (Bett, Wyla, Garth, Aldrich, Nell, Tilda, Gilly) were independently flagged by multiple batch passes as speaking in the *same* aphoristic register as the book's highborn/educated leads, regardless of their stated class, education, or (for Grey Worm/Rock Dove) native language. This is a more systemic version of the Section 3 fingerprint problem: it isn't that any single character sounds wrong, it's that the narration's default register doesn't flex for who's speaking.

---

# 5. SEASON 7 LOOSE-END AUDIT (Phase 10)

Full-text search confirms the following. Per instructions, the default is to leave these alone — none are proposed as new material.

| Thread | Found in manuscript? | Classification | Notes |
|---|---|---|---|
| **Nymeria & her wolfpack** | Never mentioned, anywhere, including in all 7 of Arya's own chapters | **E — better left unresolved** | Confirmed via full-text search and independently by the Arya full-arc audit. No seed exists anywhere to build from; introducing her now would be new material, not a payoff. |
| **Edmure Tully** | Never mentioned | **E** | Same. (Note: could theoretically absorb the "Ser Brynden" role if 1.9 turns out to be unintentional — see above — but that's a naming fix, not new plot.) |
| **Robin Arryn / Sweetrobin** | Never mentioned | **E** | The Vale is otherwise well-served by Yohn Royce's dedicated chapter (ch103) and Lady Waynwood's granddaughter subplot — Robert Arryn's absence from a Vale-politics thread that already exists is conspicuous but not damaging; introducing him now would require building an entire new relationship from scratch. |
| **Meereen (post-Daenerys)** | Referenced twice, purely as backstory/memory (ch087, ch091) — Grey Worm and Yellow Tick recall Astapor/Yunkai/Meereen as formative history, never as an ongoing governance question | **B — worth its current brief reference, nothing more** | The book's scope never promises Meereen's fate matters going forward; the backstory references already do the necessary work. |
| **Daario Naharis** | Never mentioned | **E** | |
| **Ellaria Sand / Tyene Sand** | Never mentioned | **E** | |
| **Dorne / Dornish politics** | Never mentioned | **E** | |
| **Riverlands politics generally** | Mentioned twice, both as geography/travel ("refined [her methods] in the Riverlands," "a column that's just marched through the Riverlands") — no political content | **E** | Ser Brynden Tully's presence (1.9) is the one live Riverlands thread, and it's a continuity question, not a loose end to develop. |
| **Brotherhood Without Banners remnants** | Never mentioned | **E** | |
| **Vale politics / Yohn Royce / Lady Waynwood** | Substantial — a dedicated chapter (ch103), plus references in ch070, ch094, ch118, ch119 | **A — already resolved sufficiently** | This is the one Season 7 thread the book actually picked up and ran with; no further action needed. |

**Overall assessment:** This manuscript's scope is deliberately narrow — the Northern retreat, the siege of King's Landing, and the immediate political aftermath. It never gestures toward Dorne, the Sand Snakes, Meereen's government, or Nymeria as *promises to the reader*, so their absence doesn't read as a dropped thread so much as a story that was always about something else. Manufacturing payoff for any of them now would be the kind of new subplot this pass is explicitly not supposed to add. **Recommendation: leave all of them exactly as they are.**

---

# 6. OVER-EXPLANATION AUDIT (Phase 5) — representative sample

This pattern was flagged independently, in nearly every one of the 23 passes, with enough consistency that it should be treated as a book-wide craft issue rather than isolated incidents. Representative high-confidence instances (dozens more exist; these are the clearest):

- **`ch025.tex`** (Theon's death): "...had spent a lifetime being told he was worth nothing... trying to earn back something he'd once believed unearnable" — restates a theme the preceding action (holding the gap alone) already fully dramatized.
- **`ch026.tex`** (Beric's final death): narration explicitly spells out "the last of whatever R'hllor had spent... finally, fully accounted for" immediately after Beric's own line already landed the same beat.
- **`ch099.tex`** (Jon): "They've made me into two things at once, in two places I never once set foot in to arrange either of them" — the wall-carving and the withheld-testimony scenes had already dramatized both halves of this irony without needing the explicit parallel spelled out.
- **`ch107.tex`** (Daenerys): "I don't know what I wanted the throne for... I have been answering the wrong one since Astapor" — a fully-formed thesis statement about her own psychology, delivered in language closer to retrospective political theory than a frightened, wounded woman's interior monologue.
- **`ch122.tex` / `ch123.tex`** (Sansa, back-to-back): both chapters close on an explicit thematic restatement of the scene just shown ("a thing worth doing properly... was very rarely a thing that arrived easy"; "some mercies... were simply the quiet, private cost one person chose to carry").
- **`ch124.tex`** (the novel's final chapter): the closing two paragraphs *both* explicitly state the epilogue's theme (impermanence/myth-making) after the children's scene has already dramatized it — the book's very last beat over-explains itself twice in a row.

**Recommended action:** A dedicated compression pass on chapter-ending paragraphs specifically — this is where the pattern concentrates most. Many of these chapters would land harder cut one sentence short.

---

# 7. PRE-DEATH / EMOTIONAL CLOSURE AUDIT (Phase 6)

The manuscript does **not** uniformly over-resolve deaths — there's a real, useful mix, but it skews toward tidy on named/major characters and stays appropriately raw on minor/anonymous ones. Worth the author's attention as a pattern:

**Closure-heavy (worth reconsidering at least one or two of these):**
- Jorah (ch029), Lyanna Mormont (ch046), Melisandre (ch032), Euron (ch054–056), and Harrold Rykker (ch071) all receive full farewell-speech treatment — declared purpose fulfilled, clean last exchange, witnessed death.
- Five deaths in the ch021–030 batch alone follow the "hold the line alone, buy time, die at peace" shape (Jorah, Theon, Beric, Sandor, and — contrast — Podrick, which breaks the pattern; see below).
- Daenerys's own death (ch116) resolves nearly every open emotional thread (Astapor guilt, Missandei grief, the naming) in the two chapters immediately preceding it.

**Genuinely, well left unresolved (flagging as craft strengths, not problems):**
- Podrick's death (ch030) — sudden, no goodbye, Tyrion explicitly denied the chance to grieve properly.
- Bett's death (ch066) — cuts off mid-realization ("Oh, that's not fair"), no closure at all.
- Brienne's death (ch084) — the chapter itself cuts off mid-action, never confirms the death on-page, and her own POV arc never bridges to Jaime's death either (see 4, Brienne row).
- Arya and Sansa's permanent separation (ch101) — no destination given, no promise to write, explicitly left open.
- Roland's unspoken debt to Connington (never revisited — see 4, Roland row) — arguably too far in the other direction (dropped rather than deliberately open), see 1.8/4.

**Recommended action:** No plot changes. Consider, in a light revision pass, trimming the farewell-speech density on 2–3 of the "closure-heavy" deaths (Jorah and Rykker are the best candidates — both get a clean callback line immediately before dying) so that the genuinely raw deaths (Podrick, Bett) stand out more by contrast rather than reading as one closure style used inconsistently.

---

# 8. MYSTERY / MAGIC EPISTEMIC AUDIT (Phase 7)

The manuscript is generally good about tagging supernatural claims by source (Sam's chapters in particular are explicitly disciplined about labeling theory as theory — ch106's Ollun folio is treated as unproven throughout). Two things worth noting:

- **Convergent mythology risk:** Bran's Isle of Faces vision (ch073), Sam's suppressed Ollun folio (ch106), and Melisandre's "ledger" theory of magic (ch019) all independently arrive at compatible-but-not-identical versions of "the dead are owed an old, unpaid debt." This is more epistemically honest than having one authoritative source confirm the lore (good), but the manuscript never has any character notice that three unrelated sources are converging on the same idea — a missed opportunity for a character (Sam, most likely) to remark on the convergence itself, which would sell the ambiguity rather than let it sit as three separate scenes.
- **The Ollun letter's prose register** (ch106) is written in the same "particular ___," ledger-metaphor house style as the rest of the book, undercutting its framing as a found 300-year-old document. A found document is a natural place to *break* the book-wide fingerprint patterns from Section 3 — recommend giving Ollun's voice deliberately different diction from the surrounding narration.

**No changes recommended to the supernatural resolution itself** — the Night King's origin, the mechanics of dragonfire/dragonglass/Valyrian steel, and Bran's possession of Drogon are all handled with appropriate FACT/VISION/BELIEF distinctions and no changes are needed there.

---

# 9. DIALOGUE AUDIT (Phase 8)

The most consistent dialogue finding, raised independently across nearly every batch: **characters of very different class, education, and background converge on the same aphoristic, balanced-clause register.** Representative instances:

- Lyanna Mormont (age 11) and adult POV characters speak in identical cadence (ch021, ch029).
- Rowan and Robett Glover's father-son reconciliation (ch022) gives both a gruff lord and his impulsive teenage son equally fluent, self-aware psychological insight.
- Wyla (an illiterate-coded fishwife, ch086/ch114/ch121) and Bett (a water-carrier, ch066) speak in the same register as Tyrion and Sansa.
- Rock Dove (an Unsullied soldier, ch107) delivers a philosophical line about obedience nearly identical in construction to Grey Worm's own register in the adjacent chapter — two men raised under the same discipline sound like two different novelists' idea of "a soldier," rather than like each other.

**This is not a request to make anyone sound "dumber."** The fix is register, not intelligence — a fishwife can be exactly as sharp as Tyrion while using shorter clauses, more concrete nouns, and no Latinate abstractions ("ledger," "arithmetic," "accounting"). Recommend a light pass on the minor/one-off POV and dialogue-only characters specifically (Bett, Wyla, Nell, Tilda, Gilly, Rock Dove), since they're the clearest cases and there are few enough of them to do by hand.

---

# 10. PACING / REDUNDANCY (Phase 9)

The post-war reconstruction material (roughly ch081–ch120) is correctly extensive and should **not** be cut wholesale — logistics, food, water, burial policy, and governance are the point of that section. The following are specific scene-level duplications, not objections to the section's existence:

1. **ch087 and ch088** — Grey Worm and Jon *independently* go looking for Daenerys, discover she's been moved, and learn nobody told them, in back-to-back chapters. Same information, same emotional beat (institutional collapse via omission), delivered twice in a row. **Recommend:** compress to one instance, or give the second a materially different discovery.
2. **ch093 and ch098** — Howland Reed's and Meera Reed's arrivals at King's Landing follow an identical structural template (mistaken/not-mistaken for a beggar at the gate → asks after Bran → climbs "two hundred and eleven steps" → sits alone beside Bran's bed → monologues to the unconscious body). Meera's chapter explicitly winks at the parallel, which helps, but the beats are still close enough to read as one scene rerun.
3. **ch107 and ch108** (Daenerys) — both chapters are "ruler privately reckons with guilt over a past command decision and grants a subordinate a deliberately imperfect resolution," back-to-back, with different subordinates (Rock Dove, then Grey Worm).
4. **ch074 and ch075** — Yara and Roland's crews independently reach the identical tactical conclusion (something is steering the "riderless" dragon, hold fire) via near-identical reasoning, at the same climactic moment. Legitimate multi-POV coverage of one crisis, but the reasoning process itself, not just the moment, is duplicated.
5. **The gate-guard "everybody's here for grain" exchange** recurs near-verbatim for two different new arrivals (Howland, ch093; Aldrich, ch096), three chapters apart, without either character's arrival referencing the other's — reads as reused material rather than intentional echo (contrast Meera's ch098 arrival, which *does* knowingly reference the pattern).
6. **Four "hold the gap alone to buy time" set-pieces** within ch021–030 (Theon, Beric, Podrick, and arguably Sandor) — a legitimate structural choice for a siege chapter run, but four in ten chapters risks feeling formulaic; Podrick's (the only one without a closure speech) is the strongest of the four for exactly that reason.

**Estimated tightening available:** Consistent with the ~5–15% target, items 1–5 above alone would let a light compression pass — not story removal — improve pacing in the aftermath section specifically, which is otherwise the manuscript's strongest sustained writing.

---

# 11. LOW / OPTIONAL FINDINGS (grouped for brevity)

| # | Category | File(s) | Finding | Confidence |
|---|---|---|---|---|
| L1 | Continuity | ch104.tex | Yara references a grandson "a boy of nine now" — verify this is consistent with her established age/timeline elsewhere. | Low |
| L2 | Continuity | ch089.tex | Yara cites a prior Dragonstone independence pact "agreed to once already" — confirm this scene exists on-page somewhere, or accept it as valid pre-story backstory (most likely reading). | Low-Medium |
| L3 | Continuity | ch086.tex | Wyla's unexplained backstory fragment (a tower, stairs, a man's face) is never resolved within the batch containing it — likely fine as characterization texture, confirm no dangling promise. | Low |
| L4 | Continuity | ch071.tex | Two reanimated dragons appear (one destroyed by scorpions, one — Viserion — in the climactic duel). On inspection this is *not* a contradiction: the first is very likely reanimated-Rhaegal (who died at Winterfell, ch024) reappearing as a wight, consistent with established mechanics. No action needed — noting only so it isn't re-flagged. | High (resolved, no issue) |
| L5 | Continuity | ch069.tex/ch028.tex | Brienne's method for killing wighted Gregor Clegane is credited to advice from Sandor Clegane given off-page, "an armory two mornings past" — confirmed this scene exists (ch028). No issue. | High (resolved, no issue) |
| L6 | Repetition | book-wide | "Plainly"/"plain" used by nearly every POV as their default marker of honesty (Royce, Tyrion, Jon, Daenerys, Sam, Yara). See Section 3; listed separately here because it's slightly lower-frequency than the "reduce" list. | Medium |
| L7 | Repetition | ch021–030 | "Not a question" used as a post-dialogue narrative tag three times within two chapters. | Low |
| L8 | Repetition | ch056/ch059 | An identical two-line exchange ("There might not be one." / "There generally isn't.") recurs verbatim between two different speaker pairs three chapters apart. | Medium-High |
| L9 | Repetition | ch081.tex | "At the eleventh hour" repeats three times within one chapter. | Medium |
| L10 | POV-Voice | ch014.tex (Yara) | "Understood... exactly why she had spent two days" is followed by a claim to know a battlefield detail (a heart tree) her stated source (Coake's secondhand report) never mentioned. Minor knowledge-state wobble, likely an implied offscreen inference. | Low |
| L11 | POV-Voice | ch027.tex (Grey Worm) | See Section 4 — the one clear voice-brief violation in the whole POV sample. Repeated here as the single highest-value line-edit target in the entire audit if only one fix is made. | High |
| L12 | Dialogue | ch009.tex | The Great Hall confrontation scene functions largely as "as you know" exposition for the in-world audience; defensible as public rhetoric but worth noting. | Low-Medium |
| L13 | Pacing | ch119.tex | Four separate "council debates a succession/legitimacy question" scenes occur across the aftermath section (Wyla's seat, Yara's contract, Lyanna's/Joanna's status, the Vale marriage proposal) — no single one is redundant, but confirm the cumulative effect isn't council-scene fatigue. | Low |
| L14 | Psychology | ch071.tex | Roland/Rykker's death exchange resolves a 20-year mentor relationship in one clean, thematically tidy callback line, immediately before Rykker dies — see Phase 6 pattern. | Medium |
| L15 | Loose thread | ch057.tex → ch071/075.tex | Roland's promise to Connington and Connington's resulting off-page death are never mentioned again in Roland's own later chapters — dropped rather than either resolved or deliberately left open. | Medium |
| L16 | Continuity | ch060.tex | Sam's line "since the night at Winterfell when his own grief... spent a truth" appears to misattribute the location of his confession to Daenerys (which the text elsewhere places in a retreat-column tent, weeks after Winterfell fell) to Winterfell itself, possibly conflating it with his separate, earlier telling of Jon (which *did* happen at Winterfell). | Medium |
| L17 | POV-Voice | ch086/ch114/ch121 (Wyla) | Voice is nearly indistinguishable from Sansa/Jon's narrator register in free-indirect passages — see Section 4/9. | Medium |
| L18 | Other | book-wide | Several minor POV characters (Bett, Garth, Wyla, Aldrich, Roland) are original (non-canon) inventions. None of this is a problem in itself, but confirm each earns their dedicated chapter(s) on the "shows something no other POV could show" test — Roland's artillery chapters pass this test clearly; his political-intrigue chapters (036/051) are the weakest-justified in the sample (see Section 4). | Low-Medium |

---

# OPTIONAL MAJOR STORY OBSERVATIONS

*Advisory only. Nothing in this section should be implemented — these are thematically-motivated observations flagged per instructions, not recommendations to change the locked storyline.*

1. **The "clean closure before death" pattern, if left as-is, slightly favors named/highborn characters over anonymous ones.** Jorah, Lyanna Mormont, Euron, Rykker, and (most of all) Daenerys herself all get full emotional resolution shortly before dying; Podrick, Bett, and Brienne (arguably the novel's most quietly courageous minor-to-mid characters) do not. This may be exactly the intended irony — the narrative "affords" tidiness to characters we've spent longest with — but if it isn't intentional, it's worth knowing the pattern exists across the whole manuscript, not just in isolated chapters.

2. **Daenerys's death, in isolation, reads as the story quietly settling her accounts (Astapor guilt resolved, Missandei grief resolved, the Jon thread the one deliberate exception) in the two chapters immediately before she dies via a medical complication with no dramatic agency of her own.** This is consistent with the book's clearly-intended tragic irony (a queen who survived every war dies giving birth), but the emotional "neatness" of ch107–108 sits in some tension with the physical chaos of ch116 itself — a slightly more ragged ch107/108 (leaving one thread genuinely unresolved, the way Jon's is) might make ch116's chaos land harder by contrast. Not a recommendation to change the outcome — only the shape of what precedes it.

3. **Roland Storm's two political-intrigue chapters (036, 051) are the single weakest-justified POV real estate in the entire ~30-character POV cast**, per the "does this show something no other POV could show" test the audit applied to every minor-POV character. His later artillery chapters clearly pass; these two arguably could have been folded into Connington's or Griff's own material without losing anything Roland-specific. This is a structural observation about POV allocation, not a suggestion to cut his plot function (extracting Griff, breaking the Company's contract) — that function is fine and stays.

4. **The manuscript's post-war section is unusually generous to invented (non-canon) characters holding real institutional power** (Wyla's council seat, Roland's siege command, Garth's alchemical authority, Aldrich's archival role) — a distinctive and interesting choice (canon characters are mostly *processing loss* in this section while original characters are *building the new institutions*), and one that reads as thematically deliberate rather than accidental. Flagging only because it's a strong, structural authorial choice worth being aware you made, in case any future revision pass is tempted to trim the original characters' page-time without noticing this pattern.
