# Book 3 — Lesson 4: Speed Techniques — Problem Sets

**Source content file**, paired with `concepts.md`. Several items are timed on purpose —
the point of this lesson is recognizing when a shortcut applies, not just knowing it
exists. All answers verified by a `sympy`/`fractions.Fraction` script, not hand-computed.
Set 7 Item 1 is an original problem built in the same structural pattern as a real College
Board Hard-tagged question (see `concepts.md` Model Example 3's source), with fresh numbers.

---

## Set 1 — Vieta's Formulas: Pure Drill

For each equation, find what's asked **without solving for the individual roots**.

1. $x^2-7x+12=0$. Find the sum and the product of the roots.
2. $2x^2+5x-3=0$. Find the sum and the product of the roots.
3. $x^2+9x+20=0$. Find only the sum of the roots.
4. $3x^2-10x+3=0$. Find only the product of the roots.
5. $x^2-kx+15=0$ has roots whose sum is $8$. Find $k$.
6. $x^2+6x+c=0$ has roots whose product is $-16$. Find $c$.

## Set 2 — Vieta's Applied to Systems (timed: under 30 seconds each after reaching the quadratic)

Each system has two solutions $(x_1,y_1)$ and $(x_2,y_2)$. Find what's asked **without**
finding each solution point individually.

1. $y=x^2-6x+5$, $y=2x-7$. Find $x_1+x_2$ and $y_1+y_2$.
2. $y=x^2+4x-1$, $y=-3x+5$. Find $x_1+x_2$ and $y_1+y_2$. *(The individual roots are
   irrational — Vieta's still gives a clean answer.)*
3. $y=2x^2-3x-5$, $y=x+1$. Find $x_1+x_2$ and $y_1+y_2$.
4. $y=x^2-2x-15$, $y=4x-3$. Find $x_1+x_2$ and $y_1+y_2$. *(Irrational roots again — same
   lesson: the shortcut doesn't care.)*
5. $y=x^2+x-6$, $y=-2x+6$. Find $x_1+x_2$ and $y_1+y_2$.

## Set 3 — The Repeated-Root Shortcut (timed: under 20 seconds, no quadratic formula allowed)

Each equation/system has **exactly one solution**. Find $x$ directly via $-b/(2a)$ —
do not compute any unknown constant first unless the question asks for it.

1. $y=x^2-10x+k$, $y=0$. Find $x$.
2. $y=2x^2+8x+k$, $y=0$. Find $x$.
3. $y=x^2-12x+k$, $y=0$. Find $x$.
4. $y=x^2-9x+k$, $y=2x-5$. Find $x$.
5. $y=3x^2-24x+k$, $y=0$. Find $x$.

## Set 4 — Factoring-Pattern Recognition

For each, name which reference-table pattern applies, then factor.

1. $x^2+10x+25$
2. $x^2-14x+49$
3. $x^2-81$
4. $4x^2-9$
5. $x^3+8$
6. $x^3-27$
7. $x^3+2x^2+3x+6$ *(grouping)*
8. $2x^3-6x^2+5x-15$ *(grouping)*

## Set 5 — Mixed: Choose the Fastest Technique

Not every item here has a shortcut — part of the skill is recognizing when the full
method is genuinely required.

1. $x^2+12x+c=0$ has roots whose product is $-28$. Find $c$. *(Vieta's)*
2. $x^2-5x-14=0$. Find **both** roots individually. *(No shortcut applies — the question
   asks for the roots themselves, not a sum/product; solve fully.)*
3. $9x^2-25$. Factor. *(Pattern recognition)*
4. $y=5x^2-20x+k$, $y=0$, exactly one solution. Find $x$. *(Repeated-root shortcut)*
5. $y=x^2-3x-10$, $y=5x+2$. Find $y_1+y_2$. *(Vieta's applied to a system)*

## Set 6 — Spot the Error

Each item shows a technically-not-wrong but **time-wasting** solution, or a genuine
factoring error. Name what's wrong (or what's slow), and give the fast/correct path.

1. $x^2-9x+14=0$ has roots whose sum is asked. *Shown solution:* "Faktorlab:
   $(x-7)(x-2)=0$, $x=7$ yoki $x=2$, demak yig'indi $7+2=9$." *(Not wrong — but
   name the faster path.)*
2. $y=4x^2-16x+k$, $y=0$, exactly one solution; find $x$. *Shown solution:* "Avval $k$ ni
   diskriminant orqali topamiz, keyin to'liq kvadrat formulaga qo'yamiz..." *(Not wrong —
   but name the faster path and give the direct answer.)*
3. Factor $x^2+16$. *Shown solution:* "$(x+4)(x-4)$ — kvadratlar ayirmasi." *(Genuine
   error: name it and give the correct factoring — or explain why it can't be factored
   over the reals.)*
4. $y=x^2-8x+15$, $y=0$. *Shown solution:* "Ikkala ildizni alohida toping: $x=3$ va $x=5$,
   so'ngra ularning yig'indisini hisoblang: $3+5=8$." *(Not wrong if individual roots
   are also needed for a later part — but if only the sum was asked, name the faster path.)*
5. $2x^2+5x-3=0$. Find the product of the roots. *Shown solution:* "Ko'paytma $= c/a =
   -3$." *(Genuine error: name exactly which value was used incorrectly, and give the
   correct product.)*

