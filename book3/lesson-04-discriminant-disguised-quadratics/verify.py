#!/usr/bin/env python3
"""Book 3, Lesson 4 "Discriminant edge cases & disguised quadratics": the problem bank AND its verifier.

Every problem is registered with:
  * its stem and choices (LaTeX),
  * a worked solution (this is what students see),
  * a `calc` function (or an `each` predicate for "which option ..." items) that recomputes the
    answer independently of the printed solution (sympy / numeric root scans / brute force over integer grids).

Running `python3 verify.py` recomputes every answer, checks that exactly one MC choice is correct
and that choices are distinct, balances the correct letters, and prints ALL OK / FAIL.
(`build.py` imports PROBLEMS from this file to write problems.md and the .tex files.)
No imaginary numbers anywhere: "no real solutions" is the only language used.
"""
import sys
from fractions import Fraction
from itertools import product
from sympy import (real_roots, Symbol, symbols, Rational, Integer, sqrt, cbrt, solve, solveset, simplify, expand, Poly, Matrix,
                   EmptySet, floor, ceiling, Eq, S, nsimplify, Abs, oo, sympify, latex, together, fraction, div,
                   powsimp, diff, FiniteSet, Float, root, cancel, factor)
import mpmath

x, y, z, a, b, c, d, k, m, n, p, q, r, s, t = symbols('x y z a b c d k m n p q r s t', real=True)
A_, B_ = symbols('A B', real=True)
w, v, u = symbols('w v u', real=True)
xp = Symbol('xp', positive=True)

PROBLEMS = []
SET_TITLES = {
    1: ("Set 1", "Bridge: the core moves", "Medium and Hard"),
    2: ("Set 2", "The discriminant backward: tangents, intersections and parameters", "Hard"),
    3: ("Set 3", "Equations that become quadratics: radicals, fractions, quadratic form, word problems", "Hard"),
    4: ("Set 4", "Equivalent expressions and completing the square", "Hard"),
    5: ("Set 5", "Summit: the hardest mixed problems", "Hard"),
}

# ---------------------------------------------------------------- helpers
def C(tex_or_val, val=None):
    """Numeric choice: C(66) or C(r"\\dfrac14", Rational(1,4)) or C("5.5", Rational(11,2)) -> (latex, value)."""
    if val is None:
        v_ = tex_or_val
        return ("$%s$" % latex(sympify(v_)), sympify(v_))
    return ("$%s$" % tex_or_val, val)

def T(text, val=None):
    """Text choice. Value defaults to the text itself; pass a value for ordering/keys."""
    return (text, text if val is None else val)

def same(u_, v_):
    try:
        if sympify(u_) == sympify(v_):
            return True
    except Exception:
        pass
    if isinstance(u_, (tuple, str, list)) or isinstance(v_, (tuple, str, list)) or callable(u_) or callable(v_):
        return u_ == v_
    return simplify(sympify(u_) - sympify(v_)) == 0

def mc(sett, diff_, stem, right, wrongs, calc, trick, sol, order='auto', each=None):
    PROBLEMS.append(dict(set=sett, diff=diff_, kind='mc', stem=stem, right=right, wrongs=wrongs,
                         calc=calc, trick=trick, sol=sol, order=order, each=each))

def gi(sett, diff_, stem, ans_tex, ans_val, calc, trick, sol):
    PROBLEMS.append(dict(set=sett, diff=diff_, kind='gi', stem=stem, ans_tex=ans_tex, ans_val=ans_val,
                         calc=calc, trick=trick, sol=sol))

def rs(expr, var=x):
    """Sorted list of the real solutions of expr = 0 (sympy solveset over the reals)."""
    st = solveset(expr, var, S.Reals)
    if st == EmptySet:
        return []
    return sorted(list(st)) if isinstance(st, FiniteSet) else None

def nreal(expr, var=x):
    L = rs(expr, var)
    return len(L)

def rsol(expr, var=x):
    """Real solutions of a rational expression = 0: solve the numerator, then discard values that
    make the ORIGINAL expression undefined."""
    nu, _ = fraction(together(expr))
    out = []
    for s_ in solveset(nu, var, S.Reals):
        v_ = expr.subs(var, s_)
        if v_.is_finite and simplify(v_) == 0:
            out.append(s_)
    return sorted(out)

def disc(expr, var=x):
    return Poly(expand(expr), var).discriminant()

def scan(f, lo=-30.0, hi=30.0, steps=60000):
    """Numeric real roots of f on [lo, hi] (sign changes + exact zeros), refined by bisection."""
    xs = [lo + (hi - lo) * i / steps for i in range(steps + 1)]
    out = []
    prev = None
    for xv in xs:
        try:
            fv = f(xv)
        except (ValueError, ZeroDivisionError, OverflowError):
            prev = None
            continue
        if isinstance(fv, complex):
            prev = None
            continue
        if abs(fv) < 1e-12:
            out.append(round(xv, 6))
        elif prev is not None and prev[1] * fv < 0:
            a_, b_ = prev[0], xv
            fa = prev[1]
            for _ in range(60):
                mid = (a_ + b_) / 2
                fm = f(mid)
                if fa * fm <= 0:
                    b_ = mid
                else:
                    a_, fa = mid, fm
            out.append(round((a_ + b_) / 2, 6))
        prev = (xv, fv)
    ded = []
    for r_ in sorted(out):
        if not ded or abs(r_ - ded[-1]) > 1e-4:
            ded.append(r_)
    return ded

def nsys(eqs, vs=(x, y)):
    """Number of real solutions (ordered pairs) of a polynomial system."""
    sols = solve(list(eqs), list(vs), dict=True)
    cnt = 0
    for s_ in sols:
        if all(sympify(s_.get(v_, 0)).is_real for v_ in vs):
            cnt += 1
    return cnt


def rad_count(kk):
    """Number of real solutions of sqrt(2x+kk) = x (candidates from squaring, then checked)."""
    cands = solveset(x**2 - 2*x - kk, x, S.Reals)
    return len([t_ for t_ in cands if t_ >= 0 and 2*t_ + kk >= 0 and simplify(sqrt(2*t_ + kk) - t_) == 0])

def creal(n_):
    """Real cube root of an integer."""
    return Integer(abs(n_))**Rational(1, 3) * (1 if n_ >= 0 else -1)

def divisible(poly, fac, var=x):
    return div(Poly(expand(poly), var), Poly(expand(fac), var))[1].is_zero

# ============================================================ SET 1  (Medium/Hard, 12)
mc(1, 'M',
   r"How many real solutions does the equation $4x^2+9=12x$ have?",
   T("Exactly one", 1), [T("Zero", 0), T("Exactly two", 2), T("Infinitely many", 'infinite')],
   lambda: nreal(4*x**2 + 9 - 12*x),
   "Discriminant: count the solutions",
   r"Move everything to one side: $4x^2-12x+9=0$. Then $D=(-12)^2-4(4)(9)=144-144=0$, so there is exactly one real solution ($x=\frac32$). (Zero comes from forgetting to move the $12x$ across; two comes from reading $(2x-3)^2=0$ as two different roots.)",
   order='free')

mc(1, 'M',
   r"In the equation $x^2+bx+49=0$, $b$ is a positive constant. The equation has exactly one real solution. What is the value of $b$?",
   C(14), [C(7), C(-14), C(196)],
   lambda: [bb for bb in range(1, 300) if disc(x**2 + bb*x + 49) == 0],
   "D = 0 means exactly one solution",
   r"Exactly one real solution means $D=b^2-4(1)(49)=0$, so $b^2=196$ and $b=14$ (positive). (7 solves $b^2=49$ and forgets the $4$; $-14$ ignores $b>0$; 196 is $b^2$, not $b$.)")

