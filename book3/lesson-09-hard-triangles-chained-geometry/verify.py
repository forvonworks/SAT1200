#!/usr/bin/env python3
"""Book 3, Lesson 9 "Hard right triangles & chained geometry": the problem bank AND its verifier.

Every problem is registered with its stem/choices (LaTeX), a worked solution (what students see), and a `calc`
function (or an `each` predicate) that recomputes the answer independently of the printed solution (exact sympy
arithmetic, coordinate geometry or brute force).  Figures come from figs.py, which asserts that every drawn
length/angle equals the printed one.  `python3 verify.py` prints OK/FAIL per item, checks exactly-one-correct-choice,
balanced letters, and ALL OK.  (build.py imports PROBLEMS from here.)
"""
import sys, math
from fractions import Fraction
from sympy import (Symbol, symbols, Rational, Integer, sqrt, solve, simplify, S, sympify, latex, floor, ceiling,
                   pi, sin, cos, tan, Eq, nsimplify)
import figs

x, y, z, k, p, q, r, s, t, w, n, N = symbols('x y z k p q r s t w n N', real=True)

PROBLEMS = []
SET_TITLES = {
    1: ("Set 1", "Bridge: the core moves", "Medium and Hard"),
    2: ("Set 2", "Right triangles, trigonometry and special triangles", "Hard"),
    3: ("Set 3", "Similar triangles, angle chasing and triangle facts", "Hard"),
    4: ("Set 4", "Chained geometry: coordinates, composite figures, word problems", "Hard"),
    5: ("Set 5", "Summit: the hardest mixed problems", "Hard"),
}

def C(tex_or_val, val=None):
    if val is None:
        v = tex_or_val
        return ("$%s$" % latex(sympify(v)), sympify(v))
    return ("$%s$" % tex_or_val, val)

def T(text, val=None):
    return (text, text if val is None else val)

def same(u, v):
    try:
        if sympify(u) == sympify(v):
            return True
    except Exception:
        pass
    if isinstance(u, (tuple, str, list)) or isinstance(v, (tuple, str, list)) or callable(u) or callable(v):
        return u == v
    return simplify(sympify(u) - sympify(v)) == 0

def mc(sett, diff_, stem, right, wrongs, calc, trick, sol, order='auto', each=None, md=None, fig=None, figdesc=None):
    PROBLEMS.append(dict(set=sett, diff=diff_, kind='mc', stem=stem, right=right, wrongs=wrongs,
                         calc=calc, trick=trick, sol=sol, order=order, each=each, md=md, fig=fig, figdesc=figdesc))

def gi(sett, diff_, stem, ans_tex, ans_val, calc, trick, sol, md=None, fig=None, figdesc=None):
    PROBLEMS.append(dict(set=sett, diff=diff_, kind='gi', stem=stem, ans_tex=ans_tex, ans_val=ans_val,
                         calc=calc, trick=trick, sol=sol, md=md, fig=fig, figdesc=figdesc))

def R(a, b=1):
    return Rational(a, b)

def dist(a, b):
    return sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

def tri_area(a, b, c):
    return sympify(abs((b[0] - a[0]) * (c[1] - a[1]) - (c[0] - a[0]) * (b[1] - a[1]))) / 2

S3_ = sqrt(3)
S2_ = sqrt(2)

def golden_gap(a):
    """isosceles ABC (AB=AC, BC=1, apex a degrees); D on AC with AD=1; returns BD-1 (zero when AD=BD=BC)."""
    base = (180 - a) / 2.0 * math.pi / 180
    B = (0.0, 0.0); Cc = (1.0, 0.0); A = (0.5, 0.5 * math.tan(base))
    ac = math.dist(A, Cc)
    if ac <= 1 + 1e-9:
        return 9.0   # D would not lie strictly inside segment AC
    Dd = (A[0] + (Cc[0] - A[0]) / ac, A[1] + (Cc[1] - A[1]) / ac)
    return math.dist(B, Dd) - 1.0

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

# ================================================================== verification
LETTERS = "ABCD"

def _num(v):
    try:
        return float(sympify(v)) if not isinstance(v, (tuple, str)) and not callable(v) else None
    except Exception:
        return None

