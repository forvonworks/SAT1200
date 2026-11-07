# Book 2 — Lesson 6: Quadratics II — Problem Sets

**Source content file**, paired with `concepts.md`. All answers verified by a
`sympy` script (`sp.solve`, vertex forms confirmed by re-expanding) — not
hand-computed.

---

## Set 1 — Complete the Square → Vertex Form

Convert each to $a(x-h)^2+k$ form.

1. $y = x^2-4x+3$
2. $y = x^2+2x-5$
3. $y = x^2-8x+10$
4. $y = x^2+6x+4$
5. $y = x^2-10x+21$
6. $y = x^2+2x+1$

## Set 2 — Quadratic Formula Drill (clean discriminants)

Solve using the quadratic formula.

1. $x^2-5x+6=0$
2. $x^2+x-6=0$
3. $2x^2-3x-2=0$
4. $x^2-9=0$
5. $3x^2+5x+2=0$
6. $x^2-7x+12=0$

## Set 3 — Quadratic Formula, Irrational Roots

1. $x^2-4x+1=0$
2. $x^2+2x-4=0$
3. $2x^2-4x-1=0$
4. $x^2-6x+7=0$
5. $x^2+4x+2=0$
6. $3x^2-6x+2=0$

## Set 4 — Mixed (choose completing-the-square or the formula)

1. $x^2+8x+15=0$
2. $x^2-2x-5=0$
3. $4x^2-4x-3=0$
4. $x^2+5x+3=0$

## Set 5 — Two-Root Verification

Find **both** roots, then substitute each back into the original equation to
confirm it equals zero.

1. $x^2-x-12=0$
2. $x^2+3x-10=0$
3. $2x^2+x-6=0$

## Set 6 — Spot the Error

1. $x^2-6x+4=0$ — *"$x=\dfrac{-6\pm\sqrt{36-16}}{2}$" (used $b$ instead of $-b$)*
2. $x^2+2x-2=0$ — *"Diskriminant $=4-8=-4$, formula $x=\dfrac{-2\pm\sqrt{-4}}{2}$" (arithmetic slip: $4-4(1)(-2)=4+8=12$, not $-4$)*
3. $x^2-4x-1=0$ — *"$x=\dfrac{4+\sqrt{20}}{2}=2+\sqrt5$. Javob: $x=2+\sqrt5$." (stopped after one root)*

## Set 7 — Bonus / Challenge ($a\ne1$)

1. $2x^2+6x+3=0$
2. $3x^2-2x-2=0$
3. $5x^2+4x-1=0$
4. $2x^2-7x+4=0$

---

## Answer Key

**Set 1 (vertex form):**
1. $(x-2)^2-1$  2. $(x+1)^2-6$  3. $(x-4)^2-6$  4. $(x+3)^2-5$  5. $(x-5)^2-4$  6. $(x+1)^2$

**Set 2:** 1) $x=2,3$  2) $x=-3,2$  3) $x=-\frac12,2$  4) $x=\pm3$  5) $x=-1,-\frac23$  6) $x=3,4$

**Set 3:** 1) $x=2\pm\sqrt3$  2) $x=-1\pm\sqrt5$  3) $x=1\pm\dfrac{\sqrt6}{2}$  4) $x=3\pm\sqrt2$  5) $x=-2\pm\sqrt2$  6) $x=1\pm\dfrac{\sqrt3}{3}$

**Set 4:** 1) $x=-5,-3$  2) $x=1\pm\sqrt6$  3) $x=-\frac12,\frac32$  4) $x=\dfrac{-5\pm\sqrt{13}}{2}$

**Set 5:** 1) $x=-3,4$  2) $x=-5,2$  3) $x=-2,\frac32$ — all check to $0$.

**Set 6:**
1. Error — used $b=-6$ directly instead of $-b=6$. Correct: $x=3\pm\sqrt5$.
2. Error — discriminant arithmetic: $b^2-4ac = 4-4(1)(-2)=4+8=12$, not $-4$.
   Correct: $x=-1\pm\sqrt3$.
3. Error — stopped after one root. Correct: $x=2\pm\sqrt5$ (both).

**Set 7:** 1) $x=-\dfrac32\pm\dfrac{\sqrt3}{2}$  2) $x=\dfrac13\pm\dfrac{\sqrt7}{3}$  3) $x=-1,\frac15$  4) $x=\dfrac74\pm\dfrac{\sqrt{17}}{4}$
