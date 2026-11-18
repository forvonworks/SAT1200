
# ============================================================ SET 4  (Hard, 14)
mc(4, 'H',
   r"In the figure, $AB=13$, $BC=20$ and $AC=21$. What is the area of triangle $ABC$?",
   C(126), [C(130), C("136.5", R(273, 2)), C(210)],
   lambda: (lambda s_: sqrt(s_ * (s_ - 13) * (s_ - 20) * (s_ - 21)))(R(13 + 20 + 21, 2)),
   "Unknown height: Pythagoras on both sides of the altitude",
   r"Drop the altitude $h$ to $AC$ and let the foot split $AC$ into $a$ and $21-a$: $13^2-a^2=20^2-(21-a)^2$ gives $a=5$, so $h=12$. Area $=\frac12(21)(12)=126$ (Heron's formula agrees). ($130$, $136.5$, $210$ treat two of the sides as perpendicular legs.)",
   fig=lambda: figs.fig_tri3(13, 20, 21), figdesc="Triangle ABC with AB = 13, BC = 20, AC = 21; drawn to scale (it is not a right triangle).")

mc(4, 'H',
   r"A tower stands on level ground. Points $A$ and $B$ are on the ground in line with the base $O$ of the tower, with $A$ between $B$ and $O$ and $AB=40$ meters. The angle of elevation of the top $T$ of the tower is $45^\circ$ from $A$ and $30^\circ$ from $B$. What is the height of the tower, in meters?",
   C(r"20(\sqrt3+1)", 20 * (S3_ + 1)), [C(r"40\sqrt3", 40 * S3_), C(r"40(\sqrt3-1)", 40 * (S3_ - 1)), C(r"20\sqrt3", 20 * S3_)],
   lambda: solve(Eq(x + 40, x * S3_), x)[0],
   "Two observation points: height $h$ is the shared side",
   r"With height $h$: $OA=h$ (45-45-90) and $OB=h\sqrt3$ (30-60-90). Their difference is $40$: $h(\sqrt3-1)=40$, so $h=\frac{40}{\sqrt3-1}=20(\sqrt3+1)$. ($40\sqrt3$ uses only the $30^\circ$ view; $40(\sqrt3-1)$ inverts the factor; $20\sqrt3$ halves $40\sqrt3$.)",
   fig=lambda: figs.fig_elev(40), figdesc="Vertical tower OT on level ground; observation points A and B on the ground, AB = 40 m; angle of elevation 45 degrees at A and 30 degrees at B; drawn to scale.")

mc(4, 'H',
   r"A $25$-foot ladder leans against a vertical wall with its top $24$ feet above the ground. The foot of the ladder is pulled away from the wall until the top of the ladder is $20$ feet above the ground. How many feet did the foot of the ladder move?",
   C(8), [C(4), C(15), C(22)],
   lambda: sqrt(25 ** 2 - 20 ** 2) - sqrt(25 ** 2 - 24 ** 2),
   "The ladder length stays the hypotenuse",
   r"Before: foot $=\sqrt{25^2-24^2}=7$. After: foot $=\sqrt{25^2-20^2}=15$. The foot moved $15-7=8$ feet. ($4$ is how far the top slid; $15$ is the new distance; $22=7+15$.)")

gi(4, 'H',
   r"In the $xy$-plane, $P=(-2,1)$ and $R=(7,-2)$. Point $Q$ has coordinates $(4,k)$, and $\angle PQR$ is a right angle. What is the sum of all possible values of $k$?",
   "-1", Integer(-1),
   lambda: sum(solve((-2 - 4) * (7 - 4) + (1 - k) * (-2 - k), k)),
   "Perpendicular vectors: dot product $=0$",
   r"$\overrightarrow{QP}\cdot\overrightarrow{QR}=0$: $(-6)(3)+(1-k)(-2-k)=0$, which simplifies to $k^2+k-20=0$, so $k=4$ or $k=-5$. The sum is $-1$ (also the sum of roots $-\frac ba$).",
   fig=lambda: figs.fig_coord(), figdesc="Coordinate plane (equal scales on both axes) with points P(-2,1) and R(7,-2) and the dashed vertical line x = 4 on which Q lies.")

