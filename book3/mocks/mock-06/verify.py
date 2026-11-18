#!/usr/bin/env python3
"""Independent verification of every answer in mock06-problems.md (Mock Test 6, Book 3).

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
MD = os.path.join(HERE, "mock06-problems.md")
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
    s = s.replace("\\left", "").replace("\\right", "")
    s = s.replace("{,}", "").replace("\\pi", "pi").replace("\\cdot", "*")
    s = re.sub(r"(?<=\d),(?=\d{3})", "", s)
    for _ in range(8):
        s = re.sub(r"\^\{([^{}]*)\}", r"^(\1)", s)
        s = re.sub(r"\\sqrt\{([^{}]*)\}", r"sqrt(\1)", s)
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
def pct_vals(txt):
    return [float(v) for v in re.findall(r"\d+\.?\d*", txt)]


def solve_all():
    A = {}
    t = sp.symbols("t")

    # ================= MODULE 1 =================
    A[(1, 1)] = sp.solve(sp.Eq(R(2, 3) * z - 5, 7), z)[0]
    zeros2 = sp.solve((z - 4) * (z + 2), z)
    A[(1, 2)] = max(zeros2) - min(zeros2)
    A[(1, 3)] = R(1600) * (1 - R(45, 100))
    ab, bc = 8, 15
    hyp = sp.sqrt(ab ** 2 + bc ** 2)
    A[(1, 4)] = bc / hyp                                                    # sin A = opp/hyp
    xx = sp.solve([sp.Eq(y, 3 * x), sp.Eq(x + y, 20)], [x, y])
    A[(1, 5)] = xx[x]
    A[(1, 6)] = ("pred", lambda txt: sp.expand(tex_to_expr(txt, {"x": z}) - (4 * z ** 2 - 25)) == 0)
    w7 = sp.symbols("w7")
    A[(1, 7)] = sp.solve(sp.Eq(2 * (w7 + 2 * w7 + 4), 44), w7)[0]
    A[(1, 8)] = 3 * x ** 2 * 4 * x ** 5
    # Q9 (text choices)
    A[(1, 9)] = ("pred", lambda txt: ("each additional minute" in txt.lower() and "0.62" in txt
                                      and "points scored per game increases" in txt))
    A[(1, 10)] = min(m for m in range(0, 500) if 24000 + 1350 * m > 90000)
    s11 = sp.solve([sp.Eq(3 * x + 2 * y, 16), sp.Eq(x - y, 2)], [x, y])
    kk = sp.symbols("kk")
    A[(1, 11)] = sp.solve(sp.Eq(s11[y], kk * s11[x] + 10), kk)[0]
    ref12 = lambda tv: 50 * R(88, 100) ** (R(tv) / 3)                      # P(0)=50, x0.88 each 3 yrs
    assert ref12(3) == 44

    def pred12(txt):
        expr = parse_expr(clean(txt.split("=", 1)[1]), local_dict={"t": z}, transformations=TRANS)
        return all(abs(float(expr.subs(z, tv)) - float(ref12(tv))) < 1e-9 for tv in (0, 3, 6, 9))
    A[(1, 12)] = ("pred", pred12)
    h13 = 50 * math.tan(math.radians(55)) + 1.6
    A[(1, 13)] = int(round(h13))
    f14 = lambda v: 3 * v - 2
    g14 = lambda v: v ** 2 + 1
    A[(1, 14)] = [v for v in sp.solve(sp.Eq(f14(g14(z)), 49), z) if v > 0][0]
    mbps = 480
    A[(1, 15)] = R(mbps, 8) * 600 / 1000                                    # MB/s * s / 1000 -> GB
    tt, bb = sp.symbols("tt bb")
    A[(1, 16)] = -sp.diff(sp.solve(sp.Eq(3 * tt + R("7.5") * bb, 600), tt)[0], bb)
    sol17 = sp.solve(sp.Eq(z ** 2 - 3 * z - 4, 2 * z + 2), z)
    A[(1, 17)] = 2 * max(sol17) + 2
    sol18 = [(a, b) for a in range(1, 60) for b in range(1, 60) if a * a + b * b == 52 and a * b == 24]
    assert sol18 and len({a + b for a, b in sol18}) == 1
    A[(1, 18)] = sol18[0][0] + sol18[0][1]
    p1, p2 = (2, -3), (8, 9)
    slope_l = R(p2[1] - p1[1], p2[0] - p1[0])
    slope_m = -1 / slope_l

    def pred19(txt):
        px, py = [R(v) for v in re.findall(r"-?\d+", txt)]
        return py == slope_m * px
    A[(1, 19)] = ("pred", pred19)
    # Q20: distance from origin to line 3x+4y=36 (formula) and also check foot lies on the segment
    d20 = R(36) / sp.sqrt(3 ** 2 + 4 ** 2)
    foot = (3 * d20 / 5, 4 * d20 / 5)                                       # unit normal * d
    assert 0 <= foot[0] <= 12 and 0 <= foot[1] <= 9
    A[(1, 20)] = d20
    ks = sp.symbols("ks")
    pairs = [kv for kv in range(-60, 61)
             if sp.Poly(z ** 2 - kv * z + 18, z).discriminant() >= 0
             and abs(sp.sqrt(sp.Poly(z ** 2 - kv * z + 18, z).discriminant())) == 3]
    A[(1, 21)] = [kv for kv in pairs if kv > 0][0]
    pages = [n for n in range(1, 2000)
             if 60 + R(1, 10) * n < (R(1, 2) * n if n <= 200 else 100 + R(3, 10) * (n - 200))]
    A[(1, 22)] = pages[0]
    assert all(n >= pages[0] for n in pages)                                # B cheaper for every n from there on

    # ================= MODULE 2 =================
    A[(2, 1)] = sp.solve(sp.Eq(5 * (z - 3), 2 * z + 9), z)[0]
    vx = sp.solve(sp.diff(z ** 2 - 6 * z + 11, z), z)[0]
    A[(2, 2)] = vx
    Bs, ws, hs = sp.symbols("Bs ws hs", positive=True)
    h3 = sp.solve(sp.Eq(Bs, 703 * ws / hs ** 2), hs)[0]
    A[(2, 3)] = ("pred", lambda txt: sp.simplify(parse_expr(
        clean(txt.split("=", 1)[1]), local_dict={"B": Bs, "w": ws}, transformations=TRANS) - h3) == 0)
    A[(2, 4)] = (R(9360) + 8 * (R(9360) - R(7200)) / (20 - 8))
    b5 = sp.sqrt(R(360, 250))
    A[(2, 5)] = ("pred", lambda txt: abs(pct_vals(txt)[0] - float((b5 - 1) * 100)) < 1e-9)
    A[(2, 6)] = 5 * sp.sqrt(R(72, 18))
    s7 = sp.solve(sp.Eq(sp.Abs(3 * x - 12) - 6, 9), x) if False else None
    zr = sp.symbols("zr", real=True)
    s7 = [sp.solve(3 * zr - 12 - 15, zr)[0], sp.solve(-(3 * zr - 12) - 15, zr)[0]]
    A[(2, 7)] = abs(s7[0] - s7[1])
    roots8 = sp.solve(z ** 3 - 5 * z ** 2 - 4 * z + 20, z)
    assert len(roots8) == 3
    A[(2, 8)] = sum(r ** 2 for r in roots8)
    A[(2, 9)] = ("pred", lambda txt: sp.simplify(sp.expand(tex_to_expr(txt.split("=")[0], {"x": z}).subs(
        z, 3 + sp.sqrt(7)))) == 0 and sp.simplify(sp.expand(tex_to_expr(txt.split("=")[0], {"x": z}).subs(
            z, 3 - sp.sqrt(7)))) == 0)
    dd = next(n for n in range(0, 1000) if 420 - R(7, 2) * n < 350 - R(3, 2) * n)
    A[(2, 10)] = dd
    g11 = max(n for n in range(0, 200) if 45 + (R(17, 2) * max(0, n - 10)) <= 120)
    A[(2, 11)] = g11
    s12 = sp.solve([sp.Eq(x / 2 + y / 3, 7), sp.Eq(x / 4 - y / 6, R(3, 2))], [x, y])
    A[(2, 12)] = s12[x] * s12[y]
    # Q13 (text): causal claim needs random assignment; generalising needs random selection.
    # study: random selection = YES, random assignment = NO  ->  generalise association only.
    sel, asg = True, False
    def pred13(txt):
        t_ = txt.lower()
        claims_cause = ("causes" in t_) and ("does not show" not in t_)
        says_assoc = "associated" in t_
        denies_general = "nothing can be concluded" in t_ or "cannot be generalized" in t_
        ok_cause = (not claims_cause) if not asg else True
        ok_general = (not denies_general) if sel else True
        return says_assoc and ok_cause and ok_general
    A[(2, 13)] = ("pred", pred13)
    # Q14: 0.8^(d/5) multiplied by 0.64 -> d = 5 * log(0.64)/log(0.8) found by search over integers
    n14 = [n for n in range(1, 200) if abs(0.8 ** (n / 5) - 0.64) < 1e-12]
    A[(2, 14)] = n14[0]
    lo1, hi1 = 38 - 3.1, 38 + 3.1
    lo2, hi2 = 43 - 3.4, 43 + 3.4
    A[(2, 15)] = ("pred", lambda txt: lo1 <= pct_vals(txt)[0] <= hi1 and lo2 <= pct_vals(txt)[0] <= hi2)
    xs, ys = sp.symbols("xs ys", real=True)
    circ = xs ** 2 + ys ** 2 - 12 * xs - 16 * ys + 84
    cx, cy = sp.solve([sp.diff(circ, xs), sp.diff(circ, ys)], [xs, ys]).values()
    r16sq = sp.simplify(cx ** 2 + cy ** 2 - 84)
    r16 = sp.sqrt(r16sq)
    d0 = sp.sqrt(cx ** 2 + cy ** 2)
    assert circ.subs({xs: 0, ys: 0}) > 0 and d0 > r16
    A[(2, 16)] = d0 - r16
    vv = sp.symbols("vv", positive=True)
    A[(2, 17)] = sp.solve(sp.Eq(1 / R(6) + 1 / vv, 2 / R(8)), vv)[0]
    # Q18: Bayes on a population of 10,000
    N = 10000
    inf = N * R(2, 100)
    tp = inf * R(90, 100)
    fp = (N - inf) * R(5, 100)
    ppv = tp / (tp + fp)
    A[(2, 18)] = ("pred", lambda txt: abs(pct_vals(txt)[0] - float(ppv) * 100) < 0.6)
    # Q19: count distinct solutions for several k > 0 by exact solving
    def count19(kv):
        sols = set()
        for sgn in (1, -1):
            for e in sp.solve(sp.Eq((z - 4) ** 2, kv * sgn * (z - 4)), z):
                if sp.simplify((e - 4) ** 2 - kv * sp.Abs(e - 4)) == 0:
                    sols.add(e)
        return len(sols)
    counts19 = {count19(kv) for kv in (R(1, 2), 1, 3, 7, 10)}
    assert len(counts19) == 1
    A[(2, 19)] = counts19.pop()
    k20 = sp.symbols("k20")
    vtx = (2 * k20, (2 * k20) ** 2 - 4 * k20 * (2 * k20) + 3 * k20)
    sols20 = sp.solve(sp.Eq(vtx[1], 2 * vtx[0] - 5), k20)
    A[(2, 20)] = sum(sols20)
    sols21 = set()
    for lo, hi, expr in ((-100, 2, (2 - z) + (9 - z)), (2, 9, (z - 2) + (9 - z)), (9, 100, (z - 2) + (z - 9))):
        for e in sp.solve(sp.Eq(expr, 15), z):
            if lo <= e <= hi:
                sols21.add(e)
    A[(2, 21)] = sum(sols21)
    hh = sp.symbols("hh", positive=True)
    a28, a41 = math.radians(28), math.radians(41)
    h22 = 40 / (1 / math.tan(a28) - 1 / math.tan(a41))
    A[(2, 22)] = int(round(h22))
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
