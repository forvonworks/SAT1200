
# ============================================================ SET 5  (Summit, 20)
mc(5, 'H',
   r"In right triangle $ABC$, the right angle is at $C$, and $\overline{CH}$ is the altitude to hypotenuse $\overline{AB}$ with $H$ on $\overline{AB}$. If $CH=12$, $AH=x$ and $HB=x+7$, what is the perimeter of triangle $ABC$?",
   C(60), [C(25), C(37), C(49)],
   lambda: (lambda xv: (xv + xv + 7) + sqrt(xv ** 2 + 144) + sqrt((xv + 7) ** 2 + 144))([v for v in solve(x * (x + 7) - 144, x) if v > 0][0]),
   "$CH^2=AH\\cdot HB$, then Pythagoras twice",
   r"$12^2=x(x+7)$ gives $x^2+7x-144=0$, so $x=9$ and $HB=16$, $AB=25$. Then $AC=\sqrt{9^2+12^2}=15$, $BC=\sqrt{16^2+12^2}=20$, and the perimeter is $15+20+25=60$. ($25$ is $AB$; $37=9+16+12$ adds the segments and altitude; $49=25+12+12$.)")

gi(5, 'H',
   r"In right triangle $ABC$, the right angle is at $C$. The area of the triangle is $6$, and $\tan A+\tan B=\dfrac{25}{12}$. What is the length of the hypotenuse?",
   "5", Integer(5),
   lambda: next(sqrt(a * a + b * b) for a in range(1, 13) for b in range(1, 13)
                if a * b == 12 and R(a, b) + R(b, a) == R(25, 12) and a < b),
   "$\\tan A+\\tan B=\\dfrac{a^2+b^2}{ab}=\\dfrac{c^2}{ab}$",
   r"With legs $a=BC$, $b=AC$: $\tan A+\tan B=\frac ab+\frac ba=\frac{a^2+b^2}{ab}=\frac{c^2}{ab}$. The area gives $ab=12$, so $c^2=\frac{25}{12}\cdot12=25$ and $c=5$.")

mc(5, 'H',
   r"In trapezoid $ABCD$, $\overline{AB}\parallel\overline{CD}$, $AB=8$ and $CD=12$. The diagonals meet at $E$, and the area of triangle $CDE$ is $90$. What is the area of triangle $ABE$?",
   C(40), [C(50), C(60), C(135)],
   lambda: 90 * R(8, 12) ** 2,
   "Triangles $ABE\\sim CDE$; areas scale by $k^2$",
   r"Triangle $ABE\sim CDE$ with $k=\frac8{12}=\frac23$, so the area is $90\cdot\frac49=40$. ($50=90-40$; $60$ uses $k$ instead of $k^2$; $135$ uses $\frac32$ instead of $\frac49$.)")

gi(5, 'H',
   r"Two sides of a triangle measure $7$ and $8$, and the third side has integer length $x$. For how many values of $x$ is the triangle obtuse?",
   "6", Integer(6),
   lambda: sum(1 for xv in range(2, 15) if max(7, 8, xv) ** 2 > (7 ** 2 + 8 ** 2 + xv ** 2) - max(7, 8, xv) ** 2),
   "Two ways to be obtuse: the new side is longest or shortest",
   r"The triangle inequality gives $x=2,\dots,14$. If $x$ is longest, it is obtuse when $x^2>7^2+8^2=113$, i.e. $x=11,12,13,14$. If $8$ is longest, it is obtuse when $8^2>7^2+x^2$, i.e. $x^2<15$, so $x=2,3$. Total $6$.")

mc(5, 'H',
   r"A circle is inscribed in a right triangle with legs $9$ and $12$, touching all three sides. What is the area of the circle?",
   C(r"9\pi", 9 * pi), [C(r"\dfrac{9\pi}{4}", R(9, 4) * pi), C(r"36\pi", 36 * pi), C(r"\dfrac{225\pi}{4}", R(225, 4) * pi)],
   lambda: pi * (R(1, 2) * 9 * 12 / (R(9 + 12 + 15, 2))) ** 2,
   "Inradius $r=\\dfrac{\\text{area}}{\\text{semiperimeter}}=\\dfrac{a+b-c}{2}$",
   r"The hypotenuse is $15$. $r=\frac{9+12-15}{2}=3$ (or $\frac{54}{18}$), so the area is $9\pi$. ($36\pi$ forgets the $\frac12$, $r=6$; $\frac{9\pi}4$ divides area by the whole perimeter, $r=1.5$; $\frac{225\pi}{4}$ is the circle through the three vertices.)")

