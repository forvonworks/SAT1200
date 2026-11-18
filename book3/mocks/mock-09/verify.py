#!/usr/bin/env python3
"""Independent verification of every answer in mock09-problems.md (Mock Test 9, Book 3).

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
MD = os.path.join(HERE, "mock09-problems.md")
TRANS = standard_transformations + (implicit_multiplication_application, convert_xor)
R = sp.Rational
x, y = sp.symbols("x y", positive=True)
a_, b_ = sp.symbols("a b", positive=True)
k_ = sp.symbols("k", real=True)
m_ = sp.symbols("m", positive=True)
SYMS = {"x": x, "y": y, "a": a_, "b": b_, "k": k_, "m": m_, "sqrt": sp.sqrt, "pi": sp.pi}


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
    s = s.replace("\\left", "").replace("\\right", "").replace("\\!", "").replace("\\$", "").replace("$", "").replace("\\%", "").replace("\\,", "").replace("\\dfrac", "\\frac")
    s = s.replace("{,}", "").replace("\\pi", "pi").replace("\\sqrt", "sqrt").replace("\\cdot", "*")
    s = re.sub(r"(?<=\d),(?=\d{3})", "", s)
    for _ in range(3):
        s = re.sub(r"\\frac\{([^{}]*)\}\{([^{}]*)\}", r"((\1)/(\2))", s)
    s = s.replace("{", "(").replace("}", ")").strip()
    return parse_expr(s, local_dict=SYMS, transformations=TRANS)


def same(a, b):
    """numeric equality; for expressions with free symbols, equality at random sample points."""
    a, b = sp.sympify(a), sp.sympify(b)
    fs = (a.free_symbols | b.free_symbols)
    if not fs:
        return abs(float(sp.N(a)) - float(sp.N(b))) < 1e-9
    rnd = random.Random(12345)
    for _ in range(8):
        sub = {s: sp.Float(rnd.uniform(1.1, 9.7)) for s in fs}
        va, vb = complex(sp.N(a.subs(sub))), complex(sp.N(b.subs(sub)))
        if abs(va - vb) > 1e-9 * max(1.0, abs(va)):
            return False
    return True


# ------------------------------------------------------------------ helpers for predicates
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


def num(s):
    return float(sp.N(tex_to_expr(s)))


def pred_ages():
    import statistics as st
    old = [24, 27, 31, 35, 39, 41, 48]
    new = old + [35]
    mo, mn = st.mean(old), st.mean(new)
    mean_rel = "unchanged" if mo == mn else ("larger" if mn > mo else "smaller")
    def rel(a, b):
        return "the same" if abs(a - b) < 1e-12 else ("larger" if b > a else "smaller")
    sd_p, sd_s = rel(st.pstdev(old), st.pstdev(new)), rel(st.stdev(old), st.stdev(new))
    assert sd_p == sd_s
    def pred(txt):
        m = re.fullmatch(r"The mean is (unchanged|larger|smaller) and the standard deviation is (smaller|larger|the same)\.", txt)
        assert m, txt
        return m.group(1) == mean_rel and m.group(2) == sd_p
    return pred


def pred_concert():
    P = lambda p: -120 * (p - 25) ** 2 + 9000
    best = max(range(0, 101), key=P)
    def pred(txt):
        m = re.fullmatch(r"The maximum possible profit is \\\$([\d,]+), and it occurs when the ticket price is \\\$([\d,]+)\.", txt)
        if m:
            return int(m.group(1).replace(",", "")) == P(best) and int(m.group(2).replace(",", "")) == best
        m = re.match(r"The profit is \\\$([\d,]+) when tickets are free", txt)
        assert m, txt
        return P(0) == int(m.group(1).replace(",", ""))
    return pred


def pred_point(target):
    def pred(txt):
        m = re.fullmatch(r"\$\(([-\d.]+),\s*([-\d.]+)\)\$", txt.strip())
        assert m, txt
        return abs(float(m.group(1)) - float(target[0])) < 1e-9 and abs(float(m.group(2)) - float(target[1])) < 1e-9
    return pred


def pred_month(first):
    def pred(txt):
        m = re.fullmatch(r"Month (\d+)", txt)
        return int(m.group(1)) == first
    return pred


# ------------------------------------------------------------------ independent solvers
def distinct_real_roots(poly_expr, var):
    P = sp.Poly(sp.expand(poly_expr), var)
    out = []
    for r in P.real_roots():
        v = float(sp.N(r, 30))
        if not any(abs(v - o) < 1e-7 for o in out):
            out.append(v)
    return out


def solve_all(qs):
    A = {}
    t = sp.symbols("t")
    # ================= MODULE 1 =================
    A[(1, 1)] = sp.solve(sp.Eq(180 + 12 * t, 540), t)[0]
    A[(1, 2)] = sp.expand((x - 3) * (x + 8))
    A[(1, 3)] = R(480) * (1 - R(35, 100))
    A[(1, 4)] = (R(62, 2) - 11) * 11
    C5 = sp.symbols("C5")
    A[(1, 5)] = sp.solve(sp.Eq(R(18, 10) * C5 + 32, 86), C5)[0]
    x6 = sp.symbols("x6")
    A[(1, 6)] = 2 ** (sp.solve(sp.Eq(2 ** x6, 32), x6)[0] - 2)
    A[(1, 7)] = sp.solve(sp.Eq(240 - 8 * t, 72), t)[0]
    A[(1, 8)] = sp.sqrt(x) * x ** R(3, 2)
    A[(1, 9)] = ("pred", pred_ages())
    s10, l10 = sp.symbols("s10 l10")
    A[(1, 10)] = sp.solve([s10 + l10 - 30, 6 * s10 + 15 * l10 - 306], [s10, l10], dict=True)[0][l10]
    A[(1, 11)] = sp.expand((2 * x - 3) ** 2 - (x + 1) ** 2)
    Ax, Ay, Bx, By = -2, 5, 10, -3
    A[(1, 12)] = ("pred", pred_point((Ax + R(3, 4) * (Bx - Ax), Ay + R(3, 4) * (By - Ay))))
    A[(1, 13)] = min(a for a in range(0, 1000) if 30 * a + 18 * 100 >= 6000)
    A[(1, 14)] = (R(2000) * R(11, 10) ** 3 - 2000) - 3 * R(2000) * R(1, 10)
    w15, d15 = sp.symbols("w15 d15")
    A[(1, 15)] = sp.solve([w15 + d15 - 17, 3 * w15 + d15 - 41], [w15, d15], dict=True)[0][w15]
    A[(1, 16)] = ("pred", pred_concert())
    a17, b17 = sp.symbols("a17 b17")
    sols = [s for s in sp.solve([a17 ** 2 - b17 ** 2 - 63, a17 + b17 - 9], [a17, b17], dict=True)]
    assert len(sols) == 1
    A[(1, 17)] = sols[0][a17]
    tall, short = R(3, 4) * 320, R(1, 4) * 320
    r18 = sp.symbols("r18")
    A[(1, 18)] = sp.solve(sp.Eq((tall - r18) / short, R(5, 2)), r18)[0]
    b19 = sp.symbols("b19")
    bb = sp.solve(sp.Eq(14 * (b19 + 10) + 22 * b19, 680), b19)[0]
    A[(1, 19)] = bb + (bb + 10)
    b20, c20 = sp.symbols("b20 c20")
    f20 = lambda z: 2 * z ** 2 + b20 * z + c20
    s20 = sp.solve([f20(0) - 3, f20(1) - f20(5)], [b20, c20], dict=True)[0]
    A[(1, 20)] = f20(3).subs(s20)
    w21 = sp.symbols("w21")
    A[(1, 21)] = sp.solve(sp.Eq(w21 * R(14, 10) * R(3, 4), 63), w21)[0]
    leg = R(72 - 12 - 30, 2)
    h22 = sp.sqrt(leg ** 2 - ((30 - 12) / R(2)) ** 2)
    A[(1, 22)] = R(1, 2) * (12 + 30) * h22

    # ================= MODULE 2 =================
    p1 = sp.symbols("p1")
    A[(2, 1)] = sp.solve(sp.Eq(5 * p1 + 12, 112), p1)[0]
    g = lambda z: 3 * 2 ** z
    A[(2, 2)] = g(4) - g(2)
    lim_lb = R(265, 10) * 1000 * R(22, 10)
    assert (lim_lb / 1250) != int(lim_lb / 1250)
    A[(2, 3)] = int(sp.floor(lim_lb / 1250))
    A[(2, 4)] = R(1, 4) * x ** 2 - 3 * x + 9
    w5 = sp.symbols("w5", positive=True)
    A[(2, 5)] = sp.solve(sp.Eq((18 + 2 * w5) * (12 + 2 * w5) - 18 * 12, 18 * 12), w5)[0]
    # drone: position linear in time, steps of 30 minutes
    s6 = sp.symbols("s6")
    vx, vy = R(9 - 3), R(3 - (-1))
    steps = sp.solve(sp.Eq(3 + vx * s6, 21), s6)[0]
    A[(2, 6)] = -1 + vy * steps
    N7 = sp.symbols("N7")
    A[(2, 7)] = sp.solve(sp.Eq(R(12, 150), R(80) / N7), N7)[0]
    m8 = R(220 - 20, 212 - 32)
    A[(2, 8)] = 20 + m8 * (R(986, 10) - 32)
    first = next(tt for tt in range(1, 60) if 10 * 1.2 ** tt > 10 + 4 * tt)
    assert all(10 * 1.2 ** tt <= 10 + 4 * tt for tt in range(1, first))
    A[(2, 9)] = ("pred", pred_month(first))
    Rr = sp.sqrt(5 ** 2 + (R(24, 2)) ** 2)
    A[(2, 10)] = sp.pi * (Rr ** 2 - 5 ** 2)
    s11 = sp.symbols("s11")
    A[(2, 11)] = 200 - 2 * sp.solve(sp.Eq(18 * (200 - 2 * s11) + 12 * s11 + 10 * s11, 3320), s11)[0]
    n12 = sp.symbols("n12")
    A[(2, 12)] = sp.solve(sp.Eq(R(3, 4) * n12, R(1, 3) * n12 + 15), n12)[0] / 2
    # Q13: no solution <=> coefficient 0 and right side nonzero
    k13 = sp.symbols("k13")
    zero_coef = sp.solve(k13 ** 2 - k13 - 6, k13)
    nos = [kk for kk in zero_coef if (kk ** 2 - 9) != 0]
    inf = [kk for kk in zero_coef if (kk ** 2 - 9) == 0]
    assert len(nos) == 1 and len(inf) == 1
    A[(2, 13)] = nos[0]

    def pred14(txt):
        kk = tex_to_expr(txt)
        pts = distinct_real_roots(x ** 4 + 5 * x ** 2 + 4 - kk, x)   # x-coords of intersection (y = x^2+2 is determined by x)
        return len(pts) == 1
    A[(2, 14)] = ("pred", pred14)
    r15 = sp.symbols("r15", positive=True)
    A[(2, 15)] = sp.solve(sp.Eq(r15 ** 2 + 24 ** 2, (16 + r15) ** 2), r15)[0]

    def brute16():
        best, ways = -1, 0
        for a1 in range(1, 10):
            for a2 in range(a1, 10):
                for a3 in range(a2, 10):
                    for a5 in range(9, 71):
                        for a6 in range(a5, 71):
                            a7 = 70 - (a1 + a2 + a3 + 9 + a5 + a6)
                            if a7 < a6:
                                continue
                            arr = [a1, a2, a3, 9, a5, a6, a7]
                            cnt = Counter(arr)
                            top = max(cnt.values())
                            modes = [v for v, c in cnt.items() if c == top]
                            if modes == [8] and top >= 2:
                                if a7 > best:
                                    best, ways = a7, 0
                                if a7 == best:
                                    ways += 1
        return best
    A[(2, 16)] = brute16()
    k17 = sp.symbols("k17")
    sol17 = sp.solve(sp.Eq(49 - 4 * (k17 + 3), 25), k17)
    assert len(sol17) == 1
    # confirm directly from the roots
    kk = sol17[0]
    rts = sp.solve(x ** 2 - 5 * x + kk - (2 * x - 3), x)
    assert abs(rts[0] - rts[1]) == 5
    A[(2, 17)] = kk
    teams, mean_pts = 10, R(25, 2)
    G = teams * (teams - 1) // 2
    d18 = sp.symbols("d18")
    A[(2, 18)] = sp.solve(sp.Eq(3 * (G - d18) + 2 * d18, teams * mean_pts), d18)[0]
    t19, r19 = sp.symbols("t19 r19", positive=True)       # r19 = speed ratio b/a
    s19 = sp.solve([r19 * t19 - 9, t19 / r19 - 4], [t19, r19], dict=True)
    assert len(s19) == 1
    A[(2, 19)] = s19[0][t19]
    # Q20: quadratic from the table, then zeros of g
    rows20 = table_rows(qs[(2, 20)]["figure"])
    xs20 = [int(c) for c in rows20[0][1:]]
    ys20 = [int(c.replace("$", "").replace("-", "-")) for c in rows20[1][1:]]
    aa, bb, cc = sp.symbols("aa bb cc")
    sf = sp.solve([aa * xi ** 2 + bb * xi + cc - yi for xi, yi in zip(xs20, ys20)], [aa, bb, cc], dict=True)[0]
    f20q = lambda z: sf[aa] * z ** 2 + sf[bb] * z + sf[cc]
    zs = sp.solve(f20q((x - 3) / 2), x)
    A[(2, 20)] = sum(zs)
    ycut = sp.symbols("ycut")
    A[(2, 21)] = sp.integrate(2 * sp.sqrt(100 - ycut ** 2), (ycut, -10, -5))
    cnt22 = 0
    for kk2 in range(-60, 61):
        pts = set()
        for z in distinct_real_roots(x ** 2 - 4 * x - 5 - kk2, x) if True else []:
            pts.add(round(z, 6))
        for z in distinct_real_roots(x ** 2 - 4 * x - 5 + kk2, x):
            pts.add(round(z, 6))
        # keep only roots that really satisfy |f| = k
        good = {z for z in pts if abs(abs(z ** 2 - 4 * z - 5) - kk2) < 1e-4}
        if len(good) == 4:
            cnt22 += 1
    A[(2, 22)] = cnt22
    return A


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
                    if isinstance(val, tuple) and val[0] == "pred":
                        match = val[1](txt)
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
