#!/usr/bin/env python3
"""Book 3, Lesson 8 "Hard circles, area & volume": the problem bank AND its verifier.

Every problem is registered with:
  * its stem and choices (LaTeX),
  * a worked solution (this is what students see),
  * a `calc` function (or an `each` predicate for "which option ..." items) that recomputes the
    answer independently of the printed solution (exact arithmetic, coordinate geometry, brute-force loops),
  * optionally a `fig` (a key of figs.py): true-scale TikZ drawn from the same numbers as the stem.
    figs.py asserts the geometry of every figure (points on circles, right angles, tangency, lengths).

Running `python3 verify.py` recomputes every answer, checks that exactly one MC choice is correct
and that choices are distinct, balances the correct letters, re-asserts every figure, and prints ALL OK / FAIL.
(`build.py` imports PROBLEMS from this file to write problems.md and the .tex files.)
"""
import sys, math
from fractions import Fraction
from sympy import (Symbol, symbols, Rational, Integer, sqrt, solve, simplify, S, sympify, latex, floor, ceiling,
                   pi, expand, integrate, nsimplify, cbrt, Poly, sin)
import figs

x, y, z, k, p, q, r, s, t, w, n, N = symbols('x y z k p q r s t w n N', real=True)

PROBLEMS = []
SET_TITLES = {
    1: ("Set 1", "Bridge: the core moves", "Medium and Hard"),
    2: ("Set 2", "Circles in the plane: equations, tangents, chords, angles, arcs", "Hard"),
    3: ("Set 3", "Areas: shaded regions, composite figures and scaling", "Hard"),
    4: ("Set 4", "Solids: volume, surface area, filling and recasting", "Hard"),
    5: ("Set 5", "Summit: the hardest mixed problems", "Hard"),
}

# ---------------------------------------------------------------- helpers
def _tex(v):
    """LaTeX of a sympy value; sums print with the positive terms first (constant first), e.g. 60+9\\pi/2, 50\\pi-100."""
    v = sympify(v)
    from sympy import Add
    if not isinstance(v, Add):
        return latex(v)
    terms = list(Add.make_args(v))
    pos = [t_ for t_ in terms if not t_.could_extract_minus_sign()]
    neg = [-t_ for t_ in terms if t_.could_extract_minus_sign()]
    pos.sort(key=lambda t_: (0 if t_.is_number and not t_.has(pi) and not t_.has(sqrt(2)) and t_.is_Rational else 1))
    out = " + ".join(latex(t_) for t_ in pos)
    for t_ in neg:
        out += " - " + latex(t_)
    return out

def C(tex_or_val, val=None):
    """Numeric choice: C(66) or C(r"\\dfrac14", Rational(1,4)) or C("5.5", Rational(11,2)) -> (latex, value)."""
    if val is None:
        v = tex_or_val
        return ("$%s$" % _tex(v), sympify(v))
    return ("$%s$" % tex_or_val, val)

def T(text, val=None):
    """Text choice. Value defaults to the text itself; pass a value for ordering/keys."""
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

def rnd(v, d=0):
    """Round an exact value to d decimals (half up) and return an exact Rational."""
    sc = 10 ** d
    return Rational(int(floor(Rational(v) * sc + Rational(1, 2))), sc)

def pct(v):
    return Rational(v) * 100

def rnum(v, d=0):
    """round a sympy/float value to d decimals -> exact Rational"""
    return rnd(nsimplify(float(v), rational=True), d)


def lens_check(sd):
    """Numerically integrate the overlap of two quarter-disks in a square of side sd; a = (area + sd^2)/pi."""
    nstep = 200000
    hh = sd / nstep
    tot = 0.0
    for i in range(nstep):
        xm = (i + 0.5) * hh
        up = math.sqrt(sd * sd - xm * xm)
        low = sd - math.sqrt(sd * sd - (xm - sd) ** 2)
        tot += max(0.0, up - low) * hh
    a = (tot + sd * sd) / math.pi
    assert abs(a - round(a)) < 1e-3, a
    return Integer(round(a)) + Integer(sd * sd)

# ============================================================ SET 1  (Medium/Hard, 12)
mc(1, 'M',
   r"The graph of $(x-2)^2+(y+5)^2=36$ in the $xy$-plane is a circle. What is the length of a diameter of the circle?",
   C(12), [C(6), C(36), C(72)],
   lambda: 2 * sqrt(Integer(36)),
   "Read $r^2$, then double $r$",
   r"The right side is $r^2=36$, so $r=6$ and the diameter is $2r=12$. ($6$ is the radius; $36$ is $r^2$; $72$ doubles $r^2$.)")

mc(1, 'M',
   r"A circle in the $xy$-plane has center $(1,-2)$ and radius $5$. Which of the following points lies \emph{inside} the circle?",
   T(r"$(3,0)$", (3, 0)), [T(r"$(-3,-5)$", (-3, -5)), T(r"$(1,3)$", (1, 3)), T(r"$(6,1)$", (6, 1))],
   lambda: None,
   "Compare distance$^2$ with $r^2$",
   r"A point is inside when $(x-1)^2+(y+2)^2<25$. For $(3,0)$: $4+4=8<25$. ($(-3,-5)$ gives $16+9=25$ and $(1,3)$ gives $0+25=25$: both are \emph{on} the circle; $(6,1)$ gives $25+9=34>25$, outside.)",
   each=lambda v: (v[0] - 1) ** 2 + (v[1] + 2) ** 2 < 25)

gi(1, 'M',
   r"A circle has radius $9$. An arc of the circle has a central angle of $80^\circ$, and the length of the arc is $k\pi$. What is the value of $k$?",
   "4", Integer(4),
   lambda: R(80, 360) * 2 * 9,
   "Arc = fraction of the circumference",
   r"The arc is $\frac{80}{360}=\frac29$ of the circumference $2\pi(9)=18\pi$, so it is $\frac29\cdot18\pi=4\pi$ and $k=4$.")

mc(1, 'M',
   r"A circle has a diameter of $24$. A sector of this circle has an area of $60\pi$. What is the measure, in degrees, of the central angle of the sector?",
   C(150), [C("37.5", R(75, 2)), C(60), C(75)],
   lambda: solve(x / 360 * pi * 12 ** 2 - 60 * pi, x)[0],
   "Sector = $\\frac{\\theta}{360}\\pi r^2$ with $r=\\frac d2$",
   r"The radius is $12$, so the circle has area $144\pi$ and the sector is $\frac{60\pi}{144\pi}=\frac5{12}$ of it: $\frac5{12}(360^\circ)=150^\circ$. ($37.5$ uses the diameter $24$ as the radius; $60$ copies the coefficient; $75$ uses $180^\circ$ for the full turn.)")

mc(1, 'M',
   r"Points $A$ and $B$ lie on a circle with center $O$, and $\angle AOB=100^\circ$. Point $C$ lies on the \emph{major} arc $AB$ (the longer arc). What is the measure, in degrees, of $\angle ACB$?",
   C(r"50^\circ", 50), [C(r"100^\circ", 100), C(r"130^\circ", 130), C(r"200^\circ", 200)],
   lambda: R(100, 2),
   "Inscribed angle = half the central angle",
   r"An inscribed angle is half the central angle on the same arc: $\frac{100}2=50^\circ$. ($100$ is the central angle; $130$ is the answer if $C$ were on the minor arc, $180-50$; $200$ doubles instead of halving.)")

mc(1, 'M',
   r"A sphere has a volume of $288\pi$ cubic centimeters. What is the surface area, in square centimeters, of the sphere?",
   C(144 * pi), [C(36 * pi), C(72 * pi), C(576 * pi)],
   lambda: 4 * pi * cbrt(Integer(288) * 3 / 4) ** 2,
   "Volume gives $r$; surface area is $4\\pi r^2$",
   r"$\frac43\pi r^3=288\pi$ gives $r^3=216$, $r=6$. Then $4\pi r^2=4\pi(36)=144\pi$. ($36\pi$ is $\pi r^2$; $72\pi$ is $2\pi r^2$; $576\pi$ uses the diameter $12$ as the radius.)")

