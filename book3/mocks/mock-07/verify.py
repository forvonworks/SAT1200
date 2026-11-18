#!/usr/bin/env python3
"""Independent verification of every answer in mock07-problems.md (Mock Test 7, Book 3).

For each question the correct value is recomputed here from the problem data (sympy /
fractions / brute force) -- NOT read from the .md.  Then:
  * every printed choice is parsed from the .md text and compared with the computed value,
  * exactly ONE choice must match, and its letter must equal the letter keyed in the .md,
  * grid-in answers must equal the computed value,
  * the blueprint (difficulty / domain / grid-in counts, letter balance) is asserted.
Run:  python3 verify.py      (exit code 0 = ALL OK)
"""
import os
import re
import sys
from collections import Counter

import sympy as sp
from sympy.parsing.sympy_parser import (convert_xor, implicit_multiplication_application,
                                        parse_expr, standard_transformations)

HERE = os.path.dirname(os.path.abspath(__file__))
MD = os.path.join(HERE, "mock07-problems.md")
TRANS = standard_transformations + (implicit_multiplication_application, convert_xor)
R = sp.Rational
x, y = sp.symbols("x y", positive=True)
SYMS = {"x": x, "y": y, "sqrt": sp.sqrt, "pi": sp.pi}


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


def tex_to_expr(s):
    s = s.replace("\\$", "").replace("$", "").replace("\\%", "").replace("\\,", "").replace("\\dfrac", "\\frac")
    s = s.replace("{,}", "").replace("\\pi", "pi").replace("\\sqrt", "sqrt")
    s = re.sub(r"(?<=\d),(?=\d{3})", "", s)
    for _ in range(3):
        s = re.sub(r"\\frac\{([^{}]*)\}\{([^{}]*)\}", r"((\1)/(\2))", s)
    s = s.replace("{", "(").replace("}", ")").strip()
    return parse_expr(s, local_dict=SYMS, transformations=TRANS)


def same(a, b):
    a, b = sp.nsimplify(a), sp.nsimplify(b)
    if a.is_number and b.is_number:
        return abs(float(a) - float(b)) < 1e-9
    return sp.simplify(a - b) == 0


# ------------------------------------------------------------------ independent solvers
import math
import statistics as st


def _vals(txt):
    return [float(n) for n in re.findall(r"\d+(?:\.\d+)?", txt.replace(",", ""))]


# ---- predicates over the printed text of a choice (non-numeric choices) -----------------
def pred_samples(txt):
    """M1-Q9: two random samples; the only supported conclusion is the overlap of the two intervals."""
    lo = max(52 - 4, 47 - 3); hi = min(52 + 4, 47 + 3)
    assert (lo, hi) == (48, 50)
    m = re.search(r"between (\d+)\\% and (\d+)\\%", txt)
    if "plausible" in txt and m:
        return float(m.group(1)) == lo and float(m.group(2)) == hi
    return False          # "exactly", "more reliable", "not random" are never supported by margins of error


def pred_candle(txt):
    """M1-Q16: h through (2,21),(6,15); interpret the t-intercept."""
    m = (15 - 21) / (6 - 2); b = 21 - m * 2; t_int = -b / m
    mm = re.search(r"burns completely (\d+(?:\.\d+)?) hours", txt)
    return bool(mm) and abs(float(mm.group(1)) - t_int) < 1e-9


def pred_cubic(txt):
    """M1-Q17: cubic, negative leading coefficient, simple zero at -1, double (touching) zero at 2."""
    p = sp.Poly(sp.expand(tex_to_expr(txt)), x)
    if p.degree() != 3 or p.LC() >= 0:
        return False
    r = sp.roots(p)
    return r.get(-1) == 1 and r.get(2) == 2


def pred_quad_vertex(txt):
    """M2-Q5: opens upward, vertex (3,-4), passes through (5,4)."""
    f = sp.expand(tex_to_expr(txt))
    P = sp.Poly(f, x)
    if P.degree() != 2 or P.LC() <= 0:
        return False
    return sp.diff(f, x).subs(x, 3) == 0 and f.subs(x, 3) == -4 and f.subs(x, 5) == 4


