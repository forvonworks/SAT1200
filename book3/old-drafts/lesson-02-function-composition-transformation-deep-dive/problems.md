# Book 3 — Lesson 2: Function Composition & Transformation — Deep Dive — Problem Sets

**Source content file**, paired with `concepts.md`. All numeric/symbolic answers verified
by a Python/sympy script (kept in session scratchpad, not committed), not hand-computed.
Two items (Set 3 #1, Set 4 #1) are adapted directly from real official College Board
Hard-tagged questions (per `research/15-question-bank-analysis.md`); the rest are original
problems written to match the same difficulty and style — not distinguished in the text.

---

## Set 1 — Self-Composition & Triple Composition

1. $f(x)=2x+1$. Find $f(f(3))$.
2. $f(x)=x-4$. Find $f(f(10))$.
3. $f(x)=x^2-1$. Find $f(f(2))$.
4. $f(x)=-x+5$. Find $f(f(f(2)))$.
5. $f(x)=3x$. Find $f(f(f(1)))$.
6. $f(x)=\dfrac{x}{2}+1$. Find $f(f(4))$.

## Set 2 — Nested Composition, Two or Three Functions

1. $f(x)=x+3$, $g(x)=2x$. Find $f(g(f(1)))$.
2. $f(x)=x^2$, $g(x)=x-1$. Find $g(f(g(3)))$.
3. $f(x)=2x-1$, $g(x)=x^2+1$. Find $f(g(2))$ and $g(f(2))$ — confirm they differ.
4. $f(x)=x+1$, $g(x)=x+2$, $h(x)=x+3$. Find $f(g(h(0)))$.
5. $f(x)=-2x$. Find $f(f(f(-1)))$.

## Set 3 — Transformation + Optimization Combined

Each: $g(x) = f(x) + c$ (or $-c$), $f$ quadratic. Find the maximum or minimum of $g(x)$
without fully re-expanding and completing the square on $g$ itself — find $f$'s extreme
value first, then apply the shift.

1. $f(t) = 55t - 2t^2$. $g(t) = f(t)+3$. Find the maximum value of $g(t)$.
2. $f(x) = 40x - x^2$. $g(x) = f(x) - 6$. Find the maximum value of $g(x)$.
3. $f(x) = -3x^2+12x$. $g(x) = f(x)+7$. Find the maximum value of $g(x)$.
4. $f(x) = x^2-6x$. $g(x) = f(x)-4$. Find the minimum value of $g(x)$.

## Set 4 — Reconstruct $f$ From a Shifted Table, Then Evaluate

1. The table shows three values of $x$ and $y=f(x)+4$, $f$ quadratic:

   | $x$ | $21$ | $23$ | $25$ |
   |---|---|---|---|
   | $y$ | $-8$ | $8$ | $-8$ |

   Find the $y$-coordinate of the $y$-intercept of $y=f(x)$.

2. The table shows three values of $x$ and $y=f(x)-5$, $f$ quadratic:

   | $x$ | $2$ | $4$ | $6$ |
   |---|---|---|---|
   | $y$ | $1$ | $5$ | $1$ |

   Find $f(0)$.

3. The table shows three values of $x$ and $y=f(x)+3$, $f$ quadratic:

   | $x$ | $0$ | $2$ | $4$ |
   |---|---|---|---|
   | $y$ | $-9$ | $-1$ | $-9$ |

   Find $f(5)$.

## Set 5 — Vertical vs. Horizontal Stretch/Compression

Each pair uses the same $f$ and the same number — compute both and compare.

1. $f(x)=x^2$. Find $2f(3)$ and $f(2\times3)$.
2. $f(x)=x^2-2$. Find $3f(2)$ and $f(3\times2)$.
3. $f(x)=2x+5$. Find $\dfrac12 f(4)$ and $f\left(\dfrac12\times4\right)$.
4. $f(x)=x^2+1$. Find $4f(1)$ and $f(4\times1)$.

## Set 6 — Mixed: Composition, Then a Transformation Applied to the Result

1. $f(x)=x+2$, $g(x)=x^2$. Let $h(x)=g(f(x))+5$. Find $h(3)$.
2. $f(x)=2x$, $g(x)=x-1$. Let $h(x)=f(g(x))-3$. Find $h(5)$.
3. $f(x)=x^2-3$. Find $f(f(x))$ as an expanded expression, then evaluate it at $x=1$.

## Set 7 — Spot the Error

Each item has exactly one broken step. Name the error and give the correct answer.

1. $f(x)=2x+1$. Find $f(f(2))$. *"$f(2)=5$, so $f(f(2))=2(2)+1=5$ again."*
2. Table gives $y=f(x)+4$ with values at $x=21,23,25$ equal to $-8,8,-8$. *"The $y$-intercept
   of $y=f(x)$ is just the $y$-intercept of the table's own pattern, so it's the same as
   $y(0)$ computed directly from $y=a(x-23)^2+8$ without subtracting the $+4$ shift back out."*
3. $f(x)=x^2$. Find $f(3\times2)$. *"$f(3\times2) = 3\times f(2) = 3\times4=12$."*
4. $f(t)=55t-2t^2$, $g(t)=f(t)+3$. *"The maximum of $g(t)$ occurs at the same $t$ where
   $f(t)$ is maximized, and that maximum value is the same number as $f$'s maximum — the
   $+3$ only matters if you're asked to evaluate $g$ somewhere else, not for the max."*

## Set 8 — Bonus / Challenge

1. The table shows three values of $x$ and $y=f(x)+2$, $f$ quadratic:

   | $x$ | $1$ | $4$ | $7$ |
   |---|---|---|---|
   | $y$ | $6$ | $15$ | $6$ |

   Let $h(x)=f(x)-10$. Find the maximum value of $h(x)$.

2. $f(x)=x+1$, $g(x)=2x$, $h(x)=x^2$. Find $f(g(h(x)))$ as a simplified expression, then
   evaluate it at $x=3$.

---

## Answer Key

**Set 1:** 1) $15$  2) $2$  3) $8$  4) $3$  5) $27$  6) $\dfrac52$

