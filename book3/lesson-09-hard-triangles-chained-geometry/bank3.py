
# ============================================================ SET 3  (Hard, 14)
mc(3, 'H',
   r"In the figure, point $D$ lies on $\overline{AB}$ and point $E$ lies on $\overline{AC}$, with $\overline{DE}\parallel\overline{BC}$. If $AD=9$, $DB=6$ and $DE=12$, what is the length of $\overline{BC}$?",
   C(20), [C(8), C(18), C(30)],
   lambda: R(12) * (9 + 6) / 9,
   "Parallel line $\\Rightarrow$ similar triangles; use the whole side",
   r"Triangle $ADE\sim ABC$ with $\frac{AD}{AB}=\frac9{15}$, so $BC=12\cdot\frac{15}{9}=20$. ($8$ uses $DB$ in place of $AB$ in the numerator; $18=12+6$ adds; $30=12\cdot\frac{15}{6}$ uses $DB$ in the denominator.)",
   fig=lambda: figs.fig_parseg(9, 6, 12, 20, 17), figdesc="Triangle ABC with segment DE parallel to BC, D on AB (AD = 9, DB = 6), E on AC, DE = 12; drawn to scale.")

mc(3, 'H',
   r"In the figure, lines $m$ and $n$ are parallel and are cut by transversal $t$. What is the value of $x$?",
   C(18), [C("2.5", R(5, 2)), C(9), C(36)],
   lambda: solve((3 * x + 5) + (7 * x - 5) - 180, x)[0],
   "Same-side interior angles add to $180^\\circ$",
   r"The two marked angles lie between the lines on the same side of $t$, so they are supplementary: $(3x+5)+(7x-5)=180$, $10x=180$, $x=18$ (the angles are $59^\circ$ and $121^\circ$). ($2.5$ sets them equal; $9$ sets the sum to $90$; $36$ combines $3x+7x$ as $5x$.)",
   fig=lambda: figs.fig_trans(59, 121), figdesc="Two parallel lines l and m cut by a transversal t; two same-side interior angles are marked (3x+5) degrees and (7x-5) degrees; drawn to scale.")

gi(3, 'H',
   r"In the figure, $\angle ABC$ is a right angle, $\overline{BD}\perp\overline{AC}$, $AD=4$ and $DC=9$. What is the area of triangle $ABC$?",
   "39", Integer(39),
   lambda: (lambda yb: tri_area((0, 0), (4, yb), (13, 0)))(max(solve(-4 * 9 + y ** 2, y))),
   "Altitude to the hypotenuse: $BD^2=AD\\cdot DC$",
   r"The altitude is the geometric mean: $BD=\sqrt{4\cdot9}=6$. The hypotenuse is $AC=13$, so the area is $\frac12(13)(6)=39$.",
   fig=lambda: figs.fig_alt(math.sqrt(52), math.sqrt(117), 5.0, lab_seg=(4, 9)), figdesc="Right triangle ABC (right angle at B) with the altitude BD to hypotenuse AC; AD = 4 and DC = 9; drawn to scale.")

mc(3, 'H',
   r"In triangle $ABC$, points $M$ and $N$ are the midpoints of $\overline{AB}$ and $\overline{AC}$. If $MN=2x+3$ and $BC=5x-3$, what is the length of $\overline{BC}$?",
   C(42), [C(7), C(9), C(21)],
   lambda: (lambda xv: 5 * xv - 3)(solve(2 * (2 * x + 3) - (5 * x - 3), x)[0]),
   "Midsegment $=\\frac12$ the third side",
   r"$BC=2\,MN$: $5x-3=2(2x+3)$ gives $x=9$ and $BC=42$. ($7$ sets $MN=BC$; $9$ is just $x$; $21$ is $MN$.)")

