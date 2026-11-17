#!/usr/bin/env python3
"""Independent verification of every answer in mock04-problems.md (Mock Test 4, Book 3).

For each question the correct value is recomputed here from the problem data (sympy /
fractions / brute force / simulation) -- NOT read from the .md.  Then:
  * every printed choice is parsed from the .md text and compared with the computed value,
  * exactly ONE choice must match, and its letter must equal the letter keyed in the .md,
  * grid-in answers must equal the computed value,
  * the blueprint (difficulty / domain / grid-in counts, letter balance) is asserted.
Run:  python3 verify.py      (exit code 0 = ALL OK)
"""
import itertools
import math
import os
import re
import statistics
import sys
from collections import Counter
from fractions import Fraction

import sympy as sp
from sympy.parsing.sympy_parser import (convert_xor, implicit_multiplication_application,
                                        parse_expr, standard_transformations)

HERE = os.path.dirname(os.path.abspath(__file__))
MD = os.path.join(HERE, "mock04-problems.md")
TRANS = standard_transformations + (implicit_multiplication_application, convert_xor)
R = sp.Rational
x, y = sp.symbols("x y", positive=True)
z = sp.symbols("z")                                   # generic (not positive) symbol
SYMS = {"x": x, "y": y, "sqrt": sp.sqrt, "pi": sp.pi}
LIT = {k: sp.Symbol(k) for k in "APtr"}


# --------------------------------------------------------------------------- parsing md
def parse_md(path):
    qs, cur, in_fig = {}, None, False
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


def clean(s):
    s = s.replace("\\$", "").replace("$", "").replace("\\%", "").replace("\\,", "").replace("\\dfrac", "\\frac")
    s = s.replace("{,}", "").replace("\\pi", "pi").replace("\\cdot", "*")
    s = re.sub(r"(?<=\d),(?=\d{3})", "", s)
    s = re.sub(r"\^\{([^{}]*)\}", r"^(\1)", s)
    s = re.sub(r"\\sqrt\{([^{}]*)\}", r"sqrt(\1)", s)
    for _ in range(4):
        s = re.sub(r"\\frac\{([^{}]*)\}\{([^{}]*)\}", r"((\1)/(\2))", s)
    return s.replace("{", "(").replace("}", ")").strip()


def tex_to_expr(s, local=None):
    return parse_expr(clean(s), local_dict=local or SYMS, transformations=TRANS)


def same(a, b):
    a, b = sp.nsimplify(a), sp.nsimplify(b)
    if a.is_number and b.is_number:
        return abs(float(a) - float(b)) < 1e-9
    return sp.simplify(a - b) == 0


