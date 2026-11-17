#!/usr/bin/env python3
"""Independent verification of every answer in mock01-problems.md (Mock Test 1, Book 3).

For each question the correct value is recomputed here from the problem data (sympy /
fractions / brute force) -- NOT read from the .md.  Then:
  * every printed choice is parsed from the .md text and compared with the computed value,
  * exactly ONE choice must match, and its letter must equal the letter keyed in the .md,
  * grid-in answers must equal the computed value,
  * the blueprint (difficulty / domain / grid-in counts) is asserted.
Run:  python3 verify.py      (exit code 0 = all OK)
"""
import os
import re
import sys
from collections import Counter
from fractions import Fraction

import sympy as sp
from sympy.parsing.sympy_parser import (convert_xor, implicit_multiplication_application,
                                        parse_expr, standard_transformations)

HERE = os.path.dirname(os.path.abspath(__file__))
MD = os.path.join(HERE, "mock01-problems.md")
TRANS = standard_transformations + (implicit_multiplication_application, convert_xor)


# --------------------------------------------------------------------------- parsing md
def parse_md(path):
    qs = {}
    cur = None
    in_fig = False
    for line in open(path, encoding="utf-8"):
        line = line.rstrip("\n")
        m = re.match(r"## (M[12])-Q(\d+)$", line)
        if m:
            cur = {"mod": int(m.group(1)[1]), "n": int(m.group(2)), "choices": {}}
            qs[(cur["mod"], cur["n"])] = cur
            continue
        if cur is None:
            continue
        if line.startswith("```latex"):
            in_fig = True
            continue
        if in_fig:
            if line.startswith("```"):
                in_fig = False
            continue
        m = re.match(r"- (\w+): ?(.*)$", line)
        if not m:
            continue
        k, v = m.group(1), m.group(2).strip()
        if len(k) == 1 and k in "ABCD":
            cur["choices"][k] = v
        else:
            cur[k.lower()] = v
    return qs


def tex_to_expr(s, syms):
    """Parse a simple LaTeX math/text choice such as '\\frac{8}{13}', '2\\sqrt{13}', '\\$75.00'."""
    s = s.replace("\\$", "").replace("$", "").replace("\\%", "").replace("\\,", "").replace("\\dfrac", "\\frac")
    s = re.sub(r"(?<=\d),(?=\d{3})", "", s)          # thousands separators
    for _ in range(3):
        s = re.sub(r"\\frac\{([^{}]*)\}\{([^{}]*)\}", r"((\1)/(\2))", s)
    s = re.sub(r"\\sqrt\{([^{}]*)\}", r"*sqrt(\1)", s)
    s = s.replace("{", "(").replace("}", ")").strip()
    s = re.sub(r"^\*", "", s)
    s = s.replace("(*", "(")
    return parse_expr(s, local_dict=syms, transformations=TRANS)


x, y = sp.symbols("x y", positive=True)
SYMS = {"x": x, "y": y, "sqrt": sp.sqrt}


def same(a, b):
    if a.is_number and b.is_number:
        return abs(float(a) - float(b)) < 1e-9
    return sp.simplify(sp.nsimplify(a) - sp.nsimplify(b)) == 0