mc(1, 'M',
   r"A tank shaped like a rectangular box is $2$ m long, $1.5$ m wide and $0.8$ m deep. How many liters of water does it hold when full? ($1$ cubic meter $=1000$ liters)",
   C("2{,}400", 2400), [C("2.4", R(12, 5)), C(240), C("24{,}000", 24000)],
   lambda: R(2) * R(3, 2) * R(4, 5) * 1000,
   "Cubic meters $\\to$ liters: $\\times1000$",
   r"$V=2(1.5)(0.8)=2.4$ m$^3$, and $2.4\times1000=2400$ L. ($2.4$ forgets the conversion; $240$ and $24{,}000$ slip the decimal point.)")

mc(1, 'M',
   r"Two right circular cones are similar. The height of the larger cone is $3$ times the height of the smaller cone, and the smaller cone has a volume of $40$ cubic centimeters. What is the volume, in cubic centimeters, of the larger cone?",
   C("1{,}080", 1080), [C(120), C(360), C("3{,}240", 3240)],
   lambda: 40 * 3 ** 3,
   "Scale factor $k$: volume $\\times k^3$",
   r"Lengths scale by $k=3$, so volume scales by $k^3=27$: $40\times27=1080$. ($120$ multiplies by $3$; $360$ by $k^2=9$; $3{,}240$ by $3^4$.)")

gi(1, 'M',
   r"An arc of length $2\pi$ lies on a circle of radius $6$. What is the measure, in degrees, of the central angle that intercepts the arc?",
   "60", Integer(60),
   lambda: (2 * pi / (2 * pi * 6)) * 360,
   "Arc $\\div$ circumference $=\\frac{\\theta}{360}$",
   r"The circumference is $2\pi(6)=12\pi$, so the arc is $\frac{2\pi}{12\pi}=\frac16$ of the circle and $\theta=\frac16(360)=60^\circ$.")

mc(1, 'M',
   r"A region is made of a $10$-by-$6$ rectangle together with a semicircle whose diameter is a $6$-unit side of the rectangle (the semicircle lies outside the rectangle). What is the area of the region?",
   C(60 + 9 * pi / 2), [C(60 + 9 * pi), C(60 + 18 * pi), C(60 + 36 * pi)],
   lambda: 10 * 6 + R(1, 2) * pi * 3 ** 2,
   "Semicircle: $\\frac12\\pi r^2$ with $r=\\frac d2$",
   r"The semicircle has diameter $6$, so $r=3$ and its area is $\frac12\pi(3)^2=\frac92\pi$. Total $60+\frac92\pi$. ($60+9\pi$ is a full circle; $60+18\pi$ is a semicircle of radius $6$; $60+36\pi$ is a full circle of radius $6$.)")

mc(1, 'H',
   r"Water is pumped into an empty cylindrical tank with a base radius of $4$ feet at a constant rate of $24\pi$ cubic feet per minute. By how many feet does the water level rise each minute?",
   C("1.5", R(3, 2)), [C("0.375", R(3, 8)), C(3), C(6)],
   lambda: 24 * pi / (pi * 4 ** 2),
   "Rate $=$ (base area)(rise per minute)",
   r"Each minute the volume added is $\pi r^2\cdot(\text{rise})$: $24\pi=16\pi\cdot\text{rise}$, so the rise is $1.5$ ft. ($3$ divides by the circumference $8\pi$; $6$ divides by $r$; $0.375$ divides by $r^3$.)")

gi(1, 'H',
   r"The equation $x^2+y^2-6x+10y+18=0$ defines a circle in the $xy$-plane. What is the radius of the circle?",
   "4", Integer(4),
   lambda: sqrt(Integer(6 ** 2 + 10 ** 2) / 4 - 18),
   "Complete the square, then watch the constant",
   r"$(x^2-6x+9)+(y^2+10y+25)=-18+9+25$, so $(x-3)^2+(y+5)^2=16$ and $r=\sqrt{16}=4$. (Moving $18$ to the right gives $-18$, not $+18$; and $16$ is $r^2$.)")

# ============================================================ SET 2  (Circles in the plane, 14)
mc(2, 'H',
   r"In the $xy$-plane, the graph of $x^2+y^2+8x-2y+k=0$ is a circle with radius $5$. What is the value of $k$?",
   C(-8), [C(8), C(12), C(42)],
   lambda: Rational(8 ** 2 + 2 ** 2, 4) - 25,
   "Complete the square: $r^2=h^2+k^2-c$",
   r"$(x+4)^2+(y-1)^2=17-k$, and this must equal $r^2=25$, so $k=17-25=-8$. ($8$ drops the sign; $12$ uses $r=5$ instead of $r^2$; $42=17+25$.)")

gi(2, 'H',
   r"The graph of $x^2+y^2-4x+6y-12=0$ is a circle in the $xy$-plane that crosses the $x$-axis at two points. What is the distance between these two points?",
   "8", Integer(8),
   lambda: abs(solve(x ** 2 - 4 * x - 12, x)[0] - solve(x ** 2 - 4 * x - 12, x)[1]),
   "Set $y=0$ to find axis crossings",
   r"On the $x$-axis $y=0$, so $x^2-4x-12=0$, i.e. $(x-6)(x+2)=0$. The points are $x=6$ and $x=-2$, which are $8$ apart.")

mc(2, 'H',
   r"In the $xy$-plane, a circle has center $(2,-1)$. A line is tangent to the circle at the point $(5,3)$. Which of the following points also lies on this line?",
   T(r"$(9,0)$", (9, 0)), [T(r"$(9,6)$", (9, 6)), T(r"$(8,7)$", (8, 7)), T(r"$(8,-1)$", (8, -1))],
   lambda: None,
   "Tangent $\\perp$ radius: negative reciprocal slope",
   r"The radius from $(2,-1)$ to $(5,3)$ has slope $\frac43$, so the tangent has slope $-\frac34$: $y-3=-\frac34(x-5)$. At $x=9$: $y=3-3=0$. ($(8,7)$ has slope $\frac43$, parallel to the radius; $(9,6)$ has slope $+\frac34$; $(8,-1)$ has slope $-\frac43$.)",
   each=lambda v: (v[0] - 5) * (5 - 2) + (v[1] - 3) * (3 + 1) == 0)

mc(2, 'H',
   r"In the $xy$-plane, the circle $x^2+y^2=k$ is tangent to the line $3x-4y=40$. What is the value of $k$?",
   C(64), [C(8), C(40), C("1{,}600", 1600)],
   lambda: (Integer(40) / sqrt(Integer(3 ** 2 + 4 ** 2))) ** 2,
   "Tangent $\\Rightarrow$ distance from center to line $=r$",
   r"The center is the origin, whose distance to $3x-4y-40=0$ is $\frac{|{-40}|}{\sqrt{3^2+4^2}}=8$. That distance is the radius, and $k=r^2=64$. ($8$ is $r$; $40$ and $1600$ ignore the $\sqrt{3^2+4^2}$.)", order=0)

gi(2, 'H',
   r"A circle has radius $17$. Chord $AB$ has length $30$ and $M$ is the midpoint of $AB$. The line through the center $O$ and $M$ meets the circle again at point $N$ on the short arc $AB$ (see the figure). What is the length of $\overline{MN}$?",
   "9", Integer(9),
   lambda: 17 - sqrt(Integer(17 ** 2 - 15 ** 2)),
   "Perpendicular from the center bisects the chord",
   r"$OM\perp AB$ and $AM=15$, so $OM=\sqrt{17^2-15^2}=8$. Then $MN=ON-OM=17-8=9$. (The common error is to stop at $8$, the distance from the center to the chord.)",
   fig="sagitta", figdesc="circle with center O, chord AB of length 30, midpoint M, segment MN to the arc, radius 17")

