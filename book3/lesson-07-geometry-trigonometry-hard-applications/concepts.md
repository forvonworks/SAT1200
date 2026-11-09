# Book 3 — Lesson 7: Geometry & Trigonometry — Hard Applications

**Source content file**, paired with `problems.md`. New lesson, added after the real official
College Board Question Bank was analyzed (`research/15-question-bank-analysis.md`): Geometry &
Trigonometry is only ~15% of the test but contributes **25% of all Hard-tagged questions** — the
single most disproportionately hard domain, ahead of Algebra. This lesson builds on Book 2
Lessons 19 (Lines, Angles & Triangles), 21 (Circles), and 22 (Right-Triangle Trigonometry) —
none of those rules are re-taught here.

**The finding that organizes this whole lesson:** reading real Hard-tagged G&T questions
directly from the official bank (6 analyzed in depth below, by Question ID, every number
real and unaltered) shows the same pattern every time. A Hard G&T question almost never
tests a rule you don't already know. It tests **two or three rules you already know, chained
together**, usually with an algebraic unknown slipped into the middle of the chain. The skill
this lesson actually teaches is not new geometry — it's *recognizing which two tools to
connect, and in which order.*

---

## Concept 1 — Chaining Angle Rules Across a Multi-Sided Figure

### Ta'rif (Definition)

*Ko'p burchakli shaklda (masalan, beshburchakda) bitta noma'lum burchakni topish uchun, ko'pincha
bitta qoida yetarli emas — parallel chiziqlar, uchburchak burchaklari yig'indisi va tashqi burchak
qoidasi kabi bir nechta munosabatni **ketma-ket zanjirlab** qo'llash kerak bo'ladi; bu usul
**burchaklar zanjiri** deb ataladi.*

<small>(In a multi-sided figure, finding one unknown angle often isn't a single rule away —
you chain several relationships in sequence: parallel-line rules, triangle angle sum, and the
exterior-angle rule, each feeding the next. This method is called an angle chain.)</small>

**Strategiya:** yordamchi chiziqlarni (extension) chizib, berilgan burchaklardan noma'lumgacha
bo'lgan "yo'lni" toping — har bir qadamda faqat bitta allaqachon bilgan qoidani qo'llang, lekin
oldingi qadamning natijasini keyingisiga kiritib boring.

### Model Example (1-misol) — real SAT Hard question (ID `f731d88b`)

Qavariq (convex) beshburchak $ABCDE$ berilgan, $\overline{AB} \parallel \overline{DE}$.
Burchak $B$ ning o'lchovi $139°$, burchak $D$ ning o'lchovi $174°$. Burchak $C$ ning
o'lchovini toping.

