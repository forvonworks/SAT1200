# Book 3 — Lesson 3: No-Real-Solution Quadratics & Discriminant Edge Cases — Problem Sets

**Source content file**, paired with `concepts.md`. Mixes problems adapted from real
official College Board Hard-tagged SAT questions (rendered and read via the vision
pipeline in `research/15-question-bank-analysis.md`) with originally-written problems
at matching difficulty — not distinguished in the text, per house style. All answers
verified by a Python/`sympy` script before writing, not hand-computed.

---

## Set 1 — Classify by Discriminant (No Solving)

Har bir tenglama uchun, **to'liq yechmasdan**, nechta haqiqiy yechimi borligini ayting.

1. $x^2+5x+7=0$
2. $x^2-4x+4=0$
3. $2x^2+3x-5=0$
4. $-4x^2+8x-5=0$
5. $9x^2-6x+1=0$
6. $3x^2+5x+1=0$

## Set 2 — Systems Reduced to a Quadratic

Har bir tizim nechta kesishish nuqtasiga ega ekanini aniqlang. Agar aynan bitta yoki
ikkita bo'lsa, nuqta(lar)ning $x$-koordinatasini ham toping.

1. $y=x^2-6x+13$, $\quad y=4x-11$
2. $y=-x^2+4x+1$, $\quad y=2x-3$ *(faqat nechta ekanini ayting, aniq qiymatlarni emas)*
3. $y=x^2+2x+5$, $\quad y=-3$
4. $y=2x^2-4x+7$, $\quad y=x+3$
5. $y=x^2-8x+16$, $\quad y=0$
6. $y=3x^2-x+2$, $\quad y=-2x^2+5x-10$ *(faqat nechta ekanini ayting)*

## Set 3 — Discriminant Backward: Exactly One Solution ($D=0$)

1. $x^2+bx+49=0$ aynan bitta yechimga ega, $b>0$. $b=?$
2. $4x^2-20x+c=0$ aynan bitta yechimga ega. $c=?$
3. $y=-2$, $\quad y=x^2+6x+a$ — tizim aynan bitta yechimga ega. $a=?$
4. $kx^2-12x+9=0$ aynan bitta yechimga ega ($k\ne0$). $k=?$
5. $y=x^2-8x+c$, $\quad y=2x-1$ — tizim aynan bitta yechimga ega. $c=?$
6. $y=12$, $\quad y=-3x^2+bx$ — tizim aynan bitta yechimga ega, $b>0$. $b=?$

## Set 4 — Discriminant Backward: No/More-Than-One Solution (Inequalities)

1. $y=-5$, $\quad y=x^2+10x+k$ — tizim hech qanday haqiqiy yechimga ega emas, $k$ —
   musbat butun son. $k$ ning **eng kichik** mumkin bo'lgan qiymati?
2. $25x^2+bx+16=0$ tenglamasi birdan ortiq (ya'ni ikkita) haqiqiy yechimga ega
   bo'lishi uchun $b$ qanday qiymatlarni qabul qilishi kerak?
3. $y=7$, $\quad y=-2x^2+mx+1$ — tizim hech qanday haqiqiy yechimga ega emas, $m$ —
   musbat butun son. $m$ ning **eng katta** mumkin bo'lgan qiymati?
4. $x^2+px+100=0$ tenglamasi ikkita farqli haqiqiy yechimga ega bo'lishi uchun $p$
   qanday qiymatlarni qabul qilishi kerak?
5. $-3x^2+20x+c=0$ tenglamasi hech qanday haqiqiy yechimga ega emas, $c$ — butun son.
   $c$ ning **eng katta** mumkin bo'lgan qiymati?
6. $y=4$, $\quad y=x^2-14x+k$ — tizim ikkita farqli yechimga ega bo'lishi uchun $k$
   qanday qiymatlarni qabul qilishi kerak?

## Set 5 — Disguised Quadratics (hardest tier — fewer items)

1. $\sqrt{k-x}=40-x$ tenglamasi aynan bitta haqiqiy yechimga ega. $4k$ ning eng
   kichik mumkin bo'lgan qiymatini toping. *(`concepts.md` Your-Turn bilan bir xil —
   javobni shu yerda qayd eting.)*
