#!/usr/bin/env python3
"""Independent verification of every answer in mock05-problems.md (Mock Test 5, Book 3).

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
MD = os.path.join(HERE, "mock05-problems.md")
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
import random


def _vals(txt):
    return [float(n) for n in re.findall(r"\d+(?:\.\d+)?", txt.replace(",", ""))]


# ---- predicates over the printed text of a choice (for non-numeric choices) -------------
def pred_sd_compare(txt):
    """M1-Q9: compare Set P and Set Q (statement about mean and standard deviation)."""
    import statistics as st
    P, Q = [12, 14, 16, 18, 20], [14, 15, 16, 17, 18]
    mP, mQ, sP, sQ = st.mean(P), st.mean(Q), st.pstdev(P), st.pstdev(Q)
    ok_mean = ("same mean" in txt and mP == mQ) or ("Set $P$ has the greater mean" in txt and mP > mQ) \
        or ("Set $Q$ has the greater mean" in txt and mQ > mP)
    ok_sd = ("Set $P$ has the greater standard deviation" in txt and sP > sQ) \
        or ("Set $Q$ has the greater standard deviation" in txt and sQ > sP) \
        or ("same standard deviation" in txt and abs(sP - sQ) < 1e-12)
    return ok_mean and ok_sd


def pred_solar(txt):
    """M1-Q15: E(t)=5400(0.992)^t.  Is this reading of 0.992 correct?"""
    E = lambda tt: 5400 * 0.992 ** tt
    if "%" in txt:
        pct = _vals(txt)[0]
        return abs(pct - 100 * (1 - 0.992)) < 1e-9          # constant percent decrease per year
    if "kWh" in txt:
        d = _vals(txt)[0]
        drops = [E(t) - E(t + 1) for t in range(0, 10)]
        return all(abs(dd - d) < 1e-9 for dd in drops)       # a constant linear decrease?
    return False


def pred_roots(txt):
    """M1-Q19: equation text -> roots must be exactly {-3/2, 4}."""
    lhs = txt.replace("$", "").split("=")[0]
    poly = tex_to_expr(lhs)
    return set(sp.solve(sp.Eq(poly, 0), x)) == {R(-3, 2), 4} if False else \
        set(sp.roots(sp.Poly(sp.expand(poly), x)).keys()) == {R(-3, 2), 4}


def pred_poly(txt):
    """M2-Q5: degree 2, zeros -3 and 1/2, p(0) = -9."""
    p = tex_to_expr(txt)
    return sp.Poly(p, x).degree() == 2 and p.subs(x, -3) == 0 and p.subs(x, R(1, 2)) == 0 and p.subs(x, 0) == -9


def pred_gardener(txt):
    """M2-Q7: truth set of the printed system must equal {0.6x+0.4y<=12, y>=2x} on a lattice."""
    parts = re.findall(r"\$(.*?)\$", txt)
    assert len(parts) == 2
    fns = []
    for part in parts:
        m = re.match(r"(.*?)\\(le|ge)(.*)$", part)
        lhs, op, rhs = tex_to_expr(m.group(1)), m.group(2), tex_to_expr(m.group(3))
        d = sp.nsimplify(lhs - rhs, rational=True)
        fns.append((d, op))
    for xv in range(0, 41):
        for yv in range(0, 41):
            truth = (R(6, 10) * xv + R(4, 10) * yv <= 12) and (yv >= 2 * xv)
            got = True
            for d, op in fns:
                v = d.subs({x: xv, y: yv})
                got = got and (v <= 0 if op == "le" else v >= 0)
            if got != truth:
                return False
    return True


def pred_add_mean(txt):
    """M2-Q9: 12 values, mean 50, SD 8; a 13th value 50 is added.  Is the claim true for EVERY such data set?"""
    rnd = random.Random(5)
    ok_all = True
    claims = []
    for _ in range(300):
        v = [rnd.uniform(-1, 1) for _ in range(12)]
        mu = sum(v) / 12
        v = [t - mu for t in v]
        for sample in (False, True):
            ss = sum(t * t for t in v)
            sd0 = math.sqrt(ss / (11 if sample else 12))
            data = [50 + 8 * t / sd0 for t in v]
            data2 = data + [50.0]
            n2 = 13
            m2 = sum(data2) / n2
            sd2 = math.sqrt(sum((t - m2) ** 2 for t in data2) / (n2 - 1 if sample else n2))
            claims.append((m2, sd2))
    mean_ok = (("mean is 50" in txt and all(abs(m - 50) < 1e-9 for m, s in claims)) or
               ("mean is less than 50" in txt and all(m < 50 - 1e-9 for m, s in claims)))
    sd_ok = (("less than 8" in txt and all(s < 8 - 1e-9 for m, s in claims)) or
             ("exactly 8" in txt and all(abs(s - 8) < 1e-9 for m, s in claims)) or
             ("greater than 8" in txt and all(s > 8 + 1e-9 for m, s in claims)))
    return mean_ok and sd_ok


def solve_all():
    A = {}
    t = sp.symbols("t")
    a, b, k = sp.symbols("a b k")
    X, Y = sp.symbols("X Y")

    # ================= MODULE 1 =================
    A[(1, 1)] = sp.solve(sp.Eq(11 - 2 * t, -7), t)[0]
    A[(1, 2)] = sp.expand(3 * x * (x - 4) + 5 * x)
    A[(1, 3)] = R(35, 100) * 240
    A[(1, 4)] = 180 - 2 * 54
    # slope of 4x-2y=10: solve for y and read the coefficient of x
    A[(1, 5)] = sp.solve(sp.Eq(3 * (t + 2), 2 * (t + 7)), t)[0]
    pz = lambda v: (v - 3) * (v + 5) * (2 * v - 1)
    A[(1, 6)] = ("pred", lambda txt: pz(tex_to_expr(txt)) == 0)
    A[(1, 7)] = min(n for n in range(0, 500) if 6 * n >= 450)
    A[(1, 8)] = ((lambda v: (v - 2) * (v + 6))(0))
    A[(1, 9)] = ("pred", pred_sd_compare)
    # Q10: integers b with 10 kits (45 each) + 12 b <= 900
    A[(1, 10)] = max(bb for bb in range(0, 200) if 10 * 45 + 12 * bb <= 900)
    s11 = sp.solve([3 * a + 2 * b - 38, 5 * a + 4 * b - 68], [a, b]); A[(1, 11)] = s11[a]
    pp = lambda v: 2 * v ** 3 - 5 * v ** 2 + v - 4
    qq_, rr_ = sp.div(sp.Poly(pp(x), x), sp.Poly(x - 2, x)); A[(1, 12)] = rr_.as_expr()
    vol_cm3 = 300 * 200 * 7; liters = vol_cm3 / 1000          # 3 m x 2 m x 7 cm
    assert liters == 420
    A[(1, 13)] = math.ceil(R(liters) / 40)
    p14 = sp.symbols("p14", positive=True)
    A[(1, 14)] = sp.solve(sp.Eq(p14 * R(12, 10) * R(8, 10), 720), p14)[0]
    A[(1, 15)] = ("pred", pred_solar)
    # Q16: parallel to 3x+4y=20 through (4,1): same left side, new constant
    c16 = 3 * 4 + 4 * 1; A[(1, 16)] = R(c16, 4)
    # Q17: three consecutive odd integers, sum < 90; largest possible smallest integer
    A[(1, 17)] = max(n for n in range(-199, 200, 2) if n + (n + 2) + (n + 4) < 90)
    d18 = sp.expand((3 * x + 2) ** 2 - (3 * x - 2) ** 2); A[(1, 18)] = sp.Poly(d18, x).coeff_monomial(x)
    A[(1, 19)] = ("pred", pred_roots)
    A[(1, 20)] = sum(1 for xv in range(-200, 201) if -2 * (xv - 3) ** 2 + 18 > 0)
    # Q21: frustum by explicit volumes (similar cones, ratio from the heights)
    Rb, Hb, hs = 9, 12, 4
    rs = Rb * R(hs, Hb)
    Vf = R(1, 3) * Rb ** 2 * Hb - R(1, 3) * rs ** 2 * hs; A[(1, 21)] = Vf
    # Q22: hikers; simulate times with exact fractions
    s = sp.symbols("s", positive=True)
    slow = sp.solve(sp.Eq(3 * (s + s + R(3, 2)), 27), s)[0]; fast = slow + R(3, 2)
    d_slow_met = 3 * slow; d_fast_met = 3 * fast
    assert d_slow_met + d_fast_met == 27
    A[(1, 22)] = (27 - d_slow_met) / slow * 60

    # ================= MODULE 2 =================
    A[(2, 1)] = sp.solve(sp.Eq(5 * t - 3, 2 * t + 18), t)[0]
    A[(2, 2)] = (lambda z: z ** 2 - 4 * z + 1)(3)
    A[(2, 3)] = R(300) / (R(120, 60) + R(180, 45))
    k4 = sp.solve(sp.Eq(-k / 6, R(-2, 3)), k)[0]             # slope of kx+6y=30 equals slope of 2x+3y=7
    A[(2, 4)] = sp.solve(sp.Eq(k4 * X, 30), X)[0]
    A[(2, 5)] = ("pred", pred_poly)
    r6 = sp.symbols("r6", positive=True)
    r6v = sp.solve(sp.Eq(sp.pi * r6 ** 2 * 8, 200 * sp.pi), r6)[0]
    A[(2, 6)] = 2 * sp.pi * r6v ** 2 + 2 * sp.pi * r6v * 8
    A[(2, 7)] = ("pred", pred_gardener)
    A[(2, 8)] = sp.solve(sp.Eq(2 ** (t + 1) * 4 ** (t - 2), 64), t)[0]
    A[(2, 9)] = ("pred", pred_add_mean)
    # Q10: system y = 2x+7, 4x-2y = k.  Substitute; infinitely many <=> residual identically 0 in x
    resid = sp.expand(4 * X - 2 * (2 * X + 7) - k)
    A[(2, 10)] = sp.solve(sp.Poly(resid, X).all_coeffs(), k)[k] if isinstance(sp.solve(sp.Poly(resid, X).all_coeffs(), k), dict) \
        else sp.solve(resid.subs(X, 0), k)[0]
    # Q11: f(4)=9; g(x)=2 f(x-1) - 5 ; the image of (4,9) has x-1 = 4
    f_at = {4: 9}
    a11 = 4 + 1; b11 = 2 * f_at[a11 - 1] - 5; A[(2, 11)] = a11 + b11
    A[(2, 12)] = sum(1 for xv in range(-100, 101) if 3 * xv - 7 > 8 and 2 * xv + 5 <= 31)
    # Q13: shipping with rounding up
    def cost(w, d):
        w = R(w)
        return 9 if w <= 1 else 9 + d * math.ceil(w - 1)
    d13 = [dd for dd in range(1, 40) if cost(R("6.5"), dd) == 39]
    assert len(d13) == 1
    A[(2, 13)] = cost(R("12.2"), d13[0])
    # Q14: coordinates of the triangle, incircle, tangency point on BC
    B_, C_, A_ = sp.Matrix([0, 0]), sp.Matrix([14, 0]), sp.Matrix([5, 12])
    assert (A_ - B_).norm() == 13 and (A_ - C_).norm() == 15
    a_, b_, c_ = 14, 15, 13                                   # a=BC, b=CA, c=AB
    inc = (a_ * A_ + b_ * B_ + c_ * C_) / (a_ + b_ + c_)
    area = R(1, 2) * 14 * 12; rin = area / R(a_ + b_ + c_, 2)
    assert inc[1] == rin
    A[(2, 14)] = max(inc[0], 14 - inc[0])
    # Q15: sqrt(x+7) + sqrt(x-1) = 4, solve and verify
    sols = [v for v in sp.solve(sp.Eq(sp.sqrt(t + 7) + sp.sqrt(t - 1), 4), t) if abs(sp.N(sp.sqrt(v + 7) + sp.sqrt(v - 1) - 4)) < 1e-12]
    assert len(sols) == 1
    A[(2, 15)] = sp.simplify(sp.sqrt(sols[0] + 7) - sp.sqrt(sols[0] - 1))
    # Q16: band/chorus
    total, band, chorus, neither = 240, 150, 110, 40
    both = band + chorus - (total - neither)
    only_band, only_chorus = band - both, chorus - both
    assert both > 0 and only_band > 0 and only_chorus > 0
    A[(2, 16)] = R(only_band, only_band + only_chorus)
    # Q17: garden bed, area 11, length = width + 6 -> perimeter
    L17 = sp.symbols("L17", positive=True)
    l17 = [v for v in sp.solve(sp.Eq(L17 * (L17 - 6), 11), L17)]
    assert len(l17) == 1
    A[(2, 17)] = sp.simplify(2 * (l17[0] + (l17[0] - 6)))
    # Q18: positive intercepts, x-int = 2*(y-int), through (6,4)
    b18 = sp.symbols("b18", positive=True)
    s18 = sp.solve(sp.Eq(6 / (2 * b18) + 4 / b18, 1), b18); assert len(s18) == 1; A[(2, 18)] = s18[0]
    # Q19: intersection points of y = x^2 - 3 and x^2 + y^2 = 9 ; sum of y over all points
    pts = sp.solve([Y - (X ** 2 - 3), X ** 2 + Y ** 2 - 9], [X, Y], dict=True)
    pts = {(sp.simplify(p[X]), sp.simplify(p[Y])) for p in pts}
    assert len(pts) == 3, pts
    A[(2, 19)] = sum(p[1] for p in pts)
    # Q20: |x-3| = 2|x+1|, solve by squaring and keeping exact roots; verify
    r20 = sp.solve(sp.Eq((t - 3) ** 2, 4 * (t + 1) ** 2), t)
    assert all(abs(r - 3) == 2 * abs(r + 1) for r in r20) and len(r20) == 2
    A[(2, 20)] = sum(r20)
    # Q21: chords in a circle of radius 25 (coordinates), centre between them
    Rr = 25
    h1 = sp.sqrt(Rr ** 2 - 7 ** 2); h2 = sp.sqrt(Rr ** 2 - 20 ** 2)
    A[(2, 21)] = h1 + h2
    # Q22: remainder of degree <=1 modulo (x-2)(x+3), given p(2)=5 and p(-3)=-15
    a22, b22 = sp.symbols("a22 b22")
    s22 = sp.solve([2 * a22 + b22 - 5, -3 * a22 + b22 + 15], [a22, b22])
    # concrete check with an actual polynomial having those remainders
    pexample = sp.expand((x - 2) * (x + 3) * (x ** 2 + 1) + s22[a22] * x + s22[b22])
    assert sp.rem(pexample, x - 2, x) == 5 and sp.rem(pexample, x + 3, x) == -15
    assert sp.rem(pexample, x ** 2 + x - 6, x) == s22[a22] * x + s22[b22]
    A[(2, 22)] = s22[b22]
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