mc(2, 'H',
   r"In the figure, $\overline{AB}$ is a diameter of the circle with center $O$, point $C$ lies on the circle, and $\angle BAC=28^\circ$. What is the measure, in degrees, of the minor arc $AC$?",
   C(124), [C(56), C(62), C(152)],
   lambda: 2 * (180 - 90 - 28),
   "Semicircle $\\Rightarrow90^\\circ$, then arc $=2\\times$ inscribed angle",
   r"$\angle ACB=90^\circ$ (angle in a semicircle), so $\angle ABC=180-90-28=62^\circ$. Arc $AC$ is intercepted by $\angle ABC$: $2(62)=124^\circ$. ($56$ is arc $BC$; $62$ is the inscribed angle itself; $152=180-28$.)",
   fig="semicircle", figdesc="circle with diameter AB, point C on the circle, angle BAC marked 28 degrees")

mc(2, 'H',
   r"From a point $E$ outside a circle with center $O$, tangent segments $\overline{EA}$ and $\overline{EU}$ are drawn to the circle, touching it at $A$ and $U$, with $\angle AEU=50^\circ$. Point $C$ lies on the major arc $AU$. What is the measure, in degrees, of $\angle ACU$?",
   C(r"65^\circ", 65), [C(r"50^\circ", 50), C(r"115^\circ", 115), C(r"130^\circ", 130)],
   lambda: R(360 - 90 - 90 - 50, 2),
   "Kite $OAEU$: two right angles, then half the central angle",
   r"In quadrilateral $OAEU$ the angles at $A$ and $U$ are $90^\circ$, so $\angle AOU=360-90-90-50=130^\circ$. The inscribed angle on the major arc is half of it: $65^\circ$. ($130$ is the central angle; $115=180-65$ is for $C$ on the minor arc; $50$ is given.)")

gi(2, 'H',
   r"A circle has center $O$ and radius $6$. From a point $E$ outside the circle, tangent segments $\overline{EA}$ and $\overline{EU}$ of length $8$ are drawn (see the figure). Segment $\overline{OE}$ crosses the circle at $P$. What is the length of $\overline{PE}$?",
   "4", Integer(4),
   lambda: sqrt(Integer(6 ** 2 + 8 ** 2)) - 6,
   "Tangent $\\perp$ radius: $OE^2=r^2+t^2$",
   r"$\angle OAE=90^\circ$, so $OE=\sqrt{6^2+8^2}=10$. Then $PE=OE-OP=10-6=4$. (A frequent slip is to answer $10$, the distance $OE$ itself.)",
   fig="kite", figdesc="circle with center O, external point E, tangent segments EA and EU, OA = 6, EA = 8, P on segment OE")

mc(2, 'H',
   r"A sector of a circle has a central angle of $60^\circ$ and an area of $24\pi$. What is the length of the arc of the sector?",
   C(4 * pi), [C(2 * pi), C(12 * pi), C(24 * pi)],
   lambda: R(60, 360) * 2 * pi * sqrt(24 * 6),
   "Area $\\to r$, then arc $=\\frac{\\theta}{360}\\cdot2\\pi r$",
   r"$\frac{60}{360}\pi r^2=24\pi$ gives $r^2=144$, $r=12$. Arc $=\frac16(2\pi\cdot12)=4\pi$. ($24\pi$ is the whole circumference; $12\pi$ is $\pi r$; $2\pi$ halves the arc.)", order=0)

mc(2, 'H',
   r"A sector of a circle has radius $9$ and a central angle of $\frac{5\pi}{6}$ radians. What is the area of the sector?",
   C(R(135, 4) * pi), [C(R(15, 4) * pi), C(R(15, 2) * pi), C(R(135, 2) * pi)],
   lambda: R(1, 2) * 9 ** 2 * (5 * pi / 6),
   "Radians: area $=\\frac12r^2\\theta$",
   r"With $\theta$ in radians, $A=\frac12r^2\theta=\frac12(81)\cdot\frac{5\pi}6=\frac{135\pi}{4}$. ($\frac{135\pi}2$ forgets the $\frac12$; $\frac{15\pi}2$ is the arc length $r\theta$; $\frac{15\pi}4$ uses $r$ instead of $r^2$.)")

mc(2, 'H',
   r"A right triangle has legs of length $9$ and $12$. A circle is inscribed in the triangle, touching all three sides. What is the area of the part of the triangle that lies outside the circle?",
   C(54 - 9 * pi), [C(54 - 3 * pi), C(54 - 6 * pi), C(54 - 36 * pi)],
   lambda: Integer(54) - pi * (R(9 * 12, 2) / ((9 + 12 + sqrt(Integer(81 + 144))) / 2)) ** 2,
   "Inradius $=\\dfrac{\\text{area}}{\\text{semiperimeter}}$",
   r"The hypotenuse is $15$, the area is $54$ and the semiperimeter is $18$, so $r=\frac{54}{18}=3$. Shaded area $=54-\pi(3)^2=54-9\pi$. ($54-3\pi$ uses $r$; $54-6\pi$ uses the circumference; $54-36\pi$ uses $d=6$ as the radius.)",
   fig="incircle", figdesc="right triangle with legs 9 and 12 and an inscribed circle")

mc(2, 'H',
   r"A circle in the $xy$-plane has center $(-4,6)$ and is tangent to the line $y=-2$. An equation of the circle is $(x+4)^2+(y-6)^2=k$. What is the value of $k$?",
   C(64), [C(8), C(16), C(36)],
   lambda: (6 - (-2)) ** 2,
   "Tangent to a horizontal line: $r=|k_{\\text{center}}-\\text{line}|$",
   r"The radius is the vertical distance from $(-4,6)$ to $y=-2$: $6-(-2)=8$. So $k=r^2=64$. ($8$ is $r$; $36$ is tangent to the $x$-axis instead; $16$ uses $6-2=4$.)")

gi(2, 'H',
   r"Segment $\overline{PQ}$ with endpoints $P(1,2)$ and $Q(9,8)$ is a diameter of a circle in the $xy$-plane. The circle has equation $x^2+y^2+ax+by+c=0$, where $a$, $b$ and $c$ are constants. What is the value of $a+b+c$?",
   "5", Integer(5),
   lambda: (lambda e: e.coeff(x, 1) + e.coeff(y, 1) + e.subs({x: 0, y: 0}))(
       expand((x - Rational(1 + 9, 2)) ** 2 + (y - Rational(2 + 8, 2)) ** 2 - (Rational((9 - 1) ** 2 + (8 - 2) ** 2, 4)))),
   "Midpoint $=$ center, half the distance $=r$",
   r"Center $=(5,5)$; $r^2=\frac{8^2+6^2}{4}=25$. So $(x-5)^2+(y-5)^2=25$, i.e. $x^2+y^2-10x-10y+25=0$. Then $a+b+c=-10-10+25=5$. (The constant term is $25$, not $25-25=0$.)")

mc(2, 'H',
   r"In the $xy$-plane, the line $y=x+k$ is tangent to the circle $x^2+y^2=18$. Which of the following could be the value of $k$?",
   C(6), [C(3 * sqrt(2)), C(9), C(18)],
   lambda: None,
   "Tangent: distance from center to line $=r$",
   r"Write the line as $x-y+k=0$. Its distance from the origin is $\frac{|k|}{\sqrt2}$, which must equal $r=\sqrt{18}=3\sqrt2$. So $|k|=6$. ($3\sqrt2$ forgets the $\sqrt2$ in the distance; $18$ is $r^2$; $9$ is half of $18$.)", order=3,
   each=lambda v: simplify(v ** 2 / 2 - 18) == 0)

# ============================================================ SET 3  (Areas: shaded, composite, scaling; 14)
mc(3, 'H',
   r"Two circles share the same center. A chord of the larger circle is tangent to the smaller circle and has length $24$ (see the figure). What is the area of the region between the two circles?",
   C(144 * pi), [C(12 * pi), C(288 * pi), C(576 * pi)],
   lambda: (lambda vals: vals.pop() if len(set(vals)) == 1 else None)([pi * ((rr * rr + 12 ** 2) - rr * rr) for rr in (3, 5, 9, 20)]),
   "Half-chord is the leg of a right triangle: $R^2-r^2=(\\text{half-chord})^2$",
   r"At the tangent point the radius is perpendicular to the chord and bisects it, so $R^2=r^2+12^2$. Ring area $=\pi R^2-\pi r^2=\pi(12^2)=144\pi$, whatever $r$ is. ($12\pi$ forgets to square; $288\pi$ and $576\pi$ use $24^2$ with a factor slip.)", order='L',
   fig="annulus", figdesc="two concentric circles; a chord of the outer circle of length 24 touches the inner circle")

