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
