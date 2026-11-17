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
import itertools
import os
import re
import sys
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
        if k in "ABCD" and len(k) == 1:
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
    d = sp.simplify(sp.nsimplify(a) - sp.nsimplify(b)) if not (a.is_number and b.is_number) \
        else abs(float(a) - float(b))
    if a.is_number and b.is_number:
        return d < 1e-9
    return d == 0


# ------------------------------------------------------------------ independent solvers
def solve_all():
    A = {}   # (mod, n) -> computed correct value (sympy expr / number)
    R = sp.Rational

    # ================= MODULE 1 =================
    t = sp.symbols("t")
    # Q1: 3(x-4)=15, x+4
    xs = sp.solve(sp.Eq(3 * (t - 4), 15), t)[0]; A[(1, 1)] = xs + 4
    # Q2: f(-3)
    f = lambda v: 2 * v ** 2 - 3 * v + 5
    A[(1, 2)] = f(-3)
    # Q3: fifth score
    A[(1, 3)] = 5 * 88 - (90 + 85 + 92 + 95)
    # Q4: 24+18s=168
    A[(1, 4)] = sp.solve(sp.Eq(24 + 18 * t, 168), t)[0]
    # Q5: rectangle w=7, diag 25 -> perimeter
    L = sp.sqrt(25 ** 2 - 7 ** 2); A[(1, 5)] = 2 * (7 + L)
    # Q6: x+y=14, x-y=4 -> xy
    xx, yy = sp.symbols("xx yy")
    s6 = sp.solve([xx + yy - 14, xx - yy - 4], [xx, yy]); A[(1, 6)] = s6[xx] * s6[yy]
    # Q7: positive solution
    A[(1, 7)] = [r for r in sp.solve(t ** 2 - 3 * t - 28, t) if r > 0][0]
    # Q8: tickets
    a_, s_ = sp.symbols("a_ s_")
    sol = sp.solve([a_ + s_ - 240, 9 * a_ + 5 * s_ - 1720], [a_, s_]); A[(1, 8)] = sol[s_]
    # Q9: max profit  (brute-force over integer cups, and vertex)
    P = lambda c: -R(5, 100) * c ** 2 + 6 * c - 40
    A[(1, 9)] = max(P(c) for c in range(0, 241))
    # Q10: undo +20% then -15%
    A[(1, 10)] = R("76.5") / (R(12, 10) * R(85, 100))
    # Q11: x-intercept of line through (-2,7), (4,-5)
    m = R(-5 - 7, 4 + 2); b = 7 - m * (-2); A[(1, 11)] = -b / m
    # Q12: (4x^3y)^2/(2xy^2)
    A[(1, 12)] = sp.simplify((4 * x ** 3 * y) ** 2 / (2 * x * y ** 2))
    # Q13: right triangle, tan A=5/12, AC=39
    k13 = sp.symbols("k13", positive=True)
    k = sp.solve(sp.Eq(sp.sqrt((12 * k13) ** 2 + (5 * k13) ** 2), 39), k13)[0]
    A[(1, 13)] = 12 * k + 5 * k + 39
    # Q14: conditional probability
    tab = {("J", "walk"): 36, ("J", "bus"): 44, ("J", "drive"): 25,
           ("S", "walk"): 24, ("S", "bus"): 31, ("S", "drive"): 40}
    assert sum(tab.values()) == 200
    A[(1, 14)] = Fraction(tab[("S", "drive")], tab[("J", "drive")] + tab[("S", "drive")])
    A[(1, 14)] = sp.Rational(A[(1, 14)].numerator, A[(1, 14)].denominator)
    # Q15: greatest n with 175+60+35n<=900
    A[(1, 15)] = max(n for n in range(0, 100) if 175 + 60 + 35 * n <= 900)
    # Q16: sum of valid solutions of sqrt(3x+10)=x+2
    cands = sp.solve(sp.Eq(3 * t + 10, (t + 2) ** 2), t)
    good = [c for c in cands if abs(float(sp.sqrt(3 * c + 10)) - float(c + 2)) < 1e-12]
    A[(1, 16)] = sum(good)
    # Q17: 6x+9y=21, 2x+ky=14 no solution
    kk = sp.symbols("kk")
    M = sp.Matrix([[6, 9], [2, kk]])
    # no solution <=> det(coeff)=0 and the system inconsistent (21/6 != 14/2 for the parallel k)
    kval = sp.solve(M.det(), kk)[0]
    assert R(6, 2) == R(9, kval) and R(21, 14) != R(6, 2)
    A[(1, 17)] = kval
    # Q18: quadratic with roots 2,-6 and f(0)=-24 -> min value
    a18 = sp.symbols("a18")
    a18v = sp.solve(sp.Eq(a18 * (0 - 2) * (0 + 6), -24), a18)[0]
    F = lambda v: a18v * (v - 2) * (v + 6)
    A[(1, 18)] = F(-2)
    assert a18v > 0
    # Q19: mixture
    A[(1, 19)] = sp.solve(sp.Eq(R(10, 100) * t + R(50, 100) * 20, R(20, 100) * (t + 20)), t)[0]
    # Q20: combined mean
    n20 = sp.symbols("n20")
    A[(1, 20)] = sp.solve(sp.Eq((48 * 72 + 90 * n20) / (48 + n20), 78), n20)[0]
    # Q21: sphere -> cones
    A[(1, 21)] = (R(4, 3) * sp.pi * 6 ** 3) / (R(1, 3) * sp.pi * 3 ** 2 * 4)
    # Q22: percent growth per hour
    A[(1, 22)] = 100 * (1.5 ** 0.25 - 1)         # ~10.67 -> nearest printed choice 10.7

    # ================= MODULE 2 =================
    # Q1: 2(3x-4)=5(x+1)
    A[(2, 1)] = sp.solve(sp.Eq(2 * (3 * t - 4), 5 * (t + 1)), t)[0]
    # Q2: (x-5)^2-9
    A[(2, 2)] = sp.expand((x - 5) ** 2 - 9)
    # Q3: ratio 2:3:4 smallest angle
    A[(2, 3)] = 2 * 180 / (2 + 3 + 4)
    # Q4: cats:dogs=5:3 ; +14 dogs -> equal ; total before
    k4 = sp.solve(sp.Eq(3 * t + 14, 5 * t), t)[0]; A[(2, 4)] = 8 * k4
    # Q5: line through (3,-1) parallel to 4x-3y=9 ; y-intercept
    b5 = sp.symbols("b5")
    slope = R(4, 3)
    A[(2, 5)] = sp.solve(sp.Eq(-1, slope * 3 + b5), b5)[0]
    # Q6: product of roots 3x^2-8x-35
    r6 = sp.solve(3 * t ** 2 - 8 * t - 35, t); A[(2, 6)] = r6[0] * r6[1]
    # Q7: 30-60-90, hyp 12, area
    A[(2, 7)] = R(1, 2) * 6 * 6 * sp.sqrt(3)
    # Q8: 3*2^a+5=101
    A[(2, 8)] = [a for a in range(0, 30) if 3 * 2 ** a + 5 == 101][0]
    # Q9: 3a-2b=10, 5a+2b=22 -> a+b
    sol9 = sp.solve([3 * xx - 2 * yy - 10, 5 * xx + 2 * yy - 22], [xx, yy]); A[(2, 9)] = sol9[xx] + sol9[yy]
    # Q10: table (2,1),(4,-7),(6,1): quadratic; g(x)=f(x+3)+10 ; g(0)
    qa, qb, qc = sp.symbols("qa qb qc")
    sol10 = sp.solve([qa * 4 + qb * 2 + qc - 1, qa * 16 + qb * 4 + qc + 7, qa * 36 + qb * 6 + qc - 1], [qa, qb, qc])
    f10 = lambda v: sol10[qa] * v ** 2 + sol10[qb] * v + sol10[qc]
    A[(2, 10)] = f10(0 + 3) + 10
    # Q11: kx+2y=10 ; 24x+(k+2)y=40 -> no solution
    kq = sp.symbols("kq")
    nosol = []
    for kv in range(-60, 61):
        coef = sp.Matrix([[kv, 2], [24, kv + 2]])
        aug = sp.Matrix([[kv, 2, 10], [24, kv + 2, 40]])
        if coef.rank() == 1 and aug.rank() == 2:
            nosol.append(kv)
    assert len(nosol) == 1, nosol
    A[(2, 11)] = nosol[0]
    # Q12: count integer k with 2x^2+kx+8=0 having no real roots (discriminant<0)
    A[(2, 12)] = sum(1 for kv in range(-200, 201) if kv * kv - 4 * 2 * 8 < 0)
    # Q13: Bayes
    north = R(55, 100) * 800; south = 800 - north
    fn = north * R(40, 100); fs = south * R(65, 100)
    A[(2, 13)] = float(fn / (fn + fs))               # 0.4293 -> 0.43
    # Q14: circle x^2+y^2-10x+4y=20 and y=-8 : distance between intersection points
    xx2 = sp.symbols("xx2")
    pts = sp.solve(xx2 ** 2 + (-8) ** 2 - 10 * xx2 + 4 * (-8) - 20, xx2)
    A[(2, 14)] = sp.simplify(abs(pts[0] - pts[1]))
    # Q15: rates
    rate = R(1, 6) + R(1, 9) - R(1, 18); A[(2, 15)] = 1 / rate
    # Q16: maximize w(240-4w) -- brute force over a fine grid of multiples of 0.5 plus exact vertex
    wv = sp.symbols("wv")
    A[(2, 16)] = max(sp.Rational(i, 2) * (240 - 4 * sp.Rational(i, 2)) for i in range(0, 121))
    assert A[(2, 16)] == (wv * (240 - 4 * wv)).subs(wv, 30)
    # Q17: rectangle
    w17 = sp.symbols("w17")
    w17v = [v for v in sp.solve(sp.Eq((2 * w17 + 4 + 6) * (w17 - 2), (2 * w17 + 4) * w17), w17)][0]
    A[(2, 17)] = 2 * (w17v + 2 * w17v + 4)
    # Q18: S(t)=a b^t ; S(1)=6, S(4)=162 ; S(6)-S(5)
    a18_, b18 = sp.symbols("a18_ b18", positive=True)
    sol18 = sp.solve([a18_ * b18 - 6, a18_ * b18 ** 4 - 162], [a18_, b18], dict=True)[0]
    A[(2, 18)] = sol18[a18_] * sol18[b18] ** 6 - sol18[a18_] * sol18[b18] ** 5
    # Q19: |2x-7|=k, solutions differ by 9 -> product
    k19 = sp.symbols("k19", positive=True)
    k19v = sp.solve(sp.Eq(abs((7 + k19) / 2 - (7 - k19) / 2), 9), k19)[0]
    s19 = sp.solve(sp.Eq(2 * t - 7, k19v), t)[0], sp.solve(sp.Eq(-(2 * t - 7), k19v), t)[0]
    assert all(abs(2 * v - 7) == k19v for v in s19)
    A[(2, 19)] = s19[0] * s19[1]
    # Q20: percent chain, total of four quarters
    q4 = 75600; q3 = R(q4) / R("1.4"); q2 = q3 / R("0.75"); q1 = q2 / R("1.2")
    A[(2, 20)] = q1 + q2 + q3 + q4
    # Q21: similar triangles, DBCE=84 ; AD=6, DB=9
    ad, ab = 6, 15
    ratio = R(ad, ab) ** 2                     # area(ADE)/area(ABC)
    abc = sp.symbols("abc")
    A[(2, 21)] = sp.solve(sp.Eq(abc - ratio * abc, 84), abc)[0] * ratio
    # Q22: sqrt(x+7)-sqrt(x-2)=1
    cand = sp.solve(sp.Eq(sp.sqrt(t + 7) - sp.sqrt(t - 2), 1), t)
    A[(2, 22)] = cand[0]
    return A


