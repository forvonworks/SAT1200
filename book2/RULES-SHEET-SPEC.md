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

## Per-lesson content (batches 2–4: lessons 7–14 and 16–23)

Same rules as above. Read the lesson's `concepts.md` first: include every item below that the
lesson actually covers, drop anything it does not teach, and add any essential formula the lesson
teaches that is missing here. Keep within the lesson's scope (a topic that belongs to another
lesson is not repeated).

**L7 Quadratic graphs & the discriminant** — parabola `y=ax²+bx+c`: opens up if `a>0`, down if
`a<0`; larger `|a|` ⇒ narrower; y-intercept `c`; x-intercepts = roots/zeros; vertex `x=−b/(2a)`,
axis of symmetry; discriminant `D=b²−4ac`: `D>0` two real solutions (2 x-intercepts), `D=0` one
(touches the axis), `D<0` none; vertex form `a(x−h)²+k`; intercept form `a(x−r)(x−s)` with vertex
x at `(r+s)/2`; min/max value; solutions of `f(x)=k` are where the line `y=k` meets the graph.

**L8 Exponential functions** — `y=a·bˣ` (a = initial value, b = growth factor); growth `b>1`, decay
`0<b<1`; `y=a(1±r)ᵗ` (percent rate → factor); doubling `a·2^(t/d)`, half-life `a·(½)^(t/h)`; compound
interest `A=P(1+r/n)^(nt)`; exponent `t/k` when the change happens every `k` units; linear vs
exponential (constant difference vs constant ratio); graph passes through `(0,a)`.

**L9 Polynomial operations** — add/subtract (combine like terms; distribute a minus sign); multiply
(distribute / FOIL); special products `(a+b)²=a²+2ab+b²`, `(a−b)²=a²−2ab+b²`, `(a+b)(a−b)=a²−b²`;
exponent rules `xᵐ·xⁿ=xᵐ⁺ⁿ`, `(xᵐ)ⁿ=xᵐⁿ`, `xᵐ/xⁿ=xᵐ⁻ⁿ`; degree and leading coefficient; polynomial
division / remainder theorem only if the lesson teaches it. No factoring (Lesson 5).

**L10 Rational expressions & equations** — domain: denominator ≠ 0; simplify by cancelling common
*factors* (never terms); multiply (top×top, bottom×bottom); divide (multiply by the reciprocal);
add/subtract over a common denominator; solving a rational equation: multiply by the LCD, then
**check for extraneous solutions**; cross-multiplication `a/b=c/d ⇒ ad=bc`.

**L11 Function notation, composition & transformations** — `f(a)` = plug in `a`; `f(g(x))` = plug `g(x)`
into `f` (inside out); transformations of `f(x)`: `f(x)+k` up, `f(x)−k` down, `f(x−h)` right `h`,
`f(x+h)` left `h`, `−f(x)` reflects over the x-axis, `f(−x)` over the y-axis, `a·f(x)` vertical
stretch; `(a,b)` on the graph ⇔ `f(a)=b`; solving `f(x)=k`.

**L12 Nonlinear systems** — line + parabola: substitute the linear equation into the quadratic and
solve; solutions are intersection points `(x,y)` (find `x`, then `y` from the linear equation);
number of intersections from the discriminant of the combined quadratic (2 / 1 / 0); set the two
expressions equal when both are solved for `y`. Include a circle/other nonlinear form only if the
lesson covers it.

**L13 Ratios, rates & proportions** — ratio `a:b = a/b`; proportion `a/b=c/d ⇒ ad=bc`; unit rate; rate
`=quantity÷time`; `distance=rate×time`; unit conversion by multiplying conversion fractions so units
cancel; part:part vs part:whole; scale factor; areas convert with the square of the length factor and
volumes with the cube.

