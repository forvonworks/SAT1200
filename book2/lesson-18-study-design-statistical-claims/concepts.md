# Book 2 — Lesson 18: Study Design & Statistical Claims

**Source content file**, paired with `problems.md`. Last lesson of the Problem-Solving &
Data Analysis domain, and the last lesson of that domain's three-lesson statistics arc
(Lesson 15 Statistics Fundamentals → Lesson 16 Data Representations → Lesson 17
Probability Fundamentals → this lesson). Builds directly on vocabulary already taught —
**sample**, **population**, **mean** (Lesson 15), and the basic language of chance
(Lesson 17) — but introduces genuinely new content, not a computation extension.

**Research grounding:** `research/05-uzbek-student-considerations.md` names this topic
explicitly as the **single largest structural curriculum gap** for Uzbek SAT-takers:
Uzbekistan's exam specification weights "Statistika va ehtimollik" at only 7.5% of items,
probability/statistics was never part of the classical Soviet curricular tradition, and
*interpreting/critiquing study design* in particular has **no analogue at all** in the
local curriculum as documented. This lesson is written assuming **zero prior exposure** —
not a refresher, a first introduction. `research/04-common-student-mistakes.md` confirms
the exact failure pattern to build the lesson around: treating correlation shown in a
study as causation while ignoring lurking variables, and — more generally, across every
topic in that document — **stopping at a plausible-sounding conclusion instead of
checking whether the study design actually supports it.**

This lesson has almost no numbers in it. The skill is reasoning about a study's
*design*, not calculating a value from its data — that is the entire point, and nothing
here should be forced into a numeric answer just to look consistent with other lessons.

---

## Concept 1 — Random Sample vs. Convenience Sample: What Can You Generalize?

### Definition

*Populyatsiyaning har bir a'zosi tanlanish uchun bir xil imkoniyatga ega bo'lgan usul
bilan tuzilgan tanlanma — **tasodifiy tanlanma** (random sample) deb ataladi.*

<small>(A sample formed by a method in which every member of the population has an
equal chance of being selected is called a random sample.)</small>

*Aksincha, tanlanma faqat oson yetib boriladigan yoki o'z-o'zini tanlagan a'zolardan
tuzilsa — masalan, faqat bitta ma'lum joyda, ma'lum vaqtda topilgan odamlar so'ralsa —
bu **qulay tanlanma** (convenience sample) deb ataladi.*

<small>(If a sample is made up only of members who happened to be easy to reach, or who
chose to participate themselves, it is called a convenience sample.)</small>

**The one rule this concept exists to teach:** a conclusion from a sample can be safely
**generalized to the whole population** only when the sample was drawn **randomly**
from that population. A convenience sample can only tell you about the people actually
in it — not about anyone else, no matter how large it is.

**Why "large" doesn't fix it:** a bigger convenience sample is still biased in whatever
way made it convenient. 10,000 responses from a magazine's own readers still describe
only that magazine's readers, not "adults in general" — size changes precision, not
representativeness. This exact confusion (assuming sample size compensates for lack of
randomness) is a documented trap in SAT-style statistics questions.

### Model Example (1-misol)

A city has 60,000 registered voters. The city council wants to know what fraction of
*all* registered voters support building a new park, and considers two methods:

**(A)** A computer randomly selects 500 names from the complete list of all 60,000
registered voters, and all 500 are surveyed.

**(B)** A city employee stands outside the council's downtown office for one afternoon
and surveys the first 500 people who walk by.

**Qaysi usul natijani butun populyatsiyaga — barcha 60,000 ro'yxatdagi saylovchiga —
tatbiq etishga imkon beradi?**

**Yechish:** Usul (A) — har bir saylovchi ro'yxatdan tanlanish uchun bir xil imkoniyatga
ega, demak bu tasodifiy tanlanma. Natijani ehtiyotkorlik bilan butun 60,000 saylovchiga
tatbiq etish mumkin (albatta, tanlanma xatosi chegarasida).

Usul (B) esa qulay tanlanma: faqat downtown ofis atrofida, bir kun davomida, o'z
vaqtida u yerda bo'lgan odamlar so'ralgan. Bu guruh butun shahar aholisini — masalan,
boshqa rayonlarda yashovchi, ish vaqtida downtown'ga bormaydigan odamlarni —
aks ettirmasligi mumkin. Natijani faqat *shu kuni downtown'da bo'lgan 500 kishiga*
tatbiq etish mumkin, butun saylovchilar populyatsiyasiga emas.

