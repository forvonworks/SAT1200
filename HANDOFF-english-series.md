# Handoff: start the SAT Reading & Writing (English) series

Read this file first, then act. Repo `forvonworks/SAT1200`, develop and push only on branch
`claude/tender-planck-dic0r7` (unless the owner says otherwise). The owner is Salohiddin (author),
with co-author Baxtiyor Umrzaqov. Readers are Uzbek students preparing for the Digital SAT.

## 1. What exists (Math series, all finished)

| Book | File | Pages |
|---|---|---|
| MathBook 0-1 | `final/MathBook 0-1.pdf` | 114 |
| Mathbook 700+ | `final/Mathbook 700+.pdf` | 336 |
| MathBook 800 | `final/MathBook 800.pdf` | 240 |

Colours: Book 1 orange `#F46530`, Book 2 purple `#602785`, Book 3 pine green `#0F6A52`. The English series
needs its own look (pick the colour with the owner early; ask for a "feeling" reason, they like that).
Covers are Canva designs (copy an existing cover with `copy-design`, edit text with `edit-design`; elements that are
`isLocked` cannot be recolored or deleted by tools, so cover them with a new shape or ask the owner to unlock).
Export covers with `export-design` (pdf, A4) and download with curl (host `export-download.canva.com` is allowed on the
Default environment; re-export if the signed URL fails).

## 2. The environment (important)

- The Default cloud environment allows only `export-download.canva.com` outside package registries. For web research
  start the session on the personal environment named **SAT1200**, which allows College Board, test-ninjas, prepscholar,
  collegetransitions, alphatestai, sigmaprep, tigerway.substack.com, mathplanet.com. Pages I could not open last time:
  College Board "how scores are calculated", the tigerway "what changes between Module 1 and 2" post, official Practice
  Test PDFs.
- Question banks are in `Materials/` (Git LFS; run `git lfs pull --include="Materials/<file>.pdf"` first). Present now:
  SAT MATH, PSAT 10/NMSQT, PSAT 8/9 (Math). There is NO Reading & Writing bank yet: ask the owner to upload the official
  SAT Reading & Writing Question Bank PDF (same College Board export format). Everything below depends on it.
- Bank text extraction loses numbers (embedded font): render pages with `pdftoppm -png -r 150 -f N -l N` and read the
  image. `tools/qbank_find.py "<skill substring>" <Easy|Medium|Hard>` finds pages (builds a text cache). For English the
  text layer may be fine, so check first.
- `xelatex` (Libertinus fonts), `gs`, `pdftoppm`, `pdftotext` are installed. `qpdf` and `rsync` are not. PIL is broken.

## 3. Hard rules from the owner (apply to English too)

1. Every problem/passage must be ORIGINAL. Study real College Board items for the method, traps and distractor patterns,
   never copy their wording or content (College Board does not license items commercially).
2. Verify answers. Math used scripts. For English, build a defensible-answer check: each item has exactly one choice
   that satisfies the rule being tested, each wrong choice maps to a named error type, and a second reading pass confirms it.
3. English-only content, with Uzbek only in short bracketed terms, a small "New words" card per lesson, and front/back
   matter. Do not write long Uzbek explanations; the owner records videos separately (rules sheets carry a
   "WATCH THE VIDEO BEFORE YOU SOLVE" QR banner).