2. $\dfrac{x}{x-3}=x-1$ tenglamasi nechta haqiqiy yechimga ega? ($x\ne3$ ekanini
   unutmang — tekshiring.)
3. To'p balandligi $h=-16t^2+64t+c$ formulasi bilan modellanadi ($t$ — soniyalarda,
   $h$ — futlarda). To'pning trayektoriyasi $h=80$ chizig'ini **aynan bitta** vaqt
   momentida kesib o'tadi. $c$ ning qiymatini toping.

## Set 6 — Mixed (Two Techniques Combined)

1. $y=x^2-4x+c$, $\quad y=2x-9$ — tizim aynan bitta yechimga ega. Avval $c$ ni, so'ngra
   kesishish nuqtasining $x$-koordinatasini toping.
2. $x^2+kx+36=0$ tenglamasi ikkita farqli haqiqiy yechimga ega, va ikkala yechim ham
   **manfiy**. $k$ ning mumkin bo'lgan bitta butun qiymatini ko'rsating va
   tasdiqlang (ildizlar yig'indisi $-k$ ekanini eslang — bu Lesson 4'da chuqurroq
   o'rganiladi).
3. $y=-2$, $\quad y=ax^2+8x-10$ ($a\ne0$, $a<0$) — tizim aynan bitta yechimga ega.
   $a$ ning qiymatini toping.
4. $3x^2-2x+7=5x^2-2x+c$ tenglamasini soddalashtiring, so'ngra $c$ ning qaysi
   qiymatida bu tenglama aynan bitta haqiqiy yechimga ega bo'lishini toping.

## Set 7 — Spot the Error

Har bir item aynan bitta xato qadamni ko'rsatadi. Xatoni nomlang va to'g'ri javobni
toping.

1. $b^2>1600$ tengsizligini yechishda — *"Ildiz chiqaramiz: $b>40$. Javob: $b>40$."*
2. $\sqrt{x-5}=x-7$ tenglamasini yechishda — kvadratga ko'tarilgach $x^2-15x+54=0$
   hosil bo'ladi, undan $x=6$ va $x=9$ chiqadi. *"Javob: ikkala yechim ham to'g'ri,
   $x=6$ va $x=9$."* (Ikkala yechimni ham original tenglamaga qo'yib tekshiring.)
3. $y=10-x^2$ va $y=3x+c$ tizimini tenglashtirishda — *"$10-x^2=3x+c$ dan
   $-x^2-3x+10+c=0$ hosil bo'ladi."* (Ishorani diqqat bilan tekshiring.)
4. $y=0$, $\quad y=2x^2+bx+18$ tizimi aynan bitta yechimga ega ekanligi berilgan —
   *"$D=b^2-4(2)(18)=0$ dan $b^2=144$, demak $b=12$."* (Faqat bitta tarmoq olingan.)
5. Raketa balandligi $h=-5t^2+20t+k$ bilan modellangan, va savol "raketa $h=200$
   futga **hech qachon** yetmaydi" shartidan $k$ ning oralig'ini so'ramoqda —
   *"Diskriminantni $D=0$ ga tenglab, $k$ ning aniq bitta qiymatini topdim."*
   (Bu yerda "hech qachon yetmaydi" — $D<0$ tengsizligi, $D=0$ emas.)

## Set 8 — Bonus / Challenge (two unmodified real SAT Hard questions + a proof item)

1. $2x^2-4x=t$ tenglamasida $t$ — doimiy son. Agar tenglama hech qanday haqiqiy
   yechimga ega bo'lmasa, quyidagilardan qaysi biri $t$ ning qiymati bo'lishi
   mumkin? A) $-3$  B) $-1$  C) $1$  D) $3$ *(Real SAT Hard, ID `7bd10ef3`.)*