## Set 7 — Bonus / Challenge

1. The expression $6x^4+25x^2+14$ can be rewritten as $(3x^2+a)(2x^2+b)$, where $a$ and
   $b$ are positive integers, or as $(3x^2+c)(2x^2+d)$, where $c$ and $d$ are positive
   non-integers. What is the value of $a+c$? *(Same structure as a real official Hard
   question — solved via grouping, same technique as Set 4 Items 7–8, applied to find
   unknown coefficients instead of a numeric variable.)*
2. $y=x^2-7x-18$, $y=3x+2$. Find $y_1+y_2$ without finding the individual solution points.
3. $y=4x^2-20x+k$, $y=0$, exactly one solution. Find $k$ as well as $x$ (this one *does*
   need both — notice why Set 3's shortcut alone isn't enough here).

---

## Answer Key

**Set 1:** 1) sum $7$, product $12$  2) sum $-\frac{5}{2}$, product $-\frac{3}{2}$
3) sum $-9$  4) product $1$  5) $k=8$  6) $c=-16$

**Set 2:**
1) $x_1+x_2=8$, $y_1+y_2=2$
2) $x_1+x_2=-7$, $y_1+y_2=31$
3) $x_1+x_2=2$, $y_1+y_2=4$
4) $x_1+x_2=6$, $y_1+y_2=18$
5) $x_1+x_2=-3$, $y_1+y_2=18$

**Set 3:** 1) $x=5$  2) $x=-2$  3) $x=6$  4) $x=\frac{11}{2}$  5) $x=4$

**Set 4:**
1) To'liq kvadrat yig'indisi: $(x+5)^2$
2) To'liq kvadrat ayirmasi: $(x-7)^2$
3) Kvadratlar ayirmasi: $(x-9)(x+9)$
4) Kvadratlar ayirmasi: $(2x-3)(2x+3)$
5) Kublar yig'indisi: $(x+2)(x^2-2x+4)$
6) Kublar ayirmasi: $(x-3)(x^2+3x+9)$
7) Guruhlash: $(x+2)(x^2+3)$
8) Guruhlash: $(x-3)(2x^2+5)$

**Set 5:** 1) $c=-28$  2) $x=-2$ va $x=7$  3) $(3x-5)(3x+5)$  4) $x=2$  5) $y_1+y_2=44$

**Set 6:**
1. To'g'ri javob ($9$), lekin sekin — Viet teoremasi bilan $x_1+x_2=-(-9)/1=9$ to'g'ridan-to'g'ri, faktorlash shart emas.
2. To'g'ri yo'nalish, lekin sekin — takroriy ildiz yorlig'i: $x=-(-16)/(2\cdot4)=2$, $k$ ni hisoblash shart emas.
3. Xato — $x^2+16$ kvadratlar ayirmasi EMAS (yig'indi, ayirma emas); haqiqiy sonlar ustida faktorlanmaydi. To'g'ri misol: $x^2-16=(x+4)(x-4)$.
4. To'g'ri javob, lekin agar savol faqat yig'indini so'rasa — Viet teoremasi bilan $x_1+x_2=-(-8)/1=8$ to'g'ridan-to'g'ri, ildizlarni alohida topish shart emas.
5. Xato — ko'paytma $c/a$ formulasida $a=2$ ni hisobga olmagan: to'g'ri ko'paytma $=\frac{-3}{2}$, $-3$ emas.

**Set 7:** 1) $a+c=\frac{25}{2}$ (ya'ni $12.5$)  2) $y_1+y_2=34$  3) $k=25$, $x=\frac{5}{2}$