4. Per lesson: rules sheet (pill-title cards, formula/rule + at most one bare example, no explanations or warning boxes),
   small vocabulary card (10-15 terms English | O'zbekcha), 5 problem sets, a "Qaydlar uchun" notes page (Book 1 style),
   an answer key with a short worked solution for every item, set in roomy 10 pt two-column pages (the owner rejected a
   cramped 8.6 pt answer page).
5. Mock tests: answers are NOT printed after each mock; one answer sheet per mock at the end of the book.
6. Front matter / back matter (Uzbek): copy `book3/front-matter.tex`, `toc.tex`, `back-cover.tex`,
   `book3/tools/make_static_pages.py`. The dedication page is `dedication/dedication-page.tex`.
7. Tone with the owner: warm, humane, direct. They pay per message and hit usage limits, so keep replies short and avoid
   re-deriving things already decided. They said "no rest, next goal is the English 800".

## 4. Reusable tooling (read these before building anything)

- `book3/BOOK3-SPEC.md` (the spec format), `book3/PROGRESS.md` (progress-ledger pattern).
- `book3/lesson-05-speed-tricks/` and `lesson-02..09/`: finished reference lessons (problems.md, verify.py holding the
  problem bank, build.py / gen_rules.py generators, rules-sheet.tex, lessonNN-typeset.tex, notes-page.tex).
- `book3/mocks/mock-08/`: reference mock (mockNN-problems.md, verify.py, build_tex.py, typeset, answer sheet).
- `book3/tools/respace_solutions.py`, `fix_solution_kickers.py`: roomy answer pages.
- `book3/tools/assemble_book3.py`: renumbers footers, compiles, splices notes pages, merges with gs, checks that every
  printed page number equals its position (run `--partial` on a copy for dry runs; set B3ROOT and B3TMP).
- `book2/RULES-SHEET-SPEC.md`: the 8 layout-safety rules for textpos rules sheets (card height vs content, tikz
  bounding boxes, table widths, header cells with \cellcolor + \textcolor{white}, true-scale diagrams only).

## 5. How the Math books were built (the workflow that worked)

- Fresh general-purpose agents, at most 4 at a time, each owns one lesson or one mock and writes only its own folder.
  Agents NEVER run git. The orchestrator verifies (rerun verify script, recompile, look at rendered pages, check counts)
  then commits one verified group per commit and pushes. Cost is ~250-330k tokens per lesson/mock agent.
- Usage limit (5-hour window) kills running agents. Agents' work is saved on disk; resume them with SendMessage
  ("limit reset, continue"). Nothing wakes the orchestrator by itself: schedule check-ins (send_later ~40 min) and
  re-arm them, and read the progress ledger after every restart.
- A Stop hook demands that uncommitted/untracked files are committed and pushed whenever the turn ends; commit
  "in-progress checkpoint (unverified)" files, then replace with a verified commit.
- Weak spots seen in mocks: agents tend to write "hard" items that are only long, not insightful. State explicitly in
  every prompt what a hard item must need (an insight or a trap) and list the failure patterns to avoid.

## 6. The English series: starting plan (to be confirmed by research)

Digital SAT Reading & Writing, from memory and UNVERIFIED (confirm on College Board pages): two modules,
~27 questions and ~32 minutes each, adaptive like Math, one short passage per question; four content areas:
Craft & Structure (vocabulary in context, text structure and purpose, cross-text connections), Information & Ideas
(central idea, inference, command of evidence in text and in data), Standard English Conventions (sentence boundaries,
subject-verb agreement, pronouns, verb forms and tense, punctuation, modifiers), Expression of Ideas (transitions,
rhetorical synthesis).

Steps:
1. Get the real Reading & Writing bank from the owner; count items per skill and difficulty (as done for Math in
   `research/15-question-bank-analysis.md`); read ~12 Hard items per skill for the method and trap patterns.
2. Research the test with the SAT1200 environment: official structure, scoring, adaptive routing, pacing; competitor
   books (what they do badly for non-native speakers); ESL-specific problems of Uzbek students (articles, tenses,
   prepositions, vocabulary breadth, reading speed). Reuse `research/05-uzbek-student-considerations.md` and
   `research/07-uzbek-math-language-style.md` as background.
3. Decide the series shape. Suggested: Book A "Conventions + core vocabulary" (grammar is rule-based, fastest score
   gain); Book B "Reading skills" (inference, evidence, words in context, text structure); Book C "Hard questions,
   speed, mocks". Confirm with the owner after the bank counts.
4. Build a vocabulary track: the most frequent SAT passage words and academic words (use word-frequency lists from the
   bank corpus as was done for Math in `research/` and `book1/vocabulary-complete.*`), with Uzbek glosses.
5. Write the spec file (like BOOK3-SPEC.md), pick the colour with the owner, build one reference lesson and one mock
   first, show the owner, then fan out agents.
6. Mocks: reuse the 2-module blueprint, with the real R&W domain mix once the bank is analysed.

Open decisions for the owner: series title and book names, colour, number of books, whether passages should include
Uzbekistan-relevant topics, and how videos/QR codes link.