2. Quyidagi kvadrat tenglamalardan qaysi biri hech qanday haqiqiy yechimga ega emas?
   A) $x^2+14x-49=0$  B) $x^2-14x+49=0$  C) $5x^2-14x-49=0$  D) $5x^2-14x+49=0$
   *(Real SAT Hard, ID `74473be4`.)*
3. **Isbotlang:** $y=x^2+4x+13$ va $y=-x^2-4x-3$ tizimlari hech qachon kesishmaydi
   (diskriminant orqali asoslang).
4. $64x^2+bx+25=0$ tenglamasi birdan ortiq haqiqiy yechimga ega bo'lishi uchun,
   quyidagi qiymatlardan qaysi biri $b$ bo'lishi mumkin? A) $-91$  B) $-80$  C) $5$
   D) $40$ *(Real SAT Hard, ID `6011a3f8`.)*

---

## Answer Key

**Set 1:** 1) 0 ta  2) 1 ta  3) 2 ta  4) 0 ta  5) 1 ta  6) 2 ta

**Set 2:**
1. 2 ta nuqta, $x=4$ va $x=6$
2. 2 ta (aniq qiymat talab qilinmagan)
3. 0 ta
4. 0 ta
5. 1 ta nuqta, $x=4$
6. 0 ta

**Set 3:** 1) $b=14$  2) $c=25$  3) $a=7$  4) $k=4$  5) $c=24$  6) $b=12$

**Set 4:**
1. $k=21$
2. $b<-40$ yoki $b>40$
3. $m=6$
4. $p<-20$ yoki $p>20$
5. $c=-34$
6. $k<53$

**Set 5:**
1. $4k=159$
2. 2 ta ($x=\dfrac{5\pm\sqrt{13}}{2}$, ikkalasi ham $3$ ga teng emas — begona yechim yo'q)
3. $c=16$

**Set 6:**
1. $c=0$, kesishish nuqtasi $x=3$
2. Masalan $k=13$: ildizlar $x=-9$ va $x=-4$ — ikkalasi ham manfiy ✓ ($k>12$
   bo'lgan istalgan butun son to'g'ri bo'lardi)
3. $a=-2$
4. Soddalashtirilgan tenglama: $-2x^2+(7-c)=0$; $c=7$ (bitta yechim $x=0$)

**Set 7:**
1. Xato — faqat $b>\sqrt{1600}$ tarmog'i olingan, $b<-\sqrt{1600}$ unutilgan. To'g'ri:
   $b<-40$ yoki $b>40$.
2. Xato — begona yechimni tekshirmagan. $x=6$: $\sqrt{1}=1$ va $6-7=-1$ — teng emas,
   begona. $x=9$: $\sqrt4=2$ va $9-7=2$ — teng, to'g'ri. Javob: faqat $x=9$.
3. Xato — qavsni $-x^2-3x-10-c=0$ ko'rinishida ochish kerak edi (o'ng tomonning
   **barcha** hadlari ishorasini o'zgartirib ko'chiriladi), $+10+c$ emas. To'g'ri:
   $-x^2-3x+(10-c)=0$ (yoki $x^2+3x+(c-10)=0$).
4. Xato — $b^2=144$ dan faqat $b=12$ olingan, $b=-12$ unutilgan. To'g'ri: $b=12$
   yoki $b=-12$.
5. Xato — "hech qachon yetmaydi" talab $D<0$ tengsizligini beradi, bu $k$ ning butun
   bir **oralig'ini** beradi, $D=0$ orqali topilgan bitta son emas.

**Set 8:**
1. A) $-3$
2. D) $5x^2-14x+49=0$
3. Birlashtirib: $2x^2+8x+16=0$, $D=64-128=-64<0$ — haqiqiy kesishish nuqtasi yo'q,
   isbotlandi.
4. A) $-91$