# ------------------------------------------------------------------ independent solvers
def solve_all():
    A = {}   # (mod, n) -> computed correct value
    R = sp.Rational
    t = sp.symbols("t")

    # ================= MODULE 1 =================
    A[(1, 1)] = sp.solve(sp.Eq(3 * (t - 4), 15), t)[0] + 4
    f = lambda v: 2 * v ** 2 - 3 * v + 5
    A[(1, 2)] = f(-3)
    A[(1, 3)] = 5 * 88 - (90 + 85 + 92 + 95)
    A[(1, 4)] = sp.solve(sp.Eq(24 + 18 * t, 168), t)[0]
    L = sp.sqrt(25 ** 2 - 7 ** 2); A[(1, 5)] = 2 * (7 + L)
    xx, yy = sp.symbols("xx yy")
    s6 = sp.solve([xx + yy - 14, xx - yy - 4], [xx, yy]); A[(1, 6)] = s6[xx] * s6[yy]
    A[(1, 7)] = [r for r in sp.solve(t ** 2 - 3 * t - 28, t) if r > 0][0]
    a_, s_ = sp.symbols("a_ s_")
    sol = sp.solve([a_ + s_ - 240, 9 * a_ + 5 * s_ - 1720], [a_, s_]); A[(1, 8)] = sol[s_]
    P = lambda c: -R(5, 100) * c ** 2 + 6 * c - 40
    A[(1, 9)] = max(P(c) for c in range(0, 241))
    A[(1, 10)] = R("76.5") / (R(12, 10) * R(85, 100))
    m = R(-5 - 7, 4 + 2); b = 7 - m * (-2); A[(1, 11)] = -b / m
    A[(1, 12)] = sp.simplify((4 * x ** 3 * y) ** 2 / (2 * x * y ** 2))
    k13 = sp.symbols("k13", positive=True)
    k = sp.solve(sp.Eq(sp.sqrt((12 * k13) ** 2 + (5 * k13) ** 2), 39), k13)[0]
    A[(1, 13)] = 12 * k + 5 * k + 39
    tab = {("J", "walk"): 36, ("J", "bus"): 44, ("J", "drive"): 25,
           ("S", "walk"): 24, ("S", "bus"): 31, ("S", "drive"): 40}
    assert sum(tab.values()) == 200
    A[(1, 14)] = sp.Rational(tab[("S", "drive")], tab[("J", "drive")] + tab[("S", "drive")])
    A[(1, 15)] = max(n for n in range(0, 100) if 175 + 60 + 35 * n <= 900)
    cands = sp.solve(sp.Eq(3 * t + 10, (t + 2) ** 2), t)
    good = [c for c in cands if abs(float(sp.sqrt(3 * c + 10)) - float(c + 2)) < 1e-12]
    A[(1, 16)] = sum(good)
    kk = sp.symbols("kk")
    M = sp.Matrix([[6, 9], [2, kk]])
    kval = sp.solve(M.det(), kk)[0]
    assert R(6, 2) == R(9, kval) and R(21, 14) != R(6, 2)     # parallel and inconsistent
    A[(1, 17)] = kval
    a18 = sp.symbols("a18")
    a18v = sp.solve(sp.Eq(a18 * (0 - 2) * (0 + 6), -24), a18)[0]
    assert a18v > 0
    A[(1, 18)] = a18v * (-2 - 2) * (-2 + 6)
    A[(1, 19)] = sp.solve(sp.Eq(R(10, 100) * t + R(50, 100) * 20, R(20, 100) * (t + 20)), t)[0]
    n20 = sp.symbols("n20")
    A[(1, 20)] = sp.solve(sp.Eq((48 * 72 + 90 * n20) / (48 + n20), 78), n20)[0]
    A[(1, 21)] = (R(4, 3) * sp.pi * 6 ** 3) / (R(1, 3) * sp.pi * 3 ** 2 * 4)
    A[(1, 22)] = 100 * (1.5 ** 0.25 - 1)         # ~10.67 -> nearest printed choice 10.7

    # ================= MODULE 2 =================
    A[(2, 1)] = sp.solve(sp.Eq(2 * (3 * t - 4), 5 * (t + 1)), t)[0]
    A[(2, 2)] = sp.expand((x - 5) ** 2 - 9)
    A[(2, 3)] = 2 * 180 / (2 + 3 + 4)
    k4 = sp.solve(sp.Eq(3 * t + 14, 5 * t), t)[0]; A[(2, 4)] = 8 * k4
    b5 = sp.symbols("b5")
    A[(2, 5)] = sp.solve(sp.Eq(-1, R(4, 3) * 3 + b5), b5)[0]
    r6 = sp.solve(3 * t ** 2 - 8 * t - 35, t); A[(2, 6)] = r6[0] * r6[1]
    A[(2, 7)] = R(1, 2) * 6 * 6 * sp.sqrt(3)
    A[(2, 8)] = [a for a in range(0, 30) if 3 * 2 ** a + 5 == 101][0]
    sol9 = sp.solve([3 * xx - 2 * yy - 10, 5 * xx + 2 * yy - 22], [xx, yy]); A[(2, 9)] = sol9[xx] + sol9[yy]

    # Q10: f quadratic, max 25 at x=3, f(0)=16 ; g(x)=-2 f(x+1)+k has exactly one x-intercept ; g(0)
    qa = sp.symbols("qa")
    a10 = sp.solve(sp.Eq(qa * (0 - 3) ** 2 + 25, 16), qa)[0]
    assert a10 < 0                                   # it is a maximum
    f10 = lambda v: a10 * (v - 3) ** 2 + 25
    k10, X10 = sp.symbols("k10 X10")
    g10 = sp.expand(-2 * f10(X10 + 1) + k10)
    k10v = sp.solve(sp.discriminant(g10, X10), k10)  # one x-intercept <=> discriminant 0
    assert len(k10v) == 1
    A[(2, 10)] = g10.subs({k10: k10v[0], X10: 0})

    # Q11: kx+2y=10 ; 24x+(k+2)y=40 -> no solution
    nosol = []
    for kv in range(-60, 61):
        coef = sp.Matrix([[kv, 2], [24, kv + 2]])
        aug = sp.Matrix([[kv, 2, 10], [24, kv + 2, 40]])
        if coef.rank() == 1 and aug.rank() == 2:
            nosol.append(kv)
    assert len(nosol) == 1, nosol
    A[(2, 11)] = nosol[0]
    # Q12: integer k with 2x^2+kx+8=0 having no real roots
    A[(2, 12)] = sum(1 for kv in range(-200, 201) if kv * kv - 4 * 2 * 8 < 0)
    # Q13: conditional probability
    north = R(55, 100) * 800; south = 800 - north
    fn = north * R(40, 100); fs = south * R(65, 100)
    A[(2, 13)] = float(fn / (fn + fs))               # 0.4293 -> 0.43
    # Q14: circle x^2+y^2-10x+4y=20 cut by y=-8
    xx2 = sp.symbols("xx2")
    pts = sp.solve(xx2 ** 2 + (-8) ** 2 - 10 * xx2 + 4 * (-8) - 20, xx2)
    A[(2, 14)] = sp.simplify(abs(pts[0] - pts[1]))
    # Q15: rates
    A[(2, 15)] = 1 / (R(1, 6) + R(1, 9) - R(1, 18))
    # Q16: maximize w(240-4w): brute force over half-meters, compare with the vertex
    wv = sp.symbols("wv")
    A[(2, 16)] = max(sp.Rational(i, 2) * (240 - 4 * sp.Rational(i, 2)) for i in range(0, 121))
    assert A[(2, 16)] == (wv * (240 - 4 * wv)).subs(wv, 30)

    # Q17: line through (4,3), positive intercepts p,q, area 24 -> slope
    p17 = sp.symbols("p17", positive=True)
    q17 = 48 / p17                                    # (1/2) p q = 24
    sols17 = sp.solve(sp.Eq(4 / p17 + 3 / q17, 1), p17)   # (4,3) lies on x/p + y/q = 1
    assert len(sols17) == 1, sols17                   # exactly one such line
    A[(2, 17)] = -(q17 / p17).subs(p17, sols17[0])

    # Q18: y=-x^2+8x-3 and y=2x+k meet where x-coordinates differ by 4 -> y at larger x
    k18, X18 = sp.symbols("k18 X18")
    roots18 = sp.solve(sp.Eq(-X18 ** 2 + 8 * X18 - 3, 2 * X18 + k18), X18)
    kv18 = sp.solve(sp.Eq((roots18[1] - roots18[0]) ** 2, 16), k18)
    assert len(kv18) == 1
    r18 = [r.subs(k18, kv18[0]) for r in roots18]
    assert abs(r18[0] - r18[1]) == 4
    A[(2, 18)] = 2 * max(r18) + kv18[0]

    # Q19: linear f, f(f(x)) = 4x+9, f(2)>0 -> f(-10)
    a19, b19 = sp.symbols("a19 b19")
    sols19 = sp.solve([sp.Eq(a19 ** 2, 4), sp.Eq(a19 * b19 + b19, 9)], [a19, b19], dict=True)
    assert len(sols19) == 2
    sols19 = [d for d in sols19 if d[a19] * 2 + d[b19] > 0]
    assert len(sols19) == 1
    A[(2, 19)] = sols19[0][a19] * (-10) + sols19[0][b19]

    # Q20: percent chain
    q4 = 75600; q3 = R(q4) / R("1.4"); q2 = q3 / R("0.75"); q1 = q2 / R("1.2")
    A[(2, 20)] = q1 + q2 + q3 + q4
    # Q21: similar triangles
    ratio = R(6, 15) ** 2
    abc = sp.symbols("abc")
    A[(2, 21)] = sp.solve(sp.Eq(abc - ratio * abc, 84), abc)[0] * ratio

    # Q22: (x-1)/(x-k) = (x+3)/(x-2): sum of all k with no solution
    def nosol22(kv):
        kv = sp.nsimplify(kv)
        sol = sp.solve(sp.Eq((t - 1) * (t - 2), (t + 3) * (t - kv)), t)
        return not [r for r in sol if r != 2 and r != kv]
    grid = [sp.Rational(n, 2) for n in range(-80, 81)]
    bad = [kv for kv in grid if nosol22(kv)]
    assert bad == [1, 2, 6], bad
    kk2 = sp.symbols("kk2")                           # symbolic: x=(3k+2)/(6-k), or none when k=6
    xg = (3 * kk2 + 2) / (6 - kk2)
    assert set(sp.solve(sp.Eq(xg, 2), kk2)) | set(sp.solve(sp.Eq(xg, kk2), kk2)) | {6} == {1, 2, 6}
    A[(2, 22)] = sum(bad)
    return A