mc(3, 'H',
   r"Four congruent circles lie inside a square of side $20$. Each circle touches the two nearest sides of the square and the two neighboring circles (see the figure). What is the area of the part of the square outside all four circles?",
   C(400 - 100 * pi), [C(400 - 25 * pi), C(400 - 40 * pi), C(400 - 400 * pi)],
   lambda: 20 ** 2 - 4 * pi * (Rational(20, 4)) ** 2,
   "Side $=4r$ when two circles span it",
   r"Along one side, two circles fit across: $4r=20$, so $r=5$. Circles total $4\pi(5)^2=100\pi$; shaded area $=400-100\pi$. ($400-25\pi$ counts one circle; $400-40\pi$ uses circumferences; $400-400\pi$ takes $r=10$.)",
   fig="fourcircles", figdesc="square of side 20 containing four equal circles in a 2 by 2 arrangement")

mc(3, 'H',
   r"The figure shows a region made of a rectangle and two semicircles, one on each of the two short sides of the rectangle. The long side of the rectangle is $3$ times the short side. The perimeter of the whole region is $48+8\pi$. What is the area of the region?",
   C(192 + 16 * pi), [C(192 + 8 * pi), C(192 + 32 * pi), C(192 + 64 * pi)],
   lambda: (lambda ww: 3 * ww * ww + pi * (ww / 2) ** 2)(solve((6 + pi) * w - (48 + 8 * pi), w)[0]),
   "Two semicircles $=$ one circle; perimeter fixes the width",
   r"With short side $w$: perimeter $=2(3w)+\pi w=(6+\pi)w=48+8\pi$, so $w=8$. Area $=24\cdot8+\pi(4)^2=192+16\pi$. ($192+8\pi$ counts one semicircle; $192+32\pi$ and $192+64\pi$ use $r=8$.)",
   fig="stadium", figdesc="rectangle with a semicircle on each short side; long side is 3 times the short side w")

gi(3, 'H',
   r"Square $ABCD$ has side length $12$. One arc of radius $12$ is centered at $A$ and passes through $B$ and $D$. A second arc of radius $12$ is centered at $C$ and also passes through $B$ and $D$ (see the figure). The area of the shaded region where the two arcs overlap is $a\pi-b$. What is the value of $a+b$?",
   "216", Integer(216),
   lambda: lens_check(12),
   "Overlap $=$ two quarter-circles $-$ the square",
   r"The two quarter-circles together cover the square once and the lens twice, so lens $=2\left(\frac14\pi\cdot12^2\right)-12^2=72\pi-144$. Hence $a=72$, $b=144$ and $a+b=216$.",
   fig="lens", figdesc="square ABCD of side 12 with two quarter-circle arcs centered at A and at C; the lens between them is shaded")

mc(3, 'H',
   r"A square with side length $10$ is inscribed in a circle (all four vertices lie on the circle). What is the area of the region inside the circle but outside the square?",
   C(50 * pi - 100), [C(50 * pi), C(100 * pi - 100), C(200 * pi - 100)],
   lambda: pi * (sqrt(Integer(10 ** 2 + 10 ** 2)) / 2) ** 2 - 100,
   "Diagonal of the square $=$ diameter",
   r"The diagonal $10\sqrt2$ is the diameter, so $r=5\sqrt2$ and the circle has area $\pi(50)=50\pi$. Subtract the square: $50\pi-100$. ($50\pi$ forgets to subtract; $100\pi-100$ takes $r=10$; $200\pi-100$ takes $r=10\sqrt2$.)")

mc(3, 'H',
   r"Two circles have the same center. The radius of the larger circle is $25\%$ greater than the radius of the smaller circle. The region between the circles is what percent of the area of the larger circle?",
   C(r"36\%", 36), [C(r"25\%", 25), C(r"56.25\%", R(225, 4)), C(r"64\%", 64)],
   lambda: pct(1 - 1 / (R(5, 4)) ** 2),
   "Areas go with $(\\text{radius})^2$",
   r"Let the small radius be $1$ and the large one $1.25$. Areas: $1$ and $1.5625$. Ring share $=\frac{1.5625-1}{1.5625}=0.36$, i.e. $36\%$. ($64\%$ is the inner disk; $56.25\%$ compares the ring with the inner disk; $25\%$ is the radius change.)", order=3)

mc(3, 'H',
   r"In the figure, $O$ is the center of a circle of radius $6$ and $\angle AOB=60^\circ$. What is the area of the shaded region bounded by chord $\overline{AB}$ and the minor arc $AB$?",
   C(6 * pi - 9 * sqrt(3)), [C(6 * pi), C(6 * pi - 9), C(6 * pi - 18 * sqrt(3))],
   lambda: R(60, 360) * pi * 36 - R(1, 2) * 6 * 6 * sqrt(3) / 2,
   "Segment $=$ sector $-$ triangle",
   r"Sector: $\frac16\pi(36)=6\pi$. Triangle $OAB$ is equilateral with side $6$: area $\frac{\sqrt3}{4}(36)=9\sqrt3$. Segment $=6\pi-9\sqrt3$. ($6\pi$ is the sector alone; $6\pi-9$ drops the $\sqrt3$; $6\pi-18\sqrt3$ doubles the triangle.)",
   fig="segment", figdesc="circle of radius 6 with center O, central angle AOB = 60 degrees, and the segment between chord AB and the minor arc shaded")

gi(3, 'H',
   r"The radius of a circle is increased by $p\%$, and as a result the area of the circle increases by $69\%$. What is the value of $p$?",
   "30", Integer(30),
   lambda: (sqrt(R(169, 100)) - 1) * 100,
   "Area factor $=(\\text{radius factor})^2$",
   r"$(1+\frac p{100})^2=1.69$, so $1+\frac p{100}=1.3$ and $p=30$. (Halving $69$ to get $34.5$ ignores the squaring.)")

mc(3, 'H',
   r"An equilateral triangle with side length $6$ is inscribed in a circle (all three vertices lie on the circle). What is the area of the circle?",
   C(12 * pi), [C(3 * pi), C(9 * pi), C(36 * pi)],
   lambda: pi * (R(6) / sqrt(3)) ** 2,
   "Circumradius of an equilateral triangle $=\\frac{a}{\\sqrt3}$",
   r"The center is also the centroid, at distance $\frac23$ of the altitude $3\sqrt3$ from a vertex: $r=2\sqrt3$. Area $=\pi(2\sqrt3)^2=12\pi$. ($3\pi$ uses the inradius $\sqrt3$; $9\pi$ uses $r=3$; $36\pi$ uses $r=6$.)")

mc(3, 'H',
   r"Two circles with radii $4$ and $9$ are externally tangent. A line is tangent to the smaller circle at $P$ and to the larger circle at $Q$, and both circles lie on the same side of the line (see the figure). What is the length of $\overline{PQ}$?",
   C(12), [C(5), C(6), C(13)],
   lambda: sqrt(Integer((4 + 9) ** 2 - (9 - 4) ** 2)),
   "Common tangent: right triangle with legs $PQ$ and $r_2-r_1$",
   r"Draw a segment from $O_1$ parallel to $PQ$. It forms a right triangle with hypotenuse $O_1O_2=4+9=13$ and one leg $9-4=5$, so $PQ=\sqrt{13^2-5^2}=12$. ($13$ is the center distance; $5$ is the radius difference; $6=\sqrt{4\cdot9}$ forgets the factor $2$.)",
   fig="twocircles", figdesc="two externally tangent circles, radii 4 and 9, with a common external tangent line touching them at P and Q")

