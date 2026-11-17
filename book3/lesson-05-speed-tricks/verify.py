#!/usr/bin/env python3
"""Book 3, Lesson 5 "Speed tricks": the problem bank AND its verifier.

Every problem is registered with:
  * its stem and choices (LaTeX),
  * a worked solution that uses the SHORTCUT (this is what students see),
  * a `calc` function that recomputes the answer the LONG way (solve / expand /
    scan numerically with sympy), independent of the shortcut.

Running `python3 verify.py` recomputes every answer and prints OK / FAIL.
(`build.py`-style tools import PROBLEMS from this file to write problems.md and the .tex files.)
"""
import sys
from fractions import Fraction
from sympy import (Symbol, symbols, Rational, Integer, sqrt, solve, simplify, expand, factor, Poly,
                   diff, Eq, S, log, nsimplify, N as numeric, Abs, oo, sympify, degree)

x, y, z, a, b, c, d, k, m, p, q, r, s, t = symbols('x y z a b c d k m p q r s t', real=True)

PROBLEMS = []      # filled below, in order
SET_TITLES = {
    1: ("Set 1", "Bridge: ask first, then shortcut", "Medium and Hard"),
    2: ("Set 2", "Vieta: sums and products without solving", "Hard"),
    3: ("Set 3", "Vertex, axis, symmetry and graph-it", "Hard"),
    4: ("Set 4", "Do not solve: systems, factors and structure", "Hard"),
    5: ("Set 5", "Summit: the hardest mixed problems", "Hard"),
}

# ---------------------------------------------------------------- helpers
def C(tex_or_val, val=None):
    """Choice: C(66) or C(r"\\dfrac14", Rational(1,4)) -> (latex, value)."""
    if val is None:
        v = tex_or_val
        from sympy import latex
        return ("$%s$" % latex(sympify(v)), sympify(v))
    return ("$%s$" % tex_or_val, val)

def T(text):
    return (text, text)

def same(u, v):
    if isinstance(u, str) or isinstance(v, str):
        return u == v
    return simplify(sympify(u) - sympify(v)) == 0

def mc(sett, diff_, stem, right, wrongs, calc, trick, sol, order='a'):
    PROBLEMS.append(dict(set=sett, diff=diff_, kind='mc', stem=stem, right=right, wrongs=wrongs,
                         calc=calc, trick=trick, sol=sol, order=order))

def gi(sett, diff_, stem, ans_tex, ans_val, calc, trick, sol):
    PROBLEMS.append(dict(set=sett, diff=diff_, kind='gi', stem=stem, ans_tex=ans_tex, ans_val=ans_val,
                         calc=calc, trick=trick, sol=sol))

def monic(e):
    return expand(e / Poly(e, x).LC())

def count_sign_changes(f, lo=-60, hi=60, n=240001):
    """Number of real roots of f on [lo,hi] by sign changes (crossings) plus exact zeros."""
    cnt = 0
    h = (hi - lo) / (n - 1)
    prev = f(lo)
    for i in range(1, n):
        xv = lo + i * h
        v = f(xv)
        if prev == 0 or prev * v < 0:
            cnt += 1
        prev = v
    return cnt

def bisect_root(f, lo, hi):
    for _ in range(200):
        mid = (lo + hi) / 2
        if f(lo) * f(mid) <= 0:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2

# ============================================================ SET 1  (Medium/Hard, 12)
mc(1, 'M',
   r"If $5x-3=22$, what is the value of $15x-9$?",
   C(66), [C(5), C(22), C(57)],
   lambda: (lambda xs: 15*xs - 9)(solve(5*x - 3 - 22, x)[0]),
   "What is asked?",
   r"$15x-9=3(5x-3)=3\cdot22=66$. There is no need to find $x$ (it is 5).", order='a')

mc(1, 'M',
   r"$3x+2y=19$ and $2x+3y=11$. What is the value of $x+y$?",
   C(6), [C(7), C(8), C(30)],
   lambda: (lambda sol: sol[x] + sol[y])(solve([3*x + 2*y - 19, 2*x + 3*y - 11], [x, y])),
   "Add the equations",
   r"Add the equations: $5x+5y=30$, so $x+y=6$. (Subtracting would give $x-y=8$, the other trap.)", order='a')

gi(1, 'M',
   r"What is the sum of the solutions of $3x^2-21x+10=0$?",
   "7", Integer(7),
   lambda: sum(solve(3*x**2 - 21*x + 10, x)),
   "Vieta",
   r"Sum of roots $=-\dfrac ba=\dfrac{21}{3}=7$. (The discriminant is positive, so both roots are real.)")

mc(1, 'M',
   r"If $2^{x+1}+2^{x}=48$, what is the value of $x$?",
   C(4), [C(3), C(5), C(16)],
   lambda: log(solve(3*Symbol('u') - 48, Symbol('u'))[0], 2),
   "Backsolve",
   r"Try the middle choices: $x=4$ gives $2^5+2^4=32+16=48$. (Or: $3\cdot2^x=48$, $2^x=16$. Choice 16 is $2^x$, not $x$.)", order='a')

mc(1, 'M',
   r"A price is increased by $30\%$, and then the new price is decreased by $10\%$. The final price is what percent of the original price?",
   C(r"117\%", 117), [C(r"103\%", 103), C(r"120\%", 120), C(r"130\%", 130)],
   lambda: 100 * Rational(130, 100) * Rational(90, 100),
   "Percent multiplier",
   r"Multipliers multiply: $1.30\times0.90=1.17$, so $117\%$. (Adding $+30\%-10\%$ gives the trap $120\%$.)", order='d')

gi(1, 'H',
   r"The polynomial $p(x)=2x^3-5x^2+kx+12$ is divisible by $x-2$, where $k$ is a constant. What is the value of $k$?",
   "-4", Integer(-4),
   lambda: solve(Poly(2*x**3 - 5*x**2 + k*x + 12, x).rem(Poly(x - 2, x)).as_expr(), k)[0],
   "Factor / remainder theorem",
   r"Divisible by $x-2$ means $p(2)=0$: $16-20+2k+12=0$, so $2k=-8$ and $k=-4$.")