gi(3, 'H',
   r"In the figure, $AB=AC$. The measure of $\angle A$ is $(3x-6)^\circ$ and the measure of exterior angle $\angle ACD$ is $(7x+10)^\circ$. What is the value of $x$?",
   "14", Integer(14),
   lambda: [v for v in solve((7 * x + 10) - ((3 * x - 6) + (180 - (3 * x - 6)) / 2), x)][0],
   "Exterior angle $=A+B$, with $B=\\frac{180-A}{2}$",
   r"The base angle is $\frac{180-(3x-6)}{2}$. The exterior angle at $C$ equals $\angle A+\angle B$: $7x+10=(3x-6)+\frac{186-3x}{2}$. Multiply by $2$: $14x+20=3x+174$, so $11x=154$ and $x=14$ (the angle at $A$ is $36^\circ$, the exterior angle $108^\circ$).",
   fig=lambda: figs.fig_isoext(36), figdesc="Isosceles triangle ABC (AB = AC) with side BC extended past C to D; angle A is marked (3x-6) degrees and exterior angle ACD is marked (7x+10) degrees; drawn to scale.")

gi(3, 'H',
   r"The side lengths of a triangle are $9$, $14$ and $3x$, where $x$ is a positive integer. How many possible values of $x$ are there?",
   "6", Integer(6),
   lambda: sum(1 for xv in range(1, 100) if 9 + 14 > 3 * xv and 9 + 3 * xv > 14 and 14 + 3 * xv > 9),
   "Triangle inequality with an algebraic side",
   r"We need $14-9<3x<14+9$, i.e. $5<3x<23$, so $x=2,3,4,5,6,7$: six values. (Forgetting the lower limit $14-9$ would wrongly allow $x=1$ and give $7$.)")

mc(3, 'H',
   r"In the figure, convex pentagon $ABCDE$ has $\overline{AB}\parallel\overline{ED}$. The angles are $\angle B=(2x+45)^\circ$, $\angle C=(3x+20)^\circ$ and $\angle D=(x+55)^\circ$. What is the measure of $\angle C$?",
   C(r"140^\circ", 140), [C(r"40^\circ", 40), C(r"95^\circ", 95), C(r"125^\circ", 125)],
   lambda: (lambda xv: 3 * xv + 20)(solve((2 * x + 45) + (3 * x + 20) + (x + 55) - (540 - 180), x)[0]),
   "Parallel sides: $\\angle A+\\angle E=180^\\circ$",
   r"Because $AB\parallel ED$, $\angle A+\angle E=180$. The five angles sum to $540$, so $\angle B+\angle C+\angle D=360$: $6x+120=360$, $x=40$, and $\angle C=3(40)+20=140$. ($40$ is $x$; $95=\angle D$; $125=\angle B$.)",
   fig=lambda: figs.fig_pent(), figdesc="Convex pentagon ABCDE with AB parallel to ED (arrow marks); angles B, C and D are marked (2x+45), (3x+20) and (x+55) degrees; drawn to scale.")

mc(3, 'H',
   r"In triangle $ABC$, point $D$ is on $\overline{AB}$ and point $E$ is on $\overline{AC}$ with $\overline{DE}\parallel\overline{BC}$ and $AD:DB=2:3$. The area of triangle $ABC$ is $100$. What is the area of quadrilateral $DBCE$?",
   C(84), [C(16), C(40), C(60)],
   lambda: 100 - 100 * R(2, 5) ** 2,
   "Area scales by $k^2$; subtract the small triangle",
   r"$AD:AB=2:5$, so $k=\frac25$ and the area of $ADE$ is $100\cdot\frac4{25}=16$. Then $DBCE=100-16=84$. ($16$ stops before subtracting; $40$ uses $k$ instead of $k^2$; $60$ is $\frac35$ of the area.)")

mc(3, 'H',
   r"In triangle $ABC$, medians $\overline{AD}$ and $\overline{BE}$ meet at $G$. If $AG=4x+2$ and $GD=x+7$, what is the length of $\overline{AD}$?",
   C(39), [C(13), C(26), C(52)],
   lambda: (lambda xv: 3 * (xv + 7))(solve(4 * x + 2 - 2 * (x + 7), x)[0]),
   "Centroid splits a median $2:1$",
   r"$AG=2\,GD$: $4x+2=2x+14$, $x=6$. Then $AG=26$, $GD=13$, and $AD=AG+GD=39$. ($13$ is $GD$; $26$ is $AG$; $52$ doubles $AG$.)")

