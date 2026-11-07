# Book 2 — Lesson 10: Rational Expressions & Equations — Problem Sets

**Source content file**, paired with `concepts.md`. All answers verified by
a `sympy` script (factoring, simplification, and equation-solving with
explicit excluded-value checks), not hand-computed.

---

## Set 1 — Simplify (Factor, Then Cancel Factors Only)

1. $\dfrac{x^2-9}{x+3}$
2. $\dfrac{x^2+5x+6}{x+2}$
3. $\dfrac{x^2-5x+6}{x^2-4}$
4. $\dfrac{2x^2+4x}{x^2-4}$
5. $\dfrac{x^2-1}{x^2+2x+1}$
6. $\dfrac{x^2-7x+10}{x^2-25}$

## Set 2 — Multiply / Divide

1. $\dfrac{x+4}{x-3}\times\dfrac{x-3}{x+1}$
2. $\dfrac{x^2-16}{3x}\times\dfrac{x}{x+4}$
3. $\dfrac{x-2}{x+5}\times\dfrac{x+5}{x-2}$
4. $\dfrac{x^2-9}{x+2}\div\dfrac{x+3}{x+2}$
5. $\dfrac{x+1}{x-5}\div\dfrac{x+1}{2x-10}$
6. $\dfrac{x^2-4}{5}\div\dfrac{x-2}{10}$

## Set 3 — Solve (No Extraneous Case Yet)

1. $\dfrac{x}{3}+1=\dfrac{x+4}{6}$
2. $\dfrac{2}{x}+1=3$
3. $\dfrac{x+1}{x+4}=\dfrac{1}{2}$
4. $\dfrac{3}{x-1}=\dfrac{2}{x+2}$
5. $\dfrac{x}{5}+\dfrac{1}{5}=\dfrac{6}{x}$ *(two answers)*

## Set 4 — Solve and CHECK (Some Candidates Must Be Rejected — Some Must Not)

For each, solve, then check the candidate against the original equation.
State clearly whether the final answer is a number or "no solution."

1. $\dfrac{x}{x-3}=\dfrac{3}{x-3}-2$
2. $\dfrac{x+1}{x-4}=\dfrac{5}{x-4}$
3. $\dfrac{2x}{x-5}=\dfrac{10}{x-5}+1$
4. $\dfrac{x+2}{x-1}=3$ *(this one is NOT a trap — confirm it)*

## Set 5 — Mixed

1. Simplify: $\dfrac{2x^2-8}{x^2-4}$ *(watch what's left after everything
   else cancels — it isn't automatically 0 or 1)*
2. Solve: $\dfrac{4}{x+1}=\dfrac{2}{x-1}$
3. Multiply: $\dfrac{x-5}{x+3}\times\dfrac{x+3}{2x}$
4. Solve and check: $\dfrac{1}{x-2}+\dfrac{1}{x+2}=\dfrac{4}{x^2-4}$
5. Simplify: $\dfrac{x^2-6x+9}{x^2-9}$

## Set 6 — Spot the Error

Each item has exactly one broken step. Name the error and give the
correct answer.

1. Simplify $\dfrac{x+5}{x}$ — *"Cancel the $x$'s: answer is $5$."*
2. Simplify $\dfrac{x^2-4}{x+2}$ — *"Everything cancels, so the answer is
   $0$."*
3. Solve $\dfrac{3x}{x-2}=\dfrac{6}{x-2}+x$ — *"Clearing gives
   $x^2-5x+6=0$, so $x=2$ or $x=3$ — both are solutions."*
4. Simplify $\dfrac{3x+6}{3x}$ — *"Cancel the $3$'s and the $x$'s: answer
   is $6$."*
5. Multiply $\dfrac{x-2}{x+3}\times\dfrac{x+3}{x-2}$ — *"Everything
   cancels, so the answer is $0$."*

## Set 7 — Bonus / Challenge

1. Solve: $\dfrac{2}{x-1}-\dfrac{3}{x+1}=1$ *(two answers)*
2. Simplify: $\dfrac{x^3-x}{x^2-1}$
3. Solve: $\dfrac{x+1}{x-3}=\dfrac{x-1}{x+3}$
4. Solve: $\dfrac{1}{x}+\dfrac{1}{x+2}=\dfrac{3}{4}$ *(two answers)*

---

## Answer Key

**Set 1:** 1) $x-3$  2) $x+3$  3) $\dfrac{x-3}{x+2}$  4) $\dfrac{2x}{x-2}$
5) $\dfrac{x-1}{x+1}$  6) $\dfrac{x-2}{x+5}$

**Set 2:** 1) $\dfrac{x+4}{x+1}$  2) $\dfrac{x-4}{3}$  3) $1$  4) $x-3$
5) $2$  6) $2x+4$

**Set 3:** 1) $x=-2$  2) $x=1$  3) $x=2$  4) $x=-8$  5) $x=-6$ or $x=5$

**Set 4:**
1. Candidate $x=3$ — but $x=3$ makes the original denominator $x-3$ zero.
   **No solution.**
2. Candidate $x=4$ — but $x=4$ makes the original denominator $x-4$ zero.
   **No solution.**
3. Candidate $x=5$ — but $x=5$ makes the original denominator $x-5$ zero.
   **No solution.**
4. $x=\dfrac{5}{2}$ — denominator $x-1=\frac32\ne0$. **Valid**, not a trap.

**Set 5:** 1) $2$ (a constant — not $0$, not $1$)  2) $x=3$  3) $\dfrac{x-5}{2x}$
4. Clearing gives candidate $x=2$, which makes $x-2$ zero — **no solution**.
5. $\dfrac{x-3}{x+3}$

**Set 6:**
1. Error — $x$ is a term of the numerator $x+5$, not a factor of it;
   nothing can be canceled. Correct: $\dfrac{x+5}{x}$ is already simplest.
2. Error — after canceling $(x+2)$, the factor $(x-2)$ remains; it doesn't
   vanish. Correct: $x-2$.
3. Error — $x=2$ was never checked against the original denominator
   $x-2$; it makes it zero and must be rejected. Correct: $x=3$ only.
4. Error — canceled $x$ as if it were a shared factor of the whole
   numerator $3x+6$, but $x$ is only a factor of one term. Correct:
   $\dfrac{3x+6}{3x}=\dfrac{3(x+2)}{3x}=\dfrac{x+2}{x}$ — cannot simplify
   further.
5. Error — the two factors genuinely do cancel completely, but the result
   of canceling identical factors is $1$, not $0$. Correct: $1$.

**Set 7:** 1) $x=-3$ or $x=2$  2) $x$  3) $x=0$  4) $x=-\dfrac{4}{3}$ or $x=2$