mc(1, 'H',
   r"The function $h$ is defined by $h(x)=-3(x-2)(x+8)$. At what value of $x$ does $h$ reach its maximum?",
   C(-3), [C(-8), C(2), C(48)],
   lambda: solve(diff(-3*(x - 2)*(x + 8), x), x)[0],
   "Axis = midpoint of the roots",
   r"The zeros are $2$ and $-8$; the vertex is halfway between them: $\dfrac{2+(-8)}2=-3$. (48 is $h(0)$.)", order='a')

mc(1, 'H',
   r"What is the sum of all solutions of $(x-7)(x+3)=5(x-7)$?",
   C(9), [C(2), C(7), C(14)],
   lambda: sum(solve((x - 7)*(x + 3) - 5*(x - 7), x)),
   "Do not divide: factor",
   r"Move everything left and factor: $(x-7)(x+3-5)=(x-7)(x-2)=0$, so $x=7$ or $2$ and the sum is $9$. Dividing by $x-7$ would lose the root $7$.", order='a')

gi(1, 'H',
   r"If $x+y=9$ and $xy=14$, what is the value of $x^2+y^2$?",
   "53", Integer(53),
   lambda: (lambda sols: sum(v**2 for v in sols))(solve(x**2 - 9*x + 14, x)),
   "Structure (identities)",
   r"$x^2+y^2=(x+y)^2-2xy=81-28=53$.")

mc(1, 'M',
   r"How many solutions does the equation $2^x=x^2$ have?",
   T("Exactly three"), [T("No solutions"), T("Exactly one"), T("Exactly two")],
   lambda: ("Exactly three" if count_sign_changes(lambda v: 2.0**v - v*v, -20, 20) == 3 else "other"),
   "Graph it (Desmos)",
   r"Graph $y=2^x$ and $y=x^2$: they cross at $x=2$, $x=4$ and once more near $x\approx-0.77$. That is 3 points.", order=2)

gi(1, 'H',
   r"The sum of two positive numbers is 18 and their difference is 4. What is their product?",
   "77", Integer(77),
   lambda: (lambda sol: sol[x]*sol[y])(solve([x + y - 18, x - y - 4], [x, y])),
   "Structure (identities)",
   r"$(a+b)^2-(a-b)^2=4ab$, so $4ab=324-16=308$ and $ab=77$. (The numbers are 11 and 7.)")

mc(1, 'H',
   r"Which expression is equivalent to $x^2-y^2-6y-9$?",
   C(r"(x-y-3)(x+y+3)", (x - y - 3)*(x + y + 3)),
   [C(r"(x-y+3)(x+y-3)", (x - y + 3)*(x + y - 3)),
    C(r"(x-y-3)^2", (x - y - 3)**2),
    C(r"(x+y+3)^2", (x + y + 3)**2)],
   lambda: x**2 - y**2 - 6*y - 9,
   "Structure (identities)",
   r"$x^2-(y^2+6y+9)=x^2-(y+3)^2=(x-y-3)(x+y+3)$: a perfect square first, then a difference of squares.", order=1)

# ============================================================ SET 2  (Hard, 14)
mc(2, 'H',
   r"The solutions of $2x^2-10x+3=0$ are $r$ and $s$. What is the value of $r^2+s^2$?",
   C(22), [C(19), C(25), C(28)],
   lambda: (lambda rs: sum(v**2 for v in rs))(solve(2*x**2 - 10*x + 3, x)),
   "Vieta (sum of squares)",
   r"$r+s=5$ and $rs=\frac32$, so $r^2+s^2=(r+s)^2-2rs=25-3=22$. (Forgetting to divide by $a$ gives 19.)", order='a')

gi(2, 'H',
   r"In the equation $x^2-12x+k=0$, $k$ is a constant and one solution is 5 times the other solution. What is the value of $k$?",
   "20", Integer(20),
   lambda: (lambda tv: tv*(5*tv))(solve(t + 5*t - 12, t)[0]),
   "Vieta",
   r"Let the roots be $t$ and $5t$. The sum is $6t=12$, so $t=2$. The product is $k=t\cdot5t=5(4)=20$.")

mc(2, 'H',
   r"The equation $3x^2-8x+2=0$ has solutions $p$ and $q$. What is the value of $\dfrac1p+\dfrac1q$?",
   C(4), [C(r"\dfrac14", Rational(1, 4)), C(r"\dfrac23", Rational(2, 3)), C(r"\dfrac83", Rational(8, 3))],
   lambda: (lambda pq: 1/pq[0] + 1/pq[1])(solve(3*x**2 - 8*x + 2, x)),
   "Vieta (reciprocals)",
   r"$\dfrac1p+\dfrac1q=\dfrac{p+q}{pq}=\dfrac{8/3}{2/3}=4$.", order='a')

mc(2, 'H',
   r"The system $y=x^2-5x+9$ and $y=2x+4$ has two solutions, $(x_1,y_1)$ and $(x_2,y_2)$. What is the value of $y_1+y_2$?",
   C(22), [C(7), C(14), C(18)],
   lambda: (lambda xs: sum(2*v + 4 for v in xs))(solve(x**2 - 5*x + 9 - (2*x + 4), x)),
   "Vieta (system)",
   r"$x^2-7x+5=0$, so $x_1+x_2=7$. Then $y_1+y_2=2(x_1+x_2)+2(4)=22$. (Forgetting the second 4 gives 18.)", order='d')

gi(2, 'H',
   r"In the $xy$-plane, the line $y=-4x+5$ and the parabola $y=x^2+bx+9$ intersect at exactly one point, and $b<0$. What is the $x$-coordinate of that point?",
   "2", Integer(2),
   lambda: (lambda bv: solve(x**2 + bv*x + 9 - (-4*x + 5), x)[0])([v for v in solve(Poly(x**2 + b*x + 9 - (-4*x + 5), x).discriminant(), b) if v < 0][0]),
   "Tangent: D = 0",
   r"$x^2+(b+4)x+4=0$ has one solution when $(b+4)^2-16=0$, so $b=0$ or $b=-8$; $b<0$ gives $b=-8$. Then $x=-\frac{b+4}2=2$.")

