# Book 3 — Lesson 6: Data-Analysis Edge Cases — Problem Sets

**Source content file**, paired with `concepts.md`. Mixes problems adapted directly from
real official College Board Hard-tagged questions (numbers recovered via the vision-render
pipeline in `research/15-question-bank-analysis.md`) with originally-written problems at
matching difficulty — not distinguished in the text. All answers verified by Python script
(`fractions.Fraction` for exact arithmetic), not hand-computed.

---

## Set 1 — Grouped-Data Min/Max Mean

To'plam $A$ ($25$ ta butun son) va to'plam $B$ ($25$ ta butun son) quyidagicha
guruhlangan:

| To'plam $A$ | Chastota | | To'plam $B$ | Chastota |
|---|---|---|---|---|
| $[50,60)$ | $5$ | | $[40,50)$ | $5$ |
| $[60,70)$ | $8$ | | $[50,60)$ | $8$ |
| $[70,80)$ | $12$ | | $[60,70)$ | $12$ |

1. $A$ to'plamining eng kichik mumkin bo'lgan arifmetik o'rtachasini toping.
2. $B$ to'plamining eng katta mumkin bo'lgan arifmetik o'rtachasini toping.
3. $A$ va $B$ o'rtachalari orasidagi **eng kichik** mumkin bo'lgan farqni toping.
4. $A$ va $B$ o'rtachalari orasidagi **eng katta** mumkin bo'lgan farqni toping.

## Set 2 — Qiymat Qo'shilganda O'rtacha va Mediana

1. Ma'lumotlar to'plami: $3,3,3,3,5,7,7,7,7$. Bu to'plamga $50$ qo'shilsa: eski mediana,
   yangi mediana, eski arifmetik o'rta, yangi arifmetik o'rtani toping. Mediana
   o'zgardimi?
2. Ma'lumotlar to'plami: $1,1,4,4,4,4,9,9,9,9$. Bu to'plamga $4$ qo'shilsa: eski mediana,
   yangi mediana, eski arifmetik o'rta, yangi arifmetik o'rtani toping. Bu safar
   arifmetik o'rta ortdimi yoki kamaydimi? Nega?
3. **(Mulohaza/Reasoning)** Agar biror to'plamga, aynan o'sha to'plamning joriy arifmetik
   o'rtasiga teng bo'lgan qiymat qo'shilsa, yangi arifmetik o'rta eskisidan farqlanadimi?
   Javobingizni asoslang (hisoblashsiz, faqat formuladan mulohaza yuritib).
4. **(Mulohaza/Reasoning)** $9$ ta qiymatdan iborat to'plamga, to'plamning joriy eng katta
   qiymatiga teng bo'lgan yana bir qiymat qo'shilsa (ya'ni eng katta qiymat takrorlansa),
   mediana albatta o'zgaradimi? Ikkala holat uchun (qiymatlar soni toqdan juftga
   o'tganda) misol bilan ko'rsating.

## Set 3 — Ko'p Mezonli Shartli Ehtimollik

1. Universitet talabalari: Birinchi kurs $22\%$, Ikkinchi kurs $28\%$, Uchinchi kurs
   $24\%$, To'rtinchi kurs $26\%$. $P(\text{to'rtinchi kurs}\mid\text{birinchi kurs
   emas})=?$