mc(5, 'H',
   r"In the $xy$-plane, point $P$ lies on the line $y=\dfrac34x$ in the first quadrant, and $P$ is $20$ units from the origin. What is the sum of the coordinates of $P$?",
   C(28), [C(7), C(20), C(35)],
   lambda: (lambda xv: xv + R(3, 4) * xv)([v for v in solve(x ** 2 + (R(3, 4) * x) ** 2 - 400, x) if v > 0][0]),
   "Slope $\\frac34$ means a $3$-$4$-$5$ triangle",
   r"The slope $\frac34$ gives legs in the ratio $4:3$ and hypotenuse $5$; scaling $5\to20$ gives $P=(16,12)$, so $x+y=28$. ($35$ takes $x=20$, $y=15$; $20$ is the distance; $7=3+4$.)")

mc(5, 'H',
   r"Two vertical poles of heights $12$ m and $20$ m stand $15$ m apart on level ground. A cable runs from the top of each pole to the base of the other, and the cables cross at point $X$. How many meters above the ground is $X$?",
   C("7.5", R(15, 2)), [C(16), C(32), C(240)],
   lambda: (lambda xv: R(20, 15) * xv)(solve(Eq(R(20, 15) * x, 12 - R(12, 15) * x), x)[0]),
   "Crossing cables: height $=\\dfrac{ab}{a+b}$",
   r"Similar triangles give $\frac1h=\frac1{12}+\frac1{20}$, so $h=\frac{12\cdot20}{32}=7.5$ (the $15$ m spacing does not matter). ($16$ is the average of $12$ and $20$; $32$ is their sum; $240$ is their product.)",
   fig=lambda: figs.fig_cross(12, 20, 15), figdesc="Two vertical poles of heights 12 and 20, 15 apart; a cable from the top of each pole to the foot of the other crosses at X; drawn to scale.")

gi(5, 'H',
   r"The side lengths of a right triangle form an arithmetic sequence, and the area of the triangle is $54$. What is the perimeter of the triangle?",
   "36", Integer(36),
   lambda: next(3 * xx for dd in range(1, 30) for xx in range(2, 200)
                if (xx - dd) ** 2 + xx ** 2 == (xx + dd) ** 2 and R((xx - dd) * xx, 2) == 54),
   "Sides $x-d,\\ x,\\ x+d$ force a $3$-$4$-$5$ shape",
   r"Let the sides be $x-d,x,x+d$. Then $(x-d)^2+x^2=(x+d)^2$ gives $x=4d$, so the sides are $3d,4d,5d$. Area $=6d^2=54$, so $d=3$ and the perimeter is $12d=36$.")

mc(5, 'H',
   r"A regular hexagon $ABCDEF$ has side length $6$. Triangle $ACE$ is formed by joining alternate vertices. What is the area of triangle $ACE$?",
   C(r"27\sqrt3", 27 * S3_), [C(r"9\sqrt3", 9 * S3_), C(r"18\sqrt3", 18 * S3_), C(r"54\sqrt3", 54 * S3_)],
   lambda: tri_area(*[(6 * cos(j * pi / 3), 6 * sin(j * pi / 3)) for j in (0, 2, 4)]),
   "Hexagon = 6 equilateral triangles; $ACE$ uses half",
   r"Each side of $ACE$ is a short diagonal $6\sqrt3$, so the area is $\frac{\sqrt3}{4}(6\sqrt3)^2=27\sqrt3$. (Check: the hexagon is $6\cdot9\sqrt3=54\sqrt3$ and $ACE$ is half.) ($9\sqrt3$ is one small triangle; $18\sqrt3$ is two; $54\sqrt3$ is the whole hexagon.)",
   fig=lambda: figs.fig_hex(6), figdesc="Regular hexagon ABCDEF with side 6 and the triangle ACE shaded; drawn to scale.")

mc(5, 'H',
   r"In a regular decagon (a polygon with $10$ equal sides and equal angles) $ABCDEFGHIJ$, what is the measure of $\angle ACD$?",
   C(r"126^\circ", 126), [C(r"18^\circ", 18), C(r"144^\circ", 144), C(r"162^\circ", 162)],
   lambda: (lambda V: Integer(round(math.degrees(math.acos(
       ((V[0][0] - V[2][0]) * (V[3][0] - V[2][0]) + (V[0][1] - V[2][1]) * (V[3][1] - V[2][1])) /
       (math.dist(V[0], V[2]) * math.dist(V[3], V[2])))))))(
       [(math.cos(2 * math.pi * j / 10), math.sin(2 * math.pi * j / 10)) for j in range(10)]),
   "Interior angle $-$ base angle of isosceles $ABC$",
   r"Each interior angle is $\frac{8\cdot180}{10}=144$. Triangle $ABC$ is isosceles with apex $144$, so $\angle ACB=18$. Then $\angle ACD=\angle BCD-\angle ACB=144-18=126$. ($18$ is $\angle ACB$; $144$ is the whole interior angle; $162=180-18$.)")