mc(2, 'H',
   r"The solutions of $x^2-5x+3=0$ are $r$ and $s$. The equation $x^2+bx+c=0$ has solutions $r+2$ and $s+2$. What is the value of $c$?",
   C(17), [C(5), C(9), C(13)],
   lambda: (lambda rs: (rs[0] + 2)*(rs[1] + 2))(solve(x**2 - 5*x + 3, x)),
   "Vieta",
   r"$c=(r+2)(s+2)=rs+2(r+s)+4=3+10+4=17$. (Leaving out the final $+4$ gives 13.)", order='d')

gi(2, 'H',
   r"The equation $2x^2-9x+4=0$ has solutions $r$ and $s$. What is the value of $(r-2)(s-2)$?",
   "-3", Integer(-3),
   lambda: (lambda rs: (rs[0] - 2)*(rs[1] - 2))(solve(2*x**2 - 9*x + 4, x)),
   "Vieta",
   r"$(r-2)(s-2)=rs-2(r+s)+4=2-2\left(\frac92\right)+4=-3$.")

mc(2, 'H',
   r"What is the positive difference between the solutions of $2x^2-12x+5=0$?",
   C(r"\sqrt{26}", sqrt(26)), [C(r"\dfrac{\sqrt{26}}2", sqrt(26)/2), C(6), C(r"2\sqrt{26}", 2*sqrt(26))],
   lambda: (lambda rs: Abs(rs[0] - rs[1]))(solve(2*x**2 - 12*x + 5, x)),
   "Vieta (difference of roots)",
   r"$D=144-40=104$, and the roots differ by $\dfrac{\sqrt D}{|a|}=\dfrac{\sqrt{104}}2=\sqrt{26}$. (Forgetting to divide by $a$ gives $2\sqrt{26}$.)", order='a')

gi(2, 'H',
   r"The equation $x^2-kx+12=0$, where $k>0$, has solutions $r$ and $s$ with $r^2+s^2=40$. What is the value of $k$?",
   "8", Integer(8),
   lambda: [v for v in solve(k**2 - 2*12 - 40, k) if v > 0][0],
   "Vieta (sum of squares)",
   r"$r+s=k$ and $rs=12$, so $r^2+s^2=k^2-24=40$. Then $k^2=64$ and $k=8$ (positive). The roots are 2 and 6.")

mc(2, 'H',
   r"A rectangle has a perimeter of 26 centimeters and an area of 36 square centimeters. What is the length, in centimeters, of its diagonal?",
   C(r"\sqrt{97}", sqrt(97)), [C(13), C(r"\sqrt{133}", sqrt(133)), C(r"\sqrt{241}", sqrt(241))],
   lambda: (lambda lw: sqrt(lw[0]**2 + lw[1]**2))(solve(x**2 - 13*x + 36, x)),
   "Vieta (sum of squares)",
   r"$l+w=13$ and $lw=36$, so $l^2+w^2=169-72=97$. The diagonal is $\sqrt{97}$. (13 is the half-perimeter.)", order='a')

mc(2, 'H',
   r"The solutions of $x^2-10x+c=0$ are $r$ and $s$, where $r>s$ and $r-s=4$. What is the value of $c$?",
   C(21), [C(16), C(24), C(25)],
   lambda: (lambda sol: sol[x]*sol[y])(solve([x + y - 10, x - y - 4], [x, y])),
   "Vieta",
   r"$r+s=10$ and $r-s=4$, so $r=7$, $s=3$ and $c=rs=21$. (25 would mean equal roots.)", order='a')

gi(2, 'H',
   r"The equation $x^2+3x-5=0$ has solutions $r$ and $s$. What is the value of $r^3+s^3$?",
   "-72", Integer(-72),
   lambda: nsimplify(expand((lambda rs: rs[0]**3 + rs[1]**3)(solve(x**2 + 3*x - 5, x)))),
   "Vieta (sum of cubes)",
   r"$r^3+s^3=(r+s)^3-3rs(r+s)=(-3)^3-3(-5)(-3)=-27-45=-72$.")

mc(2, 'H',
   r"The parabola $y=2x^2-bx+c$ has $x$-intercepts whose sum is 5 and whose product is 3. What is the value of $b+c$?",
   C(16), [C(8), C(11), C(13)],
   lambda: (lambda sol: sol[b] + sol[c])(solve([b/2 - 5, c/2 - 3], [b, c])),
   "Vieta",
   r"The roots of $2x^2-bx+c=0$ have sum $\frac b2=5$ and product $\frac c2=3$, so $b=10$, $c=6$ and $b+c=16$.", order='d')

mc(2, 'H',
   r"Which equation has, as its solutions, the reciprocals of the solutions of $3x^2-7x+2=0$?",
   ("$2x^2-7x+3=0$", monic(2*x**2 - 7*x + 3)),
   [("$3x^2-7x+2=0$", monic(3*x**2 - 7*x + 2)), ("$2x^2+7x+3=0$", monic(2*x**2 + 7*x + 3)),
    ("$3x^2-2x+7=0$", monic(3*x**2 - 2*x + 7))],
   lambda: (lambda rs: expand((x - 1/rs[0])*(x - 1/rs[1])))(solve(3*x**2 - 7*x + 2, x)),
   "Vieta (reciprocals)",
   r"New sum $=\frac{S}{P}=\frac{7/3}{2/3}=\frac72$, new product $=\frac1P=\frac32$. So $x^2-\frac72x+\frac32=0$, i.e. $2x^2-7x+3=0$ (the $a$ and $c$ swap).", order=2)

# ============================================================ SET 3  (Hard, 14)
mc(3, 'H',
   r"The function $g(x)=-x^2+bx+c$ satisfies $g(2)=g(9)$, where $b$ and $c$ are constants. What is the value of $b$?",
   C(11), [C(r"\dfrac{11}2", Rational(11, 2)), C(7), C(22)],
   lambda: solve((-4 + 2*b + c) - (-81 + 9*b + c), b)[0],
   "Symmetry (axis)",
   r"Equal outputs mean the axis is halfway: $x=\frac{2+9}2=\frac{11}2$. For $-x^2+bx+c$ the axis is $\frac b2$, so $b=11$.", order='a')