**Javob:** Faqat (A) — chunki u tasodifiy tanlanma.

### Your-Turn Example (O'zingiz bajaring)

A university has 12,000 students and wants to know the average number of hours *all*
students spend studying per week. A researcher either (C) randomly selects 300 student
ID numbers from the university's full enrollment database, or (D) surveys the first 300
students who enter the university library on a Monday morning.

Which method, if either, allows the result to be generalized to all 12,000 students,
and why? $\underline{\hspace{60mm}}$

### Common Mistake Box (conditional — documented error, include)

**Noto'g'ri yondashuv:** "Agar tanlanma juda katta bo'lsa (masalan, 5,000 kishi), u
albatta ishonchli va butun populyatsiyani vakillik qiladi — hajmi katta bo'lgani
uchun."

**To'g'ri qoida:** Tanlanma hajmi va tanlanmaning tasodifiyligi — ikki xil narsa.
Hajm — aniqlikni oshiradi (tasodifiy xatolik kamayadi); tasodifiylik — vakillikni
ta'minlaydi (kim so'ralgani adolatli tanlangan). Katta, ammo tasodifiy bo'lmagan
tanlanma (masalan, bitta ijtimoiy tarmoq ilovasi orqali o'tkazilgan so'rovnoma, 50,000
javob bilan) hali ham faqat **shu ilovadan foydalanuvchilarni** aks ettiradi — qolgan
populyatsiyani emas, hajmi qancha katta bo'lishidan qat'iy nazar.

*(Research basis: documented as a specific SAT-style trap — large sample size is
mistaken for a guarantee of representativeness, when representativeness depends on
*how* the sample was chosen, not how big it is.)*

---

## Concept 2 — Experiment with Random Assignment vs. Observational Study: Causation or Correlation Only?

### Definition

*Tadqiqotchi qatnashchilarni tasodifiy ravishda turli guruhlarga — masalan, davolash
guruhi va nazorat guruhiga — taqsimlaydigan tadqiqot usuli **tasodifiy taqsimlashli
tajriba** (experiment with random assignment) deb ataladi.*

<small>(A study method in which the researcher randomly assigns participants to
different groups — e.g., a treatment group and a control group — is called an
experiment with random assignment.)</small>

*Agar tadqiqotchi guruhlarni o'zi belgilamasdan, faqat mavjud holatni kuzatib,
natijalarni yozib borsa — bu **kuzatuv tadqiqoti** (observational study) deb ataladi.*

<small>(If the researcher does not assign the groups, but only observes an existing
situation and records the results, this is called an observational study.)</small>

**The one rule this concept exists to teach:** random assignment is what lets you claim
a **causal relationship** ("X causes Y") — because randomly splitting participants into
groups spreads every other difference between people (age, habits, health, motivation,
anything) roughly evenly across both groups, so the treatment becomes the one
systematic difference left. An observational study, no matter how large or careful,
can only support a **correlation/association claim** ("X is associated with Y") —
never causation — because some unmeasured **lurking variable** could be driving both X
and Y at once.

**Nima SO'ralmoqda? — bu yerda bu savol "Bu tadqiqot sabab-oqibatni ISBOTLAY OLADImi?"
shaklida keladi.** Ko'rsatkichlar: "taqsimlandi," "guruhlarga bo'lindi," "davolash
berildi" so'zlari — tajribani bildiradi; "kuzatildi," "qayd etildi," "o'z-o'zidan
tanladi" so'zlari — kuzatuv tadqiqotini bildiradi.

### Model Example (2-misol)

A researcher wants to know whether a new studying app improves test scores. 200
students volunteer for the study. The researcher uses a random number generator to
assign 100 of them to use the app for a month and the other 100 to study as usual with
no app. At the end of the month, the app group's average score is significantly higher.

**Bu natijadan nima xulosa chiqarish mumkin?**

**Yechish:** Guruhlarga taqsimlash tasodifiy bajarilgan — demak, bu tajriba, kuzatuv
tadqiqoti emas. Tasodifiy taqsimlash ikki guruh o'rtasidagi boshqa barcha farqlarni
(masalan, boshlang'ich bilim darajasi, motivatsiya) o'rtacha tenglashtiradi, shuning
uchun qolgan yagona tizimli farq — ilovadan foydalanish. **Bu ilova test
natijalarining yaxshilanishiga sabab bo'lgan deb aytish mumkin** (shu 200 ishtirokchi
doirasida).

