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

## Set 8 — Official SAT-Style Application

Multiple-choice (A–D), English, matching the real Digital SAT's format and
item design for this lesson's skill category (*Nonlinear functions*: function
notation, composition, and vertical and horizontal transformations). Every
item below is **original**. Each was written by studying the method, traps,
and distractor style of real, officially released SAT Suite Question Bank
items in this category, then building a new problem with new numbers and a
new setting that needs the same solving steps. Each answer was verified by
computer algebra (sympy) before inclusion. See the note at the end of this set.

15 Easy / 15 Medium / 15 Hard, matching the real-test difficulty distribution.

### Easy

1. If $f(x)=2x+7$, what is the value of $f(-3)$?
   A) $1$  B) $-13$  C) $-1$  D) $13$

2. If $g(x)=x^2-5$, what is the value of $g(4)$?
   A) $-9$  B) $11$  C) $-1$  D) $21$

3. If $f(x)=3x-2$, what is the value of $f(2)+f(-1)$?
   A) $1$  B) $5$  C) $-1$  D) $9$

4. If $f(x)=x^2+4$ and $g(x)=2x-1$, what is the value of $g(f(1))$?
   A) $5$  B) $11$  C) $1$  D) $9$

5. If $f(x)=x^2+1$, what is the value of $f(x+2)$ when $x=3$?
   A) $2$  B) $26$  C) $8$  D) $12$

6. The function $f$ has the values $f(1)=3$, $f(2)=5$, $f(3)=-4$, and $f(4)=0$. What is the value of $f(f(1))$?
   A) $-4$  B) $0$  C) $3$  D) $5$

7. If $f(x)=5-x$ and $g(x)=x^2$, what is the value of $f(g(-2))$?
   A) $9$  B) $49$  C) $7$  D) $1$

8. If $f(x)=x^2-3x$, what is the value of $f(2)+4$?
   A) $-6$  B) $-2$  C) $2$  D) $18$

9. If $f(x)=x^2+2x-3$, what is the value of $-f(2)$?
   A) $-3$  B) $5$  C) $3$  D) $-5$

10. If $g(x)=x^2+x$, what is the value of $g(x-3)$ when $x=4$?
   A) $0$  B) $17$  C) $2$  D) $56$

11. If $f(x)=3x+1$ and $g(x)=x-2$, which expression is equal to $f(g(x))$?
   A) $3x-1$  B) $3x-6$  C) $3x-5$  D) $3x-7$

12. The graph of $y=f(x)$ is shifted down $5$ units to form the graph of $y=g(x)$. If $f(x)=2x+3$, what is $g(1)$?
   A) $0$  B) $-5$  C) $5$  D) $10$

13. If $f(x)=x+3$ and $g(x)=3x$, what is the value of $g(f(-1))$?
   A) $6$  B) $0$  C) $-3$  D) $2$

14. If $f(x)=x^2-2x+5$, what is the value of $f(-x)$ when $x=-1$?
   A) $8$  B) $4$  C) $-8$  D) $-4$

15. The function $g$ is defined by $g(x)=f(x+1)$, where $f(x)=3x+6$. What is $g(2)$?
   A) $9$  B) $15$  C) $12$  D) $18$

### Medium

1. If $f(x)=3x-2$ and $g(x)=x^2+1$, what is the value of $f(g(-2))$?
   A) $13$  B) $65$  C) $-17$  D) $-8$

2. If $h(x)=2x+5$ and $f(x)=3x-2$, for what value of $x$ is $f(h(x))=0$?
   A) $-\dfrac{13}{6}$  B) $\dfrac{13}{6}$  C) $-\dfrac{5}{2}$  D) $\dfrac{2}{3}$

3. Let $f(x)=x^2-6x$, and let $g(x)=f(x)+k$, where $k$ is a constant. If $g(4)=-3$, what is the value of $k$?
   A) $-5$  B) $11$  C) $5$  D) $-11$

4. Let $f(x)=3x+2$ and $g(x)=f(x-k)$, where $k$ is a constant. If $g(4)=5$, what is the value of $k$?
   A) $-1$  B) $-3$  C) $3$  D) $1$

5. Let $f(x)=x^2-1$ and $g(x)=-f(x)$. What is the value of $g(f(2))$?
   A) $8$  B) $-3$  C) $-8$  D) $3$

6. The function $f(x)=2x+1$, and the function $g$ has the values $g(-1)=2$, $g(0)=-1$, $g(1)=0$, and $g(2)=3$. What is the value of $g(f(0))$?
   A) $-1$  B) $0$  C) $1$  D) $3$

7. If $f(x)=x^2-3x$ and $g(x)=x+2$, what is $f(g(x))$ in simplified form?
   A) $x^2-3x+2$  B) $x^2+x-2$  C) $x^2-3x-2$  D) $x^2+x+4$

8. For the functions $f(x)=2x-1$ and $g(x)=x^2+k$, where $k$ is a constant, $f(g(2))=17$. What is the value of $k$?
   A) $10$  B) $-5$  C) $\dfrac{9}{2}$  D) $5$

9. Let $f(x)=x^2+4x$ and $g(x)=f(x+3)$. What is the value of $g(-1)$?
   A) $0$  B) $-3$  C) $12$  D) $21$

10. The graph of $y=x^2$ is translated $3$ units to the left and $2$ units down. Which expression defines the translated function?
   A) $(x+3)^2-2$  B) $(x-3)^2-2$  C) $(x+3)^2+2$  D) $(x-3)^2+2$

11. If $f(x)=x^2-2$ and $g(x)=3-x$, what is the value of $f(g(-1))$?
   A) $4$  B) $2$  C) $7$  D) $14$