gi(3, 'H',
   r"A quadratic model gives the height $h(t)$, in meters, of a ball $t$ seconds after it is thrown. The ball is thrown from a height of 1.2 meters. The model estimates that the ball is at a height of 21 meters both 1 second and 5 seconds after it is thrown. How many seconds after it is thrown does the model estimate that the ball returns to a height of 1.2 meters?",
   "6", Integer(6),
   lambda: (lambda sol: [v for v in solve(sol[a]*t**2 + sol[b]*t + Rational(6, 5) - Rational(6, 5), t) if v != 0][0])(
       solve([a + b + Rational(6, 5) - 21, 25*a + 5*b + Rational(6, 5) - 21], [a, b])),
   "Symmetry (axis)",
   r"The axis is halfway between $t=1$ and $t=5$, so it is $t=3$. Launch ($t=0$) is 3 units left of the axis, so the ball is back at 1.2 m at $t=3+3=6$.")

mc(3, 'H',
   r"The function $f$ is defined by $f(x)=(x-6)(x+2)+20$. What is the minimum value of $f$?",
   C(4), [C(-16), C(2), C(-12)],
   lambda: (lambda xv: ((x - 6)*(x + 2) + 20).subs(x, xv))(solve(diff((x - 6)*(x + 2) + 20, x), x)[0]),
   "Axis = midpoint of the roots",
   r"$(x-6)(x+2)$ is lowest halfway between $-2$ and $6$, at $x=2$, where it equals $-16$. So the minimum of $f$ is $-16+20=4$. (2 is where it happens.)", order='a')

gi(3, 'H',
   r"The vertex of the parabola $y=x^2-8x+k$ lies on the line $y=3x+2$. What is the value of $k$?",
   "30", Integer(30),
   lambda: solve((x**2 - 8*x + k).subs(x, 4) - (3*4 + 2), k)[0],
   "Axis = $-b/2a$",
   r"Axis: $x=-\frac{-8}{2}=4$. On the line, $y=3(4)+2=14$. So $16-32+k=14$ and $k=30$.")

gi(3, 'H',
   r"Use a graphing calculator. What is the larger solution of $2^x=2x+7$, rounded to the nearest tenth?",
   "3.9", Rational(39, 10),
   lambda: Rational(int(round(bisect_root(lambda v: 2.0**v - 2*v - 7, 3.0, 5.0) * 10)), 10),
   "Graph it (Desmos)",
   r"Graph $y=2^x$ and $y=2x+7$ and tap the right-hand intersection: $x\approx3.885$, which rounds to $3.9$. (The other crossing is near $-3.45$.)")

mc(3, 'H',
   r"How many solutions does the equation $2^x=x^2+1$ have?",
   C(3), [C(0), C(1), C(2)],
   lambda: Integer(count_sign_changes(lambda v: 2.0**v - v*v - 1, -20, 20)),
   "Graph it (Desmos)",
   r"Graphs of $y=2^x$ and $y=x^2+1$ meet at $x=0$, $x=1$ and a third time near $x\approx4.26$. Testing whole numbers alone finds only 2.", order='a')

gi(3, 'H',
   r"The line $y=2x+k$ intersects the parabola $y=x^2-4x+5$ at exactly two points, where $k$ is an integer. What is the least possible value of $k$?",
   "-3", Integer(-3),
   lambda: min(kv for kv in range(-10, 10) if len(solve(x**2 - 4*x + 5 - (2*x + kv), x)) == 2),
   "Graph it (slider) / D > 0",
   r"$x^2-6x+(5-k)=0$ needs $D=36-4(5-k)=16+4k>0$, so $k>-4$. The least integer is $-3$. (On Desmos: add a slider for $k$ and watch the crossings.)")

mc(3, 'H',
   r"What is the sum of the $x$- and $y$-coordinates of the vertex of $y=3x^2-18x+4$?",
   C(-20), [C(-26), C(-23), C(3)],
   lambda: (lambda xv: xv + (3*x**2 - 18*x + 4).subs(x, xv))(solve(diff(3*x**2 - 18*x + 4, x), x)[0]),
   "Axis = $-b/2a$",
   r"$h=-\frac{-18}{6}=3$ and $k=3(9)-54+4=-23$, so $h+k=-20$. (A negative $h$ would give the trap $-26$.)", order='a')

mc(3, 'H',
   r"The parabola $y=a(x-1)(x-7)$ has a maximum value of 18. What is the value of $a$?",
   C(-2), [C(-6), C(2), C(6)],
   lambda: solve(a*(4 - 1)*(4 - 7) - 18, a)[0],
   "Axis = midpoint of the roots",
   r"The vertex is at $x=\frac{1+7}2=4$, where $y=a(3)(-3)=-9a$. Then $-9a=18$ and $a=-2$.", order='a')

mc(3, 'H',
   r"A parabola has its vertex at $(3,-4)$ and passes through $(5,4)$. What is the $y$-coordinate of its $y$-intercept?",
   C(14), [C(-4), C(2), C(22)],
   lambda: (lambda av: (av*(x - 3)**2 - 4).subs(x, 0))(solve(a*(5 - 3)**2 - 4 - 4, a)[0]),
   "Vertex form",
   r"$y=a(x-3)^2-4$ and $y(5)=4$ give $4a-4=4$, so $a=2$. Then $y(0)=2(9)-4=14$. (2 is $a$, not the intercept.)", order='a')

gi(3, 'H',
   r"A shop sells $120-4p$ scarves per day when the price is $p$ dollars, and each scarf costs the shop \$5. The shop's daily profit, in dollars, is $(p-5)(120-4p)$. What is the greatest possible daily profit, in dollars?",
   "625", Integer(625),
   lambda: max(((v - 5)*(120 - 4*v)) for v in [Rational(n, 2) for n in range(10, 61)]),
   "Axis = midpoint of the roots",
   r"The zeros are $p=5$ and $p=30$, so the maximum is at $p=17.5$: profit $=(12.5)(120-70)=(12.5)(50)=625$.")

mc(3, 'H',
   r"The function $f(x)=x^2+bx+c$ satisfies $f(1)=f(9)$ and has a minimum value of $-7$. What is the value of $c$?",
   C(18), [C(-10), C(-7), C(7)],
   lambda: (lambda bv: solve((x**2 + bv*x + c).subs(x, 5) + 7, c)[0])(solve((1 + b + c) - (81 + 9*b + c), b)[0]),
   "Symmetry (axis)",
   r"Axis: $x=\frac{1+9}2=5$, so $-\frac b2=5$ and $b=-10$. Minimum: $f(5)=25-50+c=-7$, so $c=18$.", order='a')

