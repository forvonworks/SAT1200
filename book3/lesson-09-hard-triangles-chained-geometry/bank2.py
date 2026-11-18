
# ============================================================ SET 2  (Hard, 14)
mc(2, 'H',
   r"In right triangle $PQR$, the right angle is at $Q$ and $\cos P=\dfrac8{17}$. The perimeter of the triangle is $160$. What is the area of the triangle?",
   C(960), [C(240), C(1920), C(2040)],
   lambda: next(R(1, 2) * (8 * kk) * (15 * kk) for kk in range(1, 100) if 8 * kk + 15 * kk + 17 * kk == 160),
   "Trig ratio gives the shape; scale with $k$",
   r"$\cos P=\frac{PQ}{PR}=\frac8{17}$, so the sides are $8k,15k,17k$. Perimeter $40k=160$ gives $k=4$: legs $32$ and $60$, area $\frac12(32)(60)=960$. ($240$ scales the area by $k$ instead of $k^2$; $1920$ drops the $\frac12$; $2040$ uses the hypotenuse as a leg.)")

gi(2, 'H',
   r"Angles $M$ and $N$ are acute, and $\sin M=\cos N$. The measures of the angles, in degrees, are $M=x^2+14$ and $N=8x-8$. What is the value of $x$?",
   "6", Integer(6),
   lambda: [v for v in solve(x ** 2 + 14 + 8 * x - 8 - 90, x) if 0 < v ** 2 + 14 < 90 and 0 < 8 * v - 8 < 90][0],
   "Complementary angles, then reject the impossible root",
   r"$M+N=90$: $x^2+8x+6=90$, so $x^2+8x-84=0$ and $(x+14)(x-6)=0$. The root $x=-14$ would make $N=-120^\circ$, which is not an angle, so $x=6$ ($M=50^\circ$, $N=40^\circ$).")

mc(2, 'H',
   r"In right triangle $ABC$, the right angle is at $B$, $\tan A=\dfrac34$, and $BC=9$. What is the distance from $B$ to the hypotenuse $\overline{AC}$?",
   C("7.2", R(36, 5)), [C("5.4", R(27, 5)), C("7.5", R(15, 2)), C("9.6", R(48, 5))],
   lambda: (lambda ab, bc: ab * bc / sqrt(ab ** 2 + bc ** 2))(9 / R(3, 4), 9),
   "Altitude to the hypotenuse $=\\dfrac{\\text{leg}\\cdot\\text{leg}}{\\text{hypotenuse}}$",
   r"$\tan A=\frac{BC}{AB}=\frac34$ gives $AB=12$, so $AC=15$. The distance from $B$ to $AC$ is the altitude: $\frac{12\cdot9}{15}=7.2$. ($7.5$ is the median to the hypotenuse; $5.4=\frac{9^2}{15}$ and $9.6=\frac{12^2}{15}$ are the pieces of the hypotenuse.)")

mc(2, 'H',
   r"In the figure, $\overline{AD}\perp\overline{BC}$, $AD=6$, $\angle B=45^\circ$ and $\angle C=60^\circ$. What is the length of $\overline{BC}$?",
   C(r"6+2\sqrt3", 6 + 2 * S3_), [C(r"6+6\sqrt3", 6 + 6 * S3_), C(r"6+3\sqrt3", 6 + 3 * S3_), C(r"6\sqrt3", 6 * S3_)],
   lambda: 6 / tan(pi / 4) + 6 / tan(pi / 3),
   "Split into two special right triangles",
   r"Triangle $ABD$ is 45-45-90, so $BD=AD=6$. Triangle $ADC$ is 30-60-90 with $AD$ opposite the $60^\circ$ angle, so $DC=\frac{6}{\sqrt3}=2\sqrt3$. Then $BC=6+2\sqrt3$. ($6+6\sqrt3$ uses $DC=6\sqrt3$; $6+3\sqrt3$ uses $DC=6\cdot\frac{\sqrt3}2$; $6\sqrt3$ leaves out $BD$.)",
   fig=lambda: figs.fig_special(6), figdesc="Triangle ABC with altitude AD = 6 to BC; angle B = 45 degrees, angle C = 60 degrees; drawn to scale.")

