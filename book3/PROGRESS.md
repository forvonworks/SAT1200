# Book 3 progress ledger (update after every verified commit)

Owner instruction: finish Book 3 using agents (fresh general-purpose agents, <=4 at a time, agents never run git;
the orchestrator verifies by recompiling + viewing pages + running verify.py, then commits one group per commit).
If usage limits hit: stop, note state here, resume agents when the limit resets (owner pre-approved continuing).

Book structure: cover -> blank -> front matter (title, copyright, about) -> TOC -> 9 lessons
(each: rules sheet with small New-words card, 5 sets, notes page "Qaydlar uchun", answer key with worked solutions)
-> Mock section (Mock 1 M1+M2, Mock 2 M1+M2, ... Mock 10) -> Answer sheets for all 10 mocks -> dedication -> back cover.
Decisions + blueprint: see BOOK3-SPEC.md.

## Status

| Item | Status |
|---|---|
| Spec, cover | done |
| Lesson 5 Speed tricks (reference lesson) | DONE, verified (74 problems, 3-page rules sheet, 8-page typeset) |
| Mock 1 | DONE, verified, final blueprint (44 q) |
| Mock 2 | DONE, verified |
| Mock 3 | DONE, verified |
| Mock 4 | DONE, verified |
| Mock 5 | DONE, verified |
| Mock 6 | DONE, verified |
| Mock 7 | DONE, verified |
| Mock 8 | in progress |
| Lesson 1 | in progress (agent a3cf13281dd1ea6c0) |
| Lesson 2 | DONE, verified (74 problems) |
| Lesson 3 | DONE, verified (74 problems, solutions respaced) |
| Lesson 4 | DONE, verified (74 problems) |
| Lesson 6 | DONE, verified (74 problems) |
| Lesson 7 | in progress |
| Mocks 4-10 | not started |
| Lessons 1,2,3,4,6,7,8,9 | not started (use lesson-05-speed-tricks as the reference once verified) |
| Front matter, TOC, notes pages, answer-sheets section, back cover, assembly + paging check | not started |

Lesson list: 1 Disguised & multi-step word problems; 2 Hard linear equations, systems & parameters; 3 Hard nonlinear
functions; 4 Discriminant edge cases & disguised quadratics; 5 Speed tricks; 6 Hard percentages, ratios & units;
7 Data-analysis edge cases; 8 Hard circles, area & volume; 9 Hard right triangles & chained geometry.
Old drafts (input only): book3/old-drafts/.
