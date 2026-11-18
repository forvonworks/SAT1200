#!/usr/bin/env python3
"""Independent verification of every answer in mock10-problems.md (Mock Test 10, Book 3).

For each question the correct value is recomputed here from the problem data (sympy /
fractions / brute force) -- NOT read from the .md.  Tables printed in figures are parsed from
the .md so the check uses the very numbers the student sees.  Then:
  * every printed choice is parsed from the .md text and compared with the computed value,
  * exactly ONE choice must match, and its letter must equal the letter keyed in the .md,
  * grid-in answers must equal the computed value,
  * the blueprint (difficulty / domain / grid-in counts, letter balance) is asserted.
Run:  python3 verify.py      (exit code 0 = ALL OK)
"""
import itertools
import math
import os
import random
import re
import sys
from collections import Counter
from fractions import Fraction

import sympy as sp
from sympy.parsing.sympy_parser import (convert_xor, implicit_multiplication_application,
                                        parse_expr, standard_transformations)

HERE = os.path.dirname(os.path.abspath(__file__))
MD = os.path.join(HERE, "mock10-problems.md")
TRANS = standard_transformations + (implicit_multiplication_application, convert_xor)
R = sp.Rational
x, y = sp.symbols("x y", positive=True)
SYMS = {"x": x, "y": y, "sqrt": sp.sqrt, "pi": sp.pi}


# --------------------------------------------------------------------------- parsing md
def parse_md(path):
    qs, cur, fig = {}, None, None
    for line in open(path, encoding="utf-8"):
        line = line.rstrip("\n")
        m = re.match(r"## (M[12])-Q(\d+)$", line)
        if m:
            cur = {"mod": int(m.group(1)[1]), "n": int(m.group(2)), "choices": {}, "figure": ""}
            qs[(cur["mod"], cur["n"])] = cur
            continue
        if cur is None:
            continue
        if line.startswith("```latex"):
            fig = []
            continue
        if fig is not None:
            if line.startswith("```"):
                cur["figure"] = "\n".join(fig)
                fig = None
            else:
                fig.append(line)
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


def tex_to_expr(s):
    s = s.replace("\\$", "").replace("$", "").replace("\\%", "").replace("\\,", "").replace("\\dfrac", "\\frac")
    s = s.replace("{,}", "").replace("\\pi", " pi ").replace("\\sqrt", " sqrt").replace("\\cdot", "*")
    s = re.sub(r"(?<=\d),(?=\d{3})", "", s)
    for _ in range(3):
        s = re.sub(r"\\frac\{([^{}]*)\}\{([^{}]*)\}", r"((\1)/(\2))", s)
    s = s.replace("{", "(").replace("}", ")").strip()
    return parse_expr(s, local_dict=SYMS, transformations=TRANS)


def same(a, b):
    a, b = sp.sympify(a), sp.sympify(b)
    return abs(float(sp.N(a)) - float(sp.N(b))) < 1e-9


def table_rows(fig):
    body = fig.split("\\hline")
    rows = []
    for chunk in body:
        chunk = chunk.replace("\\end{tabular}", "").strip()
        chunk = re.sub(r"\\begin\{tabular\}\{[^}]*\}", "", chunk).strip()
        if not chunk:
            continue
        for r in chunk.split("\\\\"):
            r = r.strip()
            if r:
                rows.append([c.strip() for c in r.split("&")])
    return rows


def pair(txt):
    m = re.fullmatch(r"\$\((\d+),(\d+)\)\$", txt.strip())
    assert m, txt
    return int(m.group(1)), int(m.group(2))


def clock(txt):
    m = re.match(r"\$(\d+)\{:\}(\d+)\$ ([ap])\.m\.", txt.strip())
    assert m, txt
    h, mi = int(m.group(1)), int(m.group(2))
    return h + mi / 60 + (12 if m.group(3) == "p" and h != 12 else 0)