12. If $f(x)=x^2-4x+3$, what is the value of $-2f(2)+3$?
   A) $-1$  B) $5$  C) $1$  D) $2$

13. If $f(x)=x^2+2$, which expression is equal to $f(x-4)$?
   A) $x^2-8x+16$  B) $x^2-8x+18$  C) $x^2+8x+18$  D) $x^2-2$

14. Let $f(x)=x-5$ and $g(x)=2x^2$. For which value(s) of $x$ is $f(g(x))=13$?
   A) $x=\pm3$  B) $x=3$ only  C) $x=\pm\sqrt{\tfrac{13}{2}}$  D) $x=\pm2$

15. If $f(x)=4x-3$ and $g(x)=\dfrac{x}{2}+1$, which expression is equal to $f(g(x))$?
   A) $2x-2$  B) $2x+4$  C) $2x-\dfrac{1}{2}$  D) $2x+1$

### Hard

1. Let $f(x)=x^2$ and $g(x)=x+2$. For what value of $x$ does $f(g(x))=g(f(x))$?
   A) $\dfrac{1}{2}$  B) $-2$  C) $0$  D) $-\dfrac{1}{2}$

2. The graph of $y=f(x)$, where $f(x)=x^2-2$, is translated $3$ units to the right and $4$ units up to form the graph of $y=g(x)$. What is the value of $g(5)$?
   A) $6$  B) $2$  C) $27$  D) $66$

3. Let $f(x)=3x-2$ and $g(x)=f(x)+k$, where $k$ is a constant. If $g(g(0))=8$, what is the value of $k$?
   A) $-4$  B) $10$  C) $2$  D) $4$

4. Let $f(x)=2x+3$ and $g(x)=f(x)-f(x-1)$. What is $g(x)$?
   A) $2x+3$  B) $-2$  C) $2$  D) $2x+1$

5. A function $f$ satisfies $f(x+2)=f(x)+4$ for all values of $x$. If $f(0)=1$, what is the value of $f(6)$?
   A) $9$  B) $17$  C) $13$  D) $25$

6. The function $f$ is defined by the table: $f(1)=4$, $f(2)=1$, $f(3)=3$, $f(4)=2$. The function $g$ is defined by $g(x)=2x-1$. For what value of $x$ is $g(f(x))=5$?
   A) $2$  B) $4$  C) $1$  D) $3$

7. Let $f(x)=x^2-6x+5$ and $g(x)=f(-x)$. For what value of $x$ is $g(x)=f(x)$?
   A) $1$  B) $-1$  C) $0$  D) $5$

8. Let $f(x)=ax+3$ and $g(x)=2x-5$, where $a$ is a constant. If $f(g(x))=g(f(x))$ for all values of $x$, what is the value of $a$?
   A) $-\dfrac{2}{5}$  B) $\dfrac{2}{5}$  C) $\dfrac{5}{2}$  D) $2$

9. The point $(2,5)$ lies on the graph of $y=f(x)$. The graph of $y=g(x)$ is obtained by translating the graph of $y=f(x)$ $3$ units to the left and $4$ units down. Which point must lie on the graph of $y=g(x)$?
   A) $(-1,1)$  B) $(5,1)$  C) $(-1,9)$  D) $(5,9)$

10. Let $f(x)=2x-3$ and $g(x)=x^2$. What are all values of $x$ for which $g(f(x))=25$?
   A) $x=4$ only  B) $x=4$ and $x=-1$  C) $x=-1$ only  D) $x=14$ and $x=-11$

11. Let $f(x)=x^2-6x+5$ and $g(x)=f(x+2)+1$. What is $g(1)$?
   A) $-3$  B) $-4$  C) $1$  D) $13$

12. Let $f(x)=x^2+1$ and $g(x)=3x-2$. What are all values of $x$ for which $f(g(x))=f(x)$?
   A) $x=1$ only  B) $x=\tfrac{1}{2}$ only  C) $x=1$ and $x=\tfrac{1}{2}$  D) $x=-1$ and $x=\tfrac{1}{2}$

13. Let $f$ be a function with $f(3)=5$. Let $g(x)=f(x)+4$ and $h(x)=g(x-3)$. What is the value of $h(6)$?
   A) $1$  B) $9$  C) $5$  D) $13$

14. Let $f(x)=x-4$ and $g(x)=x^2-6$. How many integers $x$ with $-3\le x\le 3$ satisfy $f(g(x))\le 0$?
   A) $2$  B) $7$  C) $4$  D) $5$

15. Let $f(x)=\dfrac{x}{2}+1$ and $g(x)=x^2-8$. For which values of $x$ is $f(g(x))=-1$?
   A) $x=\pm2$  B) $x=2$ only  C) $x=-2$ only  D) $x=\pm\sqrt{7}$

**A note on sourcing:** real, official College Board SAT questions are
copyrighted and are **not** licensed for reproduction in commercial test-prep
materials, under any circumstances, with or without attribution. No
verbatim College Board question appears in this book. The items above were
checked against the *method* and *distractor style* of real SAT Suite Question
Bank items in the *Nonlinear functions* category (substitution, composition
in both orders, and the sign-direction trap in horizontal shifts). The
numbers, names, and contexts are all original, and every answer was verified
by a sympy script.

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

**Set 8 — Easy:** 1) A  2) B  3) C  4) D  5) B  6) A  7) D  8) C  9) D  10) C  11) C  12) A  13) A  14) B  15) B

**Set 8 — Medium:** 1) A  2) A  3) C  4) C  5) C  6) B  7) B  8) D  9) C  10) A  11) D  12) B  13) B  14) A  15) D

**Set 8 — Hard:** 1) D  2) A  3) D  4) C  5) C  6) D  7) C  8) B  9) A  10) B  11) A  12) C  13) B  14) B  15) A