gi(4, 'H',
   r"In the $xy$-plane, $A=(1,1)$, $B=(13,1)$ and $C=(7,k)$, where $k>0$. The area of triangle $ABC$ is $48$. What is the perimeter of triangle $ABC$?",
   "32", Integer(32),
   lambda: (lambda kv: dist((1, 1), (13, 1)) + dist((1, 1), (7, kv)) + dist((13, 1), (7, kv)))(
       [v for v in solve(6 * (k - 1) - 48, k) + solve(-6 * (k - 1) - 48, k) if v > 0][0]),
   "Height is $k-1$, not $k$; $C$ is above the midpoint",
   r"The base $AB=12$ lies on $y=1$, so the height is $k-1$: $\frac12(12)(k-1)=48$ gives $k=9$. Then $AC=BC=\sqrt{6^2+8^2}=10$ (since $x=7$ is the midpoint of $AB$), and the perimeter is $12+10+10=32$.")

mc(4, 'H',
   r"The figure is a rectangle topped by an isosceles triangle. The rectangle measures $12$ by $6$, and each of the two equal sides of the triangle is $10$. What is the area of the whole figure?",
   C(120), [C(48), C(132), C(168)],
   lambda: 12 * 6 + R(1, 2) * 12 * sqrt(10 ** 2 - 6 ** 2),
   "Composite figure: find the hidden height",
   r"The roof's height is $\sqrt{10^2-6^2}=8$, so its area is $\frac12(12)(8)=48$. Total $=72+48=120$. ($48$ is the roof alone; $132=72+\frac12\cdot12\cdot10$ uses the slant as height; $168=72+96$ forgets the $\frac12$.)",
   fig=lambda: figs.fig_house(12, 6, 10), figdesc="A 12 by 6 rectangle with an isosceles triangle on its top side; the two equal sides of the triangle are 10; drawn to scale.")

mc(4, 'H',
   r"A vertical pole stands on level ground. Two straight cables run from the top of the pole to points $A$ and $B$ on the ground on opposite sides of the pole. The cables are $17$ meters and $10$ meters long, and $A$ and $B$ are $21$ meters apart. How tall is the pole, in meters?",
   C(8), [C(6), C(9), C(15)],
   lambda: next(h for h in [R(m, 2) for m in range(1, 40)] if sqrt(17 ** 2 - h ** 2) + sqrt(10 ** 2 - h ** 2) == 21),
   "Shared side of two right triangles: subtract the squares",
   r"Let the pole be $h$ with $AO=a$, $OB=b$, $a+b=21$. $17^2-a^2=10^2-b^2$ gives $a^2-b^2=189$, so $a-b=\frac{189}{21}=9$, $a=15$, $b=6$, and $h=\sqrt{17^2-15^2}=8$. ($15$ and $6$ are the distances from the pole; $9$ is $a-b$.)")

gi(4, 'H',
   r"In the figure, $\angle ABC$ and $\angle ACD$ are right angles, $AB=9$, $\tan\angle BAC=\dfrac43$ and $\sin\angle CAD=\dfrac45$. What is the perimeter of quadrilateral $ABCD$?",
   "66", Integer(66),
   lambda: 9 + 9 * R(4, 3) + (lambda ac: ac / R(3, 5) + (ac / R(3, 5)) * R(4, 5))(sqrt(9 ** 2 + (9 * R(4, 3)) ** 2)),
   "Two right triangles share $AC$: chain the ratios",
   r"Triangle $ABC$: $BC=9\cdot\frac43=12$, so $AC=15$. Triangle $ACD$: $\sin\angle CAD=\frac{CD}{AD}=\frac45$ gives sides $3k,4k,5k$ with $AC=3k=15$, so $k=5$, $CD=20$, $AD=25$. Perimeter $=9+12+20+25=66$.",
   fig=lambda: figs.fig_chain(9, 12, 20), figdesc="Quadrilateral ABCD with diagonal AC; right angles at B (angle ABC) and at C (angle ACD); AB = 9; drawn to scale.")

mc(4, 'H',
   r"A lamp is fixed to the top of a vertical post on level ground. A person $1.5$ m tall stands $6$ m from the post and casts a shadow $2$ m long (the shadow points away from the post). The person then walks directly away from the post until the shadow is $4$ m long. How many meters did the person walk?",
   C(6), [C(2), C(4), C(12)],
   lambda: (lambda H: H * 4 / R(3, 2) - 4 - 6)(R(3, 2) * (6 + 2) / 2),
   "Similar triangles: lamp height stays fixed",
   r"Lamp height $H$: $\frac H{6+2}=\frac{1.5}2$ gives $H=6$. At shadow $4$: $\frac H{d+4}=\frac{1.5}4$ gives $d+4=16$, $d=12$. The person walked $12-6=6$ m. ($2$ is how much the shadow grew; $4$ is the new shadow; $12$ is the new distance.)")