# ------------------------------------------------------------------ independent solvers
def solve_all():
    A = {}
    t = sp.symbols("t")

    # ================= MODULE 1 =================
    A[(1, 1)] = sp.solve(sp.Eq(z / 4 + 9, 17), z)[0]
    h = lambda v: v ** 2 - 5
    A[(1, 2)] = h(6) - h(2)
    A[(1, 3)] = R(3, 2) * 14
    r4 = sp.solve(sp.Eq(sp.pi * z ** 2, 81 * sp.pi), z)
    A[(1, 4)] = 2 * sp.pi * [v for v in r4 if v > 0][0]
    pts5 = [(xx, sp.solve(sp.Eq(4 * xx - 2 * z, 10), z)[0]) for xx in (0, 3)]
    A[(1, 5)] = R(pts5[1][1] - pts5[0][1], pts5[1][0] - pts5[0][0])
    A[(1, 6)] = ("pred", lambda txt: sp.expand(sp.Poly(z ** 2 + 2 * z - 24, z).eval(
        sp.solve(tex_to_expr(txt, {"x": z}), z)[0])) == 0)
    A[(1, 7)] = 5 + 3 * (0 - 2)
    A[(1, 8)] = 30 * 2 ** R(18, 6)
    A[(1, 9)] = R("3.1") + (R("4.7") - R("3.1")) / (36 - 20) * (30 - 20)
    A[(1, 10)] = [Lg for Lg in range(0, 41) if 24 * Lg + 15 * (40 - Lg) == 762][0]
    A[(1, 11)] = max(v for v in range(-100, 101) if 4 - 3 * (v - 2) > -14)
    tab12 = {0: R(6), 1: R(9), 2: R(27, 2), 3: R(81, 4)}
    A[(1, 12)] = ("pred", lambda txt: all(
        sp.nsimplify(tex_to_expr(txt.split("=", 1)[1], {"x": z}).subs(z, k)) == v for k, v in tab12.items()))
    A[(1, 13)] = R(60 * 30 * (R(3, 4) * 40), 1000)
    q14 = sp.interpolate([(1, 11), (3, 3), (5, 11)], z)
    assert sp.degree(q14, z) == 2
    A[(1, 14)] = q14.subs(z, 7)
    data = [10, 12, 15, 20, 26, 28, 30, 32, 35, 40, 44, 80]               # consistent sample data set
    assert len(data) == 12 and statistics.mean(data) == 31 and statistics.median(data) == 29
    assert sorted(data)[-2:] == [44, 80]
    new = [50 if v == 80 else v for v in data]
    A[(1, 15)] = ("pred", lambda txt: [float(v) for v in re.findall(r"\d+\.?\d*", txt)] ==
                  [float(statistics.mean(new)), float(statistics.median(new))])
    aa, bb = sp.symbols("aa bb")
    s16 = sp.solve([aa * (-1) + bb - 7, aa * 3 + bb + 5], [aa, bb])
    vals16 = {"ab": s16[aa] * s16[bb], "a-b": s16[aa] - s16[bb], "a+b": s16[aa] + s16[bb], "b-a": s16[bb] - s16[aa]}
    A[(1, 16)] = vals16["a-b"]
    tgt17 = z / (z + 2) + 3 / (z - 1)
    A[(1, 17)] = ("pred", lambda txt: sp.simplify(tex_to_expr(txt, {"x": z}) - tgt17) == 0)
    k18 = R("0.09") * 16
    A[(1, 18)] = [d for d in sp.solve(sp.Eq(k18 / z ** 2, R("0.01")), z) if d > 0][0]
    temp, minute = 600, 0
    while temp < 1800:
        temp += 4 if minute < 150 else 3
        minute += 1
    A[(1, 19)] = minute
    fz = lambda v: v ** 2 - 6 * v
    A[(1, 20)] = sp.solve(sp.Eq(fz(z + 2) - fz(z), 16), z)[0]
    arc = R(216, 360) * 2 * 10
    rbase = arc / 2                                                         # arc/pi = 2 r
    A[(1, 21)] = sp.sqrt(10 ** 2 - rbase ** 2)
    ws = [w for w in range(1, 200) if (w + 3) * (w + 5 + 3) - w * (w + 5) == 66]
    assert len(ws) == 1
    A[(1, 22)] = 2 * (ws[0] + ws[0] + 5)

    # ================= MODULE 2 =================
    def ineq_pred(txt):
        m = re.match(r"\$?x\\(le|ge)\s*(-?\d+)\$?$", txt.strip())
        op, c = m.group(1), int(m.group(2))
        for xv in [R(n, 2) for n in range(-40, 41)]:
            truth = (6 - 3 * xv) >= 21
            cand = (xv <= c) if op == "le" else (xv >= c)
            if truth != cand:
                return False
        return True
    A[(2, 1)] = ("pred", ineq_pred)
    A[(2, 2)] = sp.sqrt(49 * x ** 8)
    slope3 = R(12700 - 14200, 10)
    A[(2, 3)] = 2010 + (10000 - 14200) / slope3
    kk = sp.symbols("kk")
    A[(2, 4)] = sp.solve(sp.Eq((-kk / 3) * R(2, 5), -1), kk)[0]
    q5 = sp.interpolate([(1, 7), (2, 13), (3, 25), (4, 43)], z)
    assert sp.degree(q5, z) == 2
    A[(2, 5)] = q5.subs(z, 10)
    A[(2, 6)] = R("2.4") * 50 ** 3 / 1000
    left = 900 - 18 * 15
    A[(2, 7)] = R(left, 18 + 12)
    A[(2, 8)] = min(n for n in range(1, 500) if R(4, 5) * 12 * n - 150 >= 400)
    run, width = R(32, 2), 40
    rise = run * R(9, 12)
    A[(2, 9)] = 2 * sp.sqrt(run ** 2 + rise ** 2) * width
    nn = sp.symbols("nn")
    n_real = sp.N(sp.solve(sp.Eq(440 * 2 ** (nn / 12), 1320), nn)[0])
    A[(2, 10)] = int(round(float(n_real)))
    Ls, Ps, ts, rs = sp.symbols("Ls Ps ts rs")
    r_sol = sp.solve(sp.Eq(Ls, Ps * (1 + rs * ts)), rs)[0]
    A[(2, 11)] = ("pred", lambda txt: sp.simplify(
        parse_expr(clean(txt.split("=", 1)[1]), local_dict={"A": Ls, "P": Ps, "t": ts, "r": rs},
                   transformations=TRANS) - r_sol) == 0)
    A[(2, 12)] = R(2, 3) + R(3, 4) - R(1, 2)
    # Q13
    gala, fuji, tot = 200, 300, 500
    blight_total = 140
    blight_gala = R(25, 100) * gala
    blight_fuji = blight_total - blight_gala
    healthy_fuji = fuji - blight_fuji
    healthy = tot - blight_total
    assert gala + fuji == tot
    A[(2, 13)] = R(healthy_fuji, healthy)
    f14 = lambda v: v ** 2 - 4 * v + 9
    g14 = lambda v: f14(v + 5) - 2                                       # left 5, down 2
    h14 = sp.expand(g14(4 - z))                                          # reflect across x = 2
    h14 = sp.expand(h14.subs(z, z))
    p14 = sp.Poly(h14, z)
    assert p14.all_coeffs()[0] == 1
    A[(2, 14)] = p14.all_coeffs()[1] + p14.all_coeffs()[2]
    cc = sp.symbols("cc")
    gap = sp.expand((-z ** 2 + 6 * z + cc) - (2 * z - 5))                # must be <= 0 everywhere
    xv = sp.solve(sp.diff(gap, z), z)[0]
    A[(2, 15)] = sp.solve(sp.Eq(gap.subs(z, xv), 0), cc)[0]               # max of gap = 0 at greatest c
    # Q16 pyramid by coordinates
    hh = sp.symbols("hh", positive=True)
    apex = sp.Matrix([0, 0, hh])
    base_v = sp.Matrix([6, 6, 0])
    h16 = sp.solve(sp.Eq((apex - base_v).dot(apex - base_v), 11 ** 2), hh)[0]
    A[(2, 16)] = R(1, 3) * 12 * 12 * h16
    # Q17
    s0 = R(20, 100) * 50
    vol_boiled = s0 / R(25, 100)
    yy = sp.symbols("yy")
    y17 = sp.solve(sp.Eq((s0 + R(10, 100) * yy) / (vol_boiled + yy), R(20, 100)), yy)[0]
    A[(2, 17)] = vol_boiled + y17
    # Q18
    m18, b18 = sp.symbols("m18 b18")
    sf = sp.solve([m18 * 2 + b18 - 5, m18 * 6 + b18 - 17], [m18, b18])
    f18 = lambda v: sf[m18] * v + sf[b18]
    ga, gb = sp.symbols("ga gb")
    cond = sp.Poly(sp.expand(ga * f18(z) + gb - (4 * z - 3)), z).all_coeffs()
    sg = sp.solve(cond, [ga, gb])
    g18 = lambda v: sg[ga] * v + sg[gb]
    A[(2, 18)] = sp.solve(sp.Eq(g18(z), f18(z)), z)[0]
    # Q19
    ratio = R("36.864") / 72
    b19 = float(ratio) ** (1 / 3)
    a19 = 72 / b19
    assert abs(b19 - 0.8) < 1e-12 and abs(a19 - 90) < 1e-9
    A[(2, 19)] = min(rr for rr in range(1, 100) if a19 * b19 ** rr < 10)
    # Q20
    cands = sp.solve(sp.Eq((2 * z + 3) + (z - 2) + 2 * sp.sqrt((2 * z + 3) * (z - 2)), 5 * z + 1), z)
    good = []
    allc = sp.solve((sp.sqrt(2 * z + 3) + sp.sqrt(z - 2)) ** 2 - (5 * z + 1), z)
    pool = set([sp.nsimplify(c) for c in cands] + [sp.nsimplify(c) for c in allc] + [3, -2])
    for c in pool:
        try:
            lhs = sp.sqrt(2 * c + 3) + sp.sqrt(c - 2)
            rhs = sp.sqrt(5 * c + 1)
            if abs(complex(sp.N(lhs - rhs))) < 1e-9 and sp.im(sp.N(lhs)) == 0:
                good.append(c)
        except Exception:
            pass
    assert sorted(good) == [3] and -2 in pool                              # -2 is extraneous
    A[(2, 20)] = sum(good)
    # Q21
    r1, r2 = 4, 9
    d = sp.sqrt((r1 + r2) ** 2 - (r2 - r1) ** 2)
    P, Q, O1, O2 = (0, 0), (d, 0), (0, r1), (d, r2)
    poly = [P, Q, O2, O1]
    shoelace = sum(poly[i][0] * poly[(i + 1) % 4][1] - poly[(i + 1) % 4][0] * poly[i][1] for i in range(4)) / 2
    A[(2, 21)] = abs(shoelace)
    assert sp.simplify(sp.sqrt((O2[0] - O1[0]) ** 2 + (O2[1] - O1[1]) ** 2) - (r1 + r2)) == 0
    # Q22: exactly two intersection points <=> positive discriminant of x^2+(x+k)^2=50
    cnt22 = 0
    for kv in range(-200, 201):
        a_, b_, c_ = 2, 2 * kv, kv ** 2 - 50
        if b_ ** 2 - 4 * a_ * c_ > 0:
            cnt22 += 1
    A[(2, 22)] = cnt22
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
                for L in "ABCD":
                    txt = q["choices"][L]
                    if isinstance(val, tuple) and val[0] == "pred":
                        match = bool(val[1](txt))
                    else:
                        match = same(tex_to_expr(txt), val)
                    if match:
                        hits.append(L)
                assert len(hits) == 1, f"{len(hits)} choices match computed value {val}: {hits}"
                assert hits[0] == q["answer"], f"computed letter {hits[0]} != keyed {q['answer']}"
                letters[key[0]].append(hits[0])
                msg = f"answer {q['answer']}  (value {'pred' if isinstance(val, tuple) else sp.N(val, 6)})"
            else:
                assert not q["choices"], "grid-in must have no choices"
                keyed = tex_to_expr(q["answer"])
                assert abs(float(sp.N(keyed)) - float(sp.N(val))) < 1e-9, f"computed {val} != keyed {q['answer']}"
                limit = 6 if q["answer"].startswith("-") else 5
                assert len(q["answer"]) <= limit, "too many characters for a grid-in"
                msg = f"grid-in {q['answer']}  (value {sp.N(val, 6)})"
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
        print(f"{name:76s} {'OK' if cond else 'FAIL'}")
        fails += (not cond)

    chk("44 questions present", len(qs) == 44)
    for mod, spec in ((1, dict(E=range(1, 9), M=range(9, 20), H=range(20, 23))),
                      (2, dict(E=range(1, 3), M=range(3, 13), H=range(13, 23)))):
        qq = [qs[(mod, n)] for n in range(1, 23)]
        chk(f"M{mod}: 22 questions", len(qq) == 22)
        for d in "EMH":
            want = list(spec[d])
            got = [q["n"] for q in qq if q["difficulty"] == d]
            chk(f"M{mod}: difficulty {d} at Q{want[0]}-Q{want[-1]} ({len(want)})", got == want)
        for dname, cnt in dict(ALG=8, ADV=8, PSDA=3, GT=3).items():
            chk(f"M{mod}: domain {dname} = {cnt}", sum(q["domain"] == dname for q in qq) == cnt)
        g = [q["n"] for q in qq if q["type"] == "GRID"]
        chk(f"M{mod}: grid-ins {len(g)} in 5-6 -> Q{g}", 5 <= len(g) <= 6)
        chk(f"M{mod}: grid-ins spread (no two adjacent, first<=Q4, last>=Q17)",
            all(b - a >= 2 for a, b in zip(g, g[1:])) and g[0] <= 4 and g[-1] >= 17)
        c = Counter(letters[mod])
        print(f"   M{mod} MC answer-letter distribution: {dict(sorted(c.items()))}")
        chk(f"M{mod}: every letter used 3-5 times", all(3 <= c.get(L, 0) <= 5 for L in "ABCD"))
        seq = [qs[(mod, n)]["answer"] if qs[(mod, n)]["type"] == "MC" else None for n in range(1, 23)]
        run3 = any(seq[i] and seq[i] == seq[i + 1] == seq[i + 2] for i in range(20))
        chk(f"M{mod}: no three identical MC letters in consecutive questions", not run3)
    print()
    print("ALL OK" if fails == 0 else f"{fails} FAILURE(S)")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