gi(5, 'H',
   r"Rectangle $ABCD$ has $AB=12$ and $BC=16$. The perpendicular from $A$ to diagonal $\overline{BD}$ meets $\overline{BD}$ at $H$. What is the value of $DH-BH$?",
   "5.6", R(28, 5),
   lambda: (lambda A, B, Dd: (lambda H: dist(Dd, H) - dist(B, H))(
       (lambda t_: (B[0] + t_ * (Dd[0] - B[0]), B[1] + t_ * (Dd[1] - B[1])))(
           ((A[0] - B[0]) * (Dd[0] - B[0]) + (A[1] - B[1]) * (Dd[1] - B[1])) / ((Dd[0] - B[0]) ** 2 + (Dd[1] - B[1]) ** 2))))(
       (Integer(0), Integer(0)), (Integer(12), Integer(0)), (Integer(0), Integer(16))),
   "Legs squared over hypotenuse",
   r"In right triangle $ABD$ (right angle at $A$) the hypotenuse is $BD=20$. The altitude's feet divide it so that $BH=\frac{AB^2}{BD}=\frac{144}{20}=7.2$ and $DH=\frac{AD^2}{BD}=\frac{256}{20}=12.8$. Then $DH-BH=5.6$.")

mc(5, 'H',
   r"From the top of a vertical tower $30$ m tall, the angles of depression of two cars on the level road, in line with the base of the tower and on opposite sides of it, are $45^\circ$ and $30^\circ$. How far apart are the cars, in meters?",
   C(r"30+30\sqrt3", 30 + 30 * S3_), [C(r"30\sqrt3-30", 30 * S3_ - 30), C(r"30\sqrt3", 30 * S3_), C(60)],
   lambda: 30 / tan(pi / 4) + 30 / tan(pi / 6),
   "Angle of depression $=$ angle of elevation from the ground",
   r"Each car's distance from the base is $\frac{30}{\tan\theta}$: $30$ for $45^\circ$ and $30\sqrt3$ for $30^\circ$. On opposite sides they add: $30+30\sqrt3$. ($30\sqrt3-30$ is the answer for cars on the same side; $30\sqrt3$ counts one car; $60$ treats both as $45^\circ$.)")

mc(5, 'H',
   r"In parallelogram $ABCD$, $AB=14$, $AD=10$ and $\angle A=60^\circ$. What is the area of the parallelogram?",
   C(r"70\sqrt3", 70 * S3_), [C(140), C(70), C(r"35\sqrt3", 35 * S3_)],
   lambda: 14 * 10 * sin(pi / 3),
   "Height $=10\\sin60^\\circ$; area = base $\\times$ height",
   r"The height on base $AB$ is $10\sin60^\circ=5\sqrt3$, so the area is $14\cdot5\sqrt3=70\sqrt3$. ($140$ multiplies the sides, ignoring the angle; $70$ halves that; $35\sqrt3$ is the triangle $ABD$, half the parallelogram.)")

gi(5, 'H',
   r"An isosceles triangle has two sides of length $25$ and an area of $168$. What is the sum of all possible lengths of the third side?",
   "62", Integer(62),
   lambda: sum(2 * m for m in [v for v in solve(x ** 2 * (625 - x ** 2) - 168 ** 2, x) if v > 0]),
   "Two triangles fit: base angle acute or obtuse",
   r"Let the base be $2m$; the height is $\sqrt{625-m^2}$ and $m\sqrt{625-m^2}=168$. This gives $m^2=49$ or $m^2=576$, so $m=7$ or $24$ and the bases are $14$ and $48$ (heights $24$ and $7$). The sum is $62$.")

mc(5, 'H',
   r"In isosceles trapezoid $ABCD$, $\overline{AB}\parallel\overline{DC}$, $AB=10$, $DC=26$ and $AD=BC=10$. What is the area of the trapezoid?",
   C(108), [C(156), C(180), C(216)],
   lambda: R(1, 2) * (10 + 26) * sqrt(10 ** 2 - ((26 - 10) / 2) ** 2),
   "Drop perpendiculars: overhang $=\\frac{26-10}{2}$",
   r"Each overhang is $\frac{26-10}2=8$, so the height is $\sqrt{10^2-8^2}=6$ and the area is $\frac12(10+26)(6)=108$. ($180$ uses the slant $10$ as height; $216$ drops the $\frac12$; $156=26\cdot6$ uses only the long base.)",
   fig=lambda: figs.fig_trap(10, 26, 10), figdesc="Isosceles trapezoid ABCD with AB = 10 on top, DC = 26 on the bottom and legs AD = BC = 10; drawn to scale.")