gi(3, 'H',
   r"The radii of two circles are in the ratio $2:3$. The sum of the areas of the two circles is $52\pi$. What is the radius of the smaller circle?",
   "4", Integer(4),
   lambda: 2 * solve(13 * k ** 2 - 52, k)[-1],
   "Ratio $2k:3k$, then add the squares",
   r"Radii $2k$ and $3k$: $\pi(4k^2+9k^2)=13\pi k^2=52\pi$, so $k=2$ and the smaller radius is $2k=4$. (Not $k=2$, and not $6$, the larger radius.)")

mc(3, 'H',
   r"A rectangle with sides $16$ and $12$ is inscribed in a circle (all four vertices lie on the circle). What is the area of the region inside the circle but outside the rectangle?",
   C(100 * pi - 192), [C(64 * pi - 192), C(100 * pi - 96), C(400 * pi - 192)],
   lambda: pi * (sqrt(Integer(16 ** 2 + 12 ** 2)) / 2) ** 2 - 16 * 12,
   "Diagonal of the rectangle $=$ diameter",
   r"The diagonal is $\sqrt{16^2+12^2}=20$, so $r=10$ and the circle has area $100\pi$. Subtract $16\cdot12=192$. ($64\pi-192$ uses half the long side as $r$; $100\pi-96$ subtracts half the rectangle; $400\pi-192$ uses the diagonal as $r$.)")

gi(3, 'H',
   r"A circular rug has a diameter of $240$ centimeters. Its area is $k\pi$ square meters. What is the value of $k$?",
   "1.44", R(144, 100),
   lambda: (R(240, 100) / 2) ** 2,
   "Convert length first, then square",
   r"$240$ cm $=2.4$ m, so $r=1.2$ m and the area is $\pi(1.2)^2=1.44\pi$ m$^2$. (Using $1\ \text{m}^2=100\ \text{cm}^2$ would give $144$.)")

mc(3, 'H',
   r"Circle $A$ is inscribed in a square (it touches all four sides). Circle $B$ is circumscribed about the same square (it passes through all four vertices). The area of circle $B$ is how many times the area of circle $A$?",
   C(2), [C(sqrt(2)), C(4), C(2 * sqrt(2))],
   lambda: (pi * (R(7) * sqrt(2) / 2) ** 2) / (pi * (R(7, 2)) ** 2),
   "Radius ratio $\\sqrt2$, area ratio $(\\sqrt2)^2$",
   r"For side $s$: $r_A=\frac s2$ and $r_B=\frac{s\sqrt2}2$, so $r_B=\sqrt2\,r_A$. Areas scale with the square: $(\sqrt2)^2=2$. ($\sqrt2$ is the radius ratio; $4$ squares twice; $2\sqrt2$ cubes.)", order='L')

# ============================================================ SET 4  (Solids: volume, surface area, filling, recasting; 14)
mc(4, 'H',
   r"A right circular cylinder with radius $5$ and height $12$ has the same volume as a second right circular cylinder with height $3$. What is the radius of the second cylinder?",
   C(10), [C(20), C(25), C(100)],
   lambda: sqrt(Integer(5 ** 2 * 12) / 3),
   "Equal volumes: $r^2h$ matches, so $r^2$ scales like $1/h$",
   r"$\pi(5^2)(12)=\pi r^2(3)$ gives $r^2=100$ and $r=10$. (The height drops by a factor of $4$, so the radius \emph{doubles}, not $\times4$ ($20$); $25$ is $r_1^2$; $100$ is $r_2^2$.)")

mc(4, 'H',
   r"A right circular cone has slant height $13$ and a base with diameter $10$. What is the volume of the cone?",
   C(100 * pi), [C(300 * pi), C(R(325, 3) * pi), C(R(1300, 3) * pi)],
   lambda: R(1, 3) * pi * 5 ** 2 * sqrt(Integer(13 ** 2 - 5 ** 2)),
   "Slant height is not the height: $h=\\sqrt{l^2-r^2}$",
   r"$r=5$, so $h=\sqrt{13^2-5^2}=12$ and $V=\frac13\pi(25)(12)=100\pi$. ($300\pi$ forgets the $\frac13$; $\frac{325\pi}3$ uses the slant height $13$ as $h$; $\frac{1300\pi}3$ also uses $r=10$.)")

gi(4, 'H',
   r"A cylindrical tank has a base radius of $4$ decimeters and contains some water. A solid metal sphere of radius $3$ decimeters is lowered into the tank and sinks completely below the surface (no water spills). By how many decimeters does the water level rise? (Enter the exact decimal.)",
   "2.25", R(9, 4),
   lambda: (R(4, 3) * pi * 3 ** 3) / (pi * 4 ** 2),
   "Displaced volume $=$ base area $\\times$ rise",
   r"The sphere displaces $\frac43\pi(3)^3=36\pi$ dm$^3$. This equals $\pi(4)^2\cdot h$, so $h=\frac{36}{16}=2.25$.")

mc(4, 'H',
   r"A solid metal cylinder with radius $6$ and height $8$ is melted and recast into solid spheres, each with radius $2$, with no metal lost. How many spheres are made?",
   C(27), [C(9), C(36), C(54)],
   lambda: (pi * 6 ** 2 * 8) / (R(4, 3) * pi * 2 ** 3),
   "Volume is conserved: divide total by one piece",
   r"Cylinder: $\pi(36)(8)=288\pi$. One sphere: $\frac43\pi(8)=\frac{32\pi}3$. Number $=288\pi\div\frac{32\pi}3=27$. ($9$ forgets the $\frac13$; $36$ uses $\pi r^3$; $54$ uses $\frac43\pi r^2$.)")

mc(4, 'H',
   r"A scale model of a building is built at a scale of $1:50$, so every length on the model is $\frac1{50}$ of the matching length on the real building. The floor area of the model is $0.6$ square meters. What is the floor area, in square meters, of the real building?",
   C("1{,}500", 1500), [C("0.012", R(12, 1000)), C(30), C("75{,}000", 75000)],
   lambda: R(6, 10) * 50 ** 2,
   "Areas scale by $k^2$",
   r"Real lengths are $50$ times the model's, so real areas are $50^2=2500$ times: $0.6\times2500=1500$ m$^2$. ($30$ multiplies by $50$; $75{,}000$ by $50^3$; $0.012$ divides by $50$.)")

mc(4, 'H',
   r"A square pyramid has a base with side length $10$ and a height of $12$, with its apex directly above the center of the base. What is the total surface area of the pyramid (the four triangular faces plus the base)?",
   C(360), [C(260), C(340), C(620)],
   lambda: 10 ** 2 + 4 * R(1, 2) * 10 * sqrt(Integer(12 ** 2 + 5 ** 2)),
   "Face height is the slant height $\\sqrt{h^2+(\\frac s2)^2}$",
   r"Each face has height $\sqrt{12^2+5^2}=13$ (slant height), so its area is $\frac12(10)(13)=65$. Total $=100+4(65)=360$. ($260$ omits the base; $340$ uses $12$ as the face height; $620$ drops the $\frac12$.)")

gi(4, 'H',
   r"A container is an inverted right circular cone (point down) with height $12$ (see the figure). It is filled with water to a depth of $6$. The water fills what percent of the container's volume? (Enter the number without the percent sign.)",
   "12.5", R(25, 2),
   lambda: pct(R(6, 12) ** 3),
   "Half the height is $k=\\frac12$: volume $\\times k^3$",
   r"The water forms a smaller cone similar to the container with scale factor $\frac12$, so its volume is $(\frac12)^3=\frac18=12.5\%$ of the whole, not $50\%$.",
   fig="conewater", figdesc="side view of an inverted cone of height 12 and top radius 5 holding water to depth 6")

mc(4, 'H',
   r"A rectangular tank has a base that measures $2$ meters by $1.5$ meters. Water flows into the tank at a constant rate of $45$ liters per minute. How many minutes does it take for the water level to rise $0.3$ meter? ($1$ cubic meter $=1000$ liters)",
   C(20), [C("0.02", R(2, 100)), C(2), C(200)],
   lambda: (R(2) * R(3, 2) * R(3, 10) * 1000) / 45,
   "Convert to one unit before dividing",
   r"Volume needed: $2(1.5)(0.3)=0.9$ m$^3=900$ L. Time $=\frac{900}{45}=20$ min. ($0.02$ leaves the volume in m$^3$; $2$ and $200$ slip a factor of $10$.)")

