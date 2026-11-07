# Book 2 — Lesson 11: Function Notation, Composition & Transformation — Problem Sets

**Source content file**, paired with `concepts.md`. All answers computed and
verified by Python script (`sympy` for symbolic composition; direct
evaluation for transformations), not hand-checked.

Functions used throughout unless a problem states otherwise:
$f(x)=3x-2$, $g(x)=x^2+1$, $h(x)=2x+5$.

---

## Set 1 — Evaluate Composition at a Point

1. $f(g(2))$
2. $g(f(1))$
3. $f(h(0))$
4. $h(g(1))$
5. $g(g(1))$
6. $f(f(2))$

## Set 2 — Build/Simplify Composition Algebraically

Simplify fully:

1. $f(g(x))$
2. $g(f(x))$
3. $f(h(x))$
4. $h(f(x))$
5. $g(h(x))$
6. $h(g(x))$

## Set 3 — Vertical Transformation

$f(x) = x^2-4$ for all items.

1. $f(3)+5$
2. $f(1)-3$
3. $-f(2)$
4. $2f(1)$
5. $-f(0)+1$
6. Compute $f(4)$ and $f(4)+2$. By how much did the output shift?

## Set 4 — Horizontal Transformation (the sign trap)

$f(x) = x^2-4$ for all items.

1. $f(x-3)$ at $x=5$
2. $f(x+2)$ at $x=1$
3. $f(-x)$ at $x=3$
4. $f(x-1)$ at $x=0$
5. Compute $f(x-2)$ at $x=6$ and $f(x)$ at $x=4$. What do you notice?
6. $f(-x)$ at $x=-2$

## Set 5 — Mixed (composition + transformation)

1. $f(x)=x^2+1$, $g(x)=x-3$. Simplify $f(g(x))$, then evaluate at $x=5$.
2. $f(x)=2x+3$. Evaluate $f(x-1)$ at $x=4$.
3. $g(x)=x^2-2x$. Simplify $g(-x)$.
4. $f(x)=x^2+1$, $g(x)=x+2$. Evaluate $g(f(2))$.
5. $f(x)=x^2-5$. Evaluate $-f(x-1)$ at $x=3$.
6. $f(x)=3x$. Evaluate $f(f(2))$.

## Set 6 — Spot the Error

Each item mixes two ideas from this lesson and has exactly one broken step.
Name the error, say which rule it breaks, and give the correct answer.

1. $f(x)=x^2+1$, $g(x)=2x$. Find $f(g(3))$ — *"$f(3)=10$, so'ngra $g(10)=20$."*
2. $f(x)=x^2-4$. Find $f(3)+2$ — *"$f(x+2)$ ni hisoblaymiz: $f(5)=21$."*
3. $f(x)=x^2+3x$. Find $f(x-2)$ at $x=5$ — *"Chapga siljiydi, shuning uchun
   $f(x+2)=f(7)=70$."*
4. $f(x)=x^2-1$. Find $f(-x)$ at $x=2$ — *"$f(-x)=-f(x)$, shuning uchun
   $-f(2)=-3$."*
5. $f(x)=2x+1$, $g(x)=x-4$. Find $g(f(x))$ — *"$f(g(x))=2(x-4)+1=2x-7$."*

## Set 7 — Bonus / Challenge

1. $f(x)=x^2-2x+1$, $g(x)=x+3$. Simplify $f(g(x))$ fully.
2. $f(x)=x^2-4$. Evaluate $-f(x-1)$ at $x=0$.
3. $f(x)=2x-5$, $g(x)=x^2+1$. Find $g(f(2))$ and $f(g(2))$ — are they equal?
4. $f(x)=x^2+1$. If $h(x)=f(x-3)+2$, find $h(5)$.
5. $f(x)=3x+2$. Simplify $f(f(x))$.

---

## Answer Key

**Set 1:** 1) $13$  2) $2$  3) $13$  4) $9$  5) $5$  6) $10$

**Set 2:** 1) $3x^2+1$  2) $9x^2-12x+5$  3) $6x+13$  4) $6x+1$  5) $4x^2+20x+26$  6) $2x^2+7$

**Set 3:** 1) $10$  2) $-6$  3) $0$  4) $-6$  5) $5$  6) $f(4)=12$, $f(4)+2=14$ — output shifted up by $2$

**Set 4:** 1) $0$  2) $5$  3) $5$  4) $-3$  5) both equal $12$ — confirms the shift  6) $0$

**Set 5:** 1) $f(g(x))=x^2-6x+10$; at $x=5$: $5$  2) $9$  3) $x^2+2x$  4) $7$  5) $1$  6) $18$

**Set 6:**
1. Error — reversed the composition order ($g(f(3))$ instead of $f(g(3))$).
   Correct: $g(3)=6$, $f(6)=37$.
2. Error — confused $f(x)+2$ (add to the output) with $f(x+2)$ (add to the
   input). Correct: $f(3)=5$, $f(3)+2=7$.
3. Error — assumed $f(x-h)$ shifts left; it shifts **right**. Correct:
   $f(x-2)$ at $x=5$ means $f(3)=18$.
4. Error — assumed $f(-x)=-f(x)$; reflecting the input (over the y-axis) is
   not the same as reflecting the output (over the x-axis). Correct:
   $f(-2)=3$.
5. Error — computed $f(g(x))$ instead of the requested $g(f(x))$. Correct:
   $g(f(x))=2x-3$.

**Set 7:** 1) $x^2+4x+4$  2) $3$  3) $g(f(2))=2$, $f(g(2))=5$ — not equal  4) $7$  5) $9x+8$