mc(1, 'M',
   r"In the $xy$-plane, how many points do the graphs of $y=x^2-2x+5$ and $y=2x+1$ have in common?",
   C(1), [C(0), C(2), T("Infinitely many", 'infinite')],
   lambda: nreal(x**2 - 2*x + 5 - (2*x + 1)),
   "Line and parabola: set equal, read the discriminant",
   r"Set the $y$-values equal: $x^2-4x+4=0$, i.e. $(x-2)^2=0$. The only solution is $x=2$, so the line is tangent to the parabola: exactly one common point. (Two comes from counting the repeated factor twice.)",
   order='free')

gi(1, 'M',
   r"The numbers $x$ and $y$ satisfy $x-y=2$ and $xy=15$, with $x>0$. What is the value of $x+y$?",
   "8", Integer(8),
   lambda: [s_[x] + s_[y] for s_ in solve([x - y - 2, x*y - 15], [x, y], dict=True) if s_[x] > 0][0],
   "Substitute into the product",
   r"Put $y=x-2$ into $xy=15$: $x^2-2x-15=0$, so $x=5$ or $x=-3$. Since $x>0$, $x=5$ and $y=3$, so $x+y=8$. (The pair $x=-3,y=-5$ would give $-8$.)")

mc(1, 'M',
   r"What is the sum of all real solutions of $\sqrt{3x+4}=x$?",
   C(4), [C(3), C(-1), C(5)],
   lambda: sum(t_ for t_ in solveset(sqrt(3*x + 4) - x, x, S.Reals)),
   "Radical equation: square, then check",
   r"Squaring: $3x+4=x^2$, so $x^2-3x-4=0$ and $x=4$ or $x=-1$. Check: $\sqrt{16}=4$ works, but $\sqrt1=1\ne-1$, so $-1$ is extraneous. Only $x=4$ is a solution. (3 is the sum of both roots; $-1$ is the extraneous root; 5 is their difference.)")

mc(1, 'H',
   r"How many real solutions does the equation $$\dfrac{3}{x-2}-\dfrac{12}{x^2-4}=1$$ have?",
   C(1), [C(0), C(2), C(3)],
   lambda: len(rsol(3/(x - 2) - 12/(x**2 - 4) - 1)),
   "Rational equation: reject excluded values",
   r"Multiply by $(x-2)(x+2)$: $3(x+2)-12=x^2-4$, so $x^2-3x+2=0$ and $x=1$ or $x=2$. But $x=2$ makes a denominator $0$, so only $x=1$ is a solution. (Two is the trap: it counts the excluded value.)")

mc(1, 'M',
   r"How many real solutions does the equation $x^4-5x^2-36=0$ have?",
   C(2), [C(0), C(1), C(4)],
   lambda: len(scan(lambda t_: t_**4 - 5*t_**2 - 36, -10, 10, 20000)),
   "Quadratic form: u = x squared",
   r"Let $u=x^2$: $u^2-5u-36=0$, so $u=9$ or $u=-4$. Since $x^2$ cannot be negative, only $x^2=9$ works: $x=3$ or $x=-3$, two solutions. (Four counts the impossible $x^2=-4$; one forgets $-3$.)")

mc(1, 'M',
   r"The circle with equation $x^2+y^2-6x+10y+18=0$ has center $(h,k)$. What is the value of $h+k$?",
   C(-2), [C(2), C(8), C(-8)],
   lambda: (lambda sol_: sol_[x] + sol_[y])(solve([diff(x**2 + y**2 - 6*x + 10*y + 18, x), diff(x**2 + y**2 - 6*x + 10*y + 18, y)], [x, y])),
   "Completing the square: read the center",
   r"$(x^2-6x+9)+(y^2+10y+25)=-18+9+25$, so $(x-3)^2+(y+5)^2=16$. The center is $(3,-5)$ and $h+k=-2$. (Reading $(-3,5)$ gives 2; adding absolute values gives 8; $-8$ uses $(-3,-5)$.)")

gi(1, 'H',
   r"When $x^3-4x^2+2x+9$ is divided by $x-3$, the result can be written as $x^2+ax+b+\dfrac{r}{x-3}$, where $a$, $b$ and $r$ are constants. What is the value of $a+b+r$?",
   "4", Integer(4),
   lambda: (lambda qr: Poly(qr[0], x).coeff_monomial(x) + Poly(qr[0], x).coeff_monomial(1) + qr[1])(div(x**3 - 4*x**2 + 2*x + 9, x - 3)),
   "Polynomial division (synthetic)",
   r"Synthetic division by $3$ on the coefficients $1,-4,2,9$ gives $1,-1,-1$ and remainder $6$. So the quotient is $x^2-x-1$ and $r=6$: $a+b+r=-1-1+6=4$.")

mc(1, 'M',
   r"For $x>0$, which expression is equivalent to $\sqrt[3]{x^{2}}\cdot\sqrt{x}$?",
   C(r"x^{7/6}", Rational(7, 6)),
   [C(r"x^{1/3}", Rational(1, 3)), C(r"x^{3/5}", Rational(3, 5)), C(r"x^{1/6}", Rational(1, 6))],
   lambda: simplify((xp**2)**Rational(1, 3) * sqrt(xp)).as_base_exp()[1],
   "Fractional exponents: add when multiplying",
   r"$\sqrt[3]{x^2}=x^{2/3}$ and $\sqrt x=x^{1/2}$. Multiplying the same base adds the exponents: $\frac23+\frac12=\frac76$. ($x^{1/3}$ multiplies the exponents; $x^{3/5}$ adds tops and bottoms; $x^{1/6}$ subtracts.)",
   order='free')

gi(1, 'M',
   r"The length of a rectangular garden is 5 meters more than its width. The area is 84 square meters. What is the perimeter of the garden, in meters?",
   "38", Integer(38),
   lambda: [2*(2*w_ + 5) for w_ in solveset(w**2 + 5*w - 84, w, S.Reals) if w_ > 0][0],
   "Word problem: area gives a quadratic",
   r"With width $w$: $w(w+5)=84$, so $w^2+5w-84=0$ and $(w+12)(w-7)=0$. The width is $7$ (not $-12$) and the length is $12$, so the perimeter is $2(7+12)=38$.")

mc(1, 'H',
   r"In the equation $3x^2-6x=k$, $k$ is a constant. The equation has no real solutions. Which of the following could be the value of $k$?",
   C(-5), [C(-3), C(-1), C(2)],
   None,
   "Discriminant: strict inequality",
   r"Write it as $3x^2-6x-k=0$: $D=36+12k$. No real solutions needs $D<0$, so $k<-3$. Only $-5$ works. ($k=-3$ gives $D=0$, which is exactly one solution, so the boundary is not allowed; $-1$ and $2$ give two.)",
   each=lambda v_: nreal(3*x**2 - 6*x - v_) == 0)

# ============================================================ SET 2  (Hard, 14)
mc(2, 'H',
   r"In the $xy$-plane, the line $y=4x+c$ is tangent to the parabola $y=x^2+2x+7$. What is the value of $c$?",
   C(6), [C(-2), C(7), C(10)],
   lambda: [cc for cc in range(-40, 41) if disc(x**2 + 2*x + 7 - (4*x + cc)) == 0],
   "Tangent: D = 0 after setting equal",
   r"Set equal: $x^2-2x+(7-c)=0$. Tangent means $D=4-4(7-c)=0$, so $7-c=1$ and $c=6$. ($-2$ adds the slopes instead of subtracting; 7 is the parabola's $y$-intercept; 10 is the $y$-coordinate of the tangent point $(1,10)$.)",
   order='free')