mc(4, 'H',
   r"The surface area of a sphere is increased by $125\%$. By what percent does the volume of the sphere increase?",
   C(r"237.5\%", R(475, 2)), [C(r"125\%", 125), C(r"337.5\%", R(675, 2)), C(r"406.25\%", R(1625, 4))],
   lambda: ((1 + R(125, 100)) ** R(3, 2) - 1) * 100,
   "Area $\\times k^2$, volume $\\times k^3$: $k=\\sqrt{\\text{area factor}}$",
   r"Area factor $2.25=k^2$, so $k=1.5$. Volume factor $k^3=3.375$, an increase of $237.5\%$. ($125\%$ copies the area change; $337.5\%$ is the factor, not the increase; $406.25\%$ squares $2.25$.)")

gi(4, 'H',
   r"A closed right circular cylinder has a height of $10$ and a total surface area of $192\pi$ (both circular bases and the curved side). What is the radius of the cylinder?",
   "6", Integer(6),
   lambda: [rt for rt in solve(2 * pi * r ** 2 + 2 * pi * r * 10 - 192 * pi, r) if rt > 0][0],
   "Surface area gives a quadratic in $r$",
   r"$2\pi r^2+2\pi r(10)=192\pi\Rightarrow r^2+10r-96=0\Rightarrow(r+16)(r-6)=0$. A radius is positive, so $r=6$. (Dropping the two bases gives $9.6$; $16$ is the negative root's size.)")

gi(4, 'H',
   r"A circular sector with radius $10$ and central angle $288^\circ$ is cut out of paper, and its two straight edges are joined to form a right circular cone. The volume of the cone is $k\pi$. What is the value of $k$?",
   "128", Integer(128),
   lambda: (lambda rb: R(1, 3) * rb ** 2 * sqrt(Integer(100) - rb ** 2))(R(288, 360) * 10),
   "Sector radius becomes the slant height; arc becomes the base circumference",
   r"The arc is $\frac{288}{360}(2\pi\cdot10)=16\pi$, which is the base circumference $2\pi r$, so $r=8$. The slant height is $10$, so $h=\sqrt{100-64}=6$. $V=\frac13\pi(64)(6)=128\pi$.")

mc(4, 'H',
   r"A sphere fits snugly inside a right circular cylinder: it touches the top, the bottom and the curved side of the cylinder (see the figure). The volume of the cylinder is $432\pi$. What is the volume of the sphere?",
   C(288 * pi), [C(144 * pi), C(216 * pi), C(576 * pi)],
   lambda: R(4, 3) * pi * cbrt(Integer(432) / 2) ** 3,
   "Height $=2r$, so cylinder $=2\\pi r^3$ and sphere $=\\frac23$ of it",
   r"The cylinder has height $2r$: $\pi r^2(2r)=2\pi r^3=432\pi$, so $r^3=216$. Sphere $=\frac43\pi r^3=288\pi$, which is $\frac23$ of the cylinder. ($144\pi$ is the empty space; $216\pi$ is half; $576\pi$ is $\frac43$ of the cylinder.)",
   fig="spherecyl", figdesc="side view of a cylinder with a sphere touching its top, bottom and sides")

mc(4, 'H',
   r"A rectangular tank has a base $40$ cm by $25$ cm and contains water to a depth of $8$ cm. A solid cube with edge length $10$ cm is placed flat on the bottom of the tank. To the nearest tenth of a centimeter, what is the new depth of the water, measured from the bottom of the tank?",
   C("8.9", R(89, 10)), [C("8.0", 8), C("9.0", 9), C("10.0", 10)],
   lambda: next(rnd(d, 1) for d in [R(8000, 1000 - 100)] if d < 10),
   "Check if the object is submerged before adding its volume",
   r"Water volume $=40\cdot25\cdot8=8000$ cm$^3$. If the cube were fully covered the depth would be $\frac{9000}{1000}=9<10$, a contradiction. So the water is below the top of the cube and covers a base of $1000-100=900$: depth $=\frac{8000}{900}\approx8.9$. ($8.0$ ignores the cube; $9.0$ assumes it is submerged.)")

mc(4, 'H',
   r"A cylindrical can has a diameter of $8$ centimeters and a height of $15$ centimeters. To the nearest hundredth of a liter, how much does the can hold when full? ($1$ liter $=1000$ cubic centimeters)",
   C("0.75", R(75, 100)), [C("0.19", R(19, 100)), C("3.01", R(301, 100)), C("7.54", R(754, 100))],
   lambda: rnum(pi * 4 ** 2 * 15 / 1000, 2),
   "Diameter $\\to$ radius, then cm$^3\\to$ L",
   r"$r=4$, so $V=\pi(16)(15)=240\pi\approx753.98$ cm$^3\approx0.75$ L. ($3.01$ uses $d=8$ as $r$; $0.19$ uses $r=2$; $7.54$ divides by $100$ instead of $1000$.)")

# ============================================================ SET 5  (Summit, 20)
def _circle3():
    D, E, F = symbols('D E F')
    sl = solve([F, 144 + 12 * D + F, 25 + 5 * E + F], [D, E, F], dict=True)[0]
    return sqrt(sl[D] ** 2 / 4 + sl[E] ** 2 / 4 - sl[F])

def _chords_r():
    # bisection: sqrt(r^2-25)+sqrt(r^2-144)=17  (half-chords 12 and 5)
    lo, hi = 12.0, 100.0
    for _ in range(200):
        mid = (lo + hi) / 2
        if math.sqrt(mid * mid - 144) + math.sqrt(mid * mid - 25) < 17:
            lo = mid
        else:
            hi = mid
    return Integer(round(lo))

gi(5, 'H',
   r"Two parallel chords of a circle have lengths $24$ and $10$. The chords lie on opposite sides of the center of the circle, and the distance between the chords is $17$ (see the figure). What is the radius of the circle?",
   "13", Integer(13),
   _chords_r,
   "Two right triangles sharing $r$, with $d_1+d_2=17$",
   r"Half-chords are $12$ and $5$. If the center is $d_1$ from the long chord, then $r^2=12^2+d_1^2=5^2+(17-d_1)^2$, so $144+d_1^2=25+289-34d_1+d_1^2$, giving $d_1=5$. Then $r=\sqrt{144+25}=13$.",
   fig="parallel", figdesc="circle with center O between two parallel chords of length 24 and 10 that are 17 apart")

def _two_circles_area():
    tot = 0
    for rr in solve((2 - r) ** 2 + (1 - r) ** 2 - r ** 2, r):
        tot += pi * rr ** 2
    return simplify(tot)

mc(5, 'H',
   r"In the first quadrant of the $xy$-plane, two different circles are each tangent to both the $x$-axis and the $y$-axis, and each passes through the point $(2,1)$. What is the sum of the areas of the two circles?",
   C(26 * pi), [C(25 * pi), C(6 * pi), C(36 * pi)],
   _two_circles_area,
   "Tangent to both axes: center $(r,r)$",
   r"The center is $(r,r)$ and the circle passes through $(2,1)$: $(2-r)^2+(1-r)^2=r^2$, i.e. $r^2-6r+5=0$, so $r=1$ or $r=5$. Areas: $\pi+25\pi=26\pi$. ($25\pi$ counts only the larger circle; $36\pi$ squares the sum $1+5$; $6\pi$ multiplies the sum of radii by $\pi$.)", order=0)

gi(5, 'H',
   r"A sector of a circle has area $12$ and arc length $6$. What is the measure, in radians, of the central angle of the sector?",
   "1.5", R(3, 2),
   lambda: (lambda rad: R(6) / rad)(R(2 * 12, 6)),
   "Sector area $=\\frac12\\,r\\cdot(\\text{arc})$",
   r"For a sector, $A=\frac12rs$: $12=\frac12r(6)$ gives $r=4$. Then $\theta=\frac sr=\frac64=1.5$ radians.")