mc(3, 'H',
   r"A triangle has side lengths $9$, $12$ and $14$. Which statement about its largest angle is true?",
   T(r"It is less than $90^\circ$.", 'acute'),
   [T(r"It measures exactly $90^\circ$.", 'right'), T(r"It is greater than $90^\circ$.", 'obtuse'), T(r"Its measure cannot be found from the side lengths.", 'unknown')],
   lambda: (lambda a, b, c: 'right' if a * a + b * b == c * c else ('acute' if a * a + b * b > c * c else 'obtuse'))(9, 12, 14),
   "Compare $a^2+b^2$ with $c^2$",
   r"The largest angle is opposite the longest side, $14$. Compare $9^2+12^2=225$ with $14^2=196$: since $225>196$ the angle is acute. (It would be exactly $90^\circ$ only for $9,12,15$; a picture that merely \emph{looks} right proves nothing, and side lengths always determine every angle.)")

mc(3, 'H',
   r"In the figure, segments $\overline{AD}$ and $\overline{BC}$ intersect at $E$, and $\overline{AB}\parallel\overline{DC}$. If $AE=12$, $ED=18$ and $BE=10$, what is the length of $\overline{BC}$?",
   C(25), [C(15), C(r"\dfrac{50}{3}", R(50, 3)), C(22)],
   lambda: 10 + R(10) * 18 / 12,
   "Crossing lines with parallel ends: $AE/ED=BE/EC$",
   r"Triangles $ABE$ and $DCE$ are similar, so $\frac{BE}{EC}=\frac{AE}{ED}$: $EC=\frac{10\cdot18}{12}=15$. Then $BC=BE+EC=25$. ($15$ is only $EC$; $\frac{50}{3}$ inverts the ratio; $22=10+12$ adds the wrong pieces.)",
   fig=lambda: figs.fig_bowtie(12, 18, 10, 15), figdesc="Segments AD and BC cross at E; AB is parallel to DC (arrow marks); AE = 12, ED = 18, BE = 10; drawn to scale.")

mc(3, 'H',
   r"Each interior angle of a regular polygon measures $(4x+10)^\circ$ and each exterior angle measures $(x-5)^\circ$. How many sides does the polygon have?",
   C(12), [C(6), C(30), C(35)],
   lambda: (lambda xv: 360 / (xv - 5))(solve((4 * x + 10) + (x - 5) - 180, x)[0]),
   "Interior $+$ exterior $=180^\\circ$; sides $=360/\\text{exterior}$",
   r"Interior and exterior angles at a vertex are supplementary: $5x+5=180$, $x=35$. The exterior angle is $30^\circ$, so $n=\frac{360}{30}=12$. ($6=\frac{180}{30}$; $30$ is the exterior angle; $35$ is $x$.)")

gi(3, 'H',
   r"Two similar triangles have perimeters $24$ and $40$. The larger triangle has area $250$. What is the area of the smaller triangle?",
   "90", Integer(90),
   lambda: 250 * (R(24, 40)) ** 2,
   "Perimeter ratio $k$, area ratio $k^2$",
   r"$k=\frac{24}{40}=\frac35$, so the area ratio is $\frac9{25}$ and the smaller area is $250\cdot\frac9{25}=90$. (Using $k$ instead of $k^2$ gives $150$.)")

mc(3, 'H',
   r"In the figure, triangle $ABC$ has $AB=AC$, and point $D$ lies on $\overline{AC}$ so that $AD=BD=BC$. What is the measure of $\angle ABC$?",
   C(r"72^\circ", 72), [C(r"36^\circ", 36), C(r"60^\circ", 60), C(r"108^\circ", 108)],
   lambda: next(Integer((180 - a) // 2) for a in range(1, 89) if abs(golden_gap(a)) < 1e-9),
   "Chase isosceles triangles: $x,\\,2x,\\,2x$",
   r"Let $\angle A=x$. $AD=BD$ gives $\angle ABD=x$, so exterior $\angle BDC=2x$. $BD=BC$ gives $\angle C=2x$, and $AB=AC$ gives $\angle ABC=2x$. The angle sum is $x+2x+2x=180$, so $x=36$ and $\angle ABC=72$. ($36$ is $\angle A$; $60$ assumes an equilateral shape; $108=180-72$.)",
   fig=lambda: figs.fig_golden(), figdesc="Isosceles triangle ABC (AB = AC) with D on AC; the three segments AD, BD and BC carry the same tick marks (equal lengths); drawn to scale.")
