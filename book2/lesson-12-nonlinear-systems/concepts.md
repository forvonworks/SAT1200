# Book 2 — Lesson 12: Nonlinear Systems

**Source content file.** Last lesson of Book 2's Advanced Math domain. This is a
synthesis lesson — it teaches no new mechanical skill, only how to combine two
things already mastered: substitution (Book 2 Lesson 2) and solving quadratics
(Lessons 5-7, including the discriminant-as-solution-count idea from Lesson 7).
Don't re-derive substitution or the quadratic formula here — just apply them.

**Research grounding:** `research/01-official-sat-math-spec.md` (nonlinear
systems confirmed as official Advanced Math scope). Common-error research
(web search, tutoring-guide consensus, not an official College Board source):
the two most-cited mistakes are (1) finding only one of two solution pairs from
a line-parabola intersection, and (2) solving the quadratic for $x$ and
stopping there, forgetting to back-substitute for the matching $y$.

---

## Concept 1 — Chiziqli-Kvadrat Sistemalar (Linear-Quadratic Systems)

### Definition

*Bittasi chiziqli, ikkinchisi kvadrat ifodadan iborat bo'lgan ikki noma'lumli
tenglamalar to'plami chiziqli-kvadrat sistema deb ataladi. Bunday sistemani
yechish uchun chiziqli tenglamadagi $y$ ni kvadrat tenglamaga qo'yib, bitta
noma'lumli kvadrat tenglama hosil qilinadi.*

<small>(A system where one equation is linear and one is quadratic is a
linear-quadratic system. Solve it by substituting the linear expression for
$y$ into the quadratic equation, producing a single-variable quadratic.)</small>

**Doim ikkita javobni tekshiring:** parabola bilan to'g'ri chiziq odatda
**ikki** nuqtada kesishadi. Kvadrat tenglama ikkita ildizga ega bo'lsa, har
ikkala $x$ qiymati uchun ham mos $y$ ni topish shart — faqat bitta javob
bilan to'xtash eng ko'p uchraydigan xato.

### Model Example (1-misol)

$$y = x+1 \qquad y = x^2-1$$

