
# ============================================================ SET 1  (Medium/Hard, 12)
mc(1, 'M',
   r"In right triangle $ABC$, the right angle is at $C$, $\sin A=\dfrac45$, and $AB=30$. What is the length of $\overline{AC}$?",
   C(18), [C(24), C("22.5", R(45, 2)), C("37.5", R(75, 2))],
   lambda: sqrt(30 ** 2 - (30 * R(4, 5)) ** 2),
   "Sine is opposite over hypotenuse",
   r"$\sin A=\frac{BC}{AB}$, so $BC=30\cdot\frac45=24$, and $AC=\sqrt{30^2-24^2}=18$ (or $AC=30\cos A=30\cdot\frac35$). ($24$ is the side opposite $A$, not $AC$; $22.5$ uses $\tan A$; $37.5$ divides $30$ by $\frac45$.)")

gi(1, 'M',
   r"For two acute angles $P$ and $Q$, $\sin P=\cos Q$. If $P=(4x-6)^\circ$ and $Q=(2x+30)^\circ$, what is the value of $x$?",
   "11", Integer(11),
   lambda: solve((4 * x - 6) + (2 * x + 30) - 90, x)[0],
   "$\\sin P=\\cos Q$ means $P+Q=90^\\circ$",
   r"For acute angles, $\sin P=\cos Q$ exactly when $P$ and $Q$ are complementary: $(4x-6)+(2x+30)=90$, so $6x=66$ and $x=11$ (the angles are $38^\circ$ and $52^\circ$).")

gi(1, 'M',
   r"Two sides of a triangle have lengths $7$ and $12$, and the third side has an integer length. What is the greatest possible perimeter of the triangle?",
   "37", Integer(37),
   lambda: max(c for c in range(1, 100) if 7 + 12 > c and 7 + c > 12 and 12 + c > 7) + 19,
   "Triangle inequality: third side $<$ sum",
   r"The third side must be less than $7+12=19$ (and more than $12-7=5$). The largest integer is $18$, so the perimeter is $7+12+18=37$. (A side of $19$ would make a flat, degenerate triangle.)")

mc(1, 'M',
   r"In triangle $ABC$, the exterior angle at $C$ measures $112^\circ$. The measures of $\angle A$ and $\angle B$ are in the ratio $5:3$. What is the measure, in degrees, of the larger of $\angle A$ and $\angle B$?",
   C(r"70^\circ", 70), [C(r"42^\circ", 42), C(r"68^\circ", 68), C(r"112.5^\circ", R(225, 2))],
   lambda: R(112) * 5 / 8,
   "Exterior angle = sum of the two far interior angles",
   r"The exterior angle equals the two remote interior angles: $A+B=112$. With $5k+3k=112$, $k=14$, so the angles are $70^\circ$ and $42^\circ$. ($42$ is the smaller angle; $68=180-112$ is the interior angle at $C$; $112.5$ wrongly makes $A+B=180$.)")