mc(3, 'H',
   r"The graphs of $f(x)=x^2-6x+11$ and $g(x)=-x^2+2x+3$ in the $xy$-plane intersect. What is the $y$-coordinate of the point where they intersect?",
   C(3), [C(2), C(6), C(11)],
   lambda: (lambda xs: set((x**2 - 6*x + 11).subs(x, v) for v in xs))(solve(x**2 - 6*x + 11 - (-x**2 + 2*x + 3), x)).pop(),
   "Graph it (Desmos)",
   r"$f=g$ gives $2x^2-8x+8=2(x-2)^2=0$, so they touch only at $x=2$, where $f(2)=4-12+11=3$. (2 is the $x$-coordinate.)", order='d')

mc(3, 'H',
   r"For $k>0$, the line $y=x+k$ is tangent to the circle $x^2+y^2=25$. What is the value of $k$?",
   C(r"5\sqrt2", 5*sqrt(2)), [C(5), C(25), C(50)],
   lambda: [v for v in solve(Poly(x**2 + (x + k)**2 - 25, x).discriminant(), k) if v > 0][0],
   "Tangent: D = 0",
   r"Substitute: $2x^2+2kx+k^2-25=0$. One solution means $D=4k^2-8(k^2-25)=200-4k^2=0$, so $k^2=50$ and $k=5\sqrt2$.", order='a')

# ============================================================ SET 4  (Hard, 14)
mc(4, 'H',
   r"$5x+3y=29$ and $3x+5y=19$. What is the value of $x^2-y^2$?",
   C(30), [C(5), C(6), C(11)],
   lambda: (lambda sol: sol[x]**2 - sol[y]**2)(solve([5*x + 3*y - 29, 3*x + 5*y - 19], [x, y])),
   "Add / subtract the equations",
   r"Add: $8(x+y)=48$, so $x+y=6$. Subtract: $2(x-y)=10$, so $x-y=5$. Then $x^2-y^2=(x+y)(x-y)=30$.", order='d')

gi(4, 'H',
   r"$a+b=12$, $b+c=15$ and $a+c=17$. What is the value of $a+b+c$?",
   "22", Integer(22),
   lambda: (lambda sol: sol[a] + sol[b] + sol[c])(solve([a + b - 12, b + c - 15, a + c - 17], [a, b, c])),
   "Add the equations",
   r"Adding all three: $2(a+b+c)=44$, so $a+b+c=22$.")

mc(4, 'H',
   r"If $2x+5y=18$ and $6x-y=10$, what is the value of $8x+4y$?",
   C(28), [C(7), C(14), C(18)],
   lambda: (lambda sol: 8*sol[x] + 4*sol[y])(solve([2*x + 5*y - 18, 6*x - y - 10], [x, y])),
   "Add the equations",
   r"The expression $8x+4y$ is the sum of the two left sides: $18+10=28$.", order='a')

gi(4, 'H',
   r"If $x+\dfrac1x=5$, what is the value of $x^2+\dfrac1{x^2}$?",
   "23", Integer(23),
   lambda: nsimplify(simplify((lambda xs: xs[0]**2 + 1/xs[0]**2)(solve(x + 1/x - 5, x)))),
   "Structure (identities)",
   r"Square both sides: $x^2+2+\dfrac1{x^2}=25$, so $x^2+\dfrac1{x^2}=23$.")

mc(4, 'H',
   r"What is the remainder when $p(x)=x^4-3x^2+5x+1$ is divided by $x+2$?",
   C(-5), [C(1), C(5), C(15)],
   lambda: Poly(x**4 - 3*x**2 + 5*x + 1, x).rem(Poly(x + 2, x)).as_expr(),
   "Factor / remainder theorem",
   r"The remainder is $p(-2)=16-12-10+1=-5$. (Using $p(2)=15$ is the classic sign trap.)", order='a')

mc(4, 'H',
   r"Which of the following expressions has $x+5$ as a factor?",
   ("$x^3+2x^2-13x+10$", x**3 + 2*x**2 - 13*x + 10),
   [("$x^3+2x^2-13x-10$", x**3 + 2*x**2 - 13*x - 10),
    ("$x^3-2x^2-13x+10$", x**3 - 2*x**2 - 13*x + 10),
    ("$x^3+2x^2+13x+10$", x**3 + 2*x**2 + 13*x + 10)],
   lambda: [e for e in (x**3 + 2*x**2 - 13*x + 10, x**3 + 2*x**2 - 13*x - 10, x**3 - 2*x**2 - 13*x + 10, x**3 + 2*x**2 + 13*x + 10)
            if Poly(e, x).rem(Poly(x + 5, x)).as_expr() == 0][0],
   "Factor / remainder theorem",
   r"$x+5$ is a factor exactly when the value at $x=-5$ is 0. Only the first choice works: $-125+50+65+10=0$ (the others give $-20$, $-100$, $-130$).", order=3)

gi(4, 'H',
   r"If $(3x+2y)^2-(3x-2y)^2=96$, what is the value of $xy$?",
   "4", Integer(4),
   lambda: simplify(solve(expand((3*x + 2*y)**2 - (3*x - 2*y)**2) - 96, x)[0] * y),
   "Structure (identities)",
   r"$(A+B)^2-(A-B)^2=4AB$ with $A=3x$, $B=2y$ gives $4(3x)(2y)=24xy=96$, so $xy=4$.")

mc(4, 'H',
   r"Which expression is equivalent to $a(x+3)^2-a(x-3)^2$?",
   ("$12ax$", 12*a*x),
   [("$6ax$", 6*a*x), ("$18a$", 18*a), ("$2a(x^2+9)$", 2*a*(x**2 + 9))],
   lambda: expand(a*(x + 3)**2 - a*(x - 3)**2),
   "Structure (identities)",
   r"Factor out $a$: $(x+3)^2-(x-3)^2=\big[(x+3)-(x-3)\big]\big[(x+3)+(x-3)\big]=6\cdot2x=12x$. So the result is $12ax$.", order=1)