**Yechish:** Ikkala ifodani tenglashtiramiz: $x+1 = x^2-1$. Hammasini bir
tomonga o'tkazamiz: $x^2-x-2=0$. Ko'paytuvchilarga ajratamiz:
$(x-2)(x+1)=0$, demak $x=2$ yoki $x=-1$. **Ikkala qiymat uchun ham** $y$ ni
topamiz (chiziqli tenglamaga qo'yib): $x=2$ bo'lsa $y=2+1=3$; $x=-1$ bo'lsa
$y=-1+1=0$.

**Javob:** $(2,3)$ va $(-1,0)$ — ikkita yechim juftligi.

### Your-Turn Example (O'zingiz bajaring)

$$y = x+2 \qquad y = x^2 \qquad \Rightarrow \qquad (x,y) = \underline{\hspace{25mm}} \text{ va } \underline{\hspace{25mm}}$$

### Common Mistake Box

**Noto'g'ri:** kvadrat tenglamani yechib, faqat bitta $x$ qiymatini (yoki
faqat $x$ qiymatlarini, $y$ siz) javob deb hisoblash.

**To'g'ri:** har bir $x$ uchun mos $y$ ni toping va javobni $(x,y)$ juft
shaklida yozing — agar kvadrat tenglama ikkita haqiqiy ildizga ega bo'lsa,
sistema odatda ikkita yechimga ega bo'ladi.

---

## Concept 2 — Yechimlar Soni va Grafik (Number of Solutions ↔ the Graph)

### Definition

*Chiziqli-kvadrat sistemani yechishda hosil bo'lgan kvadrat tenglamaning
diskriminanti ($D=b^2-4ac$) sistemaning geometrik ma'nosini — to'g'ri chiziq
parabolani necha nuqtada kesishini — aniqlaydi: $D>0$ bo'lsa ikki nuqta
(ikki yechim), $D=0$ bo'lsa bitta nuqta (chiziq parabolaga urinma), $D<0$
bo'lsa kesishish yo'q (haqiqiy yechim yo'q).*

<small>(The discriminant of the resulting single-variable quadratic tells you
how many times the line crosses the parabola: two points, one tangent point,
or none — exactly the same discriminant logic from Lesson 7, just applied
after substitution.)</small>

### Model Example (2-misol)

$$y = 4x-4 \qquad y = x^2$$

**Yechish:** $4x-4=x^2 \Rightarrow x^2-4x+4=0 \Rightarrow (x-2)^2=0$.
Diskriminant: $D=(-4)^2-4(1)(4)=0$. Bitta (qo'sh) ildiz: $x=2$, $y=4$.

**Javob:** Chiziq parabolaga $(2,4)$ nuqtada **urinadi** — bitta yechim,
ikkita emas ($D=0$ bo'lgani uchun).

### Your-Turn Example (O'zingiz bajaring)

$$y = x \qquad y = x^2+5$$

Diskriminantni hisoblang va sistema nechta haqiqiy yechimga ega ekanini
ayting: $\underline{\hspace{25mm}}$

---

## Concept 3 — Kvadrat-Kvadrat Sistemalar (Quadratic-Quadratic Systems)

### Definition

*Ikkala tenglamasi ham bir xil yetakchi koeffitsientga ega kvadrat
ifodalardan iborat sistema kvadrat-kvadrat sistema deb ataladi. Bunday
sistemani yechish uchun ikkala tenglama bir-biridan ayiriladi — natijada
$x^2$ hadi qisqaradi va chiziqli tenglama hosil bo'ladi.*

<small>(When both equations are quadratics with the same leading
coefficient, subtracting one from the other cancels the $x^2$ term,
leaving a simple linear equation.)</small>

### Model Example (3-misol)

$$y = x^2+3x+2 \qquad y = x^2-x+10$$

**Yechish:** Ikkala o'ng tomonni tenglashtiramiz: $x^2+3x+2 = x^2-x+10$.
$x^2$ hadlari qisqaradi: $3x+2 = -x+10$. Hadlarni yig'amiz: $4x=8$, demak
$x=2$. Istalgan tenglamaga qo'yamiz: $y=4+6+2=12$.

**Javob:** $(2, 12)$

*(E'tibor bering: yetakchi koeffitsientlar teng bo'lgani uchun natija
chiziqli tenglama bo'ldi — demak odatda faqat bitta kesishish nuqtasi
bo'ladi, parabolalar orasidagi bu xususiy holatda.)*

### Your-Turn Example (O'zingiz bajaring)

$$y = x^2+6x+1 \qquad y = x^2-2x+9 \qquad \Rightarrow \qquad (x,y) = \underline{\hspace{25mm}}$$

### Vocabulary

| English | O'zbekcha |
|---|---|
| Nonlinear system | Nochiziqli sistema |
| Linear-quadratic system | Chiziqli-kvadrat sistema |
| Quadratic-quadratic system | Kvadrat-kvadrat sistema |
| Substitution | O'rniga qo'yish |
| Solution pair | Yechim jufti |
| Tangent (touches at one point) | Urinma |
| Intersection point | Kesishish nuqtasi |
| Discriminant | Diskriminant |

## Notes for the problems file (Sets 1–7)

1. Linear-quadratic drill — clean two-solution pairs, simple factoring.
2. Linear-quadratic, harder coefficients — still two clean solution pairs,
   including a horizontal-line case and an $x=0$ solution (don't drop it).
3. No-real-solution cases — discriminant negative, identify and explain.
4. Quadratic-quadratic — same leading coefficient, subtract to eliminate $x^2$.
5. "What's actually being asked" — sum/product/difference of coordinates,
   not the raw pairs.
6. Spot the error — targets dropped second solution, missing back-substitution,
   a sign/combination error, and misreading a negative discriminant.
7. Bonus/challenge — includes a fraction-coefficient case and the tangent
   (double-root) case.
