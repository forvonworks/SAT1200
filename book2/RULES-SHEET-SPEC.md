# Book 2 — Rules-sheet rebuild spec

Each lesson folder has `rules-sheet.tex/.pdf`, a visual formula/rules reference that comes
BEFORE the lesson's problems. The first version was too thin (missing standard SAT formulas).
This pass makes each sheet complete for its lesson. The user reviews after every 6 lessons.

## What "essential" means
- Include **every formula, rule, identity or procedure a student needs to solve this lesson's
  SAT problems**, and nothing else. Think "what would I want on a one-glance cheat sheet".
- **No page limit.** Typically 2–4 pages. Do not pad; do not cram.
- **No concept explanations.** The teacher explains on video. Each card is:
  pill title (`RULE · ...`) + the formula/rule (large, 13–15 pt) + at most one bare worked
  example + optionally one short italic caveat line. About 3 lines of text excluding the formula.
  No step-by-step walkthroughs, no Wrong/Right boxes, no warning cards.
- Only add a Uzbek bracketed term, e.g. `(qiyalik)`, on the single most important technical
  term of a card, and only where already present in the old sheet or clearly useful. Otherwise English.
- Drop cards that are not SAT-relevant (e.g. drawing conventions, regional notation notes).
- Keep any existing diagram only if it is mathematically exact; diagrams must match their own
  numbers/labels (true scale, equal mm per unit on both axes where slopes/angles matter).
  If you add a diagram it must be drawn to true scale; when in doubt use no diagram.

## Design (copy from the existing file; do not redesign)
- Start from the lesson's current `rules-sheet.tex` (same preamble, colours, macros
  `\topicheader \pagekicker \videobanner \pagefooter \cardbg \pill`). Purple only:
  accent `602785`, badge `B8A0C8`, ink `2A2E30`. No red. XeLaTeX, Libertinus fonts.
- Page 1: `\topicheader` + `\videobanner{Lesson N}` (QR banner "WATCH THE VIDEO BEFORE YOU SOLVE")
  and content from y = 40 mm. Later pages: `\topicheader` + `\pagekicker{Rules sheet -- k/K}`
  and content from y = 33 mm. Update k/K for the new page count on every page.
- Cards: `\cardbg{16}{y}{178}{h}` (x=16, width 178 mm) with `\pill{26}{y+3}{title}` and content
  textblocks at x = 26 mm, width 158 mm. Content bottom must stay ≤ y = 283 mm.
- Keep the existing footer number on page 1 and increment by 1 per extra page. (Global page
  renumbering happens later when the book is assembled; do not try to solve that here.)

## Layout rules (each of these caused a real bug before)
1. **Sum the page budget first.** Add all card heights + 6–10 mm gaps for a page *before* fixing
   any single card's height. Usable height: y=40→283 (243 mm) on page 1, y=33→283 (250 mm) later.
2. **Card height must contain its content.** Content bottom + ≥6 mm ≤ card bottom. Compute from
   the y of each textblock plus its real height (render and look; do not guess).
3. A `tikzpicture` inside a textblock hangs *downward* from the top of its drawn bounding box;
   bounding box = full extent of drawn points, not the origin. Allow its full height + ≥10 mm.
4. Do NOT use `\checkmark`, `\xRightarrow`, `\xrightarrow` or other mathtools/amssymb-only
   commands (those packages are not loaded). Use `\Rightarrow`, plain text, or `\Longrightarrow`.
5. Table width: sum of `p{}` column widths + ~14 mm padding must be < the 158 mm block width.
6. Every tikz coordinate needs an explicit unit (`12mm`); a bare number is 1 cm.
7. Compile with `xelatex -interaction=nonstopmode`; then `grep -n "^! \|Overfull" *.log` must be
   clean (≤ 1–2 mm table-border overfulls are acceptable). Render *every* page with
   `pdftoppm -png -r 110` and look at it: no clipped text, nothing outside its card, nothing
   overlapping, no empty-glyph boxes. Fix and re-render until clean.
8. Delete `*.aux *.log missfont.log` and render PNGs when done. Do NOT run git.

## Per-lesson content (batch 1: lessons 1–6)

Examples must be correct; check each worked example by script (sympy) before using it.

