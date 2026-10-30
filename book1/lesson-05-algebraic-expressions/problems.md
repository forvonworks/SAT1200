# Book 1 — Lesson 5: Algebraic Expressions — Practice Sets

**Source content file**, paired with `concepts.md`. Sets build in the order
specified at the bottom of `concepts.md`: combine like terms (positive) →
combine like terms (with subtraction) → distribute (positive multiplier) →
distribute (negative multiplier) → mixed/test-density → spot-the-error →
bonus challenge. **Every answer below was computed and verified with
`sympy.expand()`** — none were hand-simplified; see fork verification notes.

---

## Set 1 — Combine Like Terms (positive coefficients)

1. $3x + 5x$
2. $7y + 2y + y$
3. $4a + 3b + 2a$
4. $6x + 3 + 2x$
5. $5m + 4n + 3m + n$
6. $2x + 3x + 4x$
7. $8p + 5q + 2p + 3q$
8. $x + x + x + x$

## Set 2 — Combine Like Terms (with subtraction)

1. $7x - 3x$
2. $5a - 8a$
3. $4x - 7 + 2x$
4. $-3y + 5y - 2y$
5. $6m - 4n - 2m + 7n$
6. $-5x + 3x - 8$
7. $2a - 5a + 6a$
8. $9x - 4x - x$

*(Item 2 gives a negative coefficient; item 4 is a deliberate "gotcha" —
the like terms cancel completely, leaving $0$. That's a correct, normal
result, not a sign something went wrong — worth saying explicitly.)*

## Set 3 — Distributive Property (positive multiplier)

1. $3(x + 4)$
2. $5(2x - 3)$
3. $2(3a + 4b)$
4. $4(x - 1)$
5. $6(2 + 3x)$
6. $7(x + y)$
7. $3(4x - 2)$
8. $2(5x + 3)$

## Set 4 — Distributive Property (negative multiplier)

The highest-value set in this lesson — every item requires correctly
distributing a negative sign across *every* term inside the parentheses.

1. $-2(x + 3)$
2. $-(3x - 5)$
3. $-4(2x - 1)$
4. $-(x + 7)$
5. $-3(4 - x)$
6. $-(2x - 3y)$
7. $-5(x + 2)$
8. $-(-x + 4)$

## Set 5 — Mixed: Distribute, Then Combine (real-test density)

1. $3(x + 2) + 4x$
2. $5(2x - 1) - 3x$
3. $2(x + 3) - (x - 1)$
4. $4(x - 2) + 3(x + 1)$
5. $-(2x + 3) + 5x$
6. $3(x - 1) - 2(x + 2)$
7. $2(3x + 1) - (4x - 5)$
8. $5 - 2(x - 3)$

## Set 6 — Spot the Error

Each item shows a solution with exactly one broken step. Name the step, say
what rule it breaks, and give the correct simplified form.

1. Soddalashtiring: $-(3x - 5)$
   *Noto'g'ri yechim:* $-3x - 5$
2. Soddalashtiring: $4x + 3x^2$
   *Noto'g'ri yechim:* $7x^2$
3. Soddalashtiring: $-2(x - 4)$
   *Noto'g'ri yechim:* $-2x - 8$
4. Soddalashtiring: $5x - (2x - 3)$
   *Noto'g'ri yechim:* "$5x - 2x - 3 = 3x - 3$"
5. Soddalashtiring: $3(2x + 1) - 4$
   *Noto'g'ri yechim:* "$6x + 1 - 4 = 6x - 3$"

## Set 7 — Bonus / Challenge

Nested parentheses and two-variable expressions.

1. $2\left[3(x+1) - 2x\right] + 5$
2. $-3(x - 2) + 2(x + 4) - 5$
3. $4x - 2\left[x - (3x + 1)\right]$
4. $5(a - 2b) - 3(2a - b)$
5. $-\left[2(x+3) - (x-1)\right] + 4x$

---

## Answer Key

**Set 1:** 1) $8x$  2) $10y$  3) $6a+3b$  4) $8x+3$  5) $8m+5n$  6) $9x$
7) $10p+8q$  8) $4x$

**Set 2:** 1) $4x$  2) $-3a$  3) $6x-7$  4) $0$  5) $4m+3n$  6) $-2x-8$
7) $3a$  8) $4x$

**Set 3:** 1) $3x+12$  2) $10x-15$  3) $6a+8b$  4) $4x-4$  5) $18x+12$
6) $7x+7y$  7) $12x-6$  8) $10x+6$

**Set 4:** 1) $-2x-6$  2) $5-3x$  3) $4-8x$  4) $-x-7$  5) $3x-12$
6) $-2x+3y$  7) $-5x-10$  8) $x-4$

**Set 5:** 1) $7x+6$  2) $7x-5$  3) $x+7$  4) $7x-5$  5) $3x-3$  6) $x-7$
7) $2x+7$  8) $11-2x$

**Set 6:**
1. Error — the negative sign was applied only to $3x$, not to $-5$ as well.
   Correct: $-(3x-5) = -3x+5 = 5-3x$.
2. Error — $x$ and $x^2$ are not like terms (different powers of $x$), so
   they cannot be combined. Correct: $4x + 3x^2$ is already fully
   simplified (write as $3x^2 + 4x$).
3. Error — $-2 \times (-4)$ should give $+8$, not $-8$; the sign of the
   second term's product was dropped. Correct: $-2(x-4) = -2x+8 = 8-2x$.
4. Error — the negative sign in front of the parentheses was applied only
   to the first term ($2x$), not to the second term ($-3$) as well.
   Correct: $5x-(2x-3) = 5x-2x+3 = 3x+3$.
5. Error — $3 \times 1$ inside the parentheses was computed as $1$ instead
   of $3$ (the distribution to the second term was skipped). Correct:
   $3(2x+1)-4 = 6x+3-4 = 6x-1$.

**Set 7:** 1) $2x+11$  2) $9-x$  3) $8x+2$  4) $-a-7b$  5) $3x-7$