mc(4, 'H',
   r"The value of an investment increased by $20\%$ in the first year and then decreased by $25\%$ in the second year. After the two years, the value was \$5,400. What was the value of the investment at the start of the first year?",
   C(r"\$6{,}000", 6000), [C(r"\$4{,}860", 4860), C(r"\$5{,}400", 5400), C(r"\$5{,}670", 5670)],
   lambda: Integer(5400) / (Rational(120, 100) * Rational(75, 100)),
   "Percent multiplier",
   r"Net multiplier $=1.20\times0.75=0.90$. Start $=\dfrac{5400}{0.90}=6000$. (Multiplying by 0.9 instead of dividing gives 4,860.)", order='a')

mc(4, 'H',
   r"A price is reduced by $20\%$. By what percent must the reduced price be increased to return to the original price?",
   C(r"25\%", 25), [C(r"20\%", 20), C(r"30\%", 30), C(r"80\%", 80)],
   lambda: (1/Rational(8, 10) - 1) * 100,
   "Percent multiplier",
   r"Original $=1$, reduced $=0.8$. Need $0.8(1+r)=1$, so $1+r=1.25$ and $r=25\%$. (Going up by the same 20\% only gets back to 96\%.)", order='a')

mc(4, 'H',
   r"Four sandwiches and three juices cost \$29. Three sandwiches and four juices cost \$27. What is the cost, in dollars, of five sandwiches and five juices?",
   C(40), [C(8), C(25), C(29)],
   lambda: (lambda sol: 5*sol[x] + 5*sol[y])(solve([4*x + 3*y - 29, 3*x + 4*y - 27], [x, y])),
   "Add the equations",
   r"Add: $7(s+j)=56$, so $s+j=8$. Then $5(s+j)=40$. (No need for the individual prices, \$5 and \$3.)", order='a')

gi(4, 'H',
   r"If $a+b=10$ and $ab=17$, what is the value of $(a-b)^2$?",
   "32", Integer(32),
   lambda: (lambda ab: (ab[0] - ab[1])**2)(solve(x**2 - 10*x + 17, x)),
   "Structure (identities)",
   r"$(a-b)^2=(a+b)^2-4ab=100-68=32$.")

mc(4, 'H',
   r"If $3^{x+2}-3^{x}=216$, what is the value of $3^{x}$?",
   C(27), [C(3), C(9), C(24)],
   lambda: solve(9*Symbol('u') - Symbol('u') - 216, Symbol('u'))[0],
   "Structure (factor the common power)",
   r"$3^{x+2}=9\cdot3^x$, so $9\cdot3^x-3^x=8\cdot3^x=216$ and $3^x=27$. (Here $x=3$; the question asks for $3^x$, not $x$.)", order='a')

mc(4, 'H',
   r"What is the product of all solutions of $(x-8)(x+2)=(x-8)(3x-4)$?",
   C(24), [C(3), C(8), C(11)],
   lambda: (lambda sl: sl[0]*sl[1])(solve((x - 8)*(x + 2) - (x - 8)*(3*x - 4), x)),
   "Do not divide: factor",
   r"$(x-8)\big[(x+2)-(3x-4)\big]=(x-8)(6-2x)=0$, so $x=8$ or $x=3$. The product is 24. (Dividing by $x-8$ loses a root.)", order='d')

# ============================================================ SET 5  (Summit, 20)
gi(5, 'H',
   r"The graphs of $y=x^2-9x+4$ and $y=-2x+k$ intersect at two points whose $x$-coordinates are $x_1$ and $x_2$. If $x_1^2+x_2^2=59$, what is the value of $k$?",
   "9", Integer(9),
   lambda: [kv for kv in range(-20, 21)
            if simplify(sum(v**2 for v in solve(x**2 - 9*x + 4 - (-2*x + kv), x)) - 59) == 0][0],
   "Vieta (sum of squares)",
   r"$x^2-7x+(4-k)=0$, so $x_1+x_2=7$ and $x_1x_2=4-k$. Then $49-2(4-k)=59$, so $4-k=-5$ and $k=9$.")

mc(5, 'H',
   r"The graphs of $x^2+y^2=20$ and $y=mx+\dfrac b3$ intersect at the point $(4,y)$ where $y<0$; $m$ and $b$ are constants. Which expression gives the value of $b$?",
   ("$-12m-6$", -12*m - 6),
   [("$12m-6$", 12*m - 6), ("$6-12m$", 6 - 12*m), ("$12m+6$", 12*m + 6)],
   lambda: (lambda yv: solve(yv - (m*4 + b/3), b)[0])([v for v in solve(16 + y**2 - 20, y) if v < 0][0]),
   "Substitute the point",
   r"$16+y^2=20$ and $y<0$ give $y=-2$. Then $-2=4m+\frac b3$, so $b=-6-12m$. (Taking $y=+2$ gives the trap $6-12m$.)", order=0)

mc(5, 'H',
   r"What is the sum of all solutions of $\sqrt{x+30}=x$?",
   C(6), [C(-5), C(1), C(30)],
   lambda: sum(v for v in solve(x**2 - x - 30, x) if sqrt(v + 30) == v),
   "Extraneous solutions (backsolve)",
   r"Squaring gives $x^2-x-30=0$, so $x=6$ or $x=-5$. Check: $\sqrt{25}=5\neq-5$, so $-5$ is extraneous. Only $x=6$ works. (Vieta's sum, 1, is the trap.)", order='a')

mc(5, 'H',
   r"The solutions of $2x^2-12x+5=0$ are $r$ and $s$, with $r>s$. What is the value of $r^2-s^2$?",
   C(r"6\sqrt{26}", 6*sqrt(26)), [C(r"\sqrt{26}", sqrt(26)), C(6), C(r"3\sqrt{26}", 3*sqrt(26))],
   lambda: (lambda rs: (lambda hi, lo: hi**2 - lo**2)(max(rs, key=lambda v: float(v)), min(rs, key=lambda v: float(v))))(solve(2*x**2 - 12*x + 5, x)),
   "Vieta + structure",
   r"$r^2-s^2=(r+s)(r-s)$. Here $r+s=6$ and $r-s=\dfrac{\sqrt{104}}2=\sqrt{26}$, so the value is $6\sqrt{26}$.", order='a')