def _chord_angle():
    arcs = (36, 72, 108, 144)
    a = [0]
    for v in arcs[:-1]:
        a.append(a[-1] + v)
    pts = [(math.cos(math.radians(t)), math.sin(math.radians(t))) for t in a]
    A, B, C_, D = pts
    # intersection of AC and BD
    def inter(p1, p2, p3, p4):
        d1 = (p2[0] - p1[0], p2[1] - p1[1]); d2 = (p4[0] - p3[0], p4[1] - p3[1])
        den = d1[0] * d2[1] - d1[1] * d2[0]
        tt = ((p3[0] - p1[0]) * d2[1] - (p3[1] - p1[1]) * d2[0]) / den
        return (p1[0] + tt * d1[0], p1[1] + tt * d1[1])
    Pp = inter(A, C_, B, D)
    va = (A[0] - Pp[0], A[1] - Pp[1]); vb = (B[0] - Pp[0], B[1] - Pp[1])
    ang = math.degrees(math.acos((va[0] * vb[0] + va[1] * vb[1]) / (math.hypot(*va) * math.hypot(*vb))))
    return Integer(round(ang))

mc(5, 'H',
   r"Four points $A$, $B$, $C$, $D$ lie in this order on a circle so that the arcs $AB$, $BC$, $CD$ and $DA$ (the arcs between consecutive points that contain no other of the four points) are in the ratio $1:2:3:4$. Chords $\overline{AC}$ and $\overline{BD}$ intersect at point $P$ inside the circle (see the figure). What is the measure, in degrees, of $\angle APB$?",
   C(r"72^\circ", 72), [C(r"36^\circ", 36), C(r"108^\circ", 108), C(r"144^\circ", 144)],
   _chord_angle,
   "Exterior angle of $\\triangle PBC$ $=$ two inscribed angles",
   r"The ratio $1:2:3:4$ splits $360^\circ$ into arcs $36,72,108,144$. $\angle APB=\angle PCB+\angle PBC$ (exterior angle) $=\frac{36}2+\frac{108}2=72^\circ$, which is $\frac12(\text{arc }AB+\text{arc }CD)$. ($36$ is arc $AB$; $144$ is arc $DA$; $108$ is arc $CD$.)",
   fig="chords", figdesc="circle with four points A, B, C, D in order and chords AC and BD crossing at P; angle APB marked with a question mark")

mc(5, 'H',
   r"A cylindrical tank has a radius of $3$ meters and a height of $4$ meters and is initially empty. An inlet pipe adds water at a constant rate of $6\pi$ cubic meters per hour while a drain removes water at a constant rate of $2\pi$ cubic meters per hour. Both run at the same time. How many hours does it take for the tank to be completely full?",
   C(9), [C("4.5", R(9, 2)), C(6), C(18)],
   lambda: (pi * 3 ** 2 * 4) / (6 * pi - 2 * pi),
   "Net rate $=$ in $-$ out",
   r"Capacity $=\pi(9)(4)=36\pi$ m$^3$; net rate $=6\pi-2\pi=4\pi$ m$^3$/h; time $=\frac{36\pi}{4\pi}=9$ h. ($4.5$ adds the drain rate; $6$ ignores the drain; $18$ uses the drain rate alone.)")

mc(5, 'H',
   r"A solid sphere has a volume of $4500\pi$ cubic centimeters. A plane cuts the sphere at a distance of $9$ centimeters from the center of the sphere. What is the area, in square centimeters, of the circular cross-section made by the plane?",
   C(144 * pi), [C(81 * pi), C(225 * pi), C(306 * pi)],
   lambda: pi * (cbrt(Integer(4500) * 3 / 4) ** 2 - 9 ** 2),
   "Sphere cross-section: $\\rho^2=r^2-d^2$",
   r"$\frac43\pi r^3=4500\pi$ gives $r^3=3375$, $r=15$. The cross-section radius is $\sqrt{15^2-9^2}=12$, so its area is $144\pi$. ($81\pi$ uses the distance $9$ as the radius; $225\pi$ is the great circle; $306\pi=225\pi+81\pi$.)")

mc(5, 'H',
   r"A cube has edge length $6$. A sphere passes through all $8$ vertices of the cube. What is the volume of the sphere?",
   C(108 * sqrt(3) * pi), [C(36 * pi), C(72 * sqrt(2) * pi), C(288 * pi)],
   lambda: R(4, 3) * pi * (sqrt(Integer(6 ** 2 * 3)) / 2) ** 3,
   "Sphere through the vertices: $r=$ half the space diagonal",
   r"The diameter is the space diagonal $6\sqrt3$, so $r=3\sqrt3$ and $V=\frac43\pi(3\sqrt3)^3=\frac43\pi(81\sqrt3)=108\sqrt3\,\pi$. ($36\pi$ is the sphere inside the cube; $72\sqrt2\,\pi$ uses the face diagonal; $288\pi$ uses $r=6$.)", order=1)

gi(5, 'H',
   r"Two similar solids have surface areas of $18$ and $50$. The volume of the smaller solid is $54$. What is the volume of the larger solid?",
   "250", Integer(250),
   lambda: 54 * (sqrt(R(50, 18))) ** 3,
   "Area $\\propto k^2$, volume $\\propto k^3$",
   r"$k^2=\frac{50}{18}=\frac{25}{9}$, so $k=\frac53$. Volume scales by $k^3=\frac{125}{27}$: $54\cdot\frac{125}{27}=250$. (Using $\frac{50}{18}$ directly would give $150$.)")

mc(5, 'H',
   r"The radius of a right circular cylinder is increased by $10\%$ and its height is decreased by $20\%$. Which of the following describes the change in the volume of the cylinder?",
   T(r"Decreases by $3.2\%$", R(-32, 10)), [T(r"Does not change", 0), T(r"Decreases by $10\%$", -10), T(r"Decreases by $12\%$", -12)],
   lambda: ((1 + R(1, 10)) ** 2 * (1 - R(2, 10)) - 1) * 100,
   "Multiply factors; the radius is squared",
   r"Volume factor $=(1.1)^2(0.8)=1.21\times0.8=0.968$, a decrease of $3.2\%$. (``No change'' adds $10+10-20$; $-10\%$ adds $10-20$; $-12\%$ uses $1.1\times0.8$ without squaring the radius.)",
   order='a')

mc(5, 'H',
   r"In the $xy$-plane, a circle has equation $x^2+y^2-4x-6y-12=0$. Point $P$ has coordinates $(15,3)$ and lies outside the circle. A line through $P$ touches the circle at exactly one point $T$. What is the length of $\overline{PT}$?",
   C(12), [C(5), C(8), C(13)],
   lambda: sqrt(Integer((15 - 2) ** 2 + (3 - 3) ** 2) - (4 + 9 + 12)),
   "Tangent length: $PT^2=PO^2-r^2$",
   r"Completing squares: $(x-2)^2+(y-3)^2=25$, center $(2,3)$, $r=5$. $PO=13$. Since $OT\perp PT$, $PT=\sqrt{13^2-5^2}=12$. ($13$ is $PO$; $8=13-5$ is the nearest distance to the circle; $5$ is $r$.)")

gi(5, 'H',
   r"A circle in the $xy$-plane passes through the points $(0,0)$, $(12,0)$ and $(0,5)$. What is the radius of the circle?",
   "6.5", R(13, 2),
   _circle3,
   "Right angle at the origin: the hypotenuse is a diameter",
   r"The legs along the axes meet at $(0,0)$ at a right angle, so the segment from $(12,0)$ to $(0,5)$ is a diameter. Its length is $\sqrt{12^2+5^2}=13$, so $r=\frac{13}2=6.5$.")