gi(2, 'H',
   r"How many integer values of $k$ make the line $y=x+k$ intersect the circle $x^2+y^2=36$ at exactly two points?",
   "17", Integer(17),
   lambda: Integer(len([kk for kk in range(-30, 31) if disc(x**2 + (x + kk)**2 - 36) > 0])),
   "Circle and line: substitute, D > 0",
   r"Substitute $y=x+k$: $2x^2+2kx+k^2-36=0$. $D=4k^2-8(k^2-36)=288-4k^2>0$ gives $k^2<72$, so $|k|<8.49$. The integers $-8,\dots,8$ number $17$. (Edge check: $k=8$ gives $D=288-256=32>0$; $k=9$ gives $D=288-324<0$.)")

mc(2, 'H',
   r"The graphs of $y=-2x^2+12x-5$ and $y=k$ have no points in common, where $k$ is a constant. Which of the following could be the value of $k$?",
   C(14), [C(-5), C(12), C(13)],
   None,
   "Horizontal line versus the vertex",
   r"The parabola opens downward with its vertex at $x=3$: $y=-18+36-5=13$. The line misses the parabola only when $k>13$, so $14$ works. ($k=13$ touches the vertex; $12$ and $-5$ cut the parabola twice. $-5$ is the $y$-intercept.)",
   each=lambda v_: nreal(-2*x**2 + 12*x - 5 - v_) == 0)

gi(2, 'H',
   r"The equation $x^2-2kx+3k+4=0$, where $k$ is a constant, has exactly one real solution. What is the sum of all possible values of $k$?",
   "3", Integer(3),
   lambda: sum(solve(disc(x**2 - 2*k*x + 3*k + 4, x), k)),
   "D = 0 can give two values of the parameter",
   r"$D=4k^2-4(3k+4)=4(k^2-3k-4)=4(k-4)(k+1)$. $D=0$ gives $k=4$ or $k=-1$, and both give exactly one solution. The sum is $3$. (Stopping at the positive value gives 4.)")

mc(2, 'H',
   r"What is the greatest integer $c$ for which the graph of $y=x^2+6x+c$ intersects the line $y=2$ at two points?",
   C(10), [C(11), C(9), C(8)],
   lambda: max(cc for cc in range(-30, 40) if disc(x**2 + 6*x + cc - 2) > 0),
   "Two intersections: D > 0 (strict)",
   r"Set equal: $x^2+6x+(c-2)=0$ and need $D=36-4(c-2)>0$, so $c<11$. The greatest integer is $10$. ($c=11$ gives $D=0$, a tangent. $9$ and $8$ forget to subtract the $2$ from $c$.)")

mc(2, 'H',
   r"The equation $(k-2)x^2+6x+3=0$ has two distinct real solutions. Which of the following could be the value of $k$?",
   C(4), [C(2), C(5), C(7)],
   None,
   "A parameter in the leading coefficient",
   r"For $k=4$: $2x^2+6x+3=0$ has $D=36-24=12>0$, two solutions. At $k=2$ the $x^2$ term vanishes and $6x+3=0$ has one solution (not a quadratic at all). At $k=5$, $D=36-12(3)=0$; at $k=7$, $D=36-60<0$.",
   each=lambda v_: nreal((v_ - 2)*x**2 + 6*x + 3) == 2)

mc(2, 'H',
   r"The graphs of $y=x^2-4x+7$ and $y=-2x+k$ intersect at two points. Which of the following describes all possible values of $k$?",
   T(r"$k>6$", 'gt6'), [T(r"$k<6$", 'lt6'), T(r"$k\ge6$", 'ge6'), T(r"$k>7$", 'gt7')],
   None,
   "Two intersections: D > 0",
   r"Set equal: $x^2-2x+(7-k)=0$, $D=4-4(7-k)=4k-24$. Two points need $D>0$, so $k>6$. ($k=6$ is tangent, so $\ge$ is wrong; $k<6$ reverses the sign; $k>7$ uses the parabola's $y$-intercept.)",
   order='free',
   each=lambda v_: all(
       {'gt6': kk > 6, 'lt6': kk < 6, 'ge6': kk >= 6, 'gt7': kk > 7}[v_] == (nreal(x**2 - 4*x + 7 - (-2*x + kk)) == 2)
       for kk in [Rational(i, 4) for i in range(-40, 80)]))

mc(2, 'H',
   r"In the equation $x^2+kx+12=0$, $k$ is an integer. The equation has two distinct real solutions and both are negative. What is the least possible value of $k$?",
   C(7), [C(-7), C(4), C(6)],
   lambda: min(kk for kk in range(-30, 31)
               if nreal(x**2 + kk*x + 12) == 2 and all(r_ < 0 for r_ in rs(x**2 + kk*x + 12))),
   "Sign of roots: sum, product and D",
   r"Product $12>0$ means the roots have the same sign; their sum $-k$ must be negative, so $k>0$. Two distinct roots need $D=k^2-48>0$, so $k\ge7$. The least is $7$. ($k=6$ has $D<0$; $-7$ gives two positive roots; $4$ is $3+4$ from a factor pair.)")

mc(2, 'H',
   r"The line $y=-x+k$, where $k>0$, is tangent to the circle $(x-2)^2+(y-1)^2=18$. What is the value of $k$?",
   C(9), [C(-3), C(3), C(6)],
   lambda: [kk for kk in range(1, 40) if disc((x - 2)**2 + (-x + kk - 1)**2 - 18) == 0],
   "Tangent to a circle: D = 0",
   r"Substitute $y=-x+k$: $2x^2-2(k+1)x+(k-1)^2+4-18=0$ has $D=0$ exactly when $(k-3)^2=36$, so $k=9$ or $k=-3$. Since $k>0$, $k=9$. ($-3$ is the other tangent line; 3 is the center's coordinate sum; 6 is $|k-3|$ before finishing.)")

mc(2, 'H',
   r"For a constant $k$, the equation $(x+1)(x-5)=k$ has exactly one real solution. What is the value of $k$?",
   C(-9), [C(-5), C(2), C(9)],
   lambda: solve(disc(expand((x + 1)*(x - 5) - k), x), k),
   "Disguised quadratic: expand first",
   r"Expand and move $k$: $x^2-4x-5-k=0$. $D=16+4(5+k)=0$ gives $k=-9$. (It is the minimum value of $(x+1)(x-5)$, at the vertex $x=2$. $-5$ is the constant term, 2 is the vertex's $x$-coordinate, 9 is a sign slip.)")

mc(2, 'H',
   r"For how many values of $k$ does the line $y=k(x-3)+1$ meet the parabola $y=x^2-6x+10$ at exactly one point?",
   C(1), [C(0), C(2), T("Infinitely many", 'infinite')],
   lambda: len([kk for kk in solveset(disc(expand(x**2 - 6*x + 10 - (k*(x - 3) + 1)), x), k, S.Reals)]),
   "Line through the vertex",
   r"Set equal: $x^2-(6+k)x+(9+3k)=0$ has $D=(6+k)^2-4(9+3k)=k^2$. $D=0$ only for $k=0$. The point $(3,1)$ is the vertex of the parabola, so the only tangent through it is the horizontal line; every other slope cuts the parabola twice. (Two is the trap, from thinking of a point with two tangents.)",
   order='free')

mc(2, 'H',
   r"What is the greatest integer $k$ for which the graph of $y=x^2-7x+k$ has at least one $x$-intercept?",
   C(12), [C(13), C("12.25", Rational(49, 4)), C(7)],
   lambda: max(kk for kk in range(-20, 40) if disc(x**2 - 7*x + kk) >= 0),
   "At least one: D ≥ 0",
   r"An $x$-intercept needs a real solution of $x^2-7x+k=0$: $D=49-4k\ge0$, so $k\le12.25$. The greatest integer is $12$. (13 rounds up; 12.25 is the bound but is not an integer; 7 is $-b$.)")