gi(2, 'H',
   r"A right triangle has an acute angle $\theta$ with $\tan\theta=\dfrac{24}7$. The hypotenuse of the triangle is $50$. What is the area of the triangle?",
   "336", Integer(336),
   lambda: next(R(1, 2) * (24 * kk) * (7 * kk) for kk in range(1, 100) if 25 * kk == 50),
   "Triangle $7k,24k,25k$",
   r"$\tan\theta=\frac{24}{7}$ gives legs $24k$ and $7k$ and hypotenuse $25k$ (a $7$-$24$-$25$ triple). $25k=50$ gives $k=2$, legs $48$ and $14$, area $\frac12(48)(14)=336$.")

mc(2, 'H',
   r"An equilateral triangle has height $15$. What is its area?",
   C(r"75\sqrt3", 75 * S3_), [C(r"\dfrac{225\sqrt3}{4}", R(225, 4) * S3_), C(225), C(r"150\sqrt3", 150 * S3_)],
   lambda: (lambda sd: S3_ / 4 * sd ** 2)(2 * 15 / S3_),
   "Equilateral: height $=\\dfrac{\\sqrt3}{2}s$",
   r"$\frac{\sqrt3}{2}s=15$, so $s=10\sqrt3$. Area $=\frac12(10\sqrt3)(15)=75\sqrt3$. ($\frac{225\sqrt3}{4}$ treats $15$ as the side; $225$ uses a base of $30$; $150\sqrt3$ drops the $\frac12$.)")

mc(2, 'H',
   r"In right triangle $XYZ$, the right angle is at $Y$ and $\cos Z=\dfrac7{25}$. What is the value of $\tan X$?",
   C(r"\dfrac7{24}", R(7, 24)), [C(r"\dfrac{24}7", R(24, 7)), C(r"\dfrac7{25}", R(7, 25)), C(r"\dfrac{25}{24}", R(25, 24))],
   lambda: (lambda yz, xz: yz / sqrt(xz ** 2 - yz ** 2))(7, 25),
   "Complementary angles: $\\cos Z=\\sin X$",
   r"$\cos Z=\frac{YZ}{XZ}$, so take $YZ=7$, $XZ=25$, $XY=24$. Then $\tan X=\frac{\text{opposite}}{\text{adjacent}}=\frac{YZ}{XY}=\frac7{24}$. ($\frac{24}{7}$ is $\tan Z$; $\frac7{25}$ is $\sin X$; $\frac{25}{24}$ is $\frac1{\cos X}$.)")

mc(2, 'H',
   r"A rectangle has a diagonal of length $39$. The diagonal makes an angle $\theta$ with a shorter side, where $\tan\theta=\dfrac{12}5$. What is the area of the rectangle?",
   C(540), [C(195), C(270), C(468)],
   lambda: next((5 * kk) * (12 * kk) for kk in range(1, 100) if 13 * kk == 39),
   "Ratio triple $5,12,13$ scaled to the diagonal",
   r"The sides are in the ratio $5:12$ with diagonal $13k=39$, so $k=3$ and the sides are $15$ and $36$: area $540$. ($195$ and $468$ multiply a ratio term by $39$; $270$ is the area of one right triangle.)")

mc(2, 'H',
   r"The altitude to the hypotenuse of an isosceles right triangle is $8\sqrt2$. What is the area of the triangle?",
   C(128), [C(64), C(256), C(r"128\sqrt2", 128 * S2_)],
   lambda: (lambda hy: R(1, 2) * hy * 8 * S2_)(2 * 8 * S2_),
   "Altitude to the hypotenuse $=$ half the hypotenuse here",
   r"In a 45-45-90 triangle the altitude to the hypotenuse is half the hypotenuse, so the hypotenuse is $16\sqrt2$ and each leg is $16$. Area $=\frac12(16)(16)=128$ (or $\frac12\cdot16\sqrt2\cdot8\sqrt2$). ($64$ takes $8\sqrt2$ as a leg; $256$ drops the $\frac12$; $128\sqrt2$ multiplies a leg by the altitude.)")

