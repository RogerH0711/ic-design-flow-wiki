# Lint history

Appended by `scripts/lint_wiki.py --record`. Failed runs are kept on purpose.

## 2026-11-12 09:57 | ingest S1 (round 1) | PASS | lint_wiki: 20 pages, 0 errors


## 2026-11-12 10:01 | ingest S2 (round 1) | PASS | lint_wiki: 35 pages, 0 errors


## 2026-11-12 14:41 | ingest S3 (round 1) | PASS | lint_wiki: 41 pages, 0 errors


## 2026-11-12 14:43 | ingest S3 (after review fixes) | PASS | lint_wiki: 41 pages, 0 errors


## 2026-11-12 14:44 | ingest S4 (round 1) | FAIL | lint_wiki: 47 pages, 2 errors

- `TERM   wiki/concepts/asic-design-flow.md:41: use 'physical implementation' instead of 'PnR'`
- `CITE   wiki/concepts/pdk.md:16: claim without a citation: 'Related terms:'`

## 2026-11-12 14:45 | ingest S4 (round 2) | PASS | lint_wiki: 47 pages, 0 errors


## 2026-11-12 14:47 | ingest S4 (after review fixes) | PASS | lint_wiki: 47 pages, 0 errors


## 2026-11-12 14:48 | ingest S5 (round 1) | FAIL | lint_wiki: 50 pages, 23 errors

- `CITE   wiki/concepts/asic-design-flow.md:37: S5 has no section named 'Script-based synthesis flows'`
- `CITE   wiki/concepts/asic-design-flow.md:38: S5 has no section named 'Script-based synthesis flows'`
- `CITE   wiki/concepts/levels-of-abstraction.md:14: claim without a citation: 'From highest to lowest, the synthesis primer lists these lev'`
- `CITE   wiki/concepts/levels-of-abstraction.md:17: S5 has no section named 'High level'`
- `CITE   wiki/concepts/levels-of-abstraction.md:19: S5 has no section named 'Register-Transfer Level (RTL)'`
- `CITE   wiki/concepts/levels-of-abstraction.md:21: S5 has no section named 'Physical gate level'`
- `CITE   wiki/concepts/levels-of-abstraction.md:28: S5 has no section named 'Physical gate level'`
- `CITE   wiki/concepts/netlist.md:16: S5 has no section named 'Register-Transfer Level (RTL)'`
- `CITE   wiki/concepts/rtl.md:18: S5 has no section named 'Register-Transfer Level (RTL)'`
- `CITE   wiki/concepts/rtl.md:26: S5 has no section named 'Register-Transfer Level (RTL)'`
- `CITE   wiki/concepts/rtl.md:27: S5 has no section named 'Register-Transfer Level (RTL)'`
- `CITE   wiki/concepts/technology-mapping.md:18: S5 has no section named 'Physical gate level'`
- `CITE   wiki/sources/s5-yosys-synthesis-primer.md:20: S5 has no section named 'Register-Transfer Level (RTL)'`
- `CITE   wiki/sources/s5-yosys-synthesis-primer.md:23: S5 has no section named 'Script-based synthesis flows'`
- `CITE   wiki/sources/s5-yosys-synthesis-primer.md:28: S5 has no section named 'Methods from compiler design'`
- `CITE   wiki/stages/functional-verification.md:29: S5 has no section named 'Script-based synthesis flows'`
- `CITE   wiki/stages/functional-verification.md:30: S5 has no section named 'Script-based synthesis flows'`
- `CITE   wiki/stages/logic-synthesis.md:37: S5 has no section named 'Expressions in Verilog'`
- `CITE   wiki/stages/logic-synthesis.md:38: S5 has no section named 'Optimizations'`
- `CITE   wiki/stages/logic-synthesis.md:46: S5 has no section named 'Script-based synthesis flows'`
- `CITE   wiki/stages/rtl-design.md:19: S5 has no section named 'Script-based synthesis flows'`
- `CITE   wiki/stages/rtl-design.md:30: S5 has no section named 'Script-based synthesis flows'`
- `CITE   wiki/tools/yosys.md:16: S5 has no section named 'Yosys'`

## 2026-11-12 14:48 | ingest S5 (round 2, after lint bug fix) | PASS | lint_wiki: 50 pages, 0 errors


## 2026-11-12 14:50 | ingest S5 (after review fixes) | PASS | lint_wiki: 50 pages, 0 errors