2. Bir muassasada: Bo'lim A — $40$ nafar o'tgan, $10$ nafar o'tmagan ($50$ kishi);
   Bo'lim B — $0$ o'tgan, $30$ o'tmagan ($30$ kishi); Bo'lim C — $15$ o'tgan, $5$
   o'tmagan ($20$ kishi). $P(\text{o'tgan}\mid\text{Bo'lim B emas})=?$
3. Mahsulot o'lchamlari: Kichik $30\%$, O'rta $25\%$, Katta $20\%$, Juda katta $25\%$.
   $P(\text{juda katta}\mid\text{kichik emas})=?$
4. $100$ ta tugma $3$ guruh va diametr bo'yicha taqsimlangan:

   | Guruh | $<20$ mm | $20$–$30$ mm | $>30$ mm |
   |---|---|---|---|
   | $1$ | $15$ | $10$ | $5$ |
   | $2$ | $0$ | $20$ | $20$ |
   | $3$ | $12$ | $18$ | $0$ |

   Tasodifan tanlangan tugma $2$-guruhda emasligi sharti bilan, uning diametri $30$ mm
   yoki undan kichik bo'lish ehtimoli $=?$

## Set 4 — Ikki O'zgaruvchili Ma'lumotni Masshtablashtirish

1. $M$ to'plami uchun eng mos chiziq $y=12+1.5x$. $N$ to'plami $M$ ning har bir $y$
   qiymatini $3.9$ ga ko'paytirish orqali hosil qilingan. $N$ uchun eng mos chiziq $=?$
2. $G$ to'plami uchun eng mos chiziq $y=5+2x$. $H$ to'plami $G$ ning har bir $y$ qiymatini
   $2.5$ ga ko'paytirish orqali hosil qilingan. $H$ uchun eng mos chiziq $=?$
3. $J$ to'plami uchun eng mos chiziq $y=8+3x$. $K$ to'plami $J$ ning har bir $y$ qiymatini
   $0.5$ ga ko'paytirish orqali hosil qilingan. $K$ uchun eng mos chiziq $=?$
4. $L$ to'plami uchun eng mos chiziq $y=20+4x$. $M'$ to'plami $L$ ning har bir $y$
   qiymatini $1.25$ ga ko'paytirish orqali hosil qilingan. $M'$ uchun eng mos chiziq $=?$

## Set 5 — Vakillik Namunasidan Populyatsiyani Baholash

1. $X$ shtatida, $26$ nafar o'quvchidan iborat vakillik sinfida $34.6\%$ i kamida $2$ ta
   aka-uka/opa-singilga ega. Shtatda shunga o'xshash $1{,}800$ ta sinf bor. Shtat
   bo'yicha **ikkitadan kam**ga ega o'quvchilar sonini baholang.
2. $25$ nafardan iborat vakillik sinfida $28\%$ i uy hayvoniga ega. Shaharda $2{,}200$ ta
   shunga o'xshash sinf bor. Shahar bo'yicha uy hayvoniga **ega bo'lmagan** o'quvchilar
   sonini baholang.
3. $40$ kishidan iborat vakillik namunasida $25\%$ i velosiped bilan ishga qatnaydi.
   Shaharda $1{,}500$ ta shunga o'xshash guruh bor. Velosiped bilan qatnama**ydigan**lar
   sonini baholang.
4. $24$ kishidan iborat vakillik namunasida $37.5\%$ i masofaviy ishlaydi. $900$ ta
   shunga o'xshash guruh bor. Masofaviy ishlaydiganlar sonini baholang.

## Set 6 — Mixed (2+ Skills Combined)

1. $500$ kishilik guruhda $40\%$ i $Y$ toifasiga kiradi. $Y$ ga kirmaydiganlar orasida
   $30\%$ i $Z$ xususiyatiga ega. $Y$ ga kirmaydiganlar sonini, so'ngra ular orasida $Z$
   ga ega bo'lganlar sonini toping.
2. Set 3 — item 1dagi universitet $2{,}500$ nafar talabaga ega. (a) $P(\text{to'rtinchi
   kurs}\mid\text{birinchi kurs emas})$ ni toping (Set 3dan). (b) Butun $2{,}500$ talaba
   orasida nechta to'rtinchi kurs talabasi bor?

## Set 7 — Spot the Error (Real CB Wrong-Answer Traps)

Har bir item real test materialidagi haqiqiy noto'g'ri javob mantig'ini aks ettiradi.
Xatoni nomlang va to'g'ri javobni toping.

1. **Masala:** Set 1dagi $A$ va $B$ to'plamlari. Ularning o'rtachalari orasidagi eng
   kichik mumkin bo'lgan farqni toping. *Noto'g'ri yechim:* "Ikkala to'plamning range'i
   (eng katta $-$ eng kichik) teng bo'lishi mumkin, demak eng kichik farq $=0$."
2. **Masala:** Concept 2dagi bug' favvorasi misoli ($13$ ta otilish, $11$ qo'shiladi).
   *Noto'g'ri yechim:* "Qo'shilgan qiymat ($11$) juda katta bo'lgani uchun, ham mediana,
   ham arifmetik o'rta albatta ortadi."
3. **Masala:** Concept 3dagi xona sig'imi misoli. *Noto'g'ri yechim:* "$P(65\text{ dan
   katta})=24\%$ — bu to'g'ridan-to'g'ri jadvaldan olingan javob."
4. **Masala:** Concept 5dagi janob Kemp misoli ($34.6\%$, $26$ kishi, $1{,}800$ sinf).
   *Noto'g'ri yechim:* "$34.6\%$ ozchilik bo'lgani uchun, qolgan taxminan yarmi
   ($50\%$) kamroqqa ega: $0.5\times26\times1{,}800=23{,}400$."
5. **Masala:** Concept 4dagi chiziq masshtablash misoli ($y=12+1.5x$, $\times3.9$).
   *Noto'g'ri yechim:* "$y=12+5.85x$ — faqat burchak koeffitsientini $3.9$ ga
   ko'paytirib, $y$-kesishmani o'zgarishsiz qoldirish kerak."

## Set 8 — Bonus / Mastery Check

1. To'plam $C$ ($30$ ta butun son): $[60,70)$ chastotasi $6$, $[70,80)$ chastotasi $10$,
   $[80,90)$ chastotasi $14$. Eng kichik mumkin bo'lgan arifmetik o'rtachani toping.
2. $50$ kishidan iborat vakillik namunasida $62\%$ i online xarid qiladi. $1{,}200$ ta
   shunga o'xshash guruh bor. Online xarid qiluvchilar sonini baholang.