# ------------------------------------------------------------------ independent solvers
def solve_all(qs):
    A = {}
    t = sp.symbols("t")

    # ================= MODULE 1 =================
    A[(1, 1)] = sp.solve(sp.Eq(1200 + 400 * t, 3200), t)[0]
    A[(1, 2)] = ("expr", lambda e: same_fn(e, (3 * x ** 4) ** 2))
    A[(1, 3)] = R(sorted([3, 5, 4, 8, 6, 4])[2] + sorted([3, 5, 4, 8, 6, 4])[3], 2)
    A[(1, 4)] = sp.real_root(343, 3)
    A[(1, 5)] = sp.solve(sp.Eq(150 + 30 * t, 600), t)[0]
    A[(1, 6)] = 40 * 3 ** 2
    A[(1, 7)] = sp.solve(sp.Eq(9 + R(5, 4) * t, 24), t)[0]
    A[(1, 8)] = sp.sqrt(R(9, 10) ** 2 + R(12, 10) ** 2)
    A[(1, 9)] = R(271, 10) - (R(64, 10) + R(38, 100) * 50)
    tt, pp = sp.symbols("tt pp")
    A[(1, 10)] = sp.solve([tt + pp - 18, 9 * tt + 5 * pp - 130], [tt, pp], dict=True)[0][tt]
    # Q11: count real solutions of x/(x-3) = 2 + 3/(x-3), rejecting zero denominators
    sols = [s for s in sp.solve(sp.Eq(x / (x - 3), 2 + 3 / (x - 3)), x) if s != 3]
    A[(1, 11)] = len(sols)
    h = lambda z: R(2, 100) * z ** 2 - R(12, 10) * z + 25
    A[(1, 12)] = min(h(z) for z in [R(k, 2) for k in range(0, 121)])
    A[(1, 13)] = ("pair", lambda p: 18 * p[0] + 11 * p[1] >= 900 and p[0] + p[1] <= 70)
    A[(1, 14)] = R(3 ** 3, 5)
    a15 = sp.symbols("a15")
    f15 = lambda z: z ** 2 - 8 * z + 3
    s15 = [s for s in sp.solve(sp.Eq(f15(a15), f15(11)), a15) if s != 11]
    assert len(s15) == 1
    A[(1, 15)] = s15[0]
    rows = table_rows(qs[(1, 16)]["figure"])
    tab = {r[0]: [int(v) for v in r[1:]] for r in rows[1:]}
    assert sum(sum(v) for v in tab.values()) == 300
    A[(1, 16)] = Fraction(tab["Website"][0], sum(tab["Website"]))
    rate = R(748 - 472, 2)
    A[(1, 17)] = 472 - 3 * rate
    A[(1, 18)] = ("expr", lambda e: same_fn(e, (3 * x - 2) ** 2 - (x + 4) ** 2))
    L = sp.symbols("L")
    A[(1, 19)] = 2 * sp.solve(sp.Eq((L + 6) + (2 * L + 4 + 6), 49), L)[0] + 4
    s20 = sp.solve(sp.Eq((x - 4) ** 2, 3 * (x - 4)), x)
    A[(1, 20)] = sum(s20)
    # Q21: brute force over k: two distinct parallel lines 2x+ky=10, kx+8y=20
    good = []
    for kv in [R(i, 4) for i in range(-80, 81)]:
        a1, b1, c1 = 2, kv, 10
        a2, b2, c2 = kv, 8, 20
        par = (a1 * b2 - a2 * b1 == 0)
        # distinct: not proportional including constants
        prop = (a1 * c2 - a2 * c1 == 0) and (b1 * c2 - b2 * c1 == 0)
        if par and not prop:
            good.append(kv)
    assert len(good) == 1
    A[(1, 21)] = good[0]
    r = 10
    A[(1, 22)] = ("expr", lambda e: abs(float(sp.N(e)) - float(100 * sp.pi - 6 * (sp.sqrt(3) / 4) * r ** 2)) < 1e-9)

    # ================= MODULE 2 =================
    A[(2, 1)] = sp.solve(sp.Eq(40 + 85 * t, 380), t)[0]
    A[(2, 2)] = (lambda z: 3 * z ** 2 - z + 4)(-1)
    w = sp.symbols("w")
    sw = [s for s in sp.solve(sp.Eq((20 + 2 * w) * (14 + 2 * w) - 280, 152), w) if s > 0]
    assert len(sw) == 1
    A[(2, 3)] = sw[0]
    a4, b4 = sp.symbols("a4 b4")
    s4 = sp.solve([3 * a4 + 2 * b4 - 62, 2 * a4 + 5 * b4 - 100], [a4, b4], dict=True)[0]
    A[(2, 4)] = s4[a4] + s4[b4]
    A[(2, 5)] = max(hh for hh in range(10, 100) if 55 * 10 + 40 * (hh - 10) <= 1000)
    rows6 = table_rows(qs[(2, 6)]["figure"])
    vals = [int(v) for v in rows6[0][1:]]
    cnts = [int(v) for v in rows6[1][1:]]
    data = [v for v, c in zip(vals, cnts) for _ in range(c)]
    assert len(data) == 40
    data.sort()
    median = R(data[19] + data[20], 2)
    mean = R(sum(data), 40)
    A[(2, 6)] = median - mean
    rate7 = R(3000 - 2400, R(5, 2))
    A[(2, 7)] = 10 - R(2400 - 1800, 1) / rate7
    A[(2, 8)] = ("count", None)
    A[(2, 8)] = sum(1 for xv in range(0, 60) if -xv ** 2 + 14 * xv - 24 > 0)
    # Q9: similar triangles; lamp height from first config, then second
    H = R(3, 2) * (6 + 3) / 3
    s9 = sp.symbols("s9")
    A[(2, 9)] = sp.solve(sp.Eq(H / (10 + s9), R(3, 2) / s9), s9)[0]
    combos = [(n, p) for n in range(1, 15) for p in range(1, 26) if 7 * n + 4 * p == 100]
    A[(2, 10)] = sum(1 for n, p in combos if p > n)
    A[(2, 11)] = ("pair", lambda p: 480 * p[0] + 45 * p[1] >= 6000 and 8 * p[0] + p[1] <= 120)
    xs = sp.symbols("xs")
    rr = sp.solve(xs ** 2 - 4 * xs + 1, xs)
    A[(2, 12)] = sp.simplify((rr[0] + 3) * (rr[1] + 3))
    ff = lambda z: z ** 2 - 6 * z + 14
    gg = lambda z: z ** 2 - 4 * z + 1
    A[(2, 13)] = min(gg(ff(R(k, 10))) for k in range(-300, 301))
    A[(2, 14)] = None
    T = R(1590) / R(106, 100)
    tom = sp.symbols("tom")
    t1 = sp.solve(sp.Eq(R(12, 10) * tom + R(9, 10) * (T - tom), 1590), tom)[0]
    A[(2, 14)] = R(9, 10) * (T - t1)
    # Q15: cubic with p(1)=p(3)=p(5)=7, p(0)=-8
    a, b, c, d = sp.symbols("a b c d")
    P = lambda z: a * z ** 3 + b * z ** 2 + c * z + d
    sol15 = sp.solve([P(1) - 7, P(3) - 7, P(5) - 7, P(0) + 8], [a, b, c, d], dict=True)[0]
    A[(2, 15)] = P(6).subs(sol15)
    # Q16
    rr16, dd = sp.symbols("rr16 dd")
    s16 = sp.solve([dd + rr16 * (3000 - dd) - 1100, dd + rr16 * (7000 - dd) - 1900], [rr16, dd], dict=True)[0]
    B16 = sp.symbols("B16")
    A[(2, 16)] = sp.solve(sp.Eq(s16[dd] + s16[rr16] * (B16 - s16[dd]), 2000), B16)[0]
    # Q17: legs from hypotenuse 25 and area 84 by brute force; radius from coordinates
    legs = [(p, q) for p in range(1, 26) for q in range(1, 26) if p * p + q * q == 625 and p * q == 168]
    assert legs
    la, lb = legs[0]
    rad = sp.symbols("rad", positive=True)
    # centre (rad, rad) on hypotenuse x/la + y/lb = 1
    A[(2, 17)] = sp.solve(sp.Eq(rad / la + rad / lb, 1), rad)[0]
    # Q18: Bayes chain, brute force over the unknown support rate
    sup_car, sup_tr = R(3, 10), R(6, 10)
    xb = sp.symbols("xb")
    totsup = R(4, 10) * sup_car + R(35, 100) * sup_tr + R(25, 100) * xb
    xv = sp.solve(sp.Eq(R(4, 10) * sup_car / totsup, R(4, 15)), xb)[0]
    A[(2, 18)] = xv * 100
    # Q19: abs equation; brute-force verification with exact algebra
    cands = sp.solve(x ** 2 - 2 * x - 8 - 4 * x, x) + sp.solve(-(x ** 2 - 2 * x - 8) - 4 * x, x)
    valid = [c for c in cands if sp.simplify(sp.Abs(c ** 2 - 2 * c - 8) - 4 * c) == 0]
    A[(2, 19)] = sum(valid)
    # Q20: count integer k
    cnt = 0
    for k in range(-500, 500):
        r2 = 29 - k
        if r2 <= 0:
            continue
        rad_ = math.sqrt(r2)
        two_x = rad_ > 2 + 1e-12
        no_y = rad_ < 5 - 1e-12
        if two_x and no_y:
            cnt += 1
    A[(2, 20)] = cnt
    # Q21: count m by direct counting of solutions of the system (exact)
    def n_sol(m):
        ys = set()
        X = sp.symbols("X")
        res = set()
        for sgn in (1, -1):
            # |x-3|=|y+2| with y = m x - 8 :  x-3 = sgn*(m x - 8 + 2)
            eq = sp.Eq(X - 3, sgn * (m * X - 6))
            for s in sp.solve(eq, X):
                res.add(s)
        return len(res) if res else 0
    # linear equation may have infinite solutions? check m=+-1 case gives eq -3 = ... handled by solve
    good21 = []
    for m in [R(i, 2) for i in range(-20, 21)] + [R(i, 3) for i in range(-9, 10)]:
        if n_sol(m) == 1:
            good21.append(m)
    A[(2, 21)] = len(set(good21))
    # Q22: scan k for exactly three distinct real solutions
    def n_sol22(k):
        Y = sp.symbols("Y")
        c = 0
        for yv in sp.solve(Y ** 2 + Y + 4 - k, Y):
            if not yv.is_real:
                continue
            xx = yv + 4
            if xx > 0:
                c += 2
            elif xx == 0:
                c += 1
        # roots could coincide
        return c
    good22 = [k for k in [R(i, 4) for i in range(0, 120)] if n_sol22(k) == 3]
    assert len(good22) == 1
    A[(2, 22)] = good22[0]
    return A