gi(5, 'H',
   r"The polynomial $p(x)=x^3+ax^2+bx-12$ is divisible by $x-1$, and the remainder when $p(x)$ is divided by $x+1$ is 6. What is the value of $a$?",
   "15", Integer(15),
   lambda: solve([(x**3 + a*x**2 + b*x - 12).subs(x, 1), (x**3 + a*x**2 + b*x - 12).subs(x, -1) - 6], [a, b])[a],
   "Factor / remainder theorem",
   r"$p(1)=0$: $a+b=11$. $p(-1)=6$: $-1+a-b-12=6$, so $a-b=19$. Adding: $2a=30$, so $a=15$.")

mc(5, 'H',
   r"A stock rose $40\%$ on Monday and then fell by $p\%$ on Tuesday, ending $12\%$ above its price before Monday. What is the value of $p$?",
   C(20), [C(12), C(28), C(40)],
   lambda: (1 - Rational(112, 100) / Rational(140, 100)) * 100,
   "Percent multiplier",
   r"$1.40\,(1-\frac p{100})=1.12$, so $1-\frac p{100}=0.80$ and $p=20$. (Subtracting $40-12$ gives the trap 28.)", order='a')

mc(5, 'H',
   r"How many solutions does the system $y=x^2-6x+8$ and $y=|x-3|$ have?",
   C(2), [C(0), C(1), C(3)],
   lambda: Integer(count_sign_changes(lambda v: v*v - 6*v + 8 - abs(v - 3), -40, 40)),
   "Graph it (Desmos)",
   r"Graph both: the V-shape touches the parabola at $x=\frac{5-\sqrt5}2\approx1.38$ and $x=\frac{7+\sqrt5}2\approx4.62$. Two points.", order='a')

gi(5, 'H',
   r"If $x+y=6$ and $x^2+y^2=20$, what is the value of $x^3+y^3$?",
   "72", Integer(72),
   lambda: (lambda sol: sol[0][0]**3 + sol[0][1]**3)(solve([x + y - 6, x**2 + y**2 - 20], [x, y])),
   "Structure (identities)",
   r"$xy=\dfrac{36-20}{2}=8$. Then $x^3+y^3=(x+y)^3-3xy(x+y)=216-3(8)(6)=72$.")

mc(5, 'H',
   r"The parabola $y=x^2+bx+c$ has two $x$-intercepts that are 8 units apart. What is the minimum value of $y$?",
   C(-16), [C(-8), C(-4), C(16)],
   lambda: (lambda f: simplify(f.subs(x, solve(diff(f, x), x)[0])))((x - r)*(x - r - 8)),
   "Axis = midpoint of the roots",
   r"The vertex lies halfway between the intercepts, 4 units from each. With $a=1$: $y=(4)(-4)=-16$ (the product of the distances, signed).", order='a')

mc(5, 'H',
   r"If $x+y+3\ne0$, which of the following expressions is equivalent to the expression below? $$\dfrac{x^2+6x+9-y^2}{x+y+3}$$",
   ("$x-y+3$", x - y + 3),
   [("$x+y+3$", x + y + 3), ("$x-y-3$", x - y - 3), ("$x+3$", x + 3)],
   lambda: simplify((x**2 + 6*x + 9 - y**2) / (x + y + 3)),
   "Structure (identities)",
   r"Numerator $=(x+3)^2-y^2=(x+3-y)(x+3+y)$. Cancel $x+y+3$ to get $x-y+3$.", order=0)

gi(5, 'H',
   r"A number is increased by $20\%$, and the result is then decreased by $20\%$. The final value is 144. What was the original number?",
   "150", Integer(150),
   lambda: Integer(144) / (Rational(120, 100) * Rational(80, 100)),
   "Percent multiplier",
   r"Net multiplier $=1.2\times0.8=0.96$. Original $=\dfrac{144}{0.96}=150$.")

mc(5, 'H',
   r"If $a+b=7$ and $a^2-b^2=21$, what is the value of $ab$?",
   C(10), [C(3), C(5), C(7)],
   lambda: (lambda sol: sol[a]*sol[b])(solve([a + b - 7, a**2 - b**2 - 21], [a, b], dict=True)[0]),
   "What is asked? / structure",
   r"$a^2-b^2=(a+b)(a-b)$, so $a-b=3$. With $a+b=7$: $a=5$, $b=2$ and $ab=10$.", order='a')

gi(5, 'H',
   r"The function $f(x)=ax^2+bx+c$ has a minimum value of $-3$, $f(1)=f(7)$ and $f(0)=5$. What is the value of $a$?",
   "1/2", Rational(1, 2),
   lambda: solve([c - 5, (a + b + c) - (49*a + 7*b + c), (a*4**2 + b*4 + c) + 3], [a, b, c])[a],
   "Symmetry (axis)",
   r"The axis is $x=\frac{1+7}2=4$, so $f(x)=a(x-4)^2-3$. Then $f(0)=16a-3=5$ and $a=\frac12$. (Enter 1/2 or 0.5.)")

mc(5, 'H',
   r"How many real solutions does the equation $x^3-3x=1$ have?",
   C(3), [C(0), C(1), C(2)],
   lambda: Integer(count_sign_changes(lambda v: v**3 - 3*v - 1, -10, 10)),
   "Graph it (Desmos)",
   r"Graph $y=x^3-3x$ and the line $y=1$. The curve rises to a local maximum of 2 at $x=-1$, falls to $-2$ at $x=1$, then rises: 3 crossings.", order='a')

mc(5, 'H',
   r"For which value of $k$ does $|x^2-6x+5|=k$ have exactly three solutions?",
   C(4), [C(-4), C(5), C(9)],
   lambda: [kv for kv in range(-10, 11) if kv >= 0 and
            len(set(solve(x**2 - 6*x + 5 - kv, x)) | set(solve(x**2 - 6*x + 5 + kv, x))) == 3][0],
   "Graph it (slider)",
   r"The graph of $|x^2-6x+5|$ flips the dip (vertex $(3,-4)$) up to a peak at $(3,4)$. The line $y=k$ crosses it three times only at the peak: $k=4$.", order='a')

mc(5, 'H',
   r"How many solutions does the following equation have? $$\dfrac{x}{x-2}=\dfrac{2}{x-2}+3$$",
   T("No solution"), [T("Exactly one"), T("Exactly two"), T("Infinitely many")],
   lambda: ("No solution" if not [v for v in solve(x - (2 + 3*(x - 2)), x) if v != 2] else "other"),
   "Extraneous solutions",
   r"For $x\ne2$ the left side minus $\frac{2}{x-2}$ is $\frac{x-2}{x-2}=1$, and $1=3$ is false. Clearing denominators gives $x=2$, which is excluded.", order=3)

