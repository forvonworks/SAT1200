# Book 2 — Lesson 2: Systems of Linear Equations — Problem Sets

**Source content file**, paired with `concepts.md`. All answers verified by a
Python (`sympy.solve`) script before finalizing — not hand-computed.

---

## Set 1 — Substitution Drill

Solve each system for $(x,y)$:

1. $y=x+3$, $\quad 2x+y=18$
2. $y=2x$, $\quad x+y=15$
3. $y=3x-4$, $\quad x+y=12$
4. $x=y+5$, $\quad 2y+x=17$
5. $y=-x+10$, $\quad 3x-y=2$
6. $y=4x-3$, $\quad 2x+y=21$

## Set 2 — Elimination Drill (some require multiplying first)

1. $x+y=9$, $\quad x-y=3$
2. $2x+y=13$, $\quad x-y=2$
3. $3x+2y=17$, $\quad x-2y=-5$
4. $2x+3y=13$, $\quad 4x-y=5$
5. $5x+2y=19$, $\quad 3x-2y=5$
6. $x+3y=14$, $\quad 2x+y=13$

## Set 3 — Mixed (choose the smarter method)

1. $y=3x-5$, $\quad 2x+3y=18$
2. $4x-y=10$, $\quad 2x+y=14$
3. $x+y=20$, $\quad x-y=-6$
4. $3x+y=7$, $\quad y=x-5$
5. $2x+5y=22$, $\quad x-y=4$
6. $6x-2y=24$, $\quad 3x+y=18$

## Set 4 — Special Cases

Classify each system as **one solution** (and solve it), **no solution**, or
**infinitely many solutions**:

1. $3x+6y=12$, $\quad x+2y=4$
2. $x+2y=5$, $\quad 2x+4y=9$
3. $x-3y=1$, $\quad 2x-6y=2$
4. $5x+y=10$, $\quad x-y=2$

Find the value of $k$:

5. For what value of $k$ does $2x+ky=6$ and $4x+8y=20$ have **no solution**?
6. For what value of $k$ does $x+3y=6$ and $2x+ky=12$ have **infinitely many
   solutions**?

## Set 5 — What's Actually Being Asked

Solve each system, then answer the specific quantity asked — not just $x$
or $y$ alone:

1. $x+y=14$, $x-y=4$ — find $xy$.
2. $2x+y=11$, $x-y=1$ — find $x+y$.
3. $x+2y=16$, $x-y=1$ — find $2x-y$.
4. $3x+y=19$, $x+y=9$ — find $x-y$.
5. $x+y=13$, $2x-y=8$ — find $x^2-y^2$.

## Set 6 — Spot the Error

Each item has exactly one broken step. Name the error and give the correct
answer.

1. $x+y=8$, $x-y=2$ — *"Qo'shib: $2x = 8-2=6$, demak $x=3$, $y=5$."*
2. $2x+y=7$, $y=3x-8$ — *"$2x+3x-8=7$, demak $5x=7$, $x=\frac{7}{5}$."*
3. $4x+2y=8$, $2x+y=5$ — *"Ikkala tenglama ham bitta chiziqni ifodalaydi,
   shuning uchun cheksiz ko'p yechim bor."*
4. $3x-y=5$, $x+y=11$ — *"Qo'shib: $4x=16$, $x=4$; so'ng $y=11+4=15$."*

## Set 7 — Bonus / Challenge

1. $2x+3y=7$, $\quad 5x-2y=8$
2. Ikki sonning yig'indisi $24$, ayirmasi $8$ ga teng. Bu ikki son nechaga teng?
3. For what value of $k$ does $3x+ky=10$ and $x+2y=3$ have **no solution**?
4. $4x+3y=25$, $\quad 2x-y=5$

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
1. Error — $8-2$ ishlatilgan, $8+2$ o'rniga (qo'shish paytida ayirish
   ishlatilgan). To'g'ri: $2x=10$, $x=5$, $y=3$.
2. Error — $-8$ hadi tenglamaning o'ng tomoniga ko'chirilmagan (faqat hadlar
   qo'shilgan, $-8$ hisobga olinmagan). To'g'ri: $5x-8=7$, $5x=15$, $x=3$,
   $y=1$.
3. Error — konstantalar tekshirilmagan. Koeffitsientlar nisbati teng
   ($4/2=2$, $2/1=2$), lekin konstanta nisbati mos kelmaydi ($8$ vs
   $2\times5=10$) — demak bu **yechimsiz** tizim, cheksiz ko'p yechim emas.
4. Error — $y=11-4$ o'rniga $y=11+4$ hisoblangan (ishora xatosi). To'g'ri:
   $y=11-4=7$, javob $(4,7)$.

**Set 7:** 1) $(2,1)$  2) Sonlar: $16$ va $8$  3) $k=6$  4) $(4,3)$