def pred_sets(txt):
    """M2-Q9: statements about data sets P and Q."""
    P, Q = [8, 8, 8, 14, 14, 14], [8, 9, 10, 12, 13, 14]
    mP, mQ, dP, dQ = st.mean(P), st.mean(Q), st.median(P), st.median(Q)
    sP, sQ = st.pstdev(P), st.pstdev(Q)
    clauses = []
    if "same mean and the same median" in txt:
        clauses += [mP == mQ, dP == dQ]
    if "same mean, but" in txt:
        clauses += [mP == mQ]
    if "same median, but" in txt:
        clauses += [dP == dQ]
    if "Set $P$ has the greater standard deviation" in txt:
        clauses.append(sP > sQ)
    if "Set $Q$ has the greater standard deviation" in txt:
        clauses.append(sQ > sP)
    if "Set $P$ has the greater median" in txt:
        clauses.append(dP > dQ)
    if "Set $Q$ has the greater mean" in txt:
        clauses.append(mQ > mP)
    assert clauses
    return all(clauses)


def numeric_quad_max(txt):
    z = sp.symbols("z", real=True)
    f = tex_to_expr(txt.split("=", 1)[1]).subs(x, z)
    crit = sp.solve(sp.diff(f, z), z)
    assert len(crit) == 1 and sp.diff(f, z, 2) < 0
    return f.subs(z, crit[0])


def cbrt(v):
    return math.copysign(abs(v) ** (1 / 3), v)


