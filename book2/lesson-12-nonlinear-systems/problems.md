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

## Set 8 — Official SAT-Style Application

Multiple-choice (A–D), English, matching the real Digital SAT's format and item
design for this lesson's skill category (*Nonlinear equations in one variable
and systems of equations in two variables*), limited to the linear-quadratic
and quadratic-quadratic systems in `concepts.md`. Every item below is
**original**: it was written by studying the method and structure of real,
officially released SAT Suite Question Bank items in that category, then
building a new problem (new numbers, new context) that needs the same solving
steps. No real College Board question text, numbers, or wording is reproduced
here or anywhere in this book — see the note at the end of this set.

15 Easy / 15 Medium / 15 Hard.

### Easy

1. Which ordered pair $(x,y)$ is a solution to the system $y=x+3$ and $y=x^2-3$?
   A) $(-3,0)$  B) $(3,6)$  C) $(0,3)$  D) $(6,3)$

2. The system $y=x+4$ and $y=x^2+2$ has two solutions. What is the sum of their $y$-coordinates?
   A) $9$  B) $1$  C) $6$  D) $18$

3. The system $y=5x-6$ and $y=x^2$ has two solutions. One of them has $x=3$. What is the $y$-coordinate of that solution?
   A) $3$  B) $4$  C) $15$  D) $9$

4. How many real solutions does the system $y=x-1$ and $y=x^2+3$ have?
   A) None  B) Exactly one  C) Exactly two  D) Infinitely many

5. How many real solutions does the system $y=6x-9$ and $y=x^2$ have?
   A) None  B) Exactly one  C) Exactly two  D) Infinitely many

6. The line $y=2x+1$ meets the parabola $y=x^2+2$ at exactly one point. What is the $y$-coordinate of that point?
   A) $1$  B) $2$  C) $5$  D) $3$

7. The line $y=2x+1$ and the parabola $y=x^2-2$ intersect at two points. What is the positive difference between the two $y$-coordinates?
   A) $4$  B) $6$  C) $8$  D) $10$

8. Which ordered pair $(x,y)$ satisfies both $y=-x+2$ and $y=x^2$?
   A) $(1,1)$  B) $(-1,3)$  C) $(2,0)$  D) $(-2,-4)$

9. The graphs of $y=x+2$ and $y=x^2$ intersect at two points. For the point with a positive $x$-coordinate, what is the product $xy$?
   A) $2$  B) $6$  C) $12$  D) $8$

10. How many points of intersection do the line $y=2x+3$ and the parabola $y=x^2$ have?
    A) Exactly one  B) Exactly two  C) None  D) Infinitely many

11. The line $y=x+1$ is tangent to the parabola $y=x^2-3x+5$. What is the $x$-coordinate of the point of tangency?
    A) $1$  B) $3$  C) $2$  D) $4$

12. The line $y=3x+4$ and the parabola $y=x^2$ intersect at two points. What is the sum of their $x$-coordinates?
    A) $3$  B) $-4$  C) $16$  D) $17$

13. The line $y=x$ and the parabola $y=x^2-6$ intersect at two points. What is the product of the $y$-coordinates of these two points?
    A) $1$  B) $-6$  C) $5$  D) $6$

14. How many points of intersection do the horizontal line $y=3$ and the parabola $y=x^2-6$ have?
    A) Exactly one  B) None  C) Exactly four  D) Exactly two

15. The line $y=2x+8$ and the parabola $y=x^2$ intersect at two points. What is the $y$-coordinate of the point whose $x$-coordinate is negative?
    A) $4$  B) $-2$  C) $8$  D) $16$

### Medium

1. The line $y=3x+1$ is tangent to the parabola $y=2x^2-x+3$. What is the $y$-coordinate of the point of tangency?
   A) $1$  B) $3$  C) $7$  D) $4$

2. The line $y=2x+1$ and the parabola $y=2x^2+3x-5$ intersect at two points. What is the sum of the $y$-coordinates of these points?
   A) $1$  B) $7$  C) $4$  D) $-1$

3. For what value of $k$ does the line $y=x+k$ touch the parabola $y=x^2$ at exactly one point?
   A) $-\dfrac{1}{4}$  B) $\dfrac{1}{4}$  C) $-4$  D) $1$

4. The line $y=4x-1$ is tangent to the parabola $y=x^2+bx+3$. If $b$ is positive, what is $b$?
   A) $-8$  B) $0$  C) $4$  D) $8$

5. The graphs of $y=2x^2+3x-1$ and $y=2x^2-x+7$ intersect at exactly one point. What is the $y$-coordinate of that point?
   A) $7$  B) $9$  C) $13$  D) $17$

6. The parabolas $y=x^2-2x+5$ and $y=x^2+4x-7$ intersect at exactly one point. What is the sum of the $x$-coordinate and the $y$-coordinate of that point?
   A) $2$  B) $7$  C) $5$  D) $10$

7. The line $y=\dfrac{1}{2}x+3$ and the parabola $y=x^2$ intersect at two points. What is the sum of their $x$-coordinates?
   A) $-\dfrac{1}{2}$  B) $2$  C) $\dfrac{1}{2}$  D) $3$

8. The line $y=-x+4$ and the parabola $y=x^2-2$ intersect at two points. For the point with the larger $x$-coordinate, what is the product $xy$?
   A) $-21$  B) $4$  C) $9$  D) $14$

9. For which values of $k$ does the line $y=kx$ intersect the parabola $y=x^2-4$ at exactly two points?
   A) $k=0$ only  B) $k>0$  C) $k<-4$  D) All real values of $k$

10. A company's revenue is $R=6x$ and its cost is $C=x^2-2x+12$, where $x$ is the number of units produced and both are in dollars. Break-even occurs where $R=C$. What is the sum of the break-even values of $x$?
    A) $6$  B) $12$  C) $8$  D) $18$