mc(1, 'M',
   r"Each exterior angle of a regular polygon measures $24^\circ$. What is the sum of the interior angles of the polygon?",
   C(r"2{,}340^\circ", 2340), [C(r"360^\circ", 360), C(r"2{,}160^\circ", 2160), C(r"2{,}700^\circ", 2700)],
   lambda: (360 // 24 - 2) * 180,
   "Exterior angles sum to $360^\circ$; interior sum $=(n-2)180$",
   r"$n=\frac{360}{24}=15$ sides, so the interior sum is $(15-2)(180)=2340$. ($360$ is the exterior sum; $2160$ uses $n-1$; $2700$ uses $15\cdot180$.)")

mc(1, 'M',
   r"Triangle $ABC$ is similar to triangle $DEF$, with $AB=6$ corresponding to $DE=15$. The perimeter of triangle $ABC$ is $28$. What is the perimeter of triangle $DEF$?",
   C(70), [C("11.2", R(56, 5)), C(37), C(175)],
   lambda: 28 * R(15, 6),
   "Perimeters scale by $k$, areas by $k^2$",
   r"The scale factor is $k=\frac{15}{6}=2.5$, and perimeter scales by $k$: $28\cdot2.5=70$. ($11.2$ inverts the ratio; $37$ adds $15-6$ instead of multiplying; $175$ uses $k^2$, the area factor.)")

mc(1, 'M',
   r"In right triangle $ABC$, the right angle is at $B$, $\angle A=30^\circ$, and $AC=14$. What is the area of the triangle?",
   C(r"\dfrac{49\sqrt3}{2}", R(49, 2) * S3_), [C(49), C(98), C(r"49\sqrt3", 49 * S3_)],
   lambda: R(1, 2) * (14 * sin(pi / 6)) * (14 * cos(pi / 6)),
   "30-60-90: $1:\\sqrt3:2$",
   r"The hypotenuse is $AC=14$, so the short leg is $BC=7$ and the long leg is $AB=7\sqrt3$. Area $=\frac12(7)(7\sqrt3)=\frac{49\sqrt3}{2}$. ($49$ and $98$ treat $7$ and $14$ as the legs; $49\sqrt3$ forgets the $\frac12$.)")

mc(1, 'H',
   r"The hypotenuse of an isosceles right triangle is $12$. What is the area of the triangle?",
   C(36), [C(18), C(72), C(r"36\sqrt2", 36 * S2_)],
   lambda: R(1, 2) * (12 / S2_) ** 2,
   "45-45-90: leg $=\\text{hypotenuse}/\\sqrt2$",
   r"Each leg is $\frac{12}{\sqrt2}=6\sqrt2$, so the area is $\frac12(6\sqrt2)^2=36$. (Shortcut: area $=\frac14(\text{hyp})^2$.) ($72$ takes the legs as $12$; $18$ takes them as $6$; $36\sqrt2$ pairs the hypotenuse with a leg.)")

gi(1, 'M',
   r"The legs of a right triangle measure $15$ and $20$. What is the length of the altitude drawn to the hypotenuse?",
   "12", Integer(12),
   lambda: 2 * tri_area((0, 0), (15, 0), (0, 20)) / dist((15, 0), (0, 20)),
   "Area two ways",
   r"The hypotenuse is $\sqrt{15^2+20^2}=25$. Area $=\frac12(15)(20)=150=\frac12(25)h$, so $h=12$.")

mc(1, 'H',
   r"Line $\ell$ passes through the point $(2,5)$ and is perpendicular to the line $y=-\dfrac23x+1$. What is the $y$-intercept of $\ell$?",
   C(2), [C(R(11, 3)), C(R(19, 3)), C(8)],
   lambda: 5 - (-1 / R(-2, 3)) * 2,
   "Perpendicular slope: flip and negate",
   r"The perpendicular slope is $\frac32$. Then $5=\frac32(2)+b$ gives $b=2$. ($\frac{19}{3}$ keeps the slope $-\frac23$; $8$ flips the fraction but keeps the negative sign, $-\frac32$; $\frac{11}{3}$ negates without flipping, $\frac23$.)")

mc(1, 'H',
   r"Two similar triangles have areas $18$ and $98$. What is the ratio of the perimeter of the smaller triangle to the perimeter of the larger?",
   C(r"\dfrac37", R(3, 7)), [C(r"\dfrac{9}{49}", R(9, 49)), C(r"\dfrac73", R(7, 3)), C(r"\dfrac{27}{343}", R(27, 343))],
   lambda: sqrt(R(18, 98)),
   "Area ratio $=k^2$, so lengths scale by $k$",
   r"The area ratio is $\frac{18}{98}=\frac9{49}=k^2$, so $k=\frac37$, and perimeters have the same ratio $\frac37$. ($\frac9{49}$ is the area ratio; $\frac73$ is inverted; $\frac{27}{343}$ is the volume ratio $k^3$.)")

mc(1, 'M',
   r"In triangle $ABC$, $AB=AC$. The exterior angle at $B$, formed by extending side $CB$ past $B$, measures $130^\circ$. What is the measure of $\angle A$?",
   C(r"80^\circ", 80), [C(r"50^\circ", 50), C(r"100^\circ", 100), C(r"130^\circ", 130)],
   lambda: 180 - 2 * (180 - 130),
   "Exterior angle, then isosceles base angles",
   r"The interior angle at $B$ is $180-130=50$. Since $AB=AC$, $\angle C=50$ too, so $\angle A=180-50-50=80$. ($50$ is a base angle; $100=\angle B+\angle C$; $130$ is the exterior angle itself.)")