**Solishtirish uchun:** agar 200 talaba o'zlari ilovadan foydalanish-foydalanmaslikni
tanlagan bo'lsa (tasodifiy taqsimlash yo'q), natija bir xil bo'lsa ham, xulosa boshqa
bo'lardi: balki ko'proq motivatsiyalangan talabalar ilovani o'zlari tanlagan va ular
baribir yaxshi natija ko'rsatardi, ilovasiz ham. Bu holda faqat **bog'liqlik**
(association) haqida gapirish mumkin, sabab haqida emas.

**Javob:** Ilova sababli ekanligini aytish mumkin — chunki taqsimlash tasodifiy edi.

### Your-Turn Example (O'zingiz bajaring)

A health website tracks 5,000 of its readers over a year. It finds that readers who
report drinking green tea daily have, on average, lower blood pressure than readers who
don't. No groups were assigned by the researchers — this was simply recorded from
readers' own habits and survey responses.

Can the website correctly claim "drinking green tea daily causes lower blood pressure"?
Why or why not? $\underline{\hspace{60mm}}$

### Common Mistake Box (conditional — documented error, include)

**Noto'g'ri yondashuv:** "Ikki narsa birga o'zgarsa (bog'liqlik ko'rinsa), demak
birinchisi ikkinchisiga sabab bo'lган." (Treating any observed correlation as proof of
causation — the single most common statistical-reasoning error, confirmed across
multiple sources, including in scatterplot/line-of-best-fit contexts.)

**To'g'ri qoida:** Bog'liqlik (correlation) — ikki narsaning birga o'zgarishi. Sabab-
oqibat (causation) — birining ikkinchisini **keltirib chiqarishi**. Kuzatuv
tadqiqotida har doim **yashirin omil** (lurking variable) bo'lish ehtimoli bor — ikkala
narsani ham ta'sir qiluvchi, ammo o'lchanmagan uchinchi sabab. Masalan: yozda muzqaymoq
sotuvi ham, cho'milishda cho'kib ketish hodisalari ham oshadi — ammo muzqaymoq
cho'kishga sabab bo'lmaydi; yashirin omil — issiq ob-havo, ikkalasiga ham ta'sir
qiladi.

---

## Concept 3 — "Bu Tadqiqot Nimani ISBOTLAY OLADI?": Spotting an Overreaching Conclusion

### Definition

*Tadqiqot natijalariga asoslanib xulosa chiqarishdan oldin ikki mustaqil savolga javob
berish kerak: (1) tanlanma tasodifiy edimi — demak, xulosani **butun populyatsiyaga**
tatbiq etish mumkinmi; (2) guruhlarga taqsimlash tasodifiy edimi — demak, **sabab-
oqibat** bog'liqligini aytish mumkinmi. Bu ikki savolni birga qo'yish — "Bu tadqiqot
nimani ISBOTLAY OLADI?" tekshiruvi — deb ataladi.*

