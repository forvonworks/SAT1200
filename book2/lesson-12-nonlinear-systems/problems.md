# Book 2 — Lesson 12: Nonlinear Systems — Practice Sets

**Source content file**, paired with `concepts.md`. All answers verified by a
`sympy` script (solving each system symbolically and, for discriminant
questions, computing $b^2-4ac$ directly) — not hand-checked.

---

## Set 1 — Linear-Quadratic Drill (clean, two solutions each)

For each system of equations below, what are the solutions $(x,y)$?

1. $y=x+1$, $\quad y=x^2-1$
2. $y=2x$, $\quad y=x^2-3$
3. $y=x-2$, $\quad y=x^2-4$
4. $y=3x+2$, $\quad y=x^2+2x$
5. $y=x+6$, $\quad y=x^2$
6. $y=4x-3$, $\quad y=x^2$

## Set 2 — Linear-Quadratic, Harder Coefficients

For each system of equations below, what are the solutions $(x,y)$?

1. $y=2x-5$, $\quad y=x^2-3x+1$
2. $y=2x+4$, $\quad y=x^2+x-2$
3. $y=-3x+11$, $\quad y=x^2-x+3$
4. $y=7$, $\quad y=x^2-2$
5. $y=-x+2$, $\quad y=x^2-5x+2$

## Set 3 — No Real Solution

For each system of equations below, how many real solutions does the system have? Use the discriminant of the resulting equation to support your answer.

1. $y=x$, $\quad y=x^2+5$
2. $y=2x-1$, $\quad y=x^2+4$
3. $y=-x$, $\quad y=x^2+3$
4. $y=3x-2$, $\quad y=x^2+2x+5$

## Set 4 — Quadratic-Quadratic Systems

Each system of equations below consists of two quadratics with the same leading coefficient, so subtracting one equation from the other eliminates the $x^2$-term. What is the solution $(x,y)$ to each system?

1. $y=x^2+3x+2$, $\quad y=x^2-x+10$
2. $y=x^2+5x-1$, $\quad y=x^2+x+7$
3. $y=x^2-2x+4$, $\quad y=x^2+4x-8$
4. $y=2x^2+x-3$, $\quad y=2x^2-3x+5$
5. $y=x^2+6x+1$, $\quad y=x^2-2x+9$

## Set 5 — What's Actually Being Asked?

Solve each system of equations below, but give only the value requested — not the full solution pairs $(x,y)$.

1. $y=x+1$, $y=x^2-1$ — What is the **sum of the $y$-coordinates** of all solutions to the system?
2. $y=2x$, $y=x^2-3$ — What is the **product of the $x$-coordinates** of all solutions to the system?
3. $y=2x-5$, $y=x^2-3x+1$ — What is $x_1+x_2+y_1+y_2$ across both solutions to the system?
4. $y=4x-3$, $y=x^2$ — What is the **positive difference** between the two $y$-values of the solutions to the system?
5. $y=x+2$, $y=x^2$ — What is $x+y$ for the solution to the system with the **larger** $x$-value?

## Set 6 — Spot the Error

Each item has exactly one broken step. Name the error and give the correct answer.

1. $y=x+1$, $y=x^2-1$ — *"$x^2-x-2=0 \Rightarrow (x-2)(x+1)=0 \Rightarrow x=2 \Rightarrow y=3$. The solution is $(2,3)$."*
2. $y=2x$, $y=x^2-3$ — *"$x^2-2x-3=0 \Rightarrow x=3$ or $x=-1$. The solutions are $x=3$ and $x=-1$."*
3. $y=x^2+3x+2$, $y=x^2-x+10$ — *"Removing the $x^2$ terms: $(3x+2)+(-x+10)=0 \Rightarrow 2x+12=0 \Rightarrow x=-6$."*
4. $y=x$, $y=x^2+5$ — *"Solving $x^2-x+5=0$: $D=1-20=-19$. Even though $D$ is negative, we still find two solutions, $x=\frac{1\pm\sqrt{19}}{2}$."*

## Set 7 — Bonus / Challenge

1. For the system of equations $y=x^2-4x+1$ and $y=x^2+2x-11$, what is the solution $(x,y)$?
2. For the system of equations $y=\dfrac{1}{2}x+1$ and $y=x^2-x$, what are the solutions $(x,y)$?
3. In the $xy$-plane, how many points of intersection does the line $y=2x+7$ have with the parabola $y=x^2+4x+10$?
4. In the $xy$-plane, the line $y=4x-4$ is tangent to the parabola $y=x^2$. What is the point of tangency?
5. For the system of equations $y=-2x+5$ and $y=x^2-3x-1$, what is the **positive difference** between the two $y$-values of the solutions?

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