mc(5, 'H',
   r"In right triangle $ABC$, the right angle is at $B$ and the legs are $AB=9$ and $BC=12$. Point $D$ is on $\overline{AB}$ and point $E$ is on $\overline{BC}$ with $\overline{DE}\parallel\overline{AC}$, and the area of triangle $DBE$ is one-fourth the area of triangle $ABC$. What is the length of $\overline{DE}$?",
   C("7.5", R(15, 2)), [C("3.75", R(15, 4)), C("11.25", R(45, 4)), C(30)],
   lambda: sqrt(9 ** 2 + 12 ** 2) * sqrt(R(1, 4)),
   "Area ratio $\\frac14$ means $k=\\frac12$",
   r"$AC=15$. Triangle $DBE\sim ABC$ with area ratio $\frac14$, so $k=\sqrt{\frac14}=\frac12$ and $DE=\frac12\cdot15=7.5$. ($3.75$ multiplies by $\frac14$; $11.25$ by $\frac34$; $30$ doubles instead of halving.)")

mc(5, 'H',
   r"Square $ABCD$ has side length $12$. Point $E$ is the midpoint of $\overline{AB}$ and point $F$ is the midpoint of $\overline{BC}$. What is the area of triangle $DEF$?",
   C(54), [C(36), C(72), C(90)],
   lambda: tri_area((0, 12), (6, 0), (12, 6)),
   "Composite by subtraction: square minus three corner triangles",
   r"The three corner triangles are $ADE=\frac12(12)(6)=36$, $EBF=\frac12(6)(6)=18$, $FCD=\frac12(6)(12)=36$, total $90$. So $DEF=144-90=54$. ($90$ is the corner total; $36$ is one corner triangle; $72$ is half the square.)")

mc(5, 'H',
   r"In the figure, triangle $ABC$ has a right angle at $C$ and $\tan B=\dfrac12$. Point $D$ is on $\overline{BC}$ with $BD=4$ and $DC=6$. What is $\tan\angle ADC$?",
   C(r"\dfrac56", R(5, 6)), [C(r"\dfrac12", R(1, 2)), C(r"\dfrac65", R(6, 5)), C(r"\dfrac54", R(5, 4))],
   lambda: (lambda ac: ac / 6)(10 * R(1, 2)),
   "Find the common leg first",
   r"$BC=4+6=10$ and $\tan B=\frac{AC}{BC}=\frac12$, so $AC=5$. In the right triangle $ADC$, $\tan\angle ADC=\frac{AC}{DC}=\frac56$. ($\frac12$ is $\tan B$; $\frac65$ is the reciprocal; $\frac54$ uses $BD$ instead of $DC$.)",
   fig=lambda: figs.fig_tanD(4, 6, 5), figdesc="Right triangle ABC with the right angle at C; D lies on BC with BD = 4 and DC = 6; segment AD drawn; drawn to scale (tan B = 1/2).")

gi(5, 'H',
   r"In the $xy$-plane, point $P$ lies on the $x$-axis and is equally distant from $A=(0,6)$ and $B=(8,2)$. What is the area of triangle $PAB$?",
   "20", Integer(20),
   lambda: tri_area((solve(x ** 2 + 36 - ((x - 8) ** 2 + 4), x)[0], 0), (0, 6), (8, 2)),
   "Equal distances give a linear equation",
   r"$PA=PB$ with $P=(x,0)$: $x^2+36=(x-8)^2+4$ gives $16x=32$, $x=2$. Area of $P(2,0),A(0,6),B(8,2)$: $\frac12|2(6-2)+0(2-0)+8(0-6)|=\frac12|8-48|=20$.")

mc(5, 'H',
   r"Which of the following lists of side lengths forms a right triangle?",
   T(r"$9,\ 40,\ 41$", (9, 40, 41)), [T(r"$8,\ 15,\ 16$", (8, 15, 16)), T(r"$12,\ 35,\ 36$", (12, 35, 36)), T(r"$20,\ 21,\ 28$", (20, 21, 28))],
   None,
   "Test $a^2+b^2=c^2$ on the longest side",
   r"$9^2+40^2=81+1600=1681=41^2$. The others miss: $8^2+15^2=289\ne256$; $12^2+35^2=1369=37^2\ne36^2$; $20^2+21^2=841=29^2\ne28^2$. (Each wrong list is one number away from a real triple.)",
   each=lambda tr: sum(v * v for v in sorted(tr)[:2]) == sorted(tr)[2] ** 2)
