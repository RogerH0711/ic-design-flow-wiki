# Faithfulness review of the slide draft

Reviewer: independent sub-agent, 2026-11-14
Bullets and leads checked: 96 (91 bullets, 5 non-empty leads)   Findings: 9

Files read: `05-slides.json`, `03-evidence.json` (`wiki_sentence` only; `point` ignored), `04-outline.json`. Nothing else was read. Every card id listed in the draft exists in the evidence file.

## Findings

| # | Slide | Bullet (first words) | Verdict | Evidence | Send back to |
|---|-------|----------------------|---------|----------|--------------|
| 1 | 5 | "Library: typically several sizes of the same cell." | UNSUPPORTED | V5 says a *standard cell* library "typically contains" several sizes of the same cell. The bullet drops "standard cell" and, on a slide of definitions, presents one property as what a library is. No card defines a library (slide 19 itself lists that definition as a gap). | 5 (say "A standard cell library typically contains ..."; 3 only if a real definition is wanted) |
| 2 | 7 | "Checked by: lint. Risk: simulation and synthesis disagreeing." | UNSUPPORTED | R7 says only that Verilator lints the SystemVerilog code it is given as part of its normal use. The bullet widens this to "the stage is checked by lint", dropping the tool and the language. The "Risk" half is supported by R6. | 5 |
| 3 | 8 | "In OpenTitan, done means every checklist item ..." | WRONG-CARD | FV7 says "the project" and never names OpenTitan. The only card text that ties S10 to OpenTitan is the cited section title on FV8 ("Design Verification Methodology within OpenTitan"). Add FV8 to this bullet. Low severity: the qualifier narrows the claim. | 5 |
| 4 | 12 | "Steps: global placement, detailed placement, then timing optimization ..." | UNSUPPORTED | PL3 says the flow's list of steps "includes" these three. The bullet presents them as the steps and adds an order ("then") that the card does not state. Low severity. | 5 |
| 5 | 12 | "A repair step inserts buffers and resizes gates to fix slew, capacitance, and fanout violations." | UNSUPPORTED | PL4 ties only buffer insertion to fixing the violations ("inserts buffers to fix maximum slew, maximum capacitance, and maximum fanout violations ... and resizes gates"). The bullet makes gate resizing a fix for those violations too, and drops "maximum". | 5 |
| 6 | 19 | lead: "Ten stages, three parts:" (and the labels Front / Middle / Back in bullets 1-3) | NO-CARD | No card divides the flow into three parts or uses front, middle, or back. The only "three" in the deck is SP1 (three broad stages in the life of a design, in OpenTitan), which is a different division. | 5 (drop the three-part labels; regroup by the five steps of F1-F5) |
| 7 | 19 | "Front (stages 1-3): decide, write, and verify what the chip does." | UNSUPPORTED | Listed cards F1 and F2 cover design entry and functional verification only. Nothing in them covers "decide" (stage 1, specification). The specification cards are SP1-SP5, and SP1 limits the claim to the OpenTitan project. | 5 |
| 8 | 19 | "Back (stages 5-10): physical implementation and signoff produce a checked layout." | UNSUPPORTED | F4 names four sub-steps (floorplanning, placement, clock tree synthesis, routing); F5 is signoff. Neither covers stage 9 (layout finishing). D2 states that the source with a layout generation stage has no signoff stage and the reverse, so the merged range 5-10 is the drafter's own synthesis. | 5 |
| 9 | 19 | "Not covered by our sources: definitions of coverage and of a standard cell library, what cocotb is, the inputs of routing." | NO-CARD | No card records any gap. "cocotb" appears in no card and nowhere else in the deck. The claim about coverage sits oddly beside slide 9, where C1-C6 describe coverage at length. The four gaps cannot be checked from the evidence file. | 3 |

All other bullets and leads (87) are OK. Borderline cases judged OK, for the record:

- Slide 3, bullet 1: "one specific function" against A1 "a specific function".
- Slide 6, bullet 4: "up to three reviews" against SP5 "three reviews are mentioned", one of them "potential".
- Slide 6, bullet 3: "refined from their comments" against SP4 (authors answer comments and keep refining).
- Slide 14, bullet 4: the "so" joining CT6 and CT3; CT3 itself gives the hold-violation reason for fixing skew.
- Slide 15, bullet 3: "ends with search and repair" against RT3, where it is the last item listed.

## Teaching notes

1. **Slide 4 before slide 5.** Slide 4 uses HDL, RTL, and netlist; slide 5 ("Six words you need first") defines them one slide later. The outline says these are defined "before they are used". Either gloss them on slide 4 or move the vocabulary slide up (an outline change, so the owner decides).
2. **Slide 13: "slack" is in the title and never defined.** Bullet 3 says a violation "shows up as negative slack", and slide 16 reports worst slack and total negative slack, but no bullet says what slack is, and no card defines it. Needs a card (node 3).
3. **DRC and LVS are never spelled out; "antenna" is never explained.** DRC first appears on slide 15 ("its own DRC engine"), two slides before slide 17 introduces it. No card in the deck expands either abbreviation or says what an antenna violation is (RT6, SG5 only name it). Needs cards (node 3). EDA on slide 3 is also unexpanded, although A2 has the expansion.
4. **Slide 18: source ids.** S1, S2, S3, S4, S8, and S10 are used as if the audience knew them. The deck never says what the sources are. Name each source in words at first use, or add a legend.
5. **Slides 11-12: undefined jargon in a row.** Die, core, core utilization, macro (first used on slide 5), tap cell, endcap cell, IR drop, slew, and fanout all appear without a definition. A reader who knows only gates and flip-flops cannot follow slide 11 as written.

Not findings, noted for the owner:

- Slide 19's outline purpose is "recap the ten stages with input and output"; the draft does not list inputs and outputs per stage.
- Slide 20 asks "Why does the clock get a stage of its own? (slide 14)". Slide 14 describes skew and hold violations, but no bullet and no card states the reason in so many words.
- Slide 8, bullet 5 says "every stage", meaning the verification stages of FV7. In a deck that numbers its own slides "Stage 1" to "Stage 10" this is easy to misread.