gi(2, 'H',
   r"The line $y=2x+10$ is tangent to the circle $x^2+y^2=r^2$, where $r>0$. What is the value of $r^2$?",
   "20", Integer(20),
   lambda: [rr for rr in range(1, 400) if disc(x**2 + (2*x + 10)**2 - rr) == 0][0],
   "Tangent: the discriminant contains the radius",
   r"Substitute: $5x^2+40x+(100-r^2)=0$. $D=1600-20(100-r^2)=0$ gives $20r^2=400$, so $r^2=20$. (Check by distance: $\frac{10}{\sqrt5}=\sqrt{20}$.)")

gi(2, 'H',
   r"How many integer values of $c$ make $x^2-6x+c=0$ have two distinct real solutions that are both positive?",
   "8", Integer(8),
   lambda: Integer(len([cc for cc in range(-30, 30)
                        if nreal(x**2 - 6*x + cc) == 2 and all(r_ > 0 for r_ in rs(x**2 - 6*x + cc))])),
   "Sign of roots: D > 0 and product > 0",
   r"Two distinct real roots need $D=36-4c>0$, so $c<9$. Both roots have the same sign when the product $c>0$, and the sum $6>0$ makes them positive. So $c=1,2,\dots,8$: eight values. ($c=9$ gives one solution; $c=0$ gives the root $0$, which is not positive.)")

# ============================================================ SET 3  (Hard, 14)
mc(3, 'H',
   r"What is the sum of all real solutions of $\sqrt{x+7}+5=x$?",
   C(9), [C(2), C(11), C(18)],
   lambda: sum(t_ for t_ in solveset(sqrt(x + 7) + 5 - x, x, S.Reals)),
   "Isolate the radical, square, check",
   r"Isolate: $\sqrt{x+7}=x-5$. Squaring: $x+7=x^2-10x+25$, so $x^2-11x+18=0$ and $x=2$ or $x=9$. Check: $x=9$ gives $4+5=9$; $x=2$ gives $3+5=8\ne2$, so it is extraneous. The sum is $9$. (11 adds both roots; 2 is the extraneous root; 18 is the product.)",
   order='free')

gi(3, 'H',
   r"In the equation $\sqrt{2x+k}=x$, $k$ is a negative constant. The equation has exactly one real solution. What is the value of $k$?",
   "-1", Integer(-1),
   lambda: (lambda L: L[0] if len(L) == 1 else None)([Rational(i, 4) for i in range(-40, 0) if rad_count(Rational(i, 4)) == 1]),
   "Radical with a parameter: D = 0 and check",
   r"Square: $x^2-2x-k=0$, $D=4+4k$. For $-1<k<0$ it has two positive roots, both valid (two solutions); for $k<-1$ none. At $k=-1$: $(x-1)^2=0$, $x=1$, and $\sqrt1=1$ checks. So $k=-1$.")

mc(3, 'H',
   r"What is the sum of all solutions of $$\dfrac{x}{x-4}+\dfrac{3}{x+1}=\dfrac{20}{x^2-3x-4}\,?$$",
   C(-8), [C(-4), C(4), C(8)],
   lambda: sum(rsol(x/(x - 4) + 3/(x + 1) - 20/(x**2 - 3*x - 4))),
   "Rational equation: LCD and excluded values",
   r"Since $x^2-3x-4=(x-4)(x+1)$, multiply by it: $x(x+1)+3(x-4)=20$, so $x^2+4x-32=0$ and $x=4$ or $x=-8$. But $x=4$ makes a denominator $0$, so the only solution is $-8$. ($-4$ adds both roots; $4$ is the excluded root.)")

gi(3, 'H',
   r"Consider the equation $$\dfrac{1}{x-3}+\dfrac{k}{x^2-9}=\dfrac{2}{x+3},$$ where $k$ is a constant. What is the sum of all values of $k$ for which the equation has no solution?",
   "-18", Integer(-18),
   lambda: sum(kk for kk in range(-60, 61)
               if len(rsol(1/(x - 3) + kk/(x**2 - 9) - 2/(x + 3))) == 0),
   "Rational with a parameter: the solution lands on an excluded value",
   r"Multiply by $(x-3)(x+3)$: $(x+3)+k=2(x-3)$, so $x=k+9$. This is a solution unless it is excluded: $k+9=3$ gives $k=-6$, and $k+9=-3$ gives $k=-12$. The sum is $-18$.")

mc(3, 'H',
   r"What is the sum of all real solutions of $x^{2/3}-x^{1/3}-6=0$?",
   C(19), [C(1), C(27), C(35)],
   lambda: sum(rr for rr in range(-200, 200) if (lambda cr: cr**2 - cr - 6)(creal(rr)) == 0),
   "Quadratic form: u = cube root of x",
   r"Let $u=x^{1/3}$: $u^2-u-6=0$, so $u=3$ or $u=-2$. Cube: $x=27$ or $x=-8$. The sum is $19$. (1 is the sum of the $u$-values; 27 forgets the negative root; 35 adds $27+8$.)")

mc(3, 'H',
   r"What is the sum of all real solutions of $9^x-12\cdot3^x+27=0$?",
   C(3), [C(2), C(9), C(12)],
   lambda: sum(round(t_) for t_ in scan(lambda z_: 9.0**z_ - 12*3.0**z_ + 27, -10, 10, 40000)),
   "Quadratic form: u = 3 to the x",
   r"$9^x=(3^x)^2$. With $u=3^x$: $u^2-12u+27=0$, so $u=3$ or $u=9$, giving $x=1$ or $x=2$. The sum is $3$. (12 is the sum of the $u$-values; 9 is one $u$; 2 is the product of the $x$-values.)",
   order='free')

mc(3, 'H',
   r"What is the sum of all real solutions of $x^{-2}-5x^{-1}+4=0$?",
   C(r"\dfrac54", Rational(5, 4)), [C(5), C(r"\dfrac14", Rational(1, 4)), C(4)],
   lambda: sum(rsol(x**-2 - 5*x**-1 + 4)),
   "Quadratic form: u = 1/x",
   r"Let $u=\frac1x$: $u^2-5u+4=0$, so $u=1$ or $u=4$. Then $x=1$ or $x=\frac14$, and the sum is $\frac54$. (5 is the sum of the $u$-values; $\frac14$ is the product of the $x$-values; 4 is one $u$.)")

mc(3, 'H',
   r"A ball's height, in meters, $t$ seconds after it is thrown is $h(t)=-5t^2+30t+5$. For how many seconds is the ball more than 45 meters above the ground?",
   C(2), [C(3), C(4), C(6)],
   lambda: (lambda rts: rts[1] - rts[0])(rs(-5*t**2 + 30*t + 5 - 45, t)),
   "Projectile: two crossing times, subtract",
   r"$-5t^2+30t+5=45$ gives $t^2-6t+8=0$, so $t=2$ or $t=4$. Above 45 m between those times: $4-2=2$ seconds. (3 is the time of the peak; 4 is the later crossing alone; 6 is when the ball is back at the launch height.)")

mc(3, 'H',
   r"The sum of the squares of three consecutive positive integers is 110. What is the sum of the three integers?",
   C(18), [C(6), C(21), C(36)],
   lambda: [3*nn for nn in range(1, 60) if (nn - 1)**2 + nn**2 + (nn + 1)**2 == 110][0],
   "Consecutive integers: middle one as n",
   r"Call them $n-1,n,n+1$: $3n^2+2=110$, so $n^2=36$ and $n=6$ (positive). The integers are $5,6,7$ ($25+36+49=110$) and their sum is $18$. (6 is only the middle integer; 36 is $n^2$.)")

mc(3, 'H',
   r"Pump A alone fills a tank in 3 hours less than pump B alone. Working together they fill the tank in 2 hours. How many hours would pump B take working alone?",
   C(6), [C(3), C(5), C(9)],
   lambda: [tt + 3 for tt in solveset(1/t + 1/(t + 3) - Rational(1, 2), t, S.Reals) if tt > 0][0],
   "Work rates add: a fraction equation becomes a quadratic",
   r"If A takes $t$ hours, B takes $t+3$: $\frac1t+\frac1{t+3}=\frac12$, so $2(2t+3)=t(t+3)$, $t^2-t-6=0$ and $t=3$. Then B takes $3+3=6$ hours. (3 is pump A; 5 is $2+3$; 9 adds 3 to the wrong value.)",
   order='free')