def same_fn(txt_expr, target):
    return sp.simplify(sp.expand(txt_expr - target)) == 0


# ------------------------------------------------------------------------------ driver
def main():
    qs = parse_md(MD)
    A = solve_all(qs)
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
                    if isinstance(val, tuple) and val[0] == "pair":
                        match = val[1](pair(txt))
                    elif isinstance(val, tuple) and val[0] == "expr":
                        e = tex_to_expr(txt)
                        match = val[1](e)
                    elif key == (2, 7):
                        match = abs(clock(txt) - float(val)) < 1e-9
                    else:
                        c = tex_to_expr(txt)
                        match = same(c, val)
                    if match:
                        hits.append(L)
                assert len(hits) == 1, f"{len(hits)} choices match computed value {val}: {hits}"
                assert hits[0] == q["answer"], f"computed letter {hits[0]} != keyed {q['answer']}"
                letters[key[0]].append(hits[0])
                msg = f"answer {q['answer']}  (value {'predicate' if isinstance(val, tuple) else sp.N(val, 6)})"
            else:
                assert not q["choices"], "grid-in must have no choices"
                keyed = tex_to_expr(q["answer"])
                assert abs(float(sp.N(keyed)) - float(sp.N(val))) < 1e-9, f"computed {val} != keyed {q['answer']}"
                lim = 6 if q["answer"].startswith("-") else 5
                assert len(q["answer"]) <= lim, "too many characters for a grid-in"
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
