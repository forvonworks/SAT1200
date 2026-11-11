# Book 2 — Lesson 2: Systems of Linear Equations — Problem Sets

**Source content file**, paired with `concepts.md`. All answers verified by a
Python (`sympy.solve`) script before finalizing — not hand-computed.

---

## Set 1 — Substitution Drill

What is the solution $(x,y)$ to each system of equations below?

1. $y=x+3$ and $2x+y=18$
2. $y=2x$ and $x+y=15$
3. $y=3x-4$ and $x+y=12$
4. $x=y+5$ and $2y+x=17$
5. $y=-x+10$ and $3x-y=2$
6. $y=4x-3$ and $2x+y=21$

## Set 2 — Elimination Drill (Multiply First When Needed)

Solve each system of equations below for $(x,y)$. Some systems require
multiplying one equation by a constant before you add or subtract.

1. $x+y=9$ and $x-y=3$
2. $2x+y=13$ and $x-y=2$
3. $3x+2y=17$ and $x-2y=-5$
4. $2x+3y=13$ and $4x-y=5$
5. $5x+2y=19$ and $3x-2y=5$
6. $x+3y=14$ and $2x+y=13$

## Set 3 — Mixed (Choose the More Efficient Method)

Solve each system of equations below using substitution or elimination —
whichever method reaches the solution $(x,y)$ more efficiently.

1. $y=3x-5$ and $2x+3y=18$
2. $4x-y=10$ and $2x+y=14$
3. $x+y=20$ and $x-y=-6$
4. $3x+y=7$ and $y=x-5$
5. $2x+5y=22$ and $x-y=4$
6. $6x-2y=24$ and $3x+y=18$

## Set 4 — Special Cases

How many solutions does each system of equations below have — exactly one,
no solution, or infinitely many? If the system has exactly one solution,
give the solution $(x,y)$.

1. $3x+6y=12$ and $x+2y=4$
2. $x+2y=5$ and $2x+4y=9$
3. $x-3y=1$ and $2x-6y=2$
4. $5x+y=10$ and $x-y=2$

In each system of equations below, $k$ is a constant.

5. For what value of $k$ does the system $2x+ky=6$ and $4x+8y=20$ have **no
   solution**?
6. For what value of $k$ does the system $x+3y=6$ and $2x+ky=12$ have
   **infinitely many solutions**?

## Set 5 — What's Actually Being Asked

Solve each system of equations below, then evaluate the specific quantity
asked for — not simply the value of $x$ or $y$ alone.

1. In the system $x+y=14$ and $x-y=4$, what is the value of $xy$?
2. In the system $2x+y=11$ and $x-y=1$, what is the value of $x+y$?
3. In the system $x+2y=16$ and $x-y=1$, what is the value of $2x-y$?
4. In the system $3x+y=19$ and $x+y=9$, what is the value of $x-y$?
5. In the system $x+y=13$ and $2x-y=8$, what is the value of $x^2-y^2$?

## Set 6 — Spot the Error

Each solution below contains exactly one error. Identify the error and give
the correct answer.

1. $x+y=8$, $x-y=2$ — *"Adding the equations: $2x = 8-2=6$, so $x=3$ and
   $y=5$."*
2. $2x+y=7$, $y=3x-8$ — *"Substituting: $2x+3x-8=7$, so $5x=7$ and
   $x=\frac{7}{5}$."*
3. $4x+2y=8$, $2x+y=5$ — *"Both equations represent the same line, so the
   system has infinitely many solutions."*
4. $3x-y=5$, $x+y=11$ — *"Adding the equations: $4x=16$, so $x=4$; then
   $y=11+4=15$."*

## Set 7 — Bonus / Challenge

1. Solve the system $2x+3y=7$ and $5x-2y=8$ for $(x,y)$.
2. The sum of two numbers is $24$, and their difference is $8$. What are
   the two numbers?
3. In the system $3x+ky=10$ and $x+2y=3$, $k$ is a constant. For what
   value of $k$ does the system have **no solution**?
4. Solve the system $4x+3y=25$ and $2x-y=5$ for $(x,y)$.

---

## Answer Key

**Set 1:** 1) $(5,8)$  2) $(5,10)$  3) $(4,8)$  4) $(9,4)$  5) $(3,7)$  6) $(4,13)$

**Set 2:** 1) $(6,3)$  2) $(5,3)$  3) $(3,4)$  4) $(2,3)$  5) $(3,2)$  6) $(5,3)$

**Set 3:** 1) $(3,4)$  2) $(4,6)$  3) $(7,13)$  4) $(3,-2)$  5) $(6,2)$  6) $(5,3)$

**Set 4:**
1. Infinitely many solutions (second equation is exactly $\frac13$ of the first).
2. No solution (coefficient ratio is $2$ both times, but $5\times2=10 \ne 9$).
3. Infinitely many solutions (second equation is exactly $2\times$ the first).
4. One solution: $(x,y)=(2,0)$.
5. $k=4$
6. $k=6$

**Set 5:** 1) $xy=45$ ($x=9,y=5$)  2) $x+y=7$ ($x=4,y=3$)  3) $2x-y=7$ ($x=6,y=5$)  4) $x-y=1$ ($x=5,y=4$)  5) $x^2-y^2=13$ ($x=7,y=6$)

**Set 6:**
1. Error — $8-2$ was used instead of $8+2$ (subtraction was used where
   addition was needed). Correct: $2x=10$, $x=5$, $y=3$.
2. Error — the $-8$ term was never moved to the other side of the equation
   (the terms were simply combined, ignoring the $-8$). Correct:
   $5x-8=7$, so $5x=15$, $x=3$, $y=1$.
3. Error — the constants were never checked. The coefficient ratios match
   ($4/2=2$ and $2/1=2$), but the constant ratio does not ($8$ vs.
   $2\times5=10$) — so this system actually has **no solution**, not
   infinitely many.
4. Error — $y=11+4$ was computed instead of $y=11-4$ (a sign error).
   Correct: $y=11-4=7$, so the answer is $(4,7)$.

**Set 7:** 1) $(2,1)$  2) The numbers are $16$ and $8$.  3) $k=6$  4) $(4,3)$
