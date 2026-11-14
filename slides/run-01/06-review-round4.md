# Faithfulness review of the slide draft (round 4, narrow)

Reviewer: independent sub-agent, 2026-11-14
Scope: slides 4, 5 and 15 only; files read: 05-slides.json, 03-evidence.json, 04-outline.json
Bullets and leads checked: 15 (5 per slide; all three leads are empty)   Findings: 0

## Findings

| # | Slide | Bullet (first words) | Verdict | Evidence | Send back to |
|---|-------|----------------------|---------|----------|--------------|

No findings. All 15 bullets are supported by the cards they list.

Borderline wording, judged OK and not counted as findings:

- Slide 15, "Checked by: zero violations, and an antenna check: a long wire
  can collect charge ...": AN1 says a long *metal* wire *attached to a
  transistor gate* collects charge that can damage *the gate's thin oxide*.
  The bullet shortens this to "a long wire ... damage a transistor gate".
  Nothing is added or strengthened; the wire-to-gate attachment is only
  implied. RT4's "zero violations" is about a successful detailed routing
  run, which the slide context (routing) carries.
- Slide 5, "Design entry: ...": F1's "usually at the register transfer
  level" is omitted. This is a dropped detail, not a dropped condition; the
  remaining statement is still what the card says.
- Slide 4, "HDL ...: describes hardware; Verilog is one": V2 says a language
  for describing the structure or behavior of a hardware chip, and names
  Verilog and VHDL. Supported.

## Teaching notes

Question for this round: with slide 4 now before slide 5, does slide 5 use a
term that slides 1-4 have not introduced?

- TEACHING (minor), slide 5, bullet 4: "layout" is used without having been
  introduced. Its only earlier appearance is in passing on slide 3 ("the
  final layout file"), with no explanation. Slide 4's six words do not
  include it.
- Not a problem: "hardware description language" and "netlist" are now
  defined on slide 4 before slide 5 uses them, so the swap fixed the
  ordering it was meant to fix. "Functional verification", "synthesis" and
  "signoff" are explained inline in their own bullets. "Floorplanning,
  placement, clock tree synthesis, routing" are named without explanation,
  which is acceptable on an overview slide whose outline purpose is to
  "give the map before the details".
