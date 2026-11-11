# Book 2 — Lesson 7: Quadratic Graphs & the Discriminant — Problem Sets

**Source content file**, paired with `concepts.md`. All answers verified by a
`sympy` script (vertex via $-b/2a$, discriminant via $b^2-4ac$, roots via
`solve`) before these files were written — none hand-computed.

---

## Set 1 — Vertex, Axis, Direction, Width (from vertex form)

Each equation represents a parabola in the xy-plane. For each one, what is
the vertex and the axis of symmetry, which way does the parabola open, and
is it narrower or wider than the graph of $y=x^2$?

1. $y=3(x-1)^2+4$
2. $y=-2(x+3)^2-1$
3. $y=(x-5)^2+2$
4. $y=-\dfrac{1}{2}(x-2)^2+6$
5. $y=5(x+4)^2-7$
6. $y=-x^2+9$

## Set 2 — Discriminant & Solution Count

How many real solutions does each equation have?

1. $x^2+5x+6=0$
2. $x^2-4x+4=0$
3. $x^2+2x+5=0$
4. $2x^2-3x-5=0$
5. $3x^2+2x+1=0$
6. $x^2-6x+9=0$

## Set 3 — Finding x-Intercepts

Each equation represents a parabola in the xy-plane. What are the
$x$-intercepts of the graph of each equation?

1. $x^2-7x+10=0$
2. $x^2+x-12=0$
3. $2x^2-x-3=0$
4. $x^2-9=0$
5. $x^2+6x+9=0$
6. $3x^2+5x-2=0$

## Set 4 — Mixed: Vertex + Discriminant + Roots Together

Each equation represents a parabola in the xy-plane. For each one, what is
the vertex of the graph, the value of the discriminant, and the real
root(s), if any?

1. $y=x^2-4x+3$
2. $y=-x^2+4x-5$
3. $y=2x^2-8x+8$
4. $y=-3x^2+12x-9$
5. $y=x^2+2x+1$

## Set 5 — "Find k" (SAT-Format Discriminant Problems)

1. For what value(s) of $k$ does $x^2+kx+9=0$ have exactly one real solution?
2. For what value(s) of $k$ does $x^2-4x+k=0$ have no real solutions?
3. For what value(s) of $k$ does $2x^2+4x+k=0$ have two real solutions?
4. Find $k$ so that $x^2+6x+k=0$ has exactly one real solution.
5. For what value(s) of $k$ (with $k\ne0$) does $kx^2+4x+4=0$ have no real
   solution?

## Set 6 — Spot the Error

Each item has exactly one broken step. Name the error and give the correct
answer.

1. $y=2(x-3)^2+5$ — *"Vertex is $(-3,5)$."*
2. $x^2+2x+5=0$ — *"$D=4-20=-16$, so there are 2 real solutions since D is a
   real number."*
3. $y=-2x^2+8$ — *"Opens upward, because the number multiplying $x^2$ is
   positive 2."*
4. $x^2-5x+6=0$ — *"Factors as $(x-2)(x-3)=0$, so the roots are $x=-2,-3$."*
5. $y=x^2-4x+4$ — *"$D=16-16=0$, so there are no solutions."*

## Set 7 — Bonus / Challenge

1. A ball's height is modeled by $h(t)=-16t^2+64t+5$. At what time does it
   reach its maximum height, and what is that height?
2. For what value of $k$ does $y=x^2+(k+2)x+9$ touch the x-axis exactly once?
3. A parabola has vertex $(2,-3)$ and passes through $(0,5)$. Find $a$, $b$,
   $c$ in $y=ax^2+bx+c$.
4. How many real solutions does $3x^2-2x+1=0$ have — does its graph cross or
   touch the x-axis, or neither?
5. If the discriminant of $x^2+bx+16=0$ equals $0$, find all possible values
   of $b$.

---

## Answer Key

**Set 1:**
1. Vertex $(1,4)$, axis $x=1$, opens up, narrower
2. Vertex $(-3,-1)$, axis $x=-3$, opens down, narrower
3. Vertex $(5,2)$, axis $x=5$, opens up, same width as $y=x^2$
4. Vertex $(2,6)$, axis $x=2$, opens down, wider
5. Vertex $(-4,-7)$, axis $x=-4$, opens up, narrower
6. Vertex $(0,9)$, axis $x=0$, opens down, same width as $y=x^2$

**Set 2:** 1) $D=1$, 2 solutions  2) $D=0$, 1 solution  3) $D=-16$, 0 solutions
4) $D=49$, 2 solutions  5) $D=-8$, 0 solutions  6) $D=0$, 1 solution

**Set 3:** 1) $x=2,5$  2) $x=-4,3$  3) $x=-1,\frac32$  4) $x=-3,3$  5) $x=-3$
(double root)  6) $x=-2,\frac13$

**Set 4:**
1. Vertex $(2,-1)$, $D=4$, roots $x=1,3$
2. Vertex $(2,-1)$, $D=-4$, no real roots
3. Vertex $(2,0)$, $D=0$, root $x=2$
4. Vertex $(2,3)$, $D=36$, roots $x=1,3$
5. Vertex $(-1,0)$, $D=0$, root $x=-1$

**Set 5:** 1) $k=\pm6$  2) $k>4$  3) $k<2$  4) $k=9$  5) $k>1$

**Set 6:**
1. Error — vertex form is $a(x-h)^2+k$, so the vertex is $(h,k)=(3,5)$, not
   $(-3,5)$ (sign flips when reading $h$ off the form).
2. Error — $D<0$ means **zero** real solutions, not "2 since D is a real
   number"; the sign of D is what matters, not whether it's defined.
3. Error — ignored the negative sign in front: $a=-2<0$ means the parabola
   opens **downward**.
4. Error — $(x-2)=0$ gives $x=2$, not $x=-2$; sign flips when solving each
   factor. Correct roots: $x=2,3$.
5. Error — $D=0$ means **exactly one** real solution (the parabola touches
   the x-axis once), not zero solutions.

**Set 7:**
1. $t=2$ seconds, max height $=69$
2. $k=4$ or $k=-8$
3. $a=2$, $b=-8$, $c=5$
4. $D=-8<0$ — 0 real solutions, the graph neither crosses nor touches the
   x-axis
5. $b=\pm8$