gi(5, 'H',
   r"The equation $x^2-6x+q=0$ has solutions $r$ and $s$, and $\dfrac1r+\dfrac1s=\dfrac32$. What is the value of $r^2+s^2$?",
   "28", Integer(28),
   lambda: (lambda qv: sum(v**2 for v in solve(x**2 - 6*x + qv, x)))(solve(Rational(6, 1)/q - Rational(3, 2), q)[0]),
   "Vieta (sum of squares)",
   r"$\frac1r+\frac1s=\frac{r+s}{rs}=\frac6q=\frac32$, so $q=4$. Then $r^2+s^2=36-2(4)=28$.")

gi(5, 'H',
   r"A line with slope $-3$ is tangent to the parabola $y=2x^2+7x+5$. What is the $y$-intercept of the line?",
   "-7.5", Rational(-15, 2),
   lambda: solve(Poly(2*x**2 + 7*x + 5 - (-3*x + c), x).discriminant(), c)[0],
   "Tangent: D = 0",
   r"$2x^2+10x+(5-c)=0$ has one solution when $D=100-8(5-c)=60+8c=0$, so $c=-7.5$.")

mc(5, 'H',
   r"The side lengths, in inches, of a rectangle are the two solutions of $x^2-17x+k=0$, and its diagonal is 13 inches. What is the value of $k$?",
   C(60), [C(30), C(120), C(144)],
   lambda: (lambda sl: sl[x]*sl[y])(solve([x + y - 17, x**2 + y**2 - 169], [x, y], dict=True)[0]),
   "Vieta (sum of squares)",
   r"$r+s=17$ and $r^2+s^2=169$, so $rs=\dfrac{17^2-169}{2}=60$. (The sides are 5 and 12.)", order='a')

mc(5, 'H',
   r"The graphs of $y=x^2+bx+8$ and $y=3x+k$ intersect at two points. The midpoint of these two points has $x$-coordinate 5. What is the value of $b$?",
   C(-7), [C(-10), C(7), C(13)],
   lambda: solve(Rational(1, 2)*(3 - b) - 5, b)[0],
   "Vieta (system)",
   r"$x^2+(b-3)x+(8-k)=0$, so $x_1+x_2=3-b$. The midpoint is $\frac{3-b}2=5$, so $b=-7$. (Using the vertex, $-\frac b2=5$, ignores the line.)", order='a')

# ================================================================== verification

# Final answer-letter plan (keeps the correct letter spread across A-D; numeric choices stay sorted).
LETTER_PLAN = {
    (1, 10): 3, (1, 12): 1, (2, 14): 2, (4, 6): 3, (4, 8): 2, (5, 2): 0, (5, 10): 1, (5, 16): 0,   # text choices: position
    (2, 13): 'd', (4, 9): 'd', (3, 6): 'd', (4, 1): 'd', (4, 14): 'd', (5, 14): 'd',               # rank 3 -> A
    (2, 3): 'a', (2, 6): 'a', (2, 4): 'a',
    (2, 8): 'd', (5, 15): 'd', (1, 5): 'd', (3, 13): 'd',                                           # rank 2 from top -> C
}
LETTERS = "ABCD"

def arrange(p):
    """Return (list of (tex,val) in print order, index of the correct one)."""
    items = [p['right']] + list(p['wrongs'])
    order = p['order']
    if order in ('a', 'd'):
        items_sorted = sorted(items, key=lambda it: float(it[1]), reverse=(order == 'd'))
        return items_sorted, [i for i, it in enumerate(items_sorted) if it is p['right']][0]
    pos = int(order)
    wr = list(p['wrongs'])
    out = wr[:pos] + [p['right']] + wr[pos:]
    return out, pos

def prepare():
    for i, p in enumerate(PROBLEMS):
        p['n'] = sum(1 for q_ in PROBLEMS[:i] if q_['set'] == p['set']) + 1
        if (p['set'], p['n']) in LETTER_PLAN:
            p['order'] = LETTER_PLAN[(p['set'], p['n'])]
        if p['kind'] == 'mc':
            p['choices'], p['pos'] = arrange(p)
            p['letter'] = LETTERS[p['pos']]
            p['answer'] = p['letter']
        else:
            p['answer'] = p['ans_tex']

def check(p):
    got = p['calc']()
    if p['kind'] == 'gi':
        return same(got, p['ans_val']), got
    ok = same(got, p['right'][1])
    vals = [c_[1] for c_ in p['choices']]
    # exactly one correct choice, all choices distinct
    n_correct = sum(1 for v in vals if same(got, v))
    distinct = all(not same(vals[i], vals[j]) for i in range(4) for j in range(i + 1, 4))
    return (ok and n_correct == 1 and distinct and p['choices'][p['pos']][1] is p['right'][1]), got

def main():
    prepare()
    fails = 0
    for p in PROBLEMS:
        ok, got = check(p)
        tag = "S%d.%-2d" % (p['set'], p['n'])
        shown = p['answer'] if p['kind'] == 'gi' else "%s = %s" % (p['letter'], p['right'][0] if not p['right'][0].startswith('$') else p['right'][0])
        print("%s %-4s %s   (recomputed: %s)" % (tag, "OK" if ok else "FAIL", shown, got))
        if not ok:
            fails += 1
    from collections import Counter
    print()
    print("problems:", len(PROBLEMS), " FAIL:", fails)
    for sn in range(1, 6):
        ps = [p for p in PROBLEMS if p['set'] == sn]
        mcs = [p for p in ps if p['kind'] == 'mc']
        print("Set %d: %d problems (%d MC, %d grid-in); correct-letter counts %s; difficulty %s" %
              (sn, len(ps), len(mcs), len(ps) - len(mcs),
               dict(sorted(Counter(p['letter'] for p in mcs).items())),
               dict(Counter(p['diff'] for p in ps))))
    allmc = [p for p in PROBLEMS if p['kind'] == 'mc']
    print("All MC letter counts:", dict(sorted(Counter(p['letter'] for p in allmc).items())))
    return 1 if fails else 0

if __name__ == "__main__":
    sys.exit(main())
