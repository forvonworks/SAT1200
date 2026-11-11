# Book 2 — Lesson 11: Function Notation, Composition & Transformation — Problem Sets

**Source content file**, paired with `concepts.md`. All answers computed and
verified by Python script (`sympy` for symbolic composition; direct
evaluation for transformations), not hand-checked.

Unless an item states otherwise, every question in this lesson uses the
functions
$f(x)=3x-2$, $g(x)=x^2+1$, $h(x)=2x+5$.

---

## Set 1 — Composite Function Values

Using the functions above, answer each question.

1. What is the value of $f(g(2))$?
2. What is the value of $g(f(1))$?
3. What is the value of $f(h(0))$?
4. What is the value of $h(g(1))$?
5. What is the value of $g(g(1))$?
6. What is the value of $f(f(2))$?

## Set 2 — Simplifying Composite Functions

Using the functions above, answer each question.

1. What is $f(g(x))$ when fully simplified?
2. What is $g(f(x))$ when fully simplified?
3. What is $f(h(x))$ when fully simplified?
4. What is $h(f(x))$ when fully simplified?
5. What is $g(h(x))$ when fully simplified?
6. What is $h(g(x))$ when fully simplified?

## Set 3 — Vertical Transformation

For every item in this set, $f(x) = x^2-4$.

1. What is the value of $f(3)+5$?
2. What is the value of $f(1)-3$?
3. What is the value of $-f(2)$?
4. What is the value of $2f(1)$?
5. What is the value of $-f(0)+1$?
6. What is the value of $f(4)$? By how much does that output shift when $2$ is added, as in $f(4)+2$?

## Set 4 — Horizontal Transformation (the sign trap)

For every item in this set, $f(x) = x^2-4$.

1. What is the value of $f(x-3)$ when $x=5$?
2. What is the value of $f(x+2)$ when $x=1$?
3. What is the value of $f(-x)$ when $x=3$?
4. What is the value of $f(x-1)$ when $x=0$?
5. What is the value of $f(x-2)$ when $x=6$? How does it compare to the value of $f(x)$ when $x=4$?
6. What is the value of $f(-x)$ when $x=-2$?

## Set 5 — Mixed: Composition and Transformation

1. If $f(x)=x^2+1$ and $g(x)=x-3$, what is $f(g(x))$ in simplified form, and what is its value when $x=5$?
2. If $f(x)=2x+3$, what is the value of $f(x-1)$ when $x=4$?
3. If $g(x)=x^2-2x$, what is $g(-x)$ in simplified form?
4. If $f(x)=x^2+1$ and $g(x)=x+2$, what is the value of $g(f(2))$?
5. If $f(x)=x^2-5$, what is the value of $-f(x-1)$ when $x=3$?
6. If $f(x)=3x$, what is the value of $f(f(2))$?

## Set 6 — Identify the Error

Each item below mixes two ideas from this lesson, and the work shown contains
exactly one incorrect step. Identify the error, state which rule it violates,
and give the correct answer.

1. If $f(x)=x^2+1$ and $g(x)=2x$, what is $f(g(3))$? — *"$f(3)=10$, then $g(10)=20$."*
2. If $f(x)=x^2-4$, what is $f(3)+2$? — *"We compute $f(x+2)$: $f(5)=21$."*
3. If $f(x)=x^2+3x$, what is $f(x-2)$ when $x=5$? — *"It shifts left, so $f(x+2)=f(7)=70$."*
4. If $f(x)=x^2-1$, what is $f(-x)$ when $x=2$? — *"$f(-x)=-f(x)$, so $-f(2)=-3$."*
5. If $f(x)=2x+1$ and $g(x)=x-4$, what is $g(f(x))$? — *"$f(g(x))=2(x-4)+1=2x-7$."*

## Set 7 — Bonus / Challenge

1. If $f(x)=x^2-2x+1$ and $g(x)=x+3$, what is $f(g(x))$ in fully simplified form?
2. If $f(x)=x^2-4$, what is the value of $-f(x-1)$ when $x=0$?
3. If $f(x)=2x-5$ and $g(x)=x^2+1$, what are the values of $g(f(2))$ and $f(g(2))$? Are the two values equal?
4. If $f(x)=x^2+1$ and $h(x)=f(x-3)+2$, what is the value of $h(5)$?
5. If $f(x)=3x+2$, what is $f(f(x))$ in simplified form?

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