mc(2, 'H',
   r"In the figure, triangle $ABC$ has a right angle at $B$, and $\overline{BD}\perp\overline{AC}$. If $\sin\angle C=\dfrac5{13}$, what is $\cos\angle ABD$?",
   C(r"\dfrac{12}{13}", R(12, 13)), [C(r"\dfrac5{13}", R(5, 13)), C(r"\dfrac{12}5", R(12, 5)), C(r"\dfrac{13}{12}", R(13, 12))],
   lambda: (lambda A, B, Dd: ((A[0] - B[0]) * (Dd[0] - B[0]) + (A[1] - B[1]) * (Dd[1] - B[1])) / (dist(A, B) * dist(B, Dd)))(
       (0, 0), (R(25, 13), R(60, 13)), (R(25, 13), 0)),
   "Altitude to the hypotenuse: the small angles repeat",
   r"$\angle ABD+\angle DBC=90^\circ$ and $\angle C+\angle DBC=90^\circ$, so $\angle ABD=\angle C$. Using sides $5,12,13$: $\cos C=\frac{12}{13}$. ($\frac5{13}$ is $\sin C$; $\frac{12}{5}$ is $\tan$ of the other angle; $\frac{13}{12}$ is the reciprocal.)",
   fig=lambda: figs.fig_alt(5.0, 12.0, 5.0), figdesc="Right triangle ABC (right angle at B) with the altitude BD to hypotenuse AC; shape drawn to scale (sin C = 5/13).")

gi(2, 'H',
   r"In right triangle $ABC$, the right angle is at $C$, $\tan A=\dfrac34$, $BC=x+3$ and $AC=2x-2$. What is the length of $\overline{AB}$?",
   "20", Integer(20),
   lambda: (lambda xv: sqrt((xv + 3) ** 2 + (2 * xv - 2) ** 2))(solve(4 * (x + 3) - 3 * (2 * x - 2), x)[0]),
   "Trig ratio gives an equation; then Pythagoras",
   r"$\tan A=\frac{BC}{AC}=\frac{x+3}{2x-2}=\frac34$, so $4x+12=6x-6$ and $x=9$. Then $BC=12$, $AC=16$, and $AB=\sqrt{12^2+16^2}=20$.")

mc(2, 'H',
   r"The side lengths of a right triangle are $x$, $x+7$ and $x+8$. What is the perimeter of the triangle?",
   C(30), [C(13), C(17), C(26)],
   lambda: next(3 * xv + 15 for xv in range(1, 200) if xv ** 2 + (xv + 7) ** 2 == (xv + 8) ** 2),
   "Longest side is the hypotenuse; solve the quadratic",
   r"$x^2+(x+7)^2=(x+8)^2$ gives $x^2-2x-15=0$, so $x=5$ (reject $x=-3$): sides $5,12,13$ and perimeter $30$. ($13$ is the hypotenuse; $17=5+12$ is the two legs; $26$ doubles the hypotenuse.)")

gi(2, 'H',
   r"In right triangle $ABC$, the right angle is at $C$ and $2\sin A=3\cos A$. The area of the triangle is $48$. What is the length of $\overline{BC}$?",
   "12", Integer(12),
   lambda: next(3 * kk for kk in range(1, 100) if R(1, 2) * (3 * kk) * (2 * kk) == 48),
   "Divide by $\\cos A$ to get $\\tan A$",
   r"$2\sin A=3\cos A$ gives $\tan A=\frac{BC}{AC}=\frac32$, so $BC=3k$, $AC=2k$. Area $\frac12(3k)(2k)=3k^2=48$, so $k=4$ and $BC=12$.")

mc(2, 'H',
   r"The perimeter of a $30^\circ$-$60^\circ$-$90^\circ$ triangle is $36+12\sqrt3$. What is the area of the triangle?",
   C(r"72\sqrt3", 72 * S3_), [C(r"144\sqrt3", 144 * S3_), C(144), C(r"36\sqrt3", 36 * S3_)],
   lambda: (lambda a: R(1, 2) * a * a * S3_)(solve(x * (3 + S3_) - (36 + 12 * S3_), x)[0]),
   "Perimeter of a 30-60-90 is $a(3+\\sqrt3)$",
   r"With short leg $a$ the sides are $a$, $a\sqrt3$, $2a$, so $a(3+\sqrt3)=12(3+\sqrt3)$ and $a=12$. Area $=\frac12(12)(12\sqrt3)=72\sqrt3$. ($144\sqrt3$ drops the $\frac12$; $144=a^2$; $36\sqrt3$ pairs $12$ with $6\sqrt3$.)")