mc(4, 'H',
   r"Point $A=(2,-1)$ and point $B=(8,7)$. Which of the following points lies on the perpendicular bisector of $\overline{AB}$?",
   C(r"(9,0)", (9, 0)), [C(r"(9,6)", (9, 6)), C(r"(8,-1)", (8, -1)), C(r"(6,-4)", (6, -4))],
   None,
   "Equidistant from both endpoints",
   r"The midpoint is $(5,3)$ and the slope of $AB$ is $\frac43$, so the bisector has slope $-\frac34$: from $(5,3)$ go $4$ right and $3$ down to $(9,0)$. (Check: $\text{distance}^2$ to $A$ and to $B$ are both $50$.) ($(9,6)$ uses slope $+\frac34$; $(8,-1)$ uses $-\frac43$; $(6,-4)$ lies on the perpendicular through $A$ instead of the midpoint.)",
   each=lambda pt: dist(pt, (2, -1)) == dist(pt, (8, 7)))

mc(4, 'H',
   r"A rectangle has a diagonal of length $25$, and its two side lengths differ by $5$. What is the perimeter of the rectangle?",
   C(70), [C(35), C(50), C(100)],
   lambda: next(2 * (a + a + 5) for a in range(1, 100) if a * a + (a + 5) ** 2 == 625),
   "Diagonal and side difference: Pythagoras with an unknown",
   r"$x^2+(x+5)^2=25^2$ gives $x^2+5x-300=0$, so $x=15$ and the sides are $15$ and $20$ (a $3$-$4$-$5$ triple times $5$). Perimeter $=2(35)=70$. ($35$ is the semiperimeter; $50$ doubles the diagonal; $100=4\cdot25$.)")

mc(4, 'H',
   r"An isosceles triangle has a base of $16$ and a perimeter of $36$. What is its area?",
   C(48), [C(64), C(80), C(96)],
   lambda: (lambda leg: R(1, 2) * 16 * sqrt(leg ** 2 - 8 ** 2))(R(36 - 16, 2)),
   "Perimeter gives the leg; height is hidden",
   r"Each equal side is $\frac{36-16}{2}=10$. The altitude to the base is $\sqrt{10^2-8^2}=6$, so the area is $\frac12(16)(6)=48$. ($80$ uses the leg as the height; $96$ drops the $\frac12$; $64=\frac12\cdot16\cdot8$ uses half the base as the height.)")

gi(4, 'H',
   r"In the figure, a square is placed inside right triangle $ABC$ with one vertex at the right-angle vertex $C$ and the opposite vertex on the hypotenuse $\overline{AB}$. The legs are $CB=12$ and $CA=6$. What is the side length of the square?",
   "4", Integer(4),
   lambda: solve(Eq(x / 12 + x / 6, 1), x)[0],
   "Leftover small triangle is similar to the big one",
   r"The point $(s,s)$ lies on the hypotenuse $\frac x{12}+\frac y6=1$, so $\frac s{12}+\frac s6=1$ and $s=4$. (Similar triangles: $\frac{6-s}{6}=\frac s{12}$.)",
   fig=lambda: figs.fig_sq(12, 6), figdesc="Right triangle ABC with the right angle at C, CB = 12 and CA = 6; a square sits in the corner at C with its opposite vertex on AB; drawn to scale.")

mc(4, 'H',
   r"A rectangular box measures $6$ by $8$ by $24$. What is the length of the longest segment that can be drawn between two corners of the box?",
   C(26), [C(10), C(38), C(676)],
   lambda: sqrt(6 ** 2 + 8 ** 2 + 24 ** 2),
   "Space diagonal: two chained right triangles",
   r"The face diagonal is $\sqrt{6^2+8^2}=10$; then the space diagonal is $\sqrt{10^2+24^2}=26$ (or $\sqrt{6^2+8^2+24^2}$). ($10$ stops at the face diagonal; $38=6+8+24$; $676$ forgets the square root.)")