mc(3, 'H',
   r"A poster is 20 cm wide and 30 cm tall. A border of the same width $x$ is added on all four sides, and the new total area is 1,200 square centimeters. What is the value of $x$, in centimeters?",
   C(5), [C(10), C(25), C(30)],
   lambda: [xx for xx in solveset((20 + 2*x)*(30 + 2*x) - 1200, x, S.Reals) if xx > 0][0],
   "Border on all sides: both dimensions grow by 2x",
   r"$(20+2x)(30+2x)=1200$ gives $4x^2+100x-600=0$, so $x^2+25x-150=0$ and $(x+30)(x-5)=0$. The positive root is $5$. (10 solves $(20+x)(30+x)=1200$, one border only; 25 is the middle coefficient; 30 is the negative root with its sign dropped.)")

gi(3, 'H',
   r"The system $x-2y=4$ and $xy=48$ has two solutions $(x,y)$. What is the sum of the $x$-coordinates of the two solutions?",
   "4", Integer(4),
   lambda: sum(s_[x] for s_ in solve([x - 2*y - 4, x*y - 48], [x, y], dict=True)),
   "Substitute into the product",
   r"Put $x=2y+4$ into $xy=48$: $2y^2+4y-48=0$, so $y^2+2y-24=0$ and $y=4$ or $y=-6$. Then $x=12$ or $x=-8$. The sum of the $x$-coordinates is $12+(-8)=4$.")

mc(3, 'H',
   r"What is the sum of all real solutions of $9^{x}=3^{x^2-3}$?",
   C(2), [C(1), C(3), C(-3)],
   lambda: sum(round(t_) for t_ in scan(lambda z_: 9.0**z_ - 3.0**(z_**2 - 3), -10, 10, 40000)),
   "Same base first, then a quadratic",
   r"$9^x=3^{2x}$, so $2x=x^2-3$, i.e. $x^2-2x-3=0$ and $x=3$ or $x=-1$. The sum is $2$. (Forgetting $9=3^2$ gives $x=x^2-3$, with sum 1; 3 is one solution; $-3$ is their product.)",
   order='free')

gi(3, 'H',
   r"A cyclist rides 24 miles to a town at a constant speed. The return trip, at a speed 2 miles per hour faster, takes 1 hour less. What was the cyclist's speed, in miles per hour, on the way to the town?",
   "6", Integer(6),
   lambda: [vv for vv in solveset(24/v - 24/(v + 2) - 1, v, S.Reals) if vv > 0][0],
   "Distance = rate x time: a quadratic in the speed",
   r"If the first speed is $v$, then $\frac{24}{v}-\frac{24}{v+2}=1$. Multiply by $v(v+2)$: $48=v^2+2v$, so $v^2+2v-48=0$ and $(v+8)(v-6)=0$. So $v=6$ (times $4$ h and $3$ h).")

# ============================================================ SET 4  (Hard, 14)
mc(4, 'H',
   r"Which of the following is NOT a factor of $x^4-13x^2+36$?",
   T(r"$x^2+4$", 'x2p4'), [T(r"$x+2$", 'xp2'), T(r"$x-3$", 'xm3'), T(r"$x^2-9$", 'x2m9')],
   None,
   "Factor in quadratic form, then split fully",
   r"With $u=x^2$: $u^2-13u+36=(u-4)(u-9)$, so $x^4-13x^2+36=(x^2-4)(x^2-9)=(x-2)(x+2)(x-3)(x+3)$. So $x+2$, $x-3$ and $x^2-9$ are factors, but $x^2+4$ is not (it would come from the sign error $(x^2+4)(x^2+9)$).",
   order='free',
   each=lambda v_: not divisible(x**4 - 13*x**2 + 36, {'x2p4': x**2 + 4, 'xp2': x + 2, 'xm3': x - 3, 'x2m9': x**2 - 9}[v_]))

mc(4, 'H',
   r"Which of the following is a factor of $2x^3-3x^2-8x+12$?",
   T(r"$2x-3$", 'a'), [T(r"$2x+3$", 'b'), T(r"$3x-2$", 'c'), T(r"$x+3$", 'd')],
   None,
   "Factor by grouping",
   r"Group: $x^2(2x-3)-4(2x-3)=(2x-3)(x^2-4)=(2x-3)(x-2)(x+2)$. So $2x-3$ is a factor. (The roots are $\frac32,\,2,\,-2$, so $2x+3$ is a sign slip, $3x-2$ swaps the numbers, and $x+3$ uses a root that does not exist.)",
   order='free',
   each=lambda v_: divisible(2*x**3 - 3*x**2 - 8*x + 12, {'a': 2*x - 3, 'b': 2*x + 3, 'c': 3*x - 2, 'd': x + 3}[v_]))

gi(4, 'H',
   r"When $6x^2+x-12$ is divided by $2x-3$, the result can be written as $ax+b+\dfrac{r}{2x-3}$, where $a$, $b$ and $r$ are constants. What is the value of $a+b+r$?",
   "11", Integer(11),
   lambda: (lambda qr: Poly(qr[0], x).coeff_monomial(x) + Poly(qr[0], x).coeff_monomial(1) + qr[1])(div(6*x**2 + x - 12, 2*x - 3)),
   "Polynomial long division with a non-monic divisor",
   r"$6x^2\div2x=3x$: subtract $3x(2x-3)=6x^2-9x$, leaving $10x-12$. $10x\div2x=5$: subtract $5(2x-3)=10x-15$, leaving $3$. So $a=3$, $b=5$, $r=3$ and the sum is $11$. (Using the root $3$ instead of $\frac32$ gives the wrong remainder $33$.)")

mc(4, 'H',
   r"Which expression is equivalent to $\dfrac{2}{x-3}-\dfrac{1}{x+3}+\dfrac{12}{x^2-9}$ for $x\neq\pm3$?",
   T(r"$\dfrac{x+21}{x^2-9}$", 'a'),
   [T(r"$\dfrac{x+15}{x^2-9}$", 'b'), T(r"$\dfrac{x+9}{x^2-9}$", 'c'), T(r"$\dfrac{x+21}{2x}$", 'd')],
   None,
   "Common denominator: distribute the minus sign",
   r"Use $x^2-9=(x-3)(x+3)$: numerator $=2(x+3)-(x-3)+12=2x+6-x+3+12=x+21$. (Writing $-(x-3)$ as $-x-3$ gives $x+15$; dropping the $12$ gives $x+9$; adding denominators gives $2x$.)",
   order='free',
   each=lambda v_: all(simplify((2/(x - 3) - 1/(x + 3) + 12/(x**2 - 9)) -
                                {'a': (x + 21)/(x**2 - 9), 'b': (x + 15)/(x**2 - 9), 'c': (x + 9)/(x**2 - 9), 'd': (x + 21)/(2*x)}[v_]).subs(x, tv) == 0
                       for tv in [Rational(5), Rational(7, 2), Rational(-8)]))

mc(4, 'H',
   r"Which of the following is a factor of $x^4+x^2+1$?",
   T(r"$x^2+x+1$", 'a'), [T(r"$x^2+1$", 'b'), T(r"$x^2-x-1$", 'c'), T(r"$x^2-1$", 'd')],
   None,
   "Rewrite for a hidden difference of squares",
   r"$x^4+x^2+1=(x^4+2x^2+1)-x^2=(x^2+1)^2-x^2=(x^2+1-x)(x^2+1+x)$. So $x^2+x+1$ is a factor. (Each other choice leaves a nonzero remainder.)",
   order='free',
   each=lambda v_: divisible(x**4 + x**2 + 1, {'a': x**2 + x + 1, 'b': x**2 + 1, 'c': x**2 - x - 1, 'd': x**2 - 1}[v_]))