11. The line $y=x+2$ and the parabola $y=x^2-4x+6$ intersect at two points. What is the $y$-coordinate of the point with the smaller $x$-coordinate?
    A) $1$  B) $3$  C) $4$  D) $6$

12. The line $y=2x+3$ and the parabola $y=x^2$ intersect at two points. What is the sum of the $y$-coordinates of these points?
    A) $10$  B) $2$  C) $5$  D) $12$

13. The line $y=2x+k$ touches the parabola $y=x^2+4x+7$ at exactly one point. What is $k$?
    A) $3$  B) $5$  C) $6$  D) $8$

14. The graphs of $y=2x^2-5x+1$ and $y=2x^2+x-11$ intersect at exactly one point. What is the $y$-coordinate of that point?
    A) $1$  B) $-1$  C) $-3$  D) $5$

15. Consider the system $y=x-4$ and $y=x^2-3x+3$. Which statement is correct about the quadratic equation obtained by setting the two expressions for $y$ equal?
    A) $D=-12$, no real solutions  B) $D=-12$, two real solutions
    C) $D=12$, two real solutions  D) $D=4$, one real solution

### Hard

1. The line $y=mx+1$ is tangent to the parabola $y=x^2+3x+5$. If $m<0$, what is $m$?
   A) $-7$  B) $-1$  C) $1$  D) $7$

2. The graphs of $y=2x^2-x-1$ and $y=\dfrac{1}{2}x-\dfrac{1}{2}$ intersect at two points. What is the product of their $x$-coordinates?
   A) $-\dfrac{1}{4}$  B) $\dfrac{1}{4}$  C) $-\dfrac{3}{4}$  D) $1$

3. The parabolas $y=2x^2+5x-3$ and $y=2x^2-x+k$ intersect at a point whose $x$-coordinate is $2$. What is $k$?
   A) $9$  B) $3$  C) $7$  D) $15$

4. The line $y=2x+3$ and the parabola $y=x^2-4x+k$ intersect at two points. For any value of $k$ for which this happens, what is the sum of the $x$-coordinates of the two intersection points?
   A) $-6$  B) $6$  C) $2$  D) $4$

5. The line $y=x-1$ and the parabola $y=x^2-4x+5$ intersect at two points. What is the product of their $y$-coordinates?
   A) $3$  B) $5$  C) $2$  D) $6$

6. The line $y=3x+4$ and the parabola $y=x^2$ intersect at two points. For the point with a positive $x$-coordinate, what is the sum $x+y$?
   A) $5$  B) $16$  C) $24$  D) $20$

7. For how many values of $k$ does the line $y=kx-1$ touch the parabola $y=x^2+3$ at exactly one point?
   A) $0$  B) $1$  C) $4$  D) $2$

8. The graphs of $y=-x^2+4x+1$ and $y=x+1$ intersect at two points. What is the sum of their $y$-coordinates?
   A) $5$  B) $1$  C) $4$  D) $7$

9. A curved path is modeled by $y=x^2-6x+10$, and a straight road by $y=2x-2$. The path crosses the road at two points. What is the horizontal distance between these two points?
   A) $2$  B) $4$  C) $8$  D) $12$

10. The graphs of $y=3x^2+2x-4$ and $y=3x^2-5x+8$ intersect at exactly one point. What is the $x$-coordinate of that point?
    A) $\dfrac{7}{12}$  B) $-\dfrac{12}{7}$  C) $\dfrac{12}{7}$  D) $12$

11. The line $y=6x$ touches the curve $y=ax^2+1$ at exactly one point. What is $a$?
    A) $3$  B) $6$  C) $36$  D) $9$

12. The line $y=x$ and the parabola $y=x^2-3x+2$ intersect at two points $(x_1,y_1)$ and $(x_2,y_2)$. What is $\dfrac{1}{x_1}+\dfrac{1}{x_2}$?
    A) $2$  B) $4$  C) $\dfrac{1}{2}$  D) $-2$

13. A line passes through $(2,1)$ with slope $-3$ and intersects the parabola $y=x^2$ at two points. What is the sum of the $x$-coordinates of these two points?
    A) $-7$  B) $-3$  C) $3$  D) $7$

14. The parabolas $y=x^2+bx+3$ and $y=x^2+5x-1$ intersect at the point whose $x$-coordinate is $-2$. What is $b$?
    A) $-3$  B) $3$  C) $9$  D) $7$

15. Which system has exactly one real solution?
    A) $y=x+1$ and $y=x^2$
    B) $y=4x$ and $y=x^2+1$
    C) $y=2x-1$ and $y=x^2$
    D) $y=4x+4$ and $y=x^2$

**A note on sourcing:** real, official College Board SAT questions are
copyrighted and are **not** licensed for reproduction in commercial test-prep
materials, under any circumstances, with or without attribution. No verbatim
College Board question appears in this book. Every item above was independently
written to match the *method*, *structure*, and *officially documented
difficulty tier* of real SAT Suite Question Bank items in this lesson's skill
category: the numbers, names, and contexts are all original. Each item was
checked against that method with a symbolic (sympy) solver, including the
single correct choice and the plausible wrong answers.

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

**Set 8 — Easy:** 1) B  2) A  3) D  4) A  5) B  6) D  7) C  8) A  9) D  10) B  11) C  12) A  13) B  14) D  15) A

**Set 8 — Medium:** 1) D  2) A  3) A  4) D  5) C  6) B  7) C  8) B  9) D  10) C  11) B  12) A  13) C  14) B  15) A

**Set 8 — Hard:** 1) B  2) A  3) A  4) B  5) C  6) D  7) D  8) A  9) B  10) C  11) D  12) A  13) B  14) D  15) C