mc(5, 'H',
   r"A silo is a right circular cylinder with a hemisphere on top (see the figure). The base radius is $4$ feet, and the total height of the silo, from the ground to the top of the hemisphere, is $10$ feet. What is the volume of the silo, in cubic feet?",
   C(R(416, 3) * pi), [C(224 * pi), C(R(544, 3) * pi), C(R(608, 3) * pi)],
   lambda: pi * 4 ** 2 * (10 - 4) + R(1, 2) * R(4, 3) * pi * 4 ** 3,
   "Total height includes the dome: cylinder height $=10-r$",
   r"The hemisphere has height $4$, so the cylinder part is $6$ tall: $\pi(16)(6)=96\pi$. Hemisphere $=\frac23\pi(64)=\frac{128\pi}3$. Total $=\frac{416\pi}3$. ($\frac{608\pi}3$ uses cylinder height $10$; $\frac{544\pi}3$ uses a full sphere; $224\pi$ uses $2\pi r^3=128\pi$ for the dome.)",
   fig="silo", figdesc="side view of a silo: cylinder of base radius 4 topped by a hemisphere, total height 10")

mc(5, 'H',
   r"A cylindrical can with a radius of $10$ cm holds water to a depth of $9$ cm. All of the water is poured into an empty rectangular box whose base measures $15$ cm by $12$ cm. What is the depth, in cm, of the water in the box?",
   C(5 * pi), [C(5), C(20 * pi), C(50 * pi)],
   lambda: (pi * 10 ** 2 * 9) / (15 * 12),
   "Same volume: $\\pi r^2h=\\ell wd$",
   r"Water volume $=\pi(100)(9)=900\pi$ cm$^3$. Depth $=\frac{900\pi}{15\cdot12}=\frac{900\pi}{180}=5\pi\approx15.7$ cm. ($5$ drops the $\pi$; $20\pi$ uses the diameter as $r$; $50\pi$ slips a factor of $10$.)")

mc(5, 'H',
   r"A circle has radius $9$. The minor arc $AB$ has length $6\pi$. What is the length of chord $\overline{AB}$?",
   C(9 * sqrt(3)), [C(9), C(9 * sqrt(2)), C(18)],
   lambda: 2 * 9 * sin(pi * R(6, 18)),
   "Arc $\\to$ central angle, then the isosceles triangle",
   r"The circumference is $18\pi$, so the arc is $\frac13$ of the circle and the central angle is $120^\circ$. The chord is the base of a $30^\circ$-$30^\circ$-$120^\circ$ triangle with legs $9$: $AB=2\cdot9\sin60^\circ=9\sqrt3$. ($9$ assumes $60^\circ$; $9\sqrt2$ assumes $90^\circ$; $18$ is a diameter.)")

gi(5, 'H',
   r"A regular hexagon with side length $6$ is inscribed in a circle (all six vertices lie on the circle). The area of the region inside the circle but outside the hexagon is $a\pi-b\sqrt3$. What is the value of $a+b$?",
   "90", Integer(90),
   lambda: (lambda e: abs(e.coeff(pi)) + abs(e.coeff(sqrt(3))))(expand(pi * 6 ** 2 - 6 * (sqrt(3) / 4) * 6 ** 2)),
   "Regular hexagon $=6$ equilateral triangles; $r=$ side",
   r"The circumradius equals the side, $6$, so the circle has area $36\pi$. The hexagon is $6$ equilateral triangles: $6\cdot\frac{\sqrt3}4(36)=54\sqrt3$. The region is $36\pi-54\sqrt3$, so $a+b=36+54=90$.")

mc(5, 'H',
   r"A pyramid has a square base with side length $12$ and a height of $9$; its apex is directly above the center of the base. A plane parallel to the base cuts the pyramid at a height of $3$ above the base (see the figure). What is the area of the cross-section?",
   C(64), [C(8), C(16), C(96)],
   lambda: (R(12) * (9 - 3) / 9) ** 2,
   "Cut at height $3$ leaves a similar pyramid of height $6$",
   r"The part above the cut is similar to the whole with scale factor $\frac{9-3}9=\frac23$, so the cross-section has side $8$ and area $64$. ($8$ is the side; $96=144\cdot\frac23$ forgets to square; $16$ uses $\frac39$ as the factor.)", order=1,
   fig="pyramid", figdesc="side view of a pyramid of base 12 and height 9 with a horizontal cut 3 above the base")

gi(5, 'H',
   r"A right circular cone has height $12$. A plane parallel to the base cuts off a small cone at the top; the plane is $4$ units below the apex. The small cone has volume $8\pi$. The remaining solid (the frustum) has volume $k\pi$. What is the value of $k$?",
   "208", Integer(208),
   lambda: 8 * (R(12, 4)) ** 3 - 8,
   "Similar cones: volume $\\times k^3$ with $k=\\frac{12}4=3$",
   r"The whole cone is similar to the small one with scale factor $\frac{12}4=3$, so its volume is $27(8\pi)=216\pi$. Frustum $=216\pi-8\pi=208\pi$, $k=208$. (The frustum is $26$ times the small cone, not $3$ or $9$.)")

mc(5, 'H',
   r"A container is an inverted right circular cone (point down) with top radius $6$ cm and height $9$ cm. It is initially empty and water flows in at a constant rate of $12\pi$ cubic centimeters per minute. How many minutes does it take for the water depth to reach $4.5$ cm?",
   C("1.125", R(9, 8)), [C("4.5", R(9, 2)), C(9), C("13.5", R(27, 2))],
   lambda: (R(1, 3) * pi * (R(6) * R(9, 2) / 9) ** 2 * R(9, 2)) / (12 * pi),
   "Half the depth is only $\\frac18$ of the volume",
   r"At depth $4.5$ the water cone has radius $3$ (similar cone, $k=\frac12$): $V=\frac13\pi(9)(4.5)=13.5\pi$. Time $=\frac{13.5\pi}{12\pi}=1.125$ min. ($4.5$ treats half the depth as half the volume; $9$ is the time to fill the whole cone; $13.5$ forgets to divide by the rate.)")

mc(5, 'H',
   r"Two circles have the same center and radii $4$ and $10$. Two radii of the larger circle form an angle of $72^\circ$. What is the area of the part of the region between the two circles that lies inside this $72^\circ$ angle?",
   C(R(84, 5) * pi), [C(R(12, 5) * pi), C(R(36, 5) * pi), C(84 * pi)],
   lambda: R(72, 360) * pi * (10 ** 2 - 4 ** 2),
   "Fraction of the ring: $\\frac{\\theta}{360}\\pi(R^2-r^2)$",
   r"The angle is $\frac{72}{360}=\frac15$ of the ring, whose area is $\pi(100-16)=84\pi$. So the area is $\frac{84\pi}5=16.8\pi$. ($84\pi$ is the whole ring; $\frac{36\pi}5$ uses $(10-4)^2$; $\frac{12\pi}5$ uses $\frac15$ of $2\pi\cdot6$.)")

mc(5, 'H',
   r"A sector of a circle has an area of $36$ and a central angle of $2$ radians. What is the perimeter of the sector (the arc length plus the two straight edges)?",
   C(24), [C(12), C(18), C(36)],
   lambda: (lambda rad: 2 * rad + rad * 2)(sqrt(Integer(36) * 2 / 2)),
   "Radians: $A=\\frac12r^2\\theta$, arc $=r\\theta$",
   r"$36=\frac12r^2(2)=r^2$, so $r=6$. Arc $=r\theta=12$. Perimeter $=6+6+12=24$. ($12$ is the arc only; $18$ adds just one radius; $36$ is the area.)", order=2)
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
        elif order in ('F', 'L'):
            wsort = sorted(p_['wrongs'], key=lambda it: float(sympify(it[1])))
            pos, out = (0, [p_['right']] + wsort) if order == 'F' else (3, wsort + [p_['right']])
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
                    cands.append((over + unsorted * 1.2 + glob[pos_] * 0.8 + ps[pos_] * 0.3, pos_, out_))
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
    for kk, ff in figs.FIGS.items():
        ff()
    print('figures asserted:', len(figs.FIGS), '; used by problems:', sorted(set(p_['fig'] for p_ in PROBLEMS if p_.get('fig'))))
    unused = set(figs.FIGS) - set(p_['fig'] for p_ in PROBLEMS if p_.get('fig'))
    if unused:
        print('UNUSED FIGURES', unused); fails += 1
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