mc(4, 'H',
   r"If $(x^2+ax+4)(x^2-ax+4)=x^4-x^2+16$ for all $x$, and $a>0$, what is the value of $a$?",
   C(3), [C(1), C(7), C(9)],
   lambda: [aa for aa in range(1, 30) if expand((x**2 + aa*x + 4)*(x**2 - aa*x + 4) - (x**4 - x**2 + 16)) == 0],
   "Spot (A + B)(A - B)",
   r"The product is $(x^2+4)^2-a^2x^2=x^4+(8-a^2)x^2+16$. Matching the $x^2$-coefficient: $8-a^2=-1$, so $a^2=9$ and $a=3$. (Dropping the $8$ gives 1; $8-1=7$ and $a^2=9$ are traps.)")

gi(4, 'H',
   r"For $x>0$, $\sqrt[3]{x^4\sqrt{x}}=x^k$. What is the value of $k$?",
   "3/2", Rational(3, 2),
   lambda: simplify(((xp**4*sqrt(xp))**Rational(1, 3))).as_base_exp()[1],
   "Fractional exponents: inside first, then the root",
   r"$x^4\sqrt x=x^{4+1/2}=x^{9/2}$. The cube root is the power $\frac13$: $\left(x^{9/2}\right)^{1/3}=x^{3/2}$. So $k=\frac32=1.5$.")

mc(4, 'H',
   r"If $x<3$, which of the following is equivalent to $\sqrt{x^2-6x+9}$?",
   T(r"$3-x$", 'a'), [T(r"$x-3$", 'b'), T(r"$|x|-3$", 'c'), T(r"$x+3$", 'd')],
   None,
   "Square root of a square is an absolute value",
   r"$x^2-6x+9=(x-3)^2$, and $\sqrt{(x-3)^2}=|x-3|$. For $x<3$, $x-3$ is negative, so $|x-3|=3-x$. (Choice B is the answer only when $x\ge3$; $|x|-3$ and $x+3$ are not even equal to $|x-3|$ in general.)",
   order='free',
   each=lambda v_: all(
       sqrt(tv**2 - 6*tv + 9) == {'a': 3 - tv, 'b': tv - 3, 'c': abs(tv) - 3, 'd': tv + 3}[v_]
       for tv in [Rational(i, 2) for i in range(-20, 6)]))

mc(4, 'H',
   r"The equation $x^2+y^2+8x-2y=k$ represents a circle with radius 5 in the $xy$-plane. What is the value of $k$?",
   C(8), [C(5), C(25), C(42)],
   lambda: (lambda f: f(1, 1) if f(1, 1) == f(-4, 6) == f(-9, 1) == f(-4, -4) else None)(lambda px, py: px**2 + py**2 + 8*px - 2*py),
   "Completing the square: the right side becomes r squared",
   r"Complete both squares: $(x+4)^2+(y-1)^2=k+16+1=k+17$. The radius is 5, so $k+17=25$ and $k=8$. (5 is the radius; 25 is $r^2$; $42$ comes from $k-17=25$.)")

gi(4, 'H',
   r"One solution of $2x^2-12x+3=0$ can be written as $3+\dfrac{\sqrt b}{2}$, where $b$ is a positive constant. What is the value of $b$?",
   "30", Integer(30),
   lambda: [bb for bb in range(1, 400) if simplify((3 + sqrt(bb)/2) - max(rs(2*x**2 - 12*x + 3))) == 0][0],
   "Completing the square with a leading coefficient",
   r"Divide by 2: $x^2-6x=-\frac32$. Add $9$: $(x-3)^2=\frac{15}2$. Then $x=3\pm\sqrt{\frac{15}{2}}=3\pm\frac{\sqrt{30}}{2}$, so $b=30$. (Skipping the division by 2 gives the wrong $b$.)")

mc(4, 'H',
   r"How many points $(x,y)$ in the $xy$-plane satisfy $x^2+y^2+6x-4y+13=0$?",
   C(1), [C(0), C(2), T("Infinitely many", 'infinite')],
   lambda: (lambda f, crit: 1 if f.subs(crit) == 0 else (0 if f.subs(crit) > 0 else 2))(x**2 + y**2 + 6*x - 4*y + 13, solve([diff(x**2 + y**2 + 6*x - 4*y + 13, x), diff(x**2 + y**2 + 6*x - 4*y + 13, y)], [x, y])),
   "Completing the square: a circle of radius 0",
   r"$(x+3)^2+(y-2)^2=-13+9+4=0$. A sum of squares is $0$ only when both are $0$: $x=-3$, $y=2$. Exactly one point. (This is a circle with radius $0$; it is not a full circle with infinitely many points.)",
   order='free')

mc(4, 'H',
   r"Which expression is equivalent to $\dfrac{x^3-27}{x-3}$ for $x\neq3$?",
   T(r"$x^2+3x+9$", 'a'), [T(r"$x^2-3x+9$", 'b'), T(r"$x^2+9$", 'c'), T(r"$x^2-9$", 'd')],
   None,
   "Difference of cubes: a³ − b³",
   r"$x^3-27=(x-3)(x^2+3x+9)$, so the quotient is $x^2+3x+9$. Check by multiplying: $(x-3)(x^2+3x+9)=x^3+3x^2+9x-3x^2-9x-27$. (Wrong signs or a dropped middle term are the usual traps.)",
   order='free',
   each=lambda v_: simplify(cancel((x**3 - 27)/(x - 3)) - {'a': x**2 + 3*x + 9, 'b': x**2 - 3*x + 9, 'c': x**2 + 9, 'd': x**2 - 9}[v_]) == 0)

gi(4, 'H',
   r"For constants $A$ and $B$, $$\dfrac{5x-1}{x^2-x-2}=\dfrac{A}{x-2}+\dfrac{B}{x+1}$$ for all $x$ except $2$ and $-1$. What is the value of $AB$?",
   "6", Integer(6),
   lambda: (lambda sl: sl[A_] * sl[B_])(solve(expand((A_*(x + 1) + B_*(x - 2) - (5*x - 1))).as_poly(x).all_coeffs(), [A_, B_], dict=True)[0]),
   "Equate numerators; plug in the excluded values",
   r"Multiply by $(x-2)(x+1)$: $5x-1=A(x+1)+B(x-2)$. At $x=2$: $9=3A$, so $A=3$. At $x=-1$: $-6=-3B$, so $B=2$. Then $AB=6$.")

mc(4, 'H',
   r"If $4^x+4^x+4^x+4^x=2^{18}$, what is the value of $x$?",
   C(8), [C(9), C("4.5", Rational(9, 2)), C(16)],
   lambda: [xx for xx in range(-30, 40) if 4*Integer(4)**xx == Integer(2)**18][0],
   "Same base: combine like terms first",
   r"Four equal terms: $4\cdot4^x=4^{x+1}$. Write the right side with base 4: $2^{18}=4^9$. So $x+1=9$ and $x=8$. (9 forgets the $+1$; 4.5 divides $18$ by $4$; 16 subtracts $2$ without halving.)")

# ============================================================ SET 5  (Summit, 20)
def _rad_valid_count(kk):
    """Solutions of sqrt(x+kk) = x-4 (squared candidates, then checked in the original)."""
    cands = solveset(x**2 - 9*x + 16 - kk, x, S.Reals)
    return len([t_ for t_ in cands if t_ - 4 >= 0 and simplify(sqrt(t_ + kk) - (t_ - 4)) == 0])