# ------------------------------------------------------------------------------ driver
def main():
    qs = parse_md(MD)
    A = solve_all()
    fails = 0
    letters = {1: [], 2: []}
    for key in sorted(qs):
        q = qs[key]
        tag = f"M{key[0]}-Q{key[1]:02d}"
        ok = True
        try:
            val = A[key]
            if q["type"] == "MC":
                assert set(q["choices"]) == set("ABCD"), "needs exactly choices A-D"
                hits = []
                for Lt in "ABCD":
                    c = tex_to_expr(q["choices"][Lt], SYMS)
                    if key == (1, 22):               # nearest printed choice (percent, 1 decimal)
                        match = abs(float(c) - float(val)) < 0.05
                    elif key == (2, 13):             # nearest hundredth
                        match = abs(float(c) - float(val)) < 0.005
                    elif isinstance(val, float):
                        match = abs(float(c) - val) < 1e-9
                    else:
                        match = same(sp.nsimplify(c), sp.nsimplify(val))
                    if match:
                        hits.append(Lt)
                assert len(hits) == 1, f"{len(hits)} choices match computed value {val}: {hits}"
                assert hits[0] == q["answer"], f"computed letter {hits[0]} != keyed {q['answer']}"
                letters[key[0]].append(hits[0])
                msg = f"answer {q['answer']}  (value {val if not hasattr(val, 'free_symbols') or val.free_symbols else sp.N(val, 6)})"
            else:
                assert not q["choices"], "grid-in must have no choices"
                keyed = tex_to_expr(q["answer"], SYMS)
                assert abs(float(sp.N(keyed)) - float(sp.N(val))) < 1e-9, f"computed {val} != keyed {q['answer']}"
                msg = f"grid-in {q['answer']}"
        except AssertionError as e:
            ok = False
            msg = f"ASSERT: {e}"
        except Exception as e:      # noqa
            ok = False
            msg = f"ERROR {type(e).__name__}: {e}"
        print(f"{tag}  {'OK  ' if ok else 'FAIL'}  {msg}")
        fails += (not ok)

    print("\n-- blueprint --")

    def chk(name, cond):
        nonlocal fails
        print(f"{name:70s} {'OK' if cond else 'FAIL'}")
        fails += (not cond)

    chk("44 questions present", len(qs) == 44)
    for mod, spec in ((1, dict(E=range(1, 8), M=range(8, 18), H=range(18, 23),
                              dom=dict(ALG=8, ADV=7, PSDA=4, GT=3), grid=(5, 6))),
                      (2, dict(E=range(1, 4), M=range(4, 10), H=range(10, 23),
                              dom=dict(ALG=7, ADV=8, PSDA=3, GT=4), grid=(5, 6)))):
        qq = [qs[(mod, n)] for n in range(1, 23)]
        chk(f"M{mod}: 22 questions", len(qq) == 22)
        for d in "EMH":
            want = list(spec[d])
            got = [q["n"] for q in qq if q["difficulty"] == d]
            chk(f"M{mod}: difficulty {d} at Q{want[0]}-Q{want[-1]} ({len(want)})", got == want)
        for dname, cnt in spec["dom"].items():
            chk(f"M{mod}: domain {dname} = {cnt}", sum(q["domain"] == dname for q in qq) == cnt)
        g = [q["n"] for q in qq if q["type"] == "GRID"]
        chk(f"M{mod}: grid-ins {len(g)} in {spec['grid']} -> Q{g}", spec["grid"][0] <= len(g) <= spec["grid"][1])
        chk(f"M{mod}: grid-ins spread (no two adjacent, first<=Q4, last>=Q17)",
            all(b - a >= 2 for a, b in zip(g, g[1:])) and g[0] <= 4 and g[-1] >= 17)
        c = Counter(letters[mod])
        print(f"   M{mod} MC answer-letter distribution: {dict(sorted(c.items()))}")
        chk(f"M{mod}: no letter used more than 5 times", max(c.values()) <= 5)
    print()
    print("ALL OK" if fails == 0 else f"{fails} FAILURE(S)")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