**L1 Linear equations & inequalities** — solving order (distribute → combine like terms →
collect variable → divide); number of solutions of `ax+b = cx+d`: `a≠c` one; `a=c, b≠d` none;
`a=c, b=d` infinitely many (and the parameter version: "infinitely many ⇒ match coefficients
AND constants; no solution ⇒ match coefficients only"); "value of an expression" shortcut
(scale/shift the given equation instead of solving, e.g. `3x+5=20 ⇒ 6x+10=40`); inequality
sign-flip table; compound "and"/"or"; wording → symbol (at least ≥, at most/no more than ≤, more
than >, fewer than <); "maximum/minimum whole number" (solve, then round down for a maximum and
up for a minimum). Drop interval-notation and number-line drawing unless it fits naturally.

**L2 Systems of linear equations** — substitution and elimination (one line each, one example
each); solution count from coefficient ratios `a1/a2, b1/b2, c1/c2` (one / none / infinite) and
the slope-intercept version (same slope + different intercept ⇒ none; same line ⇒ infinite);
parameter trick (find `k` for no / infinitely many solutions); "what's asked" shortcut: add or
subtract the two equations to get `x+y` or `x−y` directly; word-problem set-up
`x+y = total`, `px+qy = total value`; the solution is the intersection point (keep the exact
intersection diagram if present).

**L3 Linear functions & graphing** — slope `m=(y2−y1)/(x2−x1)`; slope-intercept `y=mx+b`
(m = rate, b = start / y-intercept); point-slope `y−y1=m(x−x1)`; standard form `Ax+By=C` with
slope `−A/B`, y-intercept `C/B`, x-intercept `C/A`; intercepts (set `x=0` / `y=0`); horizontal
`y=k` has slope 0, vertical `x=k` has undefined slope; parallel `m1=m2`, perpendicular
`m1·m2=−1`; function notation `f(x)=mx+b` and `f(a)` substitution; slope from a table
(`Δy/Δx` is constant); "real-world meaning of m and b" one-liner.

**L4 Word-problem translation & modeling** — keep the phrase-to-symbol dictionary and the
"less than reverses the order" rule; comparison phrases; add: `total = fixed + rate × quantity`;
`distance = rate × time`; consecutive integers `n, n+1, n+2` (consecutive even/odd: `n, n+2,
n+4`); `x% of y = (x/100)·y`; average `= sum ÷ count`; ages "t years later = +t"; perimeter
`2(l+w)`. Define the variable first; answer the quantity actually asked.

**L5 Quadratics I — factoring** — standard form `ax²+bx+c=0`; factor `a=1`: two numbers with
product `c`, sum `b`; GCF first; difference of squares `a²−b²=(a−b)(a+b)`; perfect-square
trinomials `a²±2ab+b²=(a±b)²`; `a≠1` by splitting the middle term (numbers with product `ac`, sum
`b`); zero-product property (set `=0` first); roots from factors, factors from roots
`a(x−r)(x−s)`; sum of roots `−b/a`, product of roots `c/a`. Keep it factoring only (no quadratic
formula, no discriminant — those are Lessons 6–7).

**L6 Quadratics II — completing the square & quadratic formula** — vertex form
`a(x−h)²+k`, vertex `(h,k)`, axis `x=h`; completing the square `x²+bx ⇒ (x+b/2)²−(b/2)²`
(factor out `a` first when `a≠1`); vertex of `y=ax²+bx+c` is `x=−b/(2a)`, then `k=f(h)`; max or
min value is `k` (`a>0` min, `a<0` max); square-root method `(x−h)²=k ⇒ x=h±√k`; quadratic
formula `x=(−b±√(b²−4ac))/(2a)`; sign care when `b<0`; leave irrational roots in simplified radical
form. No discriminant-sign classification (Lesson 7).

## Report back (concise)
Per lesson: page count, cards kept / added / removed, any example you verified by script, and
anything you were unsure about. Do not claim visual verification you did not do.

## Owner direction: statistics lessons (15–18)
- **Standard deviation: never teach the Σ formula.** Teach it visually: more spread ⇒ bigger SD.
  A single tall "skyrocket" bar ⇒ small SD; "double top" (two peaks) ⇒ medium; flat / spread out
  ⇒ large; peaks pushed to the far ends ⇒ larger still. Draw real bar graphs from real counts
  (verify the SD ordering by script before labelling) and use the *same* mean and n in a comparison
  so only spread differs.
- Show how a **frequency table becomes a bar graph** (value on x-axis, count = bar height) and how to
  read the spread from it. Note that equal range does not mean equal SD.
- State the spread ↔ SD relationship as a short table: closer ⇒ smaller; farther ⇒ bigger; all equal
  ⇒ 0; add/subtract a constant ⇒ unchanged; multiply by k ⇒ ×|k|; far outlier ⇒ jumps up.
- Lesson 15's `rules-sheet.tex` is the reference implementation (macro `\bargraph`).
- Table header rows: use `\cellcolor{accent}\textcolor{white}{...}` per cell, not `\rowcolor` with a
  `{\color{white}...}` group (that renders the header ~5 mm too tall).