# ------------------------------------------------------------------------------ driver
def main():
    qs = parse_md(MD)
    A = solve_all()
    fails = 0
    letters = {1: [], 2: []}
    # structure / blueprint
    for key in sorted(qs):
        q = qs[key]
        tag = f"M{key[0]}-Q{key[1]:02d}"
        ok = True
        msg = ""
        try:
            val = A[key]
            if q["type"] == "MC":
                assert set(q["choices"]) == set("ABCD"), "needs exactly choices A-D"
                hits = []
                for L in "ABCD":
                    c = tex_to_expr(q["choices"][L], SYMS)
                    if key == (1, 22):               # nearest printed choice (percent, 1 decimal)
                        match = abs(float(c) - float(val)) < 0.05
                    elif key == (2, 13):             # nearest hundredth
                        match = abs(float(c) - float(val)) < 0.005
                    else:
                        match = same(sp.nsimplify(c), sp.nsimplify(val)) if not isinstance(val, float) \
                            else abs(float(c) - val) < 1e-9
                    if match:
                        hits.append(L)
                assert len(hits) == 1, f"{len(hits)} choices match computed value {val}: {hits}"
                assert hits[0] == q["answer"], f"computed letter {hits[0]} != keyed {q['answer']}"
                letters[key[0]].append(hits[0])
                msg = f"answer {q['answer']}  (value {sp.N(val, 6) if hasattr(val, 'free_symbols') and not val.free_symbols else val})"
            else:
                assert not q["choices"], "grid-in must have no choices"
                keyed = tex_to_expr(q["answer"], SYMS)
                v = val
                assert abs(float(sp.N(keyed)) - float(sp.N(v))) < 1e-9, f"computed {v} != keyed {q['answer']}"
                msg = f"grid-in {q['answer']}"
        except AssertionError as e:
            ok = False
            msg = f"ASSERT: {e}"
        except Exception as e:      # noqa
            ok = False
            msg = f"ERROR {type(e).__name__}: {e}"
        print(f"{tag}  {'OK  ' if ok else 'FAIL'}  {msg}")
        fails += (not ok)

    # ---------------- blueprint
    print("\n-- blueprint --")
    def chk(name, cond):
        nonlocal fails
        print(f"{name:70s} {'OK' if cond else 'FAIL'}")
        fails += (not cond)

    chk("44 questions present", len(qs) == 44)
    for mod, spec in ((1, dict(E=(range(1, 8)), M=range(8, 18), H=range(18, 23),
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
        chk(f"M{mod}: grid-ins spread (no two adjacent, first<=Q4/Q3, last>=Q17)",
            all(b - a >= 2 for a, b in zip(g, g[1:])) and g[0] <= 4 and g[-1] >= 17)
        from collections import Counter
        c = Counter(letters[mod])
        print(f"   M{mod} MC answer-letter distribution: {dict(sorted(c.items()))}")
        chk(f"M{mod}: no letter used more than 5 times", max(c.values()) <= 5)
    print()
    print("ALL OK" if fails == 0 else f"{fails} FAILURE(S)")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
