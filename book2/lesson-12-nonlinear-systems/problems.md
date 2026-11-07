# Book 2 — Lesson 12: Nonlinear Systems — Practice Sets

**Source content file**, paired with `concepts.md`. All answers verified by a
`sympy` script (solving each system symbolically and, for discriminant
questions, computing $b^2-4ac$ directly) — not hand-checked.

---

## Set 1 — Linear-Quadratic Drill (clean, two solutions each)

Solve each system for both $(x,y)$ pairs.

1. $y=x+1$, $\quad y=x^2-1$
2. $y=2x$, $\quad y=x^2-3$
3. $y=x-2$, $\quad y=x^2-4$
4. $y=3x+2$, $\quad y=x^2+2x$
5. $y=x+6$, $\quad y=x^2$
6. $y=4x-3$, $\quad y=x^2$

## Set 2 — Linear-Quadratic, Harder Coefficients

1. $y=2x-5$, $\quad y=x^2-3x+1$
2. $y=2x+4$, $\quad y=x^2+x-2$
3. $y=-3x+11$, $\quad y=x^2-x+3$
4. $y=7$, $\quad y=x^2-2$
5. $y=-x+2$, $\quad y=x^2-5x+2$

## Set 3 — No Real Solution

Compute the discriminant of the resulting equation and state how many real
solutions the system has.

1. $y=x$, $\quad y=x^2+5$
2. $y=2x-1$, $\quad y=x^2+4$
3. $y=-x$, $\quad y=x^2+3$
4. $y=3x-2$, $\quad y=x^2+2x+5$

## Set 4 — Quadratic-Quadratic Systems

Each pair shares the same leading coefficient — subtract to eliminate $x^2$.

1. $y=x^2+3x+2$, $\quad y=x^2-x+10$
2. $y=x^2+5x-1$, $\quad y=x^2+x+7$
3. $y=x^2-2x+4$, $\quad y=x^2+4x-8$
4. $y=2x^2+x-3$, $\quad y=2x^2-3x+5$
5. $y=x^2+6x+1$, $\quad y=x^2-2x+9$

## Set 5 — What's Actually Being Asked?

Solve the system, but give only the requested quantity — not the raw pairs.

1. $y=x+1$, $y=x^2-1$ — find the **sum of the $y$-coordinates** of all solutions.
2. $y=2x$, $y=x^2-3$ — find the **product of the $x$-coordinates** of all solutions.
3. $y=2x-5$, $y=x^2-3x+1$ — find $x_1+x_2+y_1+y_2$ across both solutions.
4. $y=4x-3$, $y=x^2$ — find the **positive difference** between the two $y$-values.
5. $y=x+2$, $y=x^2$ — find $x+y$ for the solution with the **larger** $x$-value.

## Set 6 — Spot the Error

Each item has exactly one broken step. Name the error and give the correct answer.

1. $y=x+1$, $y=x^2-1$ — *"$x^2-x-2=0 \Rightarrow (x-2)(x+1)=0 \Rightarrow x=2 \Rightarrow y=3$. Javob: $(2,3)$."*
2. $y=2x$, $y=x^2-3$ — *"$x^2-2x-3=0 \Rightarrow x=3$ yoki $x=-1$. Javob: $x=3$, $x=-1$."*
3. $y=x^2+3x+2$, $y=x^2-x+10$ — *"$x^2$ hadlarini olib tashlab: $(3x+2)+(-x+10)=0 \Rightarrow 2x+12=0 \Rightarrow x=-6$."*
4. $y=x$, $y=x^2+5$ — *"$x^2-x+5=0$ ni yechamiz: $D=1-20=-19$. $D$ manfiy bo'lsa ham, $x=\frac{1\pm\sqrt{19}}{2}$ — ikkita yechim topamiz."*

## Set 7 — Bonus / Challenge

1. $y=x^2-4x+1$, $\quad y=x^2+2x-11$ (quadratic-quadratic)
2. $y=\dfrac{1}{2}x+1$, $\quad y=x^2-x$ (fraction coefficient)
3. $y=2x+7$, $\quad y=x^2+4x+10$ — how many intersection points does the line have with the parabola?
4. $y=4x-4$, $\quad y=x^2$ — find the point of tangency.
5. $y=-2x+5$, $\quad y=x^2-3x-1$ — find the **positive difference** between the two $y$-values.

---

## Answer Key

**Set 1:** 1) $(2,3),(-1,0)$  2) $(3,6),(-1,-2)$  3) $(2,0),(-1,-3)$  4) $(2,8),(-1,-1)$  5) $(3,9),(-2,4)$  6) $(1,1),(3,9)$

**Set 2:** 1) $(2,-1),(3,1)$  2) $(3,10),(-2,0)$  3) $(2,5),(-4,23)$  4) $(3,7),(-3,7)$  5) $(0,2),(4,-2)$

**Set 3:** 1) $D=-19$, no real solution  2) $D=-16$, no real solution  3) $D=-11$, no real solution  4) $D=-27$, no real solution

**Set 4:** 1) $(2,12)$  2) $(2,13)$  3) $(2,4)$  4) $(2,7)$  5) $(1,8)$

**Set 5:** 1) $3$  2) $-3$  3) $5$  4) $8$  5) $6$ *(point is $(2,4)$)*

**Set 6:**
1. Error — dropped the second solution $x=-1$ (and its matching $y=0$). A
   factored quadratic with two distinct roots means two solution pairs, not
   one. Correct: $(2,3)$ **and** $(-1,0)$.
2. Error — solved for $x$ but never back-substituted to find $y$. An answer
   to a system must be $(x,y)$ pairs, not $x$-values alone. Correct:
   $(3,6)$ and $(-1,-2)$.
3. Error — added the two right-hand expressions instead of setting them
   equal to each other. The correct step is $3x+2=-x+10$, not
   $(3x+2)+(-x+10)=0$. Correct: $x=2$, $y=12$.
4. Error — a negative discriminant means **no real solution exists at all**;
   writing $\sqrt{19}$ doesn't fix a negative value, it signals the roots are
   complex, not real. Correct: no real solution.

**Set 7:** 1) $(2,-3)$  2) $(2,2),(-\frac12,\frac34)$  3) $D=-8$, $0$ intersection points  4) $(2,4)$ *(double root — line is tangent to the parabola here)*  5) $10$