def solve_all(qs):
    A = {}
    t = sp.symbols("t")
    a, b, k, c, h = sp.symbols("a b k c h")
    X, Y = sp.symbols("X Y")

    # ================= MODULE 1 =================
    A[(1, 1)] = sp.solve(sp.Eq(R(17, 2) + R(5, 4) * t, R(27, 2)), t)[0]
    A[(1, 2)] = sp.expand((2 * x + 5) ** 2)
    A[(1, 3)] = R(480) - R(3, 8) * 480
    r4 = sp.solve(sp.Eq(2 * sp.pi * t, 14 * sp.pi), t)[0]; A[(1, 4)] = sp.pi * r4 ** 2
    A[(1, 5)] = R(12 - 4, 5 - 1)
    A[(1, 6)] = (lambda g, f: f(g(4)))(lambda v: v ** 2, lambda v: v + 3)
    wv = sp.symbols("wv", positive=True)
    A[(1, 7)] = sp.solve([sp.Eq(2 * (X + wv), 36), sp.Eq(X, 2 * wv + 3)], [X, wv], dict=True)[0][wv]
    A[(1, 8)] = sp.expand(3 * x ** 2 * y * 4 * x * y ** 3)
    A[(1, 9)] = ("pred", pred_samples)
    s10 = sp.symbols("s10")
    A[(1, 10)] = sp.solve(sp.Eq(3 * (s10 + 9) + 4 * s10, R(131, 2)), s10)[0]
    p11 = lambda v: v ** 3 - 4 * v ** 2 - 11 * v + 30
    assert p11(2) == 0
    A[(1, 11)] = max(sp.roots(sp.Poly(p11(x), x)).keys())
    # Q12: area = rectangle + two half-discs (integral of the half-disc of radius 7)
    yy = sp.symbols("yy")
    halfdisc = sp.integrate(sp.sqrt(49 - yy ** 2), (yy, -7, 7))
    A[(1, 12)] = 30 * 14 + 2 * halfdisc
    A[(1, 13)] = min(cc for cc in range(0, 21) if 5 * cc - 2 * (20 - cc) >= 58)
    A[(1, 14)] = R(1392000, 12800) * 4 / 100
    A[(1, 15)] = min(m for m in range(0, 100) if 500 * R(112, 100) ** m > 800 + 60 * m)
    assert all((500 * R(112, 100) ** m > 800 + 60 * m) for m in range(A[(1, 15)], 100))
    A[(1, 16)] = ("pred", pred_candle)
    A[(1, 17)] = ("pred", pred_cubic)
    A[(1, 18)] = sp.solve(sp.Eq(t * (1 + R(8, 100) + R(15, 100)), R(123, 2)), t)[0]

    def pred19(txt):
        ms = {L: numeric_quad_max(q["choices"][L]) for L in "ABCD"}
        return numeric_quad_max(txt) == max(ms.values()) and list(ms.values()).count(max(ms.values())) == 1
    q = qs[(1, 19)]
    A[(1, 19)] = ("pred", pred19)
    # Q20: f = a(x-h)^2 + 19 through (1,10),(7,10)
    sol20 = sp.solve([a * (1 - h) ** 2 + 19 - 10, a * (7 - h) ** 2 + 19 - 10], [a, h], dict=True)
    sol20 = [s for s in sol20 if s[a] < 0]; assert len(sol20) == 1
    A[(1, 20)] = (sol20[0][a] * (-1 - sol20[0][h]) ** 2 + 19)
    pr = sp.symbols("pr")
    A[(1, 21)] = 120 * sp.solve(sp.Eq(120 * pr, (pr + R(3, 2)) * 105), pr)[0]
    # Q22: scan 0<x<20 for sin((4x+7) deg) = cos((2x-1) deg)
    F = lambda xv: math.sin(math.radians(4 * xv + 7)) - math.cos(math.radians(2 * xv - 1))
    roots22, step = [], 0.0005
    xv = step
    while xv < 20 - step:
        f0, f1 = F(xv), F(xv + step)
        if f0 == 0 or f0 * f1 < 0:
            lo_, hi_ = xv, xv + step
            for _ in range(60):
                mid = (lo_ + hi_) / 2
                if F(lo_) * F(mid) <= 0: hi_ = mid
                else: lo_ = mid
            roots22.append(round((lo_ + hi_) / 2, 6))
        xv += step
    assert len(roots22) == 1, roots22
    A[(1, 22)] = sp.Rational(round(roots22[0] * 1000), 1000)

    # ================= MODULE 2 =================
    A[(2, 1)] = sp.solve(sp.Eq(5 - 2 * t, 3 * t - 15), t)[0]
    A[(2, 2)] = (lambda z: z ** 2 - 3 * z + 5)(-2)
    A[(2, 3)] = (6 * R(1, 2)) * (R(9, 2) * R(1, 2))
    k4 = sp.solve(sp.Eq(5 * 2 + k * 5, 20), k)[0]
    A[(2, 4)] = sp.solve(sp.Eq(k4 * Y, 20), Y)[0]
    A[(2, 5)] = ("pred", pred_quad_vertex)
    sx = R(3) * R(2, 3)                       # side ratio X -> Z
    A[(2, 6)] = 100 / sx ** 2
    s7 = sp.solve([3 * X + 5 * Y - 17, 2 * X - Y - 7], [X, Y], dict=True)[0]
    A[(2, 7)] = 5 * s7[X] + 4 * s7[Y]
    bp = sp.symbols("bp", positive=True); ap = sp.symbols("ap", positive=True)
    s8 = sp.solve([ap * bp - 12, ap * bp ** 3 - 48], [ap, bp], dict=True)[0]
    A[(2, 8)] = s8[ap]
    A[(2, 9)] = ("pred", pred_sets)
    tol = R(15, 100); ctr = R(64, 10)
    A[(2, 10)] = (ctr + tol) - (ctr - tol)
    k11, c11 = sp.symbols("k11 c11")
    lhs = sp.Poly(sp.expand((X + 3) * (X ** 2 - 2 * X + k11) - (X ** 3 + X ** 2 - 2 * X + c11)), X)
    s11 = sp.solve(lhs.all_coeffs(), [k11, c11], dict=True)[0]
    A[(2, 11)] = s11[c11]
    A[(2, 12)] = 40 + 12 * R(150, 60)
    # Q13: P^2 = K a^3  -> a = P^(2/3); speed = 2 pi a / P ; P_Y = 8 P_X
    Pn = sp.symbols("Pn", positive=True)
    a_of = lambda P: P ** R(2, 3)
    A[(2, 13)] = sp.simplify((a_of(8 * Pn) / (8 * Pn)) / (a_of(Pn) / Pn))
    # Q14: brute force over sorted 5-tuples of positive integers, mean 14, median 12
    best = 0
    for a1 in range(1, 13):
        for b1 in range(a1, 13):
            for d1 in range(12, 71):
                e1 = 70 - a1 - b1 - 12 - d1
                if e1 >= d1:
                    best = max(best, e1)
    A[(2, 14)] = best
    A[(2, 15)] = sum(1 for kk in range(-200, 201) if kk != 3 and 12 % (kk - 3) == 0)
    # Q16: fit quadratic through three table points, check the 4th, then solve g(x) = 0
    fa, fb, fc = sp.symbols("fa fb fc")
    sf = sp.solve([fa * 0 + fb * 0 + fc + 5, fa + fb + fc + 8, 9 * fa + 3 * fb + fc + 8], [fa, fb, fc], dict=True)[0]
    f16 = lambda v: sf[fa] * v ** 2 + sf[fb] * v + sf[fc]
    assert f16(5) == 0
    r16 = sp.solve(sp.Eq(f16(2 * X - 1) + 8, 0), X)
    A[(2, 16)] = max(r16)
    # Q17: circle x^2+y^2-4x+6y-212=0, P(26,4); tangent points by perpendicularity
    cx, cy = sp.symbols("cx cy")
    eq = X ** 2 + Y ** 2 - 4 * X + 6 * Y - 212
    ctr17 = (2, -3); r17sq = 212 + 4 + 9
    assert sp.expand(eq - ((X - 2) ** 2 + (Y + 3) ** 2 - r17sq)) == 0
    P17 = (26, 4)
    tp = sp.solve([eq, (X - ctr17[0]) * (X - P17[0]) + (Y - ctr17[1]) * (Y - P17[1])], [X, Y], dict=True)
    assert len(tp) == 2
    A[(2, 17)] = sp.sqrt((tp[0][X] - tp[1][X]) ** 2 + (tp[0][Y] - tp[1][Y]) ** 2)
    # Q18: real roots of x^(2/3) - 5 x^(1/3) + 6 = 0 by sign-change scan on cube-root function
    G = lambda xv: cbrt(xv) ** 2 - 5 * cbrt(xv) + 6
    rts, xs = [], [i / 100 for i in range(-100000, 100001)]
    for x0, x1 in zip(xs, xs[1:]):
        if G(x0) == 0: rts.append(round(x0))
        elif G(x0) * G(x1) < 0: rts.append(round((x0 + x1) / 2))
    assert all(abs(G(r)) < 1e-9 for r in rts) and len(rts) == 2, rts
    A[(2, 18)] = sum(rts)
    A[(2, 19)] = sum(1 for xv in range(-200, 201) if abs(xv - 4) + abs(xv - 10) < 10)
    # Q20: l: slope m through (2,5); n perpendicular through (2,5); b_n - b_l = 5, m > 1
    m = sp.symbols("m", real=True, nonzero=True)
    bl = 5 - 2 * m; bn = 5 + 2 / m
    s20 = [v for v in sp.solve(sp.Eq(bn - bl, 5), m) if v > 1]
    assert len(s20) == 1
    A[(2, 20)] = s20[0]
    # Q21: crescents = leg semicircles minus the parts of the big circle that lie inside them
    semis = sp.pi * 4 ** 2 / 2 + sp.pi * 3 ** 2 / 2
    seg = lambda d: 5 ** 2 * sp.acos(R(d, 5)) - d * sp.sqrt(5 ** 2 - d ** 2)   # circular segment at distance d
    A[(2, 21)] = sp.N(semis - seg(3) - seg(4), 30)
    # Q22: integer p such that x^2 - p x + 24 has two integer roots (disc is a perfect square)
    cnt = 0
    for pp in range(-200, 201):
        dsc = pp * pp - 96
        if dsc >= 0 and math.isqrt(dsc) ** 2 == dsc and (pp + math.isqrt(dsc)) % 2 == 0:
            cnt += 1
    A[(2, 22)] = cnt
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
                assert len(q["answer"]) <= 6, "too many characters for a grid-in"
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
