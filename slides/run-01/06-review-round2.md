# Faithfulness review of the slide draft

Reviewer: independent sub-agent, 2026-11-14 (round 2)
Bullets and leads checked: 68   Findings: 4

Scope of this round: slides 3, 4, 5, 7, 8, 11, 12, 13, 15, 17, 18, 19 and 20
only (65 bullets and the 3 non-empty leads on slides 17, 18 and 19). Read:
`05-slides.json`, `03-evidence.json`, `04-outline.json`. Not read: the
first-round report, the wiki, `raw/`, `docs/`, git history. A card with
`"kind": "gap"` was accepted as evidence that the named wiki section carries
the "not covered" marker. Leads carry no card list in `05-slides.json`, so
each lead was checked against the cards the outline assigns to its slide.

## Findings

| # | Slide | Bullet (first words) | Verdict | Evidence | Send back to |
|---|-------|----------------------|---------|----------|--------------|
| 1 | 7 | "Style rule: non-blocking assignments for clocked logic…" | UNSUPPORTED | R3 states the practice ("Clocked logic uses non-blocking assignments…") but neither R3 nor any other card calls it a style rule or says the source is a style guide; the word "style" appears on no card. Added label. Minor: the rest of the bullet is supported. | 5 (drop the label), or 3 if the label is wanted |
| 2 | 7 | "Style rule: flip-flops, not latches…" | UNSUPPORTED | Same as finding 1 for R4: the content is supported, the "Style rule:" label is not on any card. Minor. | 5 (drop the label), or 3 if the label is wanted |
| 3 | 8 | "Testing grows from a basic smoke test to stress tests…" | UNSUPPORTED | FV4 says testing grows in steps and that the smoke test comes first. FV5 describes stress tests but does not place them in that sequence, let alone as its end point. "From … to" adds an ordering the cards do not state. The regression half (FV6) is supported. | 5 |
| 4 | 20 | "What is clock skew, and which violation does it mainly cause?" | UNSUPPORTED | CT6 says clock skew is the main cause of hold violations. The question presupposes the converse, that hold violations are the main effect of skew; CT3 only says skew problems "could later cause hold violations". Slide 14 itself keeps the card's direction. Suggested wording: "…and which violation is it the main cause of?" | 5 |

All other bullets and leads in scope are OK. Points that were looked at
closely and passed:

- Slide 8, bullet 5 ("In OpenTitan, done means…"): FV7 says "the project";
  "OpenTitan" comes from the section title in FV8's citation. Accepted as a
  narrowing, not a widening.
- Slide 8, bullet 3: FV3 reports that the tutorial "calls it essential to
  verify both"; the bullet states that both are verified. Accepted.
- Slide 12, bullet 1: PL2 gives the meaning of 0 and of 1; "from 0 … to 1"
  is a fair reading.
- Slide 12, bullet 4: PL1 says the tutorial explores the options' "impact on
  area and timing"; "affect" is accepted.
- Slide 13, bullet 4: T6 says "becomes metastable"; "can go metastable" is
  weaker, not stronger.
- Slide 17 lead: supported by SG1 (assigned to the slide in the outline, not
  listed on any bullet).
- Slide 18, all five bullets: each side of each difference matches the
  source id it carries in D1 to D5.
- Slide 19, bullet 5: each of the three gaps matches a gap card (G1 coverage
  / Definition, G2 standard cell library / Definition, G3 routing / Inputs).
- Slide 20, bullets 1, 2, 4, 5: each is answerable from the slide it points
  to, and each presupposition is on a card (LS2/LS5/LS6, T2/T3, SG3/LV1,
  C1/C5).

Two things that are not faithfulness verdicts but should be seen by the
owner:

- Slide 18 lead ("S1, S2, … are the sources under each slide") is a claim
  about the rendered deck. `05-slides.json` has no per-slide source field, so
  it cannot be confirmed from the three files reviewed; check it at the
  rendering gate.
- Slide 19: the outline purpose says "name the four open gaps" and "recap
  the ten stages with input and output". The deck has three gap cards and
  the bullet names three gaps; the recap is four sentences following the
  five-step view of slide 4, not ten stages with inputs and outputs. The
  bullet is faithful to its cards; the mismatch is with the outline text.

## Teaching notes

1. Slide 5 defines "HDL", "RTL" and "PDK" without ever spelling them out,
   although cards V2, V1 and V6 carry the expansions. Slide 4 says "hardware
   description language" in full but never attaches the abbreviation, so a
   newcomer has to guess that slide 5's "HDL" is the same thing. "RTL" is in
   the deck title and on slide 7 and is expanded on no slide in scope.
2. "Macros" appears on slide 5 (inside the definition of netlist) and on
   slide 11, and is explained nowhere; no card in the deck defines it. On
   slide 5 this means one of the six definitions depends on an undefined
   word.
3. Slide 15, bullet 4, says a charged wire can "damage a gate". Slide 5 has
   told the reader that a cell is "a CMOS logic gate", so the reader will
   take "gate" to mean a logic gate; AN1 means a transistor gate and its
   thin oxide.
4. Slide 12 uses "resizer", "buffers", "slew" and "fanout" with no
   explanation, and talks about "timing optimization" one slide before
   slide 13 introduces the timing vocabulary. The order is fixed by the
   approved outline, but a half-line gloss on slide 12 would help.
5. Slide 7, bullet 5, puts two unrelated facts in one bullet ("Verilator
   lints the code it is given. Risk: simulation and synthesis
   disagreeing."). A newcomer may read it as Verilator causing or curing
   that risk, which neither R7 nor R6 says, and "lints" is not explained.