gi(5, 'H',
   r"For how many integer values of $k$ from $-10$ to $10$, inclusive, does the equation $\sqrt{x+k}=x-4$ have exactly one real solution?",
   "14", Integer(14),
   lambda: Integer(len([kk for kk in range(-10, 11) if _rad_valid_count(kk) == 1])),
   "Radical + discriminant: which roots survive the check?",
   r"Squaring: $x^2-9x+(16-k)=0$ with $D=17+4k$. A solution must also satisfy $x\ge4$. For $k\le-5$: no real roots. For $k=-4$: roots $5$ and $4$, both valid (two solutions). For $k\ge-3$: the larger root $\frac{9+\sqrt D}{2}>4$ is valid, but the smaller root $\frac{9-\sqrt D}{2}<4$ is extraneous, so exactly one solution. The integers $-3,\dots,10$ number $14$.")

mc(5, 'H',
   r"The line $y=2x+b$, where $b>0$, is tangent to the circle $x^2+y^2-4x+2y=15$. What is the value of $b$?",
   C(5), [C(-15), C(10), C(15)],
   lambda: [bb for bb in range(1, 60) if disc(x**2 + (2*x + bb)**2 - 4*x + 2*(2*x + bb) - 15) == 0],
   "Tangent to a circle: substitute, D = 0",
   r"Substitute $y=2x+b$: $5x^2+4bx+(b^2+2b-15)=0$. $D=16b^2-20(b^2+2b-15)=-4(b^2+10b-75)=-4(b+15)(b-5)=0$, so $b=5$ or $-15$. Since $b>0$, $b=5$. ($-15$ is the other tangent; $15$ is the constant on the right; $10$ is a middle step.)")

mc(5, 'H',
   r"What is the sum of all real solutions of $2^x+2^{3-x}=9$?",
   C(3), [C(0), C(8), C(9)],
   lambda: Integer(round(sum(scan(lambda z_: 2.0**z_ + 2.0**(3 - z_) - 9, -10, 10, 40000)))),
   "Quadratic form: u and 8/u",
   r"$2^{3-x}=\dfrac{8}{2^x}$. With $u=2^x$: $u+\frac8u=9$, so $u^2-9u+8=0$ and $u=1$ or $u=8$. Then $x=0$ or $x=3$, and the sum is $3$. (9 is the sum of the $u$-values; 8 is one $u$; 0 is the product of the solutions.)")

gi(5, 'H',
   r"The equation $x^4-10x^2+9=k$ has exactly three distinct real solutions. What is the value of $k$?",
   "9", Integer(9),
   lambda: [kk for kk in range(-40, 60) if len(set(real_roots(Poly(x**4 - 10*x**2 + 9 - kk, x)))) == 3][0],
   "Quadratic form: one u must be zero",
   r"With $u=x^2$: $u^2-10u+(9-k)=0$. Each positive $u$ gives two $x$-values, $u=0$ gives one, negative $u$ gives none. Three solutions needs the roots $u=0$ and one positive $u$: $9-k=0$, so $k=9$ (then $u=0$ or $10$, and $x=0,\pm\sqrt{10}$).")

mc(5, 'H',
   r"What is the sum of all real solutions of $(x^2-5x)^2+4(x^2-5x)-21=0$?",
   C(5), [C(-4), C(3), C(10)],
   lambda: simplify(sum(rs((x**2 - 5*x)**2 + 4*(x**2 - 5*x) - 21))),
   "Quadratic form: u = x² − 5x, then check each u",
   r"Let $u=x^2-5x$: $u^2+4u-21=(u+7)(u-3)=0$. For $u=3$: $x^2-5x-3=0$ has $D=37>0$ and sum $5$. For $u=-7$: $x^2-5x+7=0$ has $D=-3<0$, no real solution. The sum is $5$. (10 counts both $u$-values as if both gave real roots; $-4$ is the sum of the $u$-values; 3 is one $u$.)",
   order='free')

mc(5, 'H',
   r"For how many integer values of $k$ does the equation $x^2+kx+k+3=0$ have no real solutions?",
   C(7), [C(6), C(8), C(9)],
   lambda: Integer(len([kk for kk in range(-40, 40) if disc(x**2 + kk*x + kk + 3) < 0])),
   "No real solutions: D < 0, a quadratic inequality in k",
   r"$D=k^2-4(k+3)=k^2-4k-12=(k-6)(k+2)<0$ gives $-2<k<6$. The integers $-1,0,\dots,5$ number $7$. (Including $k=6$ or $k=-2$, where $D=0$ gives one solution, produces 8 or 9.)")

mc(5, 'H',
   r"For which value of $k$ does the equation $\dfrac{x^2-x}{x-1}=k$ have no real solution?",
   T(r"$k=1$", 'k1'), [T(r"$k=0$", 'k0'), T(r"$k=-1$", 'km1'), T(r"There is no such $k$.", 'none')],
   None,
   "Cancel first: the hole in the graph",
   r"For $x\neq1$, $\dfrac{x(x-1)}{x-1}=x$, so the equation says $x=k$. That works for every $k$ except $k=1$, because $x=1$ is not allowed. So $k=1$ gives no solution. (The wrong idea is to cross-multiply and find $x=k$ always works.)",
   order='free',
   each=lambda v_: (lambda NOSET: NOSET == {'k1': {1}, 'k0': {0}, 'km1': {-1}, 'none': set()}[v_])(
       set(kk for kk in range(-5, 6) if len(rsol((x**2 - x)/(x - 1) - kk)) == 0)))

mc(5, 'H',
   r"The reciprocals of two consecutive positive even integers add up to $\dfrac{7}{24}$. What is the product of the two integers?",
   C(48), [C(6), C(14), C(24)],
   lambda: [nn*(nn + 2) for nn in range(2, 200, 2) if Rational(1, nn) + Rational(1, nn + 2) == Rational(7, 24)][0],
   "Reciprocals of consecutive numbers: LCD gives a quadratic",
   r"Let the integers be $n$ and $n+2$: $\frac{2n+2}{n(n+2)}=\frac7{24}$, so $48n+48=7n^2+14n$ and $7n^2-34n-48=0$. This factors as $(7n+8)(n-6)=0$, so $n=6$. The integers are $6$ and $8$, with product $48$. (6 is the smaller integer; 14 is their sum; 24 is the denominator.)")

mc(5, 'H',
   r"The circle $x^2+y^2-8x+2y+c=0$ is tangent to the $x$-axis. What is the value of $c$?",
   C(16), [C(1), C(8), C(17)],
   lambda: [cc for cc in range(-50, 60) if disc(x**2 - 8*x + cc) == 0],
   "Tangent to an axis: set y = 0, D = 0",
   r"On the $x$-axis $y=0$, so $x^2-8x+c=0$ must have exactly one solution: $64-4c=0$, $c=16$. (Check: $(x-4)^2+(y+1)^2=17-16=1$, radius $1$ equals the distance from the center $(4,-1)$ to the axis. $c=1$ would make the circle tangent to the $y$-axis; 17 is $r^2+c$.)")

gi(5, 'H',
   r"What is the sum of all real solutions of $x-3\sqrt{x}-10=0$?",
   "25", Integer(25),
   lambda: sum(solveset(x - 3*sqrt(x) - 10, x, S.Reals)),
   "Quadratic form: u = √x must be non-negative",
   r"Let $u=\sqrt x\ge0$: $u^2-3u-10=(u-5)(u+2)=0$. $u=5$ gives $x=25$; $u=-2$ is impossible because a square root is never negative. (Squaring $-2$ would give the false root $x=4$, which fails: $4-6-10\ne0$.) The only solution is $25$.")