3. Set 8 — item 1dagi to'plam $C$ ga yana bitta qiymat — eng yuqori oraliqning eng katta
   mumkin bo'lgan qiymati ($79$) — qo'shilsa ($31$ ta qiymatli yangi to'plam), yangi eng
   kichik mumkin bo'lgan arifmetik o'rtacha qanday o'zgaradi? Ortadimi yoki kamayadimi?

---

## Answer Key

**Set 1:** 1) $A$ eng kichik $=\dfrac{314}{5}=62.8$  2) $B$ eng katta $=\dfrac{309}{5}=61.8$
3) Eng kichik farq $=1$  4) Eng katta farq: $A$ eng katta $=\dfrac{359}{5}=71.8$, $B$ eng
kichik $=\dfrac{264}{5}=52.8$, farq $=19$

**Set 2:**
1) Eski mediana $=5$, yangi mediana $=6$ ($\dfrac{5+7}{2}$) — **o'zgardi**. Eski o'rtacha
$=5$, yangi o'rtacha $=\dfrac{95}{10}=9.5$.
2) Eski mediana $=\dfrac{4+4}{2}=4$, yangi mediana (n=11, $6$-qiymat) $=4$ —
   o'zgarmadi. Eski o'rtacha $=\dfrac{27}{5}=5.4$, yangi o'rtacha
   $=\dfrac{58}{11}\approx5.27$ — **kamaydi**, chunki qo'shilgan qiymat ($4$) joriy
   o'rtachadan ($5.4$) kichik edi.
3) O'zgarmaydi — chunki qo'shilgan qiymat joriy o'rtachaga teng bo'lsa, yangi yig'indi
   eski o'rtacha $\times$ (eski son$+1$) ga teng bo'ladi, bu esa yangi o'rtachani xuddi
   eskisiga teng qilib qo'yadi (formuladan to'g'ridan-to'g'ri kelib chiqadi).
4) Yo'q, albatta emas — qiymatlar soni toqdan ($9$) juftga ($10$) o'tganda, mediana endi
   ikkita o'rtadagi qiymatning o'rtachasi bo'ladi; agar eng katta qiymat takrorlansa, bu
   yangi juft son uchun o'rtadagi ikkita qiymat ko'pincha o'zgarmay qoladi (misol: eski
   to'plam $1,2,3,4,5,6,7,8,9$, mediana $5$; $9$ qo'shilsa, yangi mediana
   $=\dfrac{5+6}{2}=5.5$ — bu holda o'zgardi!). Demak javob holatga bog'liq, umumiy
   qoida yo'q — har safar qayta hisoblash kerak.

**Set 3:** 1) $\dfrac{26}{78}=\dfrac13$  2) $\dfrac{55}{70}=\dfrac{11}{14}$
3) $\dfrac{25}{70}=\dfrac{5}{14}$  4) $\dfrac{55}{60}=\dfrac{11}{12}$

**Set 4:** 1) $y=46.8+5.85x$  2) $y=12.5+5x$  3) $y=4+1.5x$  4) $y=25+5x$

**Set 5:** 1) $30{,}600$  2) $39{,}600$  3) $45{,}000$  4) $8{,}100$

**Set 6:** 1) $Y$ ga kirmaydiganlar $=300$; ular orasida $Z$ ga ega $=90$.
2) (a) $\dfrac13$ (Set 3dan)  (b) $0.26\times2{,}500=650$

**Set 7:**
1. Xato — o'rtacha o'rniga range (eng katta$-$eng kichik)ni solishtirgan; bular butunlay
   boshqa ko'rsatkichlar. To'g'ri: o'rtachalar orasidagi eng kichik farq $=1$ (Set 1,
   item 3).
2. Xato — qo'shilgan qiymat katta bo'lgani uchun ikkalasi ham albatta ortadi deb
   taxmin qilgan; mediana faqat tartiblangan o'rindagi joylashuvga bog'liq. To'g'ri:
   faqat arifmetik o'rta ortdi ($\frac{29}{13}\to\frac{20}{7}$), mediana $2$da qoldi.
3. Xato — shartni ("kamida $18$") maxrajga qo'shmasdan, to'g'ridan-to'g'ri jadvaldagi
   shartsiz foizni javob deb olgan. To'g'ri: maxrajni shartga mos uch toifaning
   yig'indisiga ($74\%$) cheklab, $\dfrac{24}{74}=\dfrac{12}{37}\approx0.324$.
4. Xato — qolgan ulushni $50\%$ deb taxmin qilgan, aslida $100\%-34.6\%=65.4\%$. To'g'ri:
   $26$ dan $34.6\%$ i $\approx9$ kishi (kamida $2$ ga ega), demak $17$ kishi
   (ikkitadan kam) har bir sinfda, $17\times1{,}800=30{,}600$ — $23{,}400$ emas.
5. Xato — faqat burchak koeffitsientini ko'paytirgan, $y$-kesishmani o'zgarishsiz
   qoldirgan. To'g'ri: ikkalasi ham $3.9$ ga ko'payadi: $y=46.8+5.85x$.

**Set 8:** 1) $\dfrac{218}{3}\approx72.67$  2) $0.62\times50\times1{,}200=37{,}200$
3) Yangi o'rtacha $=\dfrac{2259}{31}\approx72.87$ — **ortdi** (chunki qo'shilgan qiymat
$79$ eski o'rtacha $\approx72.67$dan katta edi).
