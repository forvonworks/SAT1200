# Book 2 — Lesson 5: Quadratics I — Factoring & Solving — Problem Sets

**Source content file**, paired with `concepts.md`. All answers verified by a
`sympy` script (`sp.solve`, with factorizations cross-checked by expanding
back to the original) — not hand-computed.

---

## Set 1 — Factoring, $a=1$ (all-positive $b$, $c$)

1. What are the solutions to the equation $x^2+5x+4=0$?
2. What are the solutions to the equation $x^2+6x+8=0$?
3. What are the solutions to the equation $x^2+9x+14=0$?
4. What are the solutions to the equation $x^2+3x+2=0$?
5. What are the solutions to the equation $x^2+10x+16=0$?
6. What are the solutions to the equation $x^2+8x+12=0$?
7. What are the solutions to the equation $x^2+11x+18=0$?
8. What are the solutions to the equation $x^2+7x+10=0$?

## Set 2 — Factoring, $a=1$ (negative $b$ and/or $c$)

1. What are the solutions to the equation $x^2-5x+6=0$?
2. What are the solutions to the equation $x^2+2x-15=0$?
3. What are the solutions to the equation $x^2-3x-10=0$?
4. What are the solutions to the equation $x^2-7x+12=0$?
5. What are the solutions to the equation $x^2+4x-21=0$?
6. What are the solutions to the equation $x^2-2x-24=0$?
7. What are the solutions to the equation $x^2-x-6=0$?
8. What are the solutions to the equation $x^2+x-20=0$?

## Set 3 — GCF + $a\neq1$

1. What are the solutions to the equation $3x^2+9x+6=0$?
2. What are the solutions to the equation $2x^2-8=0$?
3. What are the solutions to the equation $2x^2+5x+2=0$?
4. What are the solutions to the equation $3x^2-x-2=0$?
5. What are the solutions to the equation $4x^2+4x-8=0$?
6. What are the solutions to the equation $2x^2-3x-5=0$?
7. What are the solutions to the equation $5x^2+15x+10=0$?
8. What are the solutions to the equation $2x^2+7x+3=0$?

## Set 4 — Rearrange to Zero First

These equations are not yet set equal to zero.

1. What are the solutions to the equation $(x+2)(x-1)=4$?
2. What are the solutions to the equation $(x-2)(x+5)=18$?
3. What are the solutions to the equation $(x+1)(x+4)=10$?
4. What are the solutions to the equation $(x-3)(x-2)=2$?
5. What are the solutions to the equation $(x+6)(x-1)=-10$?
6. What are the solutions to the equation $(x-4)(x+3)=-6$?

## Set 5 — What's Actually Being Asked?

Solve each equation, then answer the ACTUAL question asked — not just "find
the solutions."

1. The equation $x^2-2x-15=0$ has two solutions. What is the **sum** of the solutions?
2. The equation $x^2+x-12=0$ has two solutions. What is the **product** of the solutions?
3. The equation $x^2-7x+6=0$ has two solutions. What is the **positive difference** between the solutions
   (larger minus smaller)?
4. The equation $x^2+3x-10=0$ has two solutions. What is the **sum** of the solutions?

## Set 6 — Spot the Error

Each item below shows one step of a flawed solution. What is the error, and
what is the correct full solution (both values, where there are two)?

1. $(x+3)(x-2)=0$ — *"Yechish: $x+3=0$, shuning uchun $x=-3$."*
2. $x^2-4x-5=0$ — *"Yechish: $(x-1)(x+5)=0$, shuning uchun $x=1$ yoki $x=-5$."*
3. $(x-2)(x+4)=16$ — *"Yechish: $x-2=16$ yoki $x+4=16$, shuning uchun $x=18$ yoki $x=12$."*
4. $2x^2+6x=0$ — *"Yechish: $2x^2=-6x$, ikkala tomonni $x$ ga bo'lamiz: $2x=-6$, $x=-3$."*

## Set 7 — Bonus / Challenge

1. What are the solutions to the equation $6x^2+5x+1=0$?
2. What are the solutions to the equation $4x^2-9=0$?
3. What are the solutions to the equation $x^2-\dfrac{1}{4}=0$?
4. What are the solutions to the equation $x^2-3x+2=12$?
5. What are the solutions to the equation $2x^2+x-3=7$?

---

## Answer Key

**Set 1:** 1) $-4,-1$  2) $-4,-2$  3) $-7,-2$  4) $-2,-1$  5) $-8,-2$  6) $-6,-2$  7) $-9,-2$  8) $-5,-2$

**Set 2:** 1) $2,3$  2) $-5,3$  3) $-2,5$  4) $3,4$  5) $-7,3$  6) $-4,6$  7) $-2,3$  8) $-5,4$

**Set 3:** 1) $-2,-1$  2) $-2,2$  3) $-\frac12,-2$  4) $-\frac23,1$  5) $-2,1$  6) $-1,\frac52$  7) $-2,-1$  8) $-\frac12,-3$

**Set 4:** 1) $-3,2$  2) $-7,4$  3) $-6,1$  4) $1,4$  5) $-4,-1$  6) $-2,3$

**Set 5:** 1) solutions $-3,5$; sum $=2$  2) solutions $-4,3$; product $=-12$  3) solutions $1,6$; difference $=5$  4) solutions $-5,2$; sum $=-3$

**Set 6:**
1. Error — stopped after finding one solution. Correct: $x=-3$ or $x=2$ (both).
2. Error — wrong sign pair: $-1$ and $5$ give $-1+5=4$, not $-4$. Correct
   pair is $-5$ and $1$: $(x-5)(x+1)=0$, so $x=5$ or $x=-1$.
3. Error — zero-product property misapplied; the right side isn't $0$.
   Correct: expand and rearrange — $x^2+2x-8=16 \Rightarrow x^2+2x-24=0
   \Rightarrow (x+6)(x-4)=0 \Rightarrow x=-6$ or $x=4$.
4. Error — divided both sides by $x$, which silently discards the $x=0$
   solution. Correct: factor instead — $2x(x+3)=0 \Rightarrow x=0$ or $x=-3$.

**Set 7:** 1) $-\frac12,-\frac13$  2) $-\frac32,\frac32$  3) $-\frac12,\frac12$  4) $-2,5$  5) $-\frac52,2$