**Set 2:** 1) $11$  2) $3$  3) $f(g(2))=9$, $g(f(2))=10$ — different, as expected  4) $6$
5) $8$

**Set 3:** 1) $\dfrac{3049}{8}=381.125$  2) $394$  3) $19$  4) $-13$

**Set 4:** 1) $-2112$  2) $-6$  3) $-22$

**Set 5:** 1) $2f(3)=18$, $f(6)=36$  2) $3f(2)=6$, $f(6)=34$  3) $\dfrac12f(4)=\dfrac{13}{2}$,
$f(2)=9$  4) $4f(1)=8$, $f(4)=17$

**Set 6:** 1) $h(3)=30$  2) $h(5)=5$  3) $f(f(x))=(x^2-3)^2-3$; at $x=1$: $1$

**Set 7:**
1. Error — treated $f(f(2))$ as re-applying $f$ to the ORIGINAL input $2$ again instead of
   to $f(2)$'s result. Correct: $f(5)=2(5)+1=11$.
2. Error — forgot that the table gives $y=f(x)+4$, not $f(x)$ itself; the $+4$ shift must be
   subtracted back out after finding $a$, $h$, $k$. Correct: $f(0)=-2112$ (see Concept 3's
   Model Example for the full method).
3. Error — treated horizontal input-scaling as if it were vertical output-scaling ($f(bx)$
   confused with $b\cdot f(x)$). Correct: $f(6)=6^2=36$.
4. Error — correct that the maximizing $t$-value is unchanged by the shift, but wrong that
   the maximum VALUE is unchanged — a vertical shift changes the height of the peak too.
   Correct: $g$'s maximum is $f$'s maximum plus $3$, i.e. $\dfrac{3025}{8}+3=\dfrac{3049}{8}$.

**Set 8:** 1) $h_{\max}=3$  2) $f(g(h(x)))=2x^2+1$; at $x=3$: $19$