mc(5, 'H',
   r"What is the greatest slope $k$ for which the line $y=kx$ and the circle $(x-5)^2+y^2=9$ have at least one point in common?",
   C(r"\dfrac34", Rational(3, 4)), [C(r"\dfrac35", Rational(3, 5)), C(r"\dfrac43", Rational(4, 3)), C(r"\dfrac53", Rational(5, 3))],
   lambda: max(solve(disc(expand((x - 5)**2 + (k*x)**2 - 9), x), k)),
   "Line through the origin and a circle: D ≥ 0",
   r"Substitute: $(1+k^2)x^2-10x+16=0$, $D=100-64(1+k^2)\ge0$, so $k^2\le\frac9{16}$ and $k\le\frac34$. (Geometry check: the radius $3$ and the distance $5$ make a 3-4-5 triangle, so the tangent slope is $\frac34$, not the sine $\frac35$ or the reciprocal $\frac43$.)")

mc(5, 'H',
   r"For how many values of the constant $k$ does the equation $kx^2+4x+k=0$ have exactly one real solution?",
   C(3), [C(0), C(1), C(2)],
   lambda: Integer(len([kk for kk in range(-10, 11) if len(rs(kk*x**2 + 4*x + kk)) == 1])),
   "Do not forget the case where the equation is not quadratic",
   r"For $k\neq0$: $D=16-4k^2=0$ gives $k=2$ or $k=-2$ (one repeated solution each). For $k=0$ the equation is $4x=0$, which also has exactly one solution. So there are $3$ values. (Two forgets the linear case.)")

mc(5, 'H',
   r"In the $xy$-plane, how many points do the graphs of $y=x^2-4$ and $x^2+y^2=16$ have in common?",
   C(3), [C(1), C(2), C(4)],
   lambda: nsys([y - (x**2 - 4), x**2 + y**2 - 16]),
   "Substitute x² (not y): solve for y first",
   r"Since $x^2=y+4$, the circle becomes $y+4+y^2=16$, so $y^2+y-12=0$ and $y=3$ or $y=-4$. For $y=3$: $x^2=7$, two points. For $y=-4$: $x^2=0$, one point $(0,-4)$. Total: $3$. (Four assumes each $y$ gives two points.)")

mc(5, 'H',
   r"If $8^x\cdot4^{x+1}=16^{x+1}$, what is the value of $x$?",
   C(2), [C(-2), C(3), C(4)],
   lambda: [xx for xx in range(-20, 20) if Integer(8)**xx * Integer(4)**(xx + 1) == Integer(16)**(xx + 1)],
   "Rewrite every power with base 2",
   r"$2^{3x}\cdot2^{2x+2}=2^{4x+4}$, so $5x+2=4x+4$ and $x=2$. (Forgetting the $2$ in $4^{x+1}=2^{2x+2}$ gives $x=4$; writing $4^{x+1}=2^{2x+1}$ gives $3$; dropping the $+4$ gives $-2$.)",
   order='free')

gi(5, 'H',
   r"Two lines pass through the point $(0,3)$ and are tangent to the parabola $y=x^2+5x+7$. What is the sum of the slopes of the two lines?",
   "10", Integer(10),
   lambda: sum(solve(disc(expand(x**2 + 5*x + 7 - (m*x + 3)), x), m)),
   "Tangent from an outside point: D = 0 in the slope",
   r"A line through $(0,3)$ is $y=mx+3$. Set equal: $x^2+(5-m)x+4=0$. $D=(5-m)^2-16=0$ gives $5-m=\pm4$, so $m=1$ or $m=9$. The slopes add to $10$.")

gi(5, 'H',
   r"For a nonzero constant $k$, the equations $x^2-6x+k=0$ and $x^2-8x+3k=0$ have exactly one solution in common. What is the value of $k$?",
   "5", Integer(5),
   lambda: [kk for kk in range(-40, 41) if kk != 0 and len(set(rs(x**2 - 6*x + kk)) & set(rs(x**2 - 8*x + 3*kk))) == 1][0],
   "Common root: subtract the equations",
   r"A common solution satisfies both, so subtract: $2x-2k=0$, i.e. $x=k$. Put $x=k$ into the first equation: $k^2-6k+k=0$, so $k=0$ or $k=5$. With $k\ne0$, $k=5$: the equations are $(x-1)(x-5)=0$ and $(x-3)(x-5)=0$, sharing $x=5$.")

mc(5, 'H',
   r"How many real solutions does $$\left(\dfrac{x}{x-1}\right)^2-4\left(\dfrac{x}{x-1}\right)+3=0$$ have?",
   C(1), [C(0), C(2), C(3)],
   lambda: len(rsol((x/(x - 1))**2 - 4*(x/(x - 1)) + 3)),
   "Quadratic form in a fraction: check each u",
   r"Let $u=\frac{x}{x-1}$: $u^2-4u+3=0$ gives $u=1$ or $u=3$. $\frac x{x-1}=1$ has no solution ($x=x-1$ is false). $\frac{x}{x-1}=3$ gives $x=\frac32$. Exactly one solution. (Two assumes each $u$ gives an $x$.)")

mc(5, 'H',
   r"A group of friends splits a \$200 bill equally. If 2 more friends join, each person pays \$5 less. How many friends were in the original group?",
   C(8), [C(5), C(10), C(25)],
   lambda: [nn for nn in solveset(200/n - 200/(n + 2) - 5, n, S.Reals) if nn > 0][0],
   "Cost per person: a fraction equation becomes a quadratic",
   r"With $n$ friends: $\frac{200}{n}-\frac{200}{n+2}=5$. Multiply by $n(n+2)$: $400=5n^2+10n$, so $n^2+2n-80=0$ and $(n+10)(n-8)=0$. So $n=8$ (\$25 each, then \$20 each with 10 people). (10 is the new group size; 25 is the first price per person.)",
   order='free')

mc(5, 'H',
   r"What is the greatest possible distance from the origin to a point on the circle $x^2+y^2-6x-8y=0$?",
   C(10), [C(5), C(7), C(25)],
   lambda: Integer(round(max(((3 + 5*mpmath.cos(th))**2 + (4 + 5*mpmath.sin(th))**2)**0.5 for th in [i*2*mpmath.pi/20000 for i in range(20000)]))),
   "Completing the square: where is the origin?",
   r"$(x-3)^2+(y-4)^2=25$: center $(3,4)$, radius $5$. The origin is on the circle (it satisfies the equation), so the farthest point is diametrically opposite: distance $2\cdot5=10$. (5 is the radius; 7 is $3+4$; 25 is $r^2$.)",
   order='free')

gi(5, 'H',
   r"What is the solution of $\sqrt{x+3}+\sqrt{x-2}=5$?",
   "6", Integer(6),
   lambda: [t_ for t_ in solveset(sqrt(x + 3) + sqrt(x - 2) - 5, x, S.Reals)][0],
   "Two radicals: isolate one, square, repeat",
   r"Isolate: $\sqrt{x+3}=5-\sqrt{x-2}$. Square: $x+3=25-10\sqrt{x-2}+x-2$, so $10\sqrt{x-2}=20$ and $\sqrt{x-2}=2$, $x=6$. Check: $\sqrt9+\sqrt4=3+2=5$.")

# ================================================================== verification
LETTERS = "ABCD"

def _num(v):
    try:
        return float(sympify(v)) if not isinstance(v, (tuple, str)) and not callable(v) else None
    except Exception:
        return None

def arrange_all():
    """Choose the print order of every MC problem; balance the correct letter globally and per set."""
    glob = [0, 0, 0, 0]
    perset = {}
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
            pa = [i for i, it in enumerate(asc) if it is p_['right']][0]
            if order == 'a':
                pos, out = pa, asc
            elif order == 'd':
                pos, out = 3 - pa, asc[::-1]
            else:
                cand = [(glob[pa], ps[pa], 0, pa), (glob[3 - pa], ps[3 - pa], 1, 3 - pa)]
                best = min(cand)
                pos = best[3]
                out = asc if best[2] == 0 else asc[::-1]
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