**Yechish:** To'g'ridan-to'g'ri qoida yo'q — yordamchi chiziq kerak. $BC$ ni $B$ dan,
$DE$ ni $D$ dan davom ettiramiz, ular $X$ nuqtada kesishsin (bu kesuvchi chiziq hosil
qiladi, $AB\parallel DE$ bo'lgani uchun).

**1-qadam (tashqi burchak, $B$ da):** $AB$ ni $B$ dan davom ettirsak, hosil bo'lgan tashqi
burchak $= 180° - 139° = 41°$.

**2-qadam (parallel chiziqlar, almashinuvchi ichki burchaklar):** $AB\parallel DE$ bo'lgani
uchun, shu $41°$ burchak va $\angle CXD$ — almashinuvchi ichki burchaklar, demak
$\angle CXD = 41°$.

**3-qadam (tashqi burchak, $D$ da):** Burchak $D$ ning tashqarisidagi burchak
$\angle CDX = 180° - 174° = 6°$.

**4-qadam (uchburchak $CDX$ dagi tashqi burchak qoidasi):** Beshburchakdagi burchak $C$ —
aslida uchburchak $CDX$ ning $C$ uchidagi **tashqi burchagi**, demak u ichki ikki burchakning
yig'indisiga teng: $\angle C = \angle CDX + \angle CXD = 6° + 41° = 47°$.

**Javob:** $\angle C = 47°$

*(To'rtta qadam, to'rtta turli qoida — tashqi burchak, parallel chiziqlar, yana tashqi burchak,
yana tashqi burchak qoidasi. Birortasini o'tkazib yuborsangiz, zanjir uziladi. Bu — Hard
darajadagi geometriya savollarining odatiy ko'rinishi: har bir alohida qoida oson, lekin
nechta qoida kerakligini va ularni qaysi tartibda bog'lashni ko'rish qiyin.)*

### Your-Turn Example (O'zingiz bajaring)

Qavariq oltiburchak $PQRSTU$ da $\overline{PQ}\parallel\overline{ST}$. Burchak $Q=152°$,
burchak $S=168°$. $PQ$ ni $Q$ dan, $ST$ ni $S$ dan davom ettirib hosil bo'lgan uchburchakdan
foydalanib, burchak $R$ ning o'lchovini toping (eslatma: bu yerda ham burchak $R$ — hosil
bo'lgan uchburchakning tashqi burchagi): $\angle R = \underline{\hspace{20mm}}$

### Common Mistake Box

**Noto'g'ri yondashuv:** ko'p burchakli shaklni ko'rib, darhol "burchaklar yig'indisi"
formulasini (masalan, beshburchak uchun $540°$) qo'llashga urinish — lekin faqat ikkita
burchak berilgan bo'lsa, bu formula yolg'iz yetarli emas, chunki qolgan uchta burchak
(shu jumladan noma'lum $C$) haqida alohida ma'lumot yo'q.

**To'g'ri qoida:** Agar parallel chiziqlar berilgan bo'lsa (yoki shart ichida yashiringan
bo'lsa), bu ko'pincha "yig'indi formulasi"dan ko'ra tezroq yo'l — yordamchi chiziq chizib,
kichik uchburchaklar orqali zanjirlang. Yig'indi formulasi faqat **barcha** boshqa burchaklar
ma'lum bo'lgandagina to'g'ridan-to'g'ri ishlaydi.

---

## Concept 2 — Trigonometriya + Algebra: O'zgaruvchi Orqali Berilgan Burchaklar

### Ta'rif (Definition)

*Bitta to'g'ri burchakli uchburchakda balandlik (altitude) tushirilganda, hosil bo'lgan ikkita
kichik uchburchak asl uchburchakka **o'xshash** bo'ladi; bu o'xshashlikdan kelib chiqadigan
burchaklar orasidagi munosabatni $a$ va $b$ kabi o'zgaruvchilar orqali ifodalab, ularni
tenglashtirish — **burchaklarni algebraik tenglashtirish** usuli deb ataladi.*

<small>(When an altitude is dropped inside a right triangle, the two smaller triangles formed
are similar to the original — and to each other. Expressing the resulting angle relationships
with variables like $a$ and $b$ and setting them equal is called equating angles algebraically.)</small>

### Model Example (2-misol) — real SAT Hard question (ID `98e02472`)

To'g'ri burchakli uchburchak $XYZ$ berilgan, to'g'ri burchak — $Y$ da (burchak $X$ va $Z$ —
o'tkir burchaklar). $R$ nuqta $\overline{XZ}$ kesmasida yotadi, shunday qilib $\overline{YR}$
$\overline{XZ}$ ga perpendikulyar. Burchak $XZY$ ning o'lchovi $a°$, burchak $XYR$ ning
o'lchovi $b°$, va $XY=19$. Agar $\sin a° = \dfrac{12}{13}$ bo'lsa, $\tan b°$ ning qiymatini
toping.

**Yechish:** Avval, $a$ va $b$ orasidagi bog'lanishni topamiz (bu — eng muhim qadam, $XY=19$
umuman kerak bo'lmaydi!). Burchak $Y = 90°$, va u ikki qismga bo'lingan: $\angle XYR=b°$ va
$\angle ZYR=(90-b)°$. Kichik uchburchak $ZRY$ da to'g'ri burchak $R$ da, demak
$\angle ZYR + \angle YZR = 90°$, ya'ni $(90-b) + a = 90$, bundan $a = b$.

Demak, $\sin a° = \sin b° = \dfrac{12}{13}$. Pifagor uchligidan ($12$-$5$-$13$),
qo'shni katet $=5$ (birlik ko'paytiruvchisi bilan). Demak:

$$\tan b° = \frac{12}{5} = 2.4$$

**Javob:** $\tan b° = \dfrac{12}{5}$ (yoki $2.4$)

*(Diqqat: savolda berilgan $XY=19$ soni — bu "chalg'ituvchi ma'lumot" (red herring) emas,
balki boshqa versiyadagi savolda kerak bo'lishi mumkin edi; bu yechimda esa $a=b$ ekanini
isbotlagach, unga ehtiyoj qolmaydi. Hard darajadagi savollarda berilgan **har bir** son
albatta kerak bo'ladi, degan taxmin — o'zi bir xato: ba'zan yechimning kaliti faqat burchaklar
orasidagi munosabatni topishda, raqamli qiymatlarda emas.)*

### Your-Turn Example (O'zingiz bajaring)

To'g'ri burchakli uchburchak $DEF$ da, to'g'ri burchak $E$ da. $G$ nuqta $\overline{DF}$ da
yotadi, $\overline{EG}\perp\overline{DF}$. Burchak $DFE = c°$, burchak $DEG = d°$. Agar
$\cos c° = \dfrac{8}{17}$ bo'lsa, $\sin d°$ ni toping (avval $c$ va $d$ orasidagi bog'lanishni
isbotlang): $\sin d° = \underline{\hspace{20mm}}$

### Common Mistake Box

**Noto'g'ri yondashuv:** $a$ va $b$ ni darhol teng deb hisoblash, isbotlamasdan — yoki
aksincha, ularni mutlaqo bog'liq emas deb, $XY=19$ dan boshlab to'g'ridan-to'g'ri hisoblashga
urinish (bu yo'l ancha uzoqroq va xato ehtimoli yuqoriroq).

**To'g'ri qoida:** Burchak yig'indisi tenglamasidan ($90+a+90-b=180$ turidagi) boshlang —
bu har doim ishlaydi va a=b kabi natijani **isbotlangan haqiqat** sifatida beradi, taxmin
sifatida emas.

---

## Concept 3 — Aylana + To'g'ri Burchakli Uchburchak: Tangens Chiziqlari

### Ta'rif (Definition)

*Aylanaga tashqi nuqtadan o'tkazilgan ikkita tangens chiziq, urinish nuqtalarigacha **teng
uzunlikka** ega bo'ladi, va har bir radius o'ziga mos tangens chiziqqa **perpendikulyar**
bo'ladi — bu ikki xususiyat birgalikda, markaz, urinish nuqtasi va tashqi nuqta orqali
**to'g'ri burchakli uchburchak** hosil qiladi, bu yerda Pifagor teoremasi qo'llaniladi.*

<small>(Two tangent lines from an external point to a circle are equal in length, and each
radius is perpendicular to its own tangent line — together these two facts form a right
triangle through the center, the point of tangency, and the external point, where the
Pythagorean theorem applies.)</small>

### Model Example (3-misol) — real SAT Hard question (ID `0acfddb5`)

Aylananing markazi $G$, nuqtalar $M$ va $N$ aylanada yotadi. $\overline{MH}$ va
$\overline{NH}$ kesmalari aylanaga mos ravishda $M$ va $N$ nuqtalarda tangens (urinma).
Aylana radiusi $168$ mm, to'rtburchak $GMHN$ ning perimetri $3{,}856$ mm. $G$ va $H$
nuqtalari orasidagi masofani toping.

**Yechish:**

**1-qadam (radiuslar):** $GM = GN = 168$ (ikkalasi ham radius).

**2-qadam (tangens kesmalari teng):** $MH = NH$. $MH = x$ deb belgilaymiz.

**3-qadam (perimetr tenglamasi):** $GM+MH+HN+NG = 3{,}856$, ya'ni
$168+x+x+168=3{,}856$, bundan $2x=3{,}520$, $x=1{,}760$.

**4-qadam (perpendikulyarlik → to'g'ri burchak):** Tangens radiusga perpendikulyar bo'lgani
uchun, $\angle GMH=90°$ — demak uchburchak $GMH$ to'g'ri burchakli, katetlar $168$ va
$1{,}760$, gipotenuza $GH$.

**5-qadam (Pifagor teoremasi):**
$$GH=\sqrt{168^2+1{,}760^2}=\sqrt{28{,}224+3{,}097{,}600}=\sqrt{3{,}125{,}824}=1{,}768$$

**Javob:** $GH = 1{,}768$ mm

*(Bu savol uchta alohida qoidani bitta zanjirga bog'laydi: tangens-radius perpendikulyarligi
→ tangens kesmalari tengligi → Pifagor teoremasi. Har biri Book 2'da alohida o'rganilgan,
lekin bu yerda birinchi marta uchtasi birga ishlatiladi.)*

### Your-Turn Example (O'zingiz bajaring)

Aylananing markazi $O$, radiusi $45$. Tashqi nuqta $P$ dan ikkita tangens chizilgan, urinish
nuqtalari $A$ va $B$. To'rtburchak $OAPB$ ning perimetri $570$. $OP$ masofasini toping:
$OP = \underline{\hspace{20mm}}$

### Common Mistake Box

**Noto'g'ri yondashuv:** $GH$ ni to'g'ridan-to'g'ri $MH$ yoki $GM+MH$ yig'indisi deb
hisoblash — ya'ni, $G$, $M$, $H$ nuqtalarini bitta to'g'ri chiziqda deb xato taxmin qilish.

**To'g'ri qoida:** $G$, $M$, $H$ — **to'g'ri burchakli uchburchakning uch uchi**, bir chiziqda
emas. $GH$ — gipotenuza, va uni topish uchun albatta Pifagor teoremasi kerak, oddiy qo'shish
emas.

---

## Concept 4 — Yuza/Hajmni Topishdan Oldin Yashirin O'lchamni Hisoblash

### Ta'rif (Definition)

*Ba'zi yuza yoki hajm masalalarida, kerakli formulaga to'g'ridan-to'g'ri qo'yish mumkin
bo'lgan o'lcham berilmaydi — avval shu o'lchamni **boshqa usul** bilan (koordinata
tekisligida to'rtburchakka joylashtirish, yoki jismning ichidagi to'g'ri burchakli
uchburchak orqali) hisoblab topish, so'ngra asosiy formulaga qo'yish kerak bo'ladi.*

<small>(Some area/volume problems don't hand you a dimension you can plug straight into a
formula — you first have to derive that dimension another way (fitting it into a bounding
rectangle on the coordinate plane, or via a right triangle hidden inside a solid), and only
then apply the main formula.)</small>

### Model Example 4a (4a-misol) — real SAT Hard question (ID `eb70d2d0`), coordinate plane

Koordinata tekisligida uchta nuqta berilgan: $(-3,4)$, $(5,3)$, va $(4,-3)$. Shu uch nuqtani
tutashtirib hosil bo'lgan uchburchakning yuzini toping.

**Yechish — tezkor usul (shoelace formula / "poyabzal ipi" formulasi):** Uchburchak tomonlari
koordinata o'qlariga parallel bo'lmagani uchun, oddiy $\frac{1}{2}bh$ ishlatib bo'lmaydi.
Nuqtalarni $(x_1,y_1), (x_2,y_2), (x_3,y_3)$ deb belgilab, quyidagi formulani qo'llaymiz:

$$\text{Yuza} = \frac{1}{2}\left|x_1(y_2-y_3)+x_2(y_3-y_1)+x_3(y_1-y_2)\right|$$

$(-3,4), (5,3), (4,-3)$ ni qo'yamiz:

$$\frac{1}{2}\left|(-3)(3-(-3))+5(-3-4)+4(4-3)\right| = \frac{1}{2}\left|(-3)(6)+5(-7)+4(1)\right|$$
$$=\frac{1}{2}\left|-18-35+4\right|=\frac{1}{2}\times49=24.5$$

**Javob:** $24.5$ kvadrat birlik

*(Rasmiy javob kaliti boshqa usulni — uchburchakni to'g'ri to'rtburchak ichiga joylab,
burchaklardagi uchta qo'shimcha uchburchakni ayirib tashlashni — ko'rsatadi; bu ham to'g'ri,
lekin uzunroq. Shoelace formulasi — har qanday uchta nuqta berilgan uchburchak uchun ishlaydigan
tezkor, ishonchli usul, va Hard darajadagi testda vaqtni tejaydi.)*

### Model Example 4b (4b-misol) — real SAT Hard question (ID `9fdc4eaa`), 3D solid

To'g'ri to'rtburchakli piramidaning to'liq yuzasi $70{,}560$ kvadrat dyuym, va piramidaning
to'rtta yon yuzining umumiy yuzasi $38{,}160$ kvadrat dyuym. Piramidaning balandligini toping.

**Yechish:**

**1-qadam (asos yuzi):** Asos yuzi $=70{,}560-38{,}160=32{,}400=s^2$, bundan $s=180$
(asosning tomoni).

**2-qadam (bitta yon yuz):** $38{,}160\div4=9{,}540$ — bu bitta uchburchak yon yuzning yuzi.

**3-qadam (yon qirra balandligi — slant height):** Yon yuz yuzasi formulasi
$A=\frac{1}{2}s\ell$ ($\ell$ — slant height). $9{,}540=\frac{1}{2}(180)\ell=90\ell$, bundan
$\ell=106$.

**4-qadam (piramida ichidagi yashirin to'g'ri burchakli uchburchak):** Piramidaning markaziy
o'qi, asosning yarim tomoni ($s/2=90$) va slant height ($\ell=106$) — uchtasi to'g'ri
burchakli uchburchak hosil qiladi, gipotenuza $=\ell$:

$$h^2+90^2=106^2 \implies h^2=11{,}236-8{,}100=3{,}136 \implies h=56$$

**Javob:** Balandlik $=56$ dyuym

*(Bu masalada asosiy qiyinchilik — formulani bilish emas, balki piramida ICHIDA yashiringan
to'g'ri burchakli uchburchakni "ko'rish": balandlik, yarim-asos va slant height doim shu
uchburchakni hosil qiladi, har qanday to'g'ri piramidada.)*

### Your-Turn Example (O'zingiz bajaring)

Koordinata tekisligida uchta nuqta: $(-2,5)$, $(6,2)$, $(1,-4)$. Shoelace formulasidan
foydalanib, shu nuqtalar hosil qiladigan uchburchakning yuzini toping:
Yuza $=\underline{\hspace{20mm}}$

### Common Mistake Box

**Noto'g'ri yondashuv:** piramida masalasida, slant height ($\ell=106$) ni balandlik ($h$)
bilan adashtirib, javob sifatida $106$ ni yozish — yoki koordinata masalasida, uchburchakning
"ko'rinadigan" asosi va balandligini taxminiy o'lchab, noto'g'ri $\frac{1}{2}bh$ qo'llash.

**To'g'ri qoida:** Slant height — piramidaning yon yuzi uchun, balandlik esa piramidaning
MARKAZIY o'qi bo'ylab — ikkalasi har doim piramida ichidagi to'g'ri burchakli uchburchak
orqali ($h^2+(s/2)^2=\ell^2$) bog'lanadi, hech qachon bir-biriga teng emas. Koordinatadagi
uchburchak uchun esa, tomonlar o'qlarga parallel bo'lmasa, shoelace formulasi (yoki
bounding-box usuli) — yagona ishonchli yo'l, "ko'z bilan o'lchash" emas.

---

## Vocabulary

| English | O'zbekcha |
|---|---|
| Angle chain | Burchaklar zanjiri |
| Exterior angle (of a triangle) | Tashqi burchak |
| Equating angles algebraically | Burchaklarni algebraik tenglashtirish |
| Tangent line (to a circle) | Tangens (urinma) chiziq |
| Point of tangency | Urinish nuqtasi |
| Shoelace formula | Shoelace formulasi (poyabzal ipi formulasi) |
| Slant height | Yon qirra balandligi (slant height) |
| Lateral face | Yon yuz |
| Bounding rectangle | Chegaralovchi to'rtburchak |

---

## Notes for the problems file (Sets 1–8)

Source questions used, by ID (real, numbers unaltered, Materials/SAT MATH.pdf):
`f731d88b` (p.1941), `98e02472` (p.1845), `0acfddb5` (p.1897), `eb70d2d0` (p.1959),
`9fdc4eaa` (p.1913) — all used as Model Examples above. Two more real Hard questions,
reserved for the problems file (not shown in concepts.md, to maximize distinct real coverage):
`2c3aefc9` (p.1672, rectangle diagonal + completing the square) and `694b7fce` (p.1980,
similar right triangles sharing an altitude). All other problems are original, written to
match the same combination-of-rules difficulty pattern, interspersed without marking which
is which.

1. Angle-chain drills (pentagon/hexagon with parallel sides) — original problems following
   the Model Example 1 pattern.
2. Trig + algebra (altitude-splits-a-right-angle setups) — original problems following Model
   Example 2's pattern.
3. Circles + tangent lines + Pythagorean theorem — original problems following Model
   Example 3's pattern.
4. Coordinate-plane area (shoelace formula practice) + the real `2c3aefc9` rectangle-diagonal
   problem.
5. 3D composite area/volume (hidden right triangle inside a solid) + the real `694b7fce`
   similar-triangles-sharing-an-altitude problem.
6. Mixed — each problem combines two of the four concepts above.
7. Spot the error — five items, each with exactly one broken step (slant-height/height
   confusion, tangent-segment misidentification, angle-chain skipped step, shoelace sign
   error, bounding-box arithmetic slip).
8. Bonus/Mastery — hardest items, timed, 3+ chained rules each.
