# Faithfulness review of the slide draft

Reviewer: independent sub-agent, 2026-11-14 (round 3, narrow: slides 5, 7, 8, 15 and 20 only)
Bullets and leads checked: 25   Findings: 1

Scope: 5 bullets on each of the five slides; all five `lead` fields are empty,
so there were no leads to check. Only `05-slides.json`, `03-evidence.json` and
`04-outline.json` were read. For the quiz slide (20), which lists no cards,
the facts each question presupposes were checked against the cards of the
slide it points to (C5, LS2/LS5/LS6, T2/T3, CT5/CT6, SG3/LV1).

## Findings

| # | Slide | Bullet (first words) | Verdict | Evidence | Send back to |
|---|-------|----------------------|---------|----------|--------------|
| 1 | 15 | "Common problem: congestion stops global routing." | UNSUPPORTED | Added frequency claim. RT5 only says a design with a congestion problem "makes global routing end with an error"; no card says the problem is common. The rest of the bullet is supported. Rewording to "Problem: ..." is enough. | 5 |

## Borderline bullets passed as OK

These were judged supported, but each rests on a reading the owner may want
to know about.

- Slide 8, "In OpenTitan, done: every checklist item ...": FV7 says "the
  project", not OpenTitan. The name appears only in the section title inside
  the citation of FV8 (same source, S10). Passed because the condition narrows
  the claim rather than widening it.
- Slide 8, "Both the RTL and, later, the gate-level netlist are verified.":
  FV3 says the tutorial "calls it essential to verify both", which is a
  recommendation; the bullet states it as what happens.
- Slide 7, "... normally at RTL.": R1 limits "normally" to "digital designs".
  Passed because the whole deck is about a digital chip.
- Slide 7, "Risk: simulation and synthesis disagreeing.": the label "Risk" is
  not in R6, but R6 says the named practices "can cause such mismatches".
- Slide 15, "Checked by: zero violations ...": RT4 is about the end of a
  detailed routing run specifically; the bullet does not say which run.

## Teaching notes

Skipped in this round by instruction.