**L14 Percentages in context** — `part = percent × whole`; `percent = part ÷ whole × 100`; percent change
`=(new−old)/old×100`; `new = old×(1±r)`; successive changes multiply (not add); original from final
`old = new ÷ (1±r)`; percent vs percentage points; markup / discount / tax / tip.

**L16 Data representations** — read a histogram / bar graph / dot plot; frequency table ⇒ bar graph
(see the statistics direction above); scatterplot trend: positive / negative / none; line of best
fit `y=mx+b`: slope = change in y per unit x, intercept = predicted y at x=0; predict by
substituting; interpolation vs extrapolation; residual `= actual − predicted`; two-way table: joint,
row/column totals, and "of those who…" restricts to one row/column.

**L17 Probability** — `P = favorable ÷ total`, `0 ≤ P ≤ 1`; complement `1−P`; `P(A or B)=P(A)+P(B)−P(A and B)`;
independent events `P(A and B)=P(A)·P(B)`; conditional `P(A|B)=P(A and B)/P(B)` (in a two-way table
restrict to the given row/column); expected count `= P × total`.

**L18 Study design & statistical claims** — random *sampling* ⇒ results generalize to the population;
random *assignment* ⇒ cause-and-effect can be concluded; observational study ⇒ association only;
both random sample and random assignment ⇒ generalize and causal; margin of error: estimate ± margin
= interval; larger sample ⇒ smaller margin of error; sample statistic vs population parameter; common
bias sources (convenience sample, voluntary response). Short table form works well here.

**L19 Lines, angles & triangles** — angles on a line sum to 180°, around a point 360°; vertical angles
equal; parallel lines cut by a transversal: corresponding and alternate interior equal, same-side
interior sum to 180°; triangle angle sum 180°; exterior angle = sum of the two remote interior angles;
isosceles base angles equal; equilateral 60° each; similar triangles (AA): sides proportional, area
ratio `k²`; triangle inequality; polygon interior angle sum `(n−2)·180°`. Any diagram must be exact.

**L20 Area & volume** — rectangle `lw`, triangle `½bh`, parallelogram `bh`, trapezoid `½(b₁+b₂)h`, circle
`πr²`; volumes: rectangular prism `lwh`, cylinder `πr²h`, cone `⅓πr²h`, sphere `4/3·πr³`, pyramid `⅓Bh`;
surface area basics only if taught; scaling: lengths ×k ⇒ area ×k², volume ×k³. Stay inside the four
solids the lesson covers (no hemisphere unless concepts.md has it).

**L21 Circles** — circumference `2πr`, area `πr²`; arc length `=(θ/360)·2πr`; sector area `=(θ/360)·πr²`;
inscribed angle = ½ the arc / central angle; tangent ⟂ radius; equation `(x−h)²+(y−k)²=r²` (center
`(h,k)`, radius `r`); complete the square to get center and radius from `x²+y²+bx+cy=d`; radians
`π rad = 180°` only if the lesson teaches it.

**L22 Right-triangle trigonometry** — SOH-CAH-TOA: `sin=opp/hyp`, `cos=adj/hyp`, `tan=opp/adj`;
`tan=sin/cos`; complementary angles `sin θ = cos(90°−θ)`; special triangles 30-60-90 (sides 1 : √3 : 2)
and 45-45-90 (1 : 1 : √2); angle of elevation / depression; inverse trig to find an angle; calculator in
degree mode. Do not include the Pythagorean theorem (Lesson 23).

**L23 Pythagorean theorem & coordinate applications** — `a²+b²=c²`; common triples 3-4-5, 5-12-13, 8-15-17,
7-24-25 (and multiples); distance `√((x₂−x₁)²+(y₂−y₁)²)`; midpoint `((x₁+x₂)/2, (y₁+y₂)/2)`; diagonal of a
rectangle `√(l²+w²)` and of a box `√(l²+w²+h²)`; converse: if `a²+b²=c²` the triangle is right;
height of an equilateral / isosceles triangle via the theorem.