def arrange_all():
    """Choose the print order of every MC problem and balance the correct letter globally.
    Numeric choices are normally printed in ascending or descending order; when a letter is already
    used more than its share, the right answer is instead placed first/last with the wrong choices sorted."""
    glob = [0, 0, 0, 0]
    perset = {}
    total_mc = sum(1 for p_ in PROBLEMS if p_['kind'] == 'mc')
    cap = -(-total_mc // 4)
    for p_ in PROBLEMS:
        if p_['kind'] != 'mc':
            continue
        ps = perset.setdefault(p_['set'], [0, 0, 0, 0])
        items = [p_['right']] + list(p_['wrongs'])
        numeric = all(_num(it[1]) is not None for it in items)
        order = p_['order']
        if isinstance(order, int):
            pos = order
            wr = list(p_['wrongs'])
            out = wr[:pos] + [p_['right']] + wr[pos:]
        elif order in ('a', 'd') or (order == 'auto' and numeric):
            asc = sorted(items, key=lambda it: float(sympify(it[1])))
            wsort = sorted(p_['wrongs'], key=lambda it: float(sympify(it[1])))
            pa = [i for i, it in enumerate(asc) if it is p_['right']][0]
            if order == 'a':
                pos, out = pa, asc
            elif order == 'd':
                pos, out = 3 - pa, asc[::-1]
            else:
                cands = []
                for out_, pos_, unsorted in ((asc, pa, 0), (asc[::-1], 3 - pa, 0),
                                              ([p_['right']] + wsort, 0, 1), (wsort + [p_['right']], 3, 1),
                                              ([p_['right']] + wsort[::-1], 0, 1), (wsort[::-1] + [p_['right']], 3, 1)):
                    over = 20 if glob[pos_] >= cap else 0
                    cands.append((over + unsorted * 2 + glob[pos_] * 0.5 + ps[pos_] * 0.3, pos_, out_))
                _, pos, out = min(cands, key=lambda c: c[0])
        else:  # free: wrongs keep listed order, right goes to the least used letter
            wr = list(p_['wrongs'])
            pos = min(range(4), key=lambda i: (glob[i], ps[i], i))
            out = wr[:pos] + [p_['right']] + wr[pos:]
        p_['choices'], p_['pos'] = out, pos
        p_['letter'] = LETTERS[pos]
        p_['answer'] = p_['letter']
        glob[pos] += 1
        ps[pos] += 1

def prepare():
    for i, p_ in enumerate(PROBLEMS):
        p_['n'] = sum(1 for q_ in PROBLEMS[:i] if q_['set'] == p_['set']) + 1
        if p_['kind'] == 'gi':
            p_['answer'] = p_['ans_tex']
    arrange_all()

def check(p_):
    if p_['kind'] == 'gi':
        got = p_['calc']()
        return (got is not None and same(got, p_['ans_val'])), got
    vals = [c_[1] for c_ in p_['choices']]
    distinct = all(not same(vals[i], vals[j]) for i in range(4) for j in range(i + 1, 4))
    if len(p_['choices']) != 4:
        return False, 'not 4 choices'
    if p_.get('each') is not None:
        truth = [bool(p_['each'](v)) for v in vals]
        ok = sum(truth) == 1 and truth[p_['pos']] and distinct
        return ok, p_['choices'][truth.index(True)][0] if any(truth) else 'none'
    got = p_['calc']()
    if isinstance(got, list):
        got = got[0] if len(got) == 1 else tuple(got)
    n_correct = sum(1 for v in vals if same(got, v))
    ok = same(got, p_['right'][1]) and n_correct == 1 and distinct and p_['choices'][p_['pos']][1] is p_['right'][1]
    return ok, got

def main():
    from collections import Counter
    prepare()
    fails = 0
    for p_ in PROBLEMS:
        if p_.get('fig'):
            p_['fig']()   # figure functions assert their own geometry
    for p_ in PROBLEMS:
        ok, got = check(p_)
        tag = "S%d.%-2d" % (p_['set'], p_['n'])
        shown = p_['answer'] if p_['kind'] == 'gi' else "%s = %s" % (p_['letter'], p_['right'][0])
        print("%s %-4s %s   (recomputed: %s)" % (tag, "OK" if ok else "FAIL", shown, got))
        if not ok:
            fails += 1
    print()
    print("problems:", len(PROBLEMS), " FAIL:", fails)
    for sn in range(1, 6):
        ps = [p_ for p_ in PROBLEMS if p_['set'] == sn]
        mcs = [p_ for p_ in ps if p_['kind'] == 'mc']
        print("Set %d: %d problems (%d MC, %d grid-in); correct-letter counts %s; difficulty %s" %
              (sn, len(ps), len(mcs), len(ps) - len(mcs),
               dict(sorted(Counter(p_['letter'] for p_ in mcs).items())),
               dict(Counter(p_['diff'] for p_ in ps))))
    allmc = [p_ for p_ in PROBLEMS if p_['kind'] == 'mc']
    print("All MC letter counts:", dict(sorted(Counter(p_['letter'] for p_ in allmc).items())))
    gcount = len(PROBLEMS) - len(allmc)
    print("grid-ins: %d of %d (%.0f%%)" % (gcount, len(PROBLEMS), 100.0*gcount/len(PROBLEMS)))
    print("ALL OK" if not fails else "SOME FAILED")
    return 1 if fails else 0

if __name__ == "__main__":
    sys.exit(main())
