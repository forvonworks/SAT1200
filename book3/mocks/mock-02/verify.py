#!/usr/bin/env python3
"""Independent verification of every answer in mock02-problems.md (Mock Test 2, Book 3).

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
MD = os.path.join(HERE, "mock02-problems.md")
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
    s = s.replace("\\pi", "pi")
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
def solve_all():
    A = {}
    t = sp.symbols("t")
    a, b = sp.symbols("a b")

    # ================= MODULE 1 =================
    A[(1, 1)] = sp.solve(sp.Eq(6 * a + 5, 41), a)[0]
    A[(1, 2)] = (lambda g: g(3))(lambda v: 5 * 2 ** v)
    A[(1, 3)] = R(36, 100) * 250
    s4 = sp.solve(sp.Eq(5 * a + (a + 30), 180), a)[0]
    A[(1, 4)] = max(5 * s4, s4 + 30)
    A[(1, 5)] = sp.solve(sp.Eq(4 + R(5, 2) * a, 29), a)[0]
    A[(1, 6)] = sp.expand((2 * x + 3) * (x - 5))
    A[(1, 7)] = sp.solve(sp.Eq(3 * a + 4 * 0, 24), a)[0]                       # y = 0
    A[(1, 8)] = min((v - 4) ** 2 + 9 for v in [R(n, 4) for n in range(-80, 81)])
    A[(1, 9)] = R(36, 150) * 2500
    # Q10: V=420-56t.  Truth of each printed interpretation computed from the model
    V = lambda tt: 420 - 56 * tt
    A[(1, 10)] = "interp"
    s11 = sp.solve([2 * a + b - 11, a - 3 * b + 12], [a, b]); A[(1, 11)] = s11[a] * s11[b]
    bb = sp.symbols("bb")
    bv = sp.solve(sp.Eq(3 ** 2 + 3 * bb + 12, 0), bb)[0]
    A[(1, 12)] = (-1) ** 2 + bv * (-1) + 12
    A[(1, 13)] = sp.pi * (sp.sqrt((5 + 1) ** 2 + (10 - 2) ** 2) / 2) ** 2
    cnt = {0: 3, 1: 5, 2: 6, 3: 4, 4: 2}
    assert sum(cnt.values()) == 20
    A[(1, 14)] = R(sum(k * v for k, v in cnt.items()), sum(cnt.values()))
    A1, B1 = 2 * x ** 2 - 3 * x + 1, x ** 2 + 4 * x - 5
    A[(1, 15)] = sp.expand(A1 - 2 * B1)
    xx, yy = sp.symbols("xx yy")
    s16 = sp.solve([xx + yy - 50, xx / 20 + yy / 15 - R(11, 4)], [xx, yy]); A[(1, 16)] = s16[xx]
    A[(1, 17)] = sp.solve(sp.Eq(R(2, 3) * (t - 6), (t + 2) / 2), t)[0]
    hs = sp.solve(sp.Eq(-5 * t ** 2 + 20 * t + 60, 0), t)
    A[(1, 18)] = [r for r in hs if r > 0][0]
    kk = sp.symbols("kk")
    A[(1, 19)] = sp.solve(sp.Eq((2 ** 3) - 5 * 2 ** 2 + kk * 2 + 6, 0), kk)[0]
    # Q20 boat
    v = sp.symbols("v", positive=True)
    v20 = sp.solve(sp.Eq(24 / (v - 2) + 24 / (v + 2), 5), v)
    assert len(v20) == 1
    A[(1, 20)] = v20[0] + 2
    # Q21 altitude to hypotenuse: coordinates check, then area
    Ap, Bp, Dp = sp.Matrix([0, 0]), sp.Matrix([13, 0]), sp.Matrix([4, 0])
    cy = sp.symbols("cy", positive=True)
    Cp = sp.Matrix([4, cy])
    cy_v = sp.solve(sp.Eq((Ap - Cp).dot(Bp - Cp), 0), cy)[0]          # right angle at C
    A[(1, 21)] = R(1, 2) * 13 * cy_v
    # Q22 lines
    X, Y = sp.symbols("X Y")
    m_slope = R(9 - 0, 5 - 2)
    sol22 = sp.solve([2 * X + Y - 14, Y - m_slope * (X - 2)], [X, Y])
    xint_l = sp.solve(sp.Eq(14 - 2 * X, 0), X)[0]
    xint_m = 2
    A[(1, 22)] = R(1, 2) * abs(xint_l - xint_m) * sol22[Y]

    # ================= MODULE 2 =================
    A[(2, 1)] = sp.solve(sp.Eq(R(2, 5) * t, 14), t)[0]
    A[(2, 2)] = sp.solve(sp.Eq(3 ** (t + 1), 81), t)[0]
    A[(2, 3)] = R(R("3.2") * R("4.5"), 72) * 60
    sl = R(49 - 70, 10 - 4); A[(2, 4)] = 70 + sl * (0 - 4)
    A[(2, 5)] = sp.Integer(36) ** R(3, 2)
    A[(2, 6)] = "pairs"
    A[(2, 7)] = R(80, 360) * sp.pi * 15 ** 2
    h8, k8 = sp.symbols("h8 k8")
    e8 = sp.Poly(sp.expand((t - h8) ** 2 + k8 - (t ** 2 - 12 * t + 40)), t).all_coeffs()
    s8 = sp.solve(e8, [h8, k8], dict=True)[0]; A[(2, 8)] = s8[h8] + s8[k8]
    A[(2, 9)] = "transform"
    AA, BB, CC = sp.symbols("AA BB CC")
    s10 = sp.solve([AA + BB - 26, BB + CC - 31, AA + CC - 33], [AA, BB, CC]); A[(2, 10)] = s10[BB]
    f11 = lambda z: 4 * 3 ** z
    kk11 = sp.simplify(f11(x + 2) / f11(x)); A[(2, 11)] = kk11
    A[(2, 12)] = R(54 * R(3, 2), 90 - 54)
    # Q13: solve for base, per-mile, per-minute from the 3 table rows, price the new trip
    bs, pm, pt = sp.symbols("bs pm pt")
    s13 = sp.solve([bs + 6 * pm + 15 * pt - R("16.15"), bs + 10 * pm + 15 * pt - R("21.75"),
                    bs + 6 * pm + 25 * pt - R("19.65")], [bs, pm, pt])
    A[(2, 13)] = s13[bs] + 14 * s13[pm] + 30 * s13[pt]
    # Q14: brute force
    bal = lambda yrs: (1 + R(9, 400)) ** (4 * yrs)
    A[(2, 14)] = min(yrs for yrs in range(1, 60) if bal(yrs) > 2)
    assert min(yrs for yrs in range(1, 60) if (1 + R(9, 100)) ** yrs > 2) == 9      # annual-compounding trap
    # Q15: circle centre (4,k), tangent to x-axis => r = k ; passes through (10,9)
    k15 = sp.symbols("k15", positive=True)
    k15v = sp.solve(sp.Eq((10 - 4) ** 2 + (9 - k15) ** 2, k15 ** 2), k15)
    assert len(k15v) == 1
    A[(2, 15)] = k15v[0] + k15v[0]
    # Q16
    p16, h16 = sp.symbols("p16 h16", positive=True)
    pay = lambda rate, hrs: 40 * rate + 1.5 * rate * (hrs - 40) if hrs > 40 else rate * hrs
    p0 = sp.solve(sp.Eq(40 * p16 + R(3, 2) * p16 * 6, 1176), p16)[0]
    p1 = p0 * R(11, 10)
    h_v = sp.solve(sp.Eq(40 * p1 + R(3, 2) * p1 * (h16 - 40), 1452), h16)[0]
    A[(2, 16)] = h_v
    # Q17: p = percent of cyclists injured
    pp = sp.symbols("pp")
    run, swim, cyc = 500 * R(40, 100), 500 * R(35, 100), 500 - 500 * R(75, 100)
    inj = lambda pc: (run * R(30, 100), swim * R(20, 100), cyc * pc / 100)
    s17 = sp.solve(sp.Eq(run * R(30, 100) / sum(inj(pp)), R(40, 100)), pp)
    assert len(s17) == 1
    A[(2, 17)] = s17[0]
    # Q18: brute force over integers k, verify the intersection lies in quadrant I
    cnt18 = 0
    for kv in range(-200, 201):
        xs = R(10 - kv, 5); ys = 3 * xs + kv
        assert 2 * xs + ys == 10
        if xs > 0 and ys > 0:
            cnt18 += 1
    A[(2, 18)] = cnt18
    # Q19: rational equation with extraneous root check
    sols19 = sp.solve(sp.Eq(t * (t + 2) + 3 * (t - 3), 15), t)
    good19 = [s for s in sols19 if s != 3 and s != -2]
    assert len(good19) == 1 and set(sols19) == {3, -8}
    A[(2, 19)] = good19[0]
    # Q20: real solutions of (x^2-4x)^2 + 2(x^2-4x) = 35
    roots20 = sp.solve(sp.Eq((t ** 2 - 4 * t) ** 2 + 2 * (t ** 2 - 4 * t), 35), t)
    real20 = [r for r in roots20 if sp.im(sp.N(r)) == 0]
    assert len(roots20) == 4 and len(real20) == 2
    A[(2, 20)] = sum(r ** 2 for r in real20)
    # Q21: square in right triangle, legs 24 and 8 (similar triangles), shaded = triangle - square
    s21 = sp.symbols("s21", positive=True)
    sv = sp.solve(sp.Eq(s21 / 24, (8 - s21) / 8), s21)[0]
    assert sp.Eq(8 - R(8, 24) * sv, sv)            # square's far corner lies on the hypotenuse
    A[(2, 21)] = R(1, 2) * 24 * 8 - sv ** 2
    # Q22: tangency <=> discriminant 0
    k22 = sp.symbols("k22")
    disc = sp.discriminant(t ** 2 + 3 * t + 4 - (k22 * t - 5), t)
    ks = sp.solve(disc, k22)
    assert len(ks) == 2
    A[(2, 22)] = ks[0] * ks[1]
    return A


# ------------------------------------------------------------ text-choice predicates
def interp_true(text):
    """M1-Q10: V=420-56t.  Is this verbal interpretation of (5,140) correct?"""
    V = lambda tt: 420 - 56 * tt
    nums = [int(n) for n in re.findall(r"\d+", text.replace(",", ""))]
    if text.startswith("After") and "holds" in text:
        return V(nums[0]) == nums[1]
    if text.startswith("After") and "drained" in text:
        return 420 - V(nums[0]) == nums[1]
    if text.startswith("During the fifth hour"):
        return V(4) - V(5) == nums[0] if len(nums) == 1 else False
    return False


def pair_true(text):
    j, s = [int(n) for n in re.findall(r"\d+", text)]
    return 28 * j + 15 * s <= 400 and j + s >= 18 and j >= 10


def transform_true(text):
    med, sd = [int(n) for n in re.findall(r"\d+", text)]
    return med == 2 * 38 - 10 and sd == 2 * 6


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
                    if val == "interp":
                        match = interp_true(txt)
                    elif val == "pairs":
                        match = pair_true(txt)
                    elif val == "transform":
                        match = transform_true(txt)
                    else:
                        c = tex_to_expr(txt)
                        match = same(c, val)
                    if match:
                        hits.append(L)
                assert len(hits) == 1, f"{len(hits)} choices match computed value {val}: {hits}"
                assert hits[0] == q["answer"], f"computed letter {hits[0]} != keyed {q['answer']}"
                letters[key[0]].append(hits[0])
                msg = f"answer {q['answer']}  (value {val if isinstance(val, str) else sp.N(val, 6)})"
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