<small>(Before drawing a conclusion from a study's results, you must answer two
independent questions: was the sample random — so can the conclusion be generalized to
the whole population; and was group assignment random — so can a causal claim be made.
Putting these two questions together is called the "What can this study ACTUALLY
PROVE?" check.)</small>

**This is the named callout for this lesson** — Concepts 1 and 2 taught the two
questions separately; this concept teaches you to ask them **together**, because a
real study's design answers them independently of each other. The two questions give
four possible combinations:

| Tanlanma tasodifiy? | Taqsimlash tasodifiy? | Nimani aytish mumkin? |
|---|---|---|
| Ha | Ha | Butun populyatsiya uchun **sabab-oqibat** (to'liq tajriba, siyrak uchraydi) |
| Ha | Yo'q | Butun populyatsiya uchun faqat **bog'liqlik** (kuzatuv, tasodifiy tanlanmada) |
| Yo'q | Ha | Faqat **shu guruh** uchun sabab-oqibat, populyatsiyaga umumlashtirib bo'lmaydi |
| Yo'q | Yo'q | Hech narsani ishonchli umumlashtirish ham, sabab deyish ham mumkin emas |

**The row students miss most often is the third one:** many real experiments (like the
app study in Concept 2) use random *assignment* among a group of **volunteers**, not a
random *sample* of the whole population. Such a study can still support a causal claim
— but only for people like the volunteers, not for "everyone," because the volunteers
themselves weren't randomly selected from the full population.

### Model Example (3-misol)

A magazine invites its readers to try a new 30-day diet and report their weight
change; 80 readers volunteer. The magazine does not split them into groups — it simply
records that 65 of the 80 lost weight. The magazine's headline reads: **"New diet
causes weight loss in adults nationwide."**

**Bu sarlavhadagi xulosada nechta muammo bor va ular nima?**

**Yechish:** Ikkita alohida muammo bor.

Birinchidan — tanlanma: 80 kishi magazine o'quvchilaridan, o'zlari ixtiyoriy ravishda
qatnashgan (qulay/o'z-o'zini tanlagan tanlanma, tasodifiy emas). Shuning uchun natijani
"adults nationwide" (butun mamlakat kattalariga) umumlashtirib bo'lmaydi — faqat shu 80
ixtiyoriychiga tegishli bo'lishi mumkin.

Ikkinchidan — taqsimlash: hech qanday nazorat guruhi yo'q, taqsimlash yo'q — bu kuzatuv
tadqiqoti. Hatto 80 kishining ko'pchiligi vazn yo'qotgan bo'lsa ham, buning sababi
dietaning o'zi emasligi mumkin (masalan, diet sinovida qatnashgan odamlar odatda ovqat
yeyishga ko'proq e'tibor bera boshlaydi, dieta tafsilotlaridan qat'iy nazar). Demak
"causes" (sababli bo'ladi) so'zini ishlatish — isbotlanmagan.

**Javob:** Sarlavha ikki marta oshirib yuborilgan (overreach): (1) qulay tanlanmadan
butun mamlakatga umumlashtirilgan, (2) kuzatuvdan sabab-oqibat xulosasi chiqarilgan.
To'g'ri xulosa: "Of the 80 volunteers who tried the diet, most reported weight loss" —
hech qanday umumlashtirish yoki sabab da'vosi bo'lmagan holda.

### Your-Turn Example (O'zingiz bajaring)

A school district randomly selects 400 students from its full enrollment of 20,000 to
take a survey about screen time and sleep. It finds that students who report more than
4 hours of daily screen time also report less sleep, on average. No groups were
assigned — this was purely a survey. A local news report concludes: **"Reducing screen
time will cause district students to sleep more."**

Is this conclusion fully justified by the study's design? Identify exactly what the
study *can* support and what it cannot. $\underline{\hspace{60mm}}$

### Common Mistake Box (conditional — documented error, include)

**Noto'g'ri yondashuv:** "Tanlanma tasodifiy bo'lgani uchun, demak bu tadqiqot sabab-
oqibatni ham isbotlaydi." (Assuming a random *sample* automatically also means random
*assignment* — i.e., confusing the two separate questions in the table above.)

**To'g'ri qoida:** Tasodifiy tanlanma va tasodifiy taqsimlash — ikki butunlay mustaqil
savol. Tasodifiy tanlanma — kimlar so'ralgani haqida (generalizatsiya savoli).
Tasodifiy taqsimlash — ular qanday guruhlarga bo'lingani haqida (sabab-oqibat savoli).
Yuqoridagi jadvaldagi ikkinchi qator aynan shu xatoning namunasi: tanlanma tasodifiy
bo'lishi mumkin, ammo taqsimlash bo'lmasa, baribir faqat bog'liqlik haqida gapirish
mumkin.

---

## Vocabulary

| English | O'zbekcha |
|---|---|
| Random sample | Tasodifiy tanlanma |
| Convenience / self-selected sample | Qulay / o'z-o'zini tanlagan tanlanma |
| Population | Populyatsiya |
| Generalize | Umumlashtirish |
| Random assignment | Tasodifiy taqsimlash |
| Experiment | Tajriba |
| Observational study | Kuzatuv tadqiqoti |
| Treatment group / control group | Davolash guruhi / nazorat guruhi |
| Causation (cause-and-effect) | Sabab-oqibat bog'liqlik |
| Correlation / association | Bog'liqlik |
| Lurking / confounding variable | Yashirin omil |
| Overreaching conclusion | Oshirib yuborilgan xulosa |

---

## Notes for the problems file (Sets 1–6)

- Set 1: random sample vs. convenience sample only — what can be generalized.
- Set 2: experiment (random assignment) vs. observational study only — causation vs.
  correlation only.
- Set 3: mixed — both questions together, using the four-row table from Concept 3.
- Set 4: spot the overreach — given a flawed real-feeling conclusion, name exactly
  which of the two questions (sample randomness, assignment randomness) it violates.
- Set 5: write the correct conclusion yourself — given a study design, state in your
  own words exactly what it does and does not support (no multiple choice).
- Set 6: bonus/challenge — layered scenarios combining a sampling issue AND an
  assignment issue in the same study, or a trick where the design is actually sound and
  the "flaw" a careless reader might assume isn't really there.
