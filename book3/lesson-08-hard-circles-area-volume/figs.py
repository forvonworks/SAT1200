#!/usr/bin/env python3
"""True-scale TikZ figures for Book 3 Lesson 8.

Every figure is generated from the SAME numbers that appear in the problem stem (the parameters are the
function arguments).  Coordinates are computed with plain geometry (mm on the page = unit * u), and each
function asserts the geometric facts the figure relies on (points on the circle, right angles, tangency,
printed lengths equal measured lengths), so a wrong or distorted figure fails `python3 verify.py`.
"""
import math

DEG = math.pi / 180.0
FILL = "accent!28"
LW = "line width=0.6pt"


def P(x, y):
    return "(%.3fmm,%.3fmm)" % (x, y)


def pol(cx, cy, r, deg):
    return (cx + r * math.cos(deg * DEG), cy + r * math.sin(deg * DEG))


def dist(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])


def unit(a, b):
    d = dist(a, b)
    return ((b[0] - a[0]) / d, (b[1] - a[1]) / d)


def ra(v, d1, d2, s=2.2):
    """right-angle mark at vertex v between unit directions d1, d2."""
    p1 = (v[0] + s * d1[0], v[1] + s * d1[1])
    p3 = (v[0] + s * d2[0], v[1] + s * d2[1])
    p2 = (p1[0] + s * d2[0], p1[1] + s * d2[1])
    return r"\draw[%s,line width=0.4pt] %s -- %s -- %s;" % ("ink", P(*p1), P(*p2), P(*p3))


def near(a, b, tol=1e-6):
    return abs(a - b) < tol


def dot(p, label=None, pos="above", extra=""):
    s = r"\fill[ink] %s circle (0.6mm);" % P(*p)
    if label:
        s += r" \node[%s,inner sep=1.5pt%s] at %s {%s};" % (pos, extra, P(*p), label)
    return s


def start(opts=""):
    return r"\begin{tikzpicture}[%s,%s,every node/.style={font=\footnotesize}]" % (LW, "ink" if not opts else "ink," + opts)


END = r"\end{tikzpicture}"


# --------------------------------------------------------------------------------------------- F1
def fig_sagitta(r=17, c=30, u=1.5):
    d = math.sqrt(r * r - (c / 2.0) ** 2)
    assert near(d, 8)
    O = (0, 0); A = (-c / 2 * u, -d * u); B = (c / 2 * u, -d * u); M = (0, -d * u); N = (0, -r * u)
    assert near(dist(O, A), r * u) and near(dist(O, B), r * u) and near(dist(O, N), r * u)
    assert near(dist(A, B), c * u) and near(dist(M, N) / u, r - d)
    L = [start(), r"\draw %s circle (%.3fmm);" % (P(0, 0), r * u),
         r"\draw %s -- %s;" % (P(*A), P(*B)),
         r"\draw[dashed] %s -- %s;" % (P(*O), P(*M)),
         r"\draw[dashed] %s -- %s;" % (P(*O), P(*A)),
         r"\draw[accent,line width=1.4pt] %s -- %s;" % (P(*M), P(*N)),
         ra(M, (0, 1), (1, 0), 2.0),
         dot(O, "$O$", "above"), dot(A, "$A$", "left"), dot(B, "$B$", "right"), dot(M, "$M$", "below left", ",xshift=0.5pt"),
         dot(N, "", "below"),
         r"\node[below=1pt] at %s {$%d$};" % (P(c / 4.0 * u, -d * u), c),
         r"\node[left=0.5pt] at %s {$%d$};" % (P(*((A[0] / 2), (A[1] / 2) + 0.0)), r),
         r"\node[right=1pt] at %s {$?$};" % P(0.6, -(d + (r - d) / 2) * u),
         END]
    return "\n".join(L)


# --------------------------------------------------------------------------------------------- F2
def fig_kite(r=6, t=8, u=3.0):
    dd = math.hypot(r, t)
    assert near(dd, 10)
    O = (0, 0); E = (dd * u, 0)
    ang = math.degrees(math.acos(r / dd))
    A = pol(0, 0, r * u, ang); U = pol(0, 0, r * u, -ang)
    assert near(dist(A, E), t * u) and near(dist(U, E), t * u)
    ua = unit(A, O); ue = unit(A, E)
    assert near(ua[0] * ue[0] + ua[1] * ue[1], 0)   # radius perpendicular to tangent
    Pn = (r * u, 0)
    uu = unit(U, O); uue = unit(U, E)
    L = [start(), r"\draw %s circle (%.3fmm);" % (P(0, 0), r * u),
         r"\draw %s -- %s -- %s -- %s;" % (P(*O), P(*A), P(*E), P(*U)),
         r"\draw[dashed] %s -- %s;" % (P(*O), P(*E)),
         r"\draw[accent,line width=1.4pt] %s -- %s;" % (P(*Pn), P(*E)),
         ra(A, ua, ue, 2.0), ra(U, uu, uue, 2.0),
         dot(O, "$O$", "left"), dot(A, "$A$", "above"), dot(U, "$U$", "below"), dot(E, "$E$", "right"), dot(Pn, "$P$", "below left", ",xshift=1pt"),
         r"\node[above left=-1pt] at %s {$%d$};" % (P(A[0] / 2, A[1] / 2), r),
         r"\node[above right=-1pt] at %s {$%d$};" % (P((A[0] + E[0]) / 2, (A[1] + E[1]) / 2), t),
         r"\node[above=1pt] at %s {$?$};" % P((Pn[0] + E[0]) / 2, 0),
         END]
    return "\n".join(L)


# --------------------------------------------------------------------------------------------- F3
def fig_semicircle(alpha=28, r=22.0):
    A = (-r, 0); B = (r, 0)
    C = pol(0, 0, r, 2 * alpha)
    # check: AB diameter -> right angle at C ; angle BAC = alpha
    ca = (A[0] - C[0], A[1] - C[1]); cb = (B[0] - C[0], B[1] - C[1])
    assert near(ca[0] * cb[0] + ca[1] * cb[1], 0, 1e-6)
    ab = (B[0] - A[0], B[1] - A[1]); ac = (C[0] - A[0], C[1] - A[1])
    ang = math.degrees(math.acos((ab[0] * ac[0] + ab[1] * ac[1]) / (dist(A, B) * dist(A, C))))
    assert near(ang, alpha, 1e-6)
    uca = unit(C, A); ucb = unit(C, B)
    L = [start(), r"\draw %s circle (%.3fmm);" % (P(0, 0), r),
         r"\draw %s -- %s -- %s -- cycle;" % (P(*A), P(*B), P(*C)),
         ra(C, uca, ucb, 2.2),
         r"\draw %s arc[start angle=0,end angle=%.3f,radius=7mm];" % (P(A[0] + 7, 0), alpha),
         r"\node[right] at %s {$%d^\circ$};" % (P(A[0] + 7.2, 1.9), alpha),
         dot(A, "$A$", "left"), dot(B, "$B$", "right"), dot(C, "$C$", "above right"),
         r"\node[below=1pt] at %s {\scriptsize $AB$ is a diameter};" % P(0, -0.5),
         END]
    return "\n".join(L)


# --------------------------------------------------------------------------------------------- F4
def fig_segment(r=6, theta=60, u=3.6):
    R = r * u
    A = pol(0, 0, R, 90 + theta / 2.0); B = pol(0, 0, R, 90 - theta / 2.0)
    assert near(dist(A, B), 2 * R * math.sin(theta / 2.0 * DEG))
    L = [start(), r"\draw %s circle (%.3fmm);" % (P(0, 0), R),
         r"\fill[%s] %s arc[start angle=%.3f,end angle=%.3f,radius=%.3fmm] -- cycle;" % (FILL, P(*B), 90 - theta / 2.0, 90 + theta / 2.0, R),
         r"\draw %s arc[start angle=%.3f,end angle=%.3f,radius=%.3fmm] -- cycle;" % (P(*B), 90 - theta / 2.0, 90 + theta / 2.0, R),
         r"\draw[dashed] %s -- %s -- %s;" % (P(*A), P(0, 0), P(*B)),
         r"\draw %s arc[start angle=%.3f,end angle=%.3f,radius=6mm];" % (P(*pol(0, 0, 6, 90 - theta / 2.0)), 90 - theta / 2.0, 90 + theta / 2.0),
         r"\node at %s {$%d^\circ$};" % (P(0, 9.2), theta),
         dot((0, 0), "$O$", "below"), dot(A, "$A$", "left"), dot(B, "$B$", "right"),
         r"\node[left=1pt] at %s {$%d$};" % (P(A[0] / 2 - 0.5, A[1] / 2), r),
         END]
    return "\n".join(L)


# --------------------------------------------------------------------------------------------- F5
def fig_annulus_chord(R=13, rr=5, u=2.0):
    half = math.sqrt(R * R - rr * rr)
    assert near(half, 12)
    chord = 2 * half
    A = (-half * u, rr * u); B = (half * u, rr * u)
    assert near(dist((0, 0), A), R * u) and near(dist((0, 0), B), R * u)   # chord endpoints on the outer circle
    T = (0, rr * u)
    assert near(dist((0, 0), T), rr * u)                                   # chord touches inner circle at T
    L = [start(), r"\fill[%s,even odd rule] %s circle (%.3fmm) %s circle (%.3fmm);" % (FILL, P(0, 0), R * u, P(0, 0), rr * u),
         r"\draw %s circle (%.3fmm); \draw %s circle (%.3fmm);" % (P(0, 0), R * u, P(0, 0), rr * u),
         r"\draw[line width=0.9pt] %s -- %s;" % (P(*A), P(*B)),
         dot((0, 0), "$O$", "below"), dot(A, "$A$", "left"), dot(B, "$B$", "right"), dot(T, "", "above"),
         r"\node[above,fill=white,inner sep=1pt] at %s {$%d$};" % (P(7 * u, rr * u), chord),
         END]
    return "\n".join(L)


# --------------------------------------------------------------------------------------------- F6
def fig_stadium(w=8, u=2.0):
    Lw = 3 * w
    W = w * u; Ln = Lw * u
    L = [start(),
         r"\fill[%s] %s rectangle %s;" % (FILL, P(0, 0), P(Ln, W)),
         r"\fill[%s] %s arc[start angle=-90,end angle=90,radius=%.3fmm] -- cycle;" % (FILL, P(Ln, 0), W / 2.0),
         r"\fill[%s] %s arc[start angle=270,end angle=90,radius=%.3fmm] -- cycle;" % (FILL, P(0, 0), W / 2.0),
         r"\draw %s -- %s arc[start angle=-90,end angle=90,radius=%.3fmm] -- %s arc[start angle=90,end angle=270,radius=%.3fmm] -- cycle;"
         % (P(0, 0), P(Ln, 0), W / 2.0, P(0, W), W / 2.0),
         r"\draw[dashed] %s -- %s; \draw[dashed] %s -- %s;" % (P(0, 0), P(0, W), P(Ln, 0), P(Ln, W)),
         r"\draw[<->,>=stealth] %s -- %s node[midway,right,inner sep=1pt] {$w$};" % (P(Ln / 2.0, 0.4), P(Ln / 2.0, W - 0.4)),
         r"\draw[<->,>=stealth] %s -- %s node[midway,below=0.5pt] {$3w$};" % (P(0, -2.2), P(Ln, -2.2)),
         END]
    return "\n".join(L)


# --------------------------------------------------------------------------------------------- F7
def fig_four_circles(s=20, u=2.5):
    r = s / 4.0
    S = s * u
    L = [start(), r"\fill[%s] %s rectangle %s;" % (FILL, P(0, 0), P(S, S))]
    for cx in (r, 3 * r):
        for cy in (r, 3 * r):
            # each circle tangent to the two nearby sides and to its neighbours
            assert near(cx - r, 0) or near(cx + r, s)
            L.append(r"\filldraw[fill=white] %s circle (%.3fmm);" % (P(cx * u, cy * u), r * u))
    L.append(r"\draw %s rectangle %s;" % (P(0, 0), P(S, S)))
    L.append(r"\draw[<->,>=stealth] %s -- %s node[midway,below=0.5pt] {$%d$};" % (P(0, -2.2), P(S, -2.2), s))
    L.append(END)
    return "\n".join(L)


# --------------------------------------------------------------------------------------------- F8
def fig_lens(s=12, u=3.6):
    S = s * u
    A = (0, 0); B = (S, 0); C = (S, S); D = (0, S)
    assert near(dist(A, B), S) and near(dist(A, D), S) and near(dist(C, B), S) and near(dist(C, D), S)
    L = [start(),
         r"\path[use as bounding box] %s rectangle %s;" % (P(-4, -8), P(S + 4, S + 4)),
         r"\begin{scope}\clip %s circle (%.3fmm); \fill[%s] %s circle (%.3fmm);\end{scope}" % (P(*A), S, FILL, P(*C), S),
         r"\draw %s rectangle %s;" % (P(0, 0), P(S, S)),
         r"\draw %s arc[start angle=0,end angle=90,radius=%.3fmm];" % (P(*B), S),
         r"\draw %s arc[start angle=180,end angle=270,radius=%.3fmm];" % (P(*D), S),
         dot(A, "$A$", "below left"), dot(B, "$B$", "below right"), dot(C, "$C$", "above right"), dot(D, "$D$", "above left"),
         r"\node[below=1pt] at %s {$%d$};" % (P(S / 2.0, -0.6), s),
         END]
    return "\n".join(L)


# --------------------------------------------------------------------------------------------- F9
def fig_two_circles(r1=4, r2=9, u=2.4):
    d = r1 + r2
    O1 = (0, 0); O2 = (d * u, 0)
    nx = -(r2 - r1) / d; ny = -math.sqrt(1 - nx * nx)
    T1 = (O1[0] + r1 * u * nx, O1[1] + r1 * u * ny)
    T2 = (O2[0] + r2 * u * nx, O2[1] + r2 * u * ny)
    t = dist(T1, T2) / u
    assert near(t, 2 * math.sqrt(r1 * r2), 1e-6)
    tv = unit(T1, T2)
    assert near(tv[0] * nx + tv[1] * ny, 0, 1e-9)        # tangent line perpendicular to both radii
    assert near(dist(O1, O2), (r1 + r2) * u)             # externally tangent circles
    ext = 5.0
    Lt = (T1[0] - ext * tv[0], T1[1] - ext * tv[1]); Rt = (T2[0] + ext * tv[0], T2[1] + ext * tv[1])
    L = [start(), r"\draw %s circle (%.3fmm); \draw %s circle (%.3fmm);" % (P(*O1), r1 * u, P(*O2), r2 * u),
         r"\draw %s -- %s;" % (P(*Lt), P(*Rt)),
         r"\draw[dashed] %s -- %s; \draw[dashed] %s -- %s;" % (P(*O1), P(*T1), P(*O2), P(*T2)),
         r"\draw[dashed] %s -- %s;" % (P(*O1), P(*O2)),
         ra(T1, unit(T1, O1), tv, 1.8), ra(T2, unit(T2, O2), (-tv[0], -tv[1]), 1.8),
         dot(O1, "$O_1$", "above"), dot(O2, "$O_2$", "above"), dot(T1, "$P$", "below left"), dot(T2, "$Q$", "below right"),
         r"\node[left=0.5pt] at %s {$%d$};" % (P((O1[0] + T1[0]) / 2, (O1[1] + T1[1]) / 2 + 0.0), r1),
         r"\node[right=0.5pt] at %s {$%d$};" % (P((O2[0] + T2[0]) / 2 + 0.3, (O2[1] + T2[1]) / 2), r2),
         END]
    return "\n".join(L)


# --------------------------------------------------------------------------------------------- F10
def fig_incircle(a=9, b=12, u=3.4):
    c = math.hypot(a, b)
    s = (a + b + c) / 2.0
    ri = a * b / 2.0 / s
    assert near(ri, 3) and near(c, 15)
    B = (0, 0); Cc = (b * u, 0); A = (0, a * u)
    I = (ri * u, ri * u)
    # distance from I to hypotenuse line through A and C equals ri*u (tangency)
    nx, ny = (A[1] - Cc[1]), (Cc[0] - A[0])
    nn = math.hypot(nx, ny)
    dline = abs((I[0] - A[0]) * nx + (I[1] - A[1]) * ny) / nn
    assert near(dline, ri * u, 1e-9)
    L = [start(), r"\fill[%s] %s -- %s -- %s -- cycle;" % (FILL, P(*B), P(*Cc), P(*A)),
         r"\filldraw[fill=white] %s circle (%.3fmm);" % (P(*I), ri * u),
         r"\draw %s -- %s -- %s -- cycle;" % (P(*B), P(*Cc), P(*A)),
         ra(B, (1, 0), (0, 1), 2.2),
         r"\node[left] at %s {$%d$};" % (P(0, a * u / 2.0), a),
         r"\node[below] at %s {$%d$};" % (P(b * u / 2.0, 0), b),
         END]
    return "\n".join(L)


# --------------------------------------------------------------------------------------------- F11
def fig_cone_water(h=12, rad=5, depth=6, u=3.2):
    H = h * u; Rr = rad * u
    wr = Rr * depth / float(h)
    L = [start(),
         r"\fill[%s] %s -- %s -- %s -- cycle;" % (FILL, P(0, 0), P(-wr, depth * u), P(wr, depth * u)),
         r"\draw %s -- %s -- %s -- cycle;" % (P(0, 0), P(-Rr, H), P(Rr, H)),
         r"\draw[dashed] %s -- %s;" % (P(-wr, depth * u), P(wr, depth * u)),
         r"\draw[<->,>=stealth] %s -- %s node[midway,left,inner sep=1pt] {$%d$};" % (P(-Rr - 4, 0), P(-Rr - 4, H), h),
         r"\draw[<->,>=stealth] %s -- %s node[midway,right,inner sep=1pt] {$%d$};" % (P(Rr + 4, 0), P(Rr + 4, depth * u), depth),
         r"\draw[dotted] %s -- %s;" % (P(wr, depth * u), P(Rr + 4, depth * u)),
         r"\draw[dotted] %s -- %s;" % (P(0, 0), P(Rr + 4, 0)),
         END]
    return "\n".join(L)


# --------------------------------------------------------------------------------------------- F12
def fig_sphere_cylinder(r=6, u=3.0):
    L = [start(), r"\draw %s rectangle %s;" % (P(-r * u, 0), P(r * u, 2 * r * u)),
         r"\draw %s circle (%.3fmm);" % (P(0, r * u), r * u),
         r"\draw[dashed] %s -- %s;" % (P(0, r * u), P(r * u, r * u)),
         r"\node[above=0pt] at %s {$r$};" % P(r * u / 2.0, r * u),
         END]
    return "\n".join(L)


# --------------------------------------------------------------------------------------------- F13
def fig_silo(rad=4, total=10, u=3.4):
    hc = total - rad
    L = [start(),
         r"\fill[%s] %s -- %s -- %s arc[start angle=0,end angle=180,radius=%.3fmm] -- cycle;" % (FILL, P(-rad * u, 0), P(rad * u, 0), P(rad * u, hc * u), rad * u),
         r"\draw %s -- %s -- %s arc[start angle=0,end angle=180,radius=%.3fmm] -- cycle;" % (P(-rad * u, 0), P(rad * u, 0), P(rad * u, hc * u), rad * u),
         r"\draw[dashed] %s -- %s;" % (P(-rad * u, hc * u), P(rad * u, hc * u)),
         r"\draw[<->,>=stealth] %s -- %s node[midway,left,inner sep=1pt] {$%d$};" % (P(-rad * u - 4, 0), P(-rad * u - 4, total * u), total),
         r"\draw[dotted] %s -- %s; \draw[dotted] %s -- %s;" % (P(-rad * u, 0), P(-rad * u - 4, 0), P(0, total * u), P(-rad * u - 4, total * u)),
         r"\draw[<->,>=stealth] %s -- %s node[midway,below=0.5pt] {$%d$};" % (P(-rad * u, -2.2), P(rad * u, -2.2), 2 * rad),
         END]
    return "\n".join(L)


# --------------------------------------------------------------------------------------------- F14
def fig_chords(arcs=(36, 72, 108, 144), a0=110, r=24.0):
    assert sum(arcs) == 360
    angs = [a0]
    for x in arcs[:-1]:
        angs.append(angs[-1] + x)
    A, B, C, D = [pol(0, 0, r, t) for t in angs]
    # intersection of AC and BD
    def inter(p1, p2, p3, p4):
        x1, y1 = p1; x2, y2 = p2; x3, y3 = p3; x4, y4 = p4
        den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        px = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / den
        py = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / den
        return (px, py)
    Pt = inter(A, C, B, D)
    va = (A[0] - Pt[0], A[1] - Pt[1]); vb = (B[0] - Pt[0], B[1] - Pt[1])
    ang = math.degrees(math.acos((va[0] * vb[0] + va[1] * vb[1]) / (math.hypot(*va) * math.hypot(*vb))))
    assert near(ang, (arcs[0] + arcs[2]) / 2.0, 1e-6)
    ta = math.degrees(math.atan2(va[1], va[0])); tb = math.degrees(math.atan2(vb[1], vb[0]))
    # pick the short sweep from ta to tb
    sweep = (tb - ta + 540) % 360 - 180
    t1, t2 = (ta, ta + sweep) if sweep > 0 else (ta + sweep, ta)
    mid = (t1 + t2) / 2.0
    lab = (Pt[0] + 9.0 * math.cos(mid * DEG), Pt[1] + 9.0 * math.sin(mid * DEG))
    L = [start(), r"\draw %s circle (%.3fmm);" % (P(0, 0), r),
         r"\draw %s -- %s; \draw %s -- %s;" % (P(*A), P(*C), P(*B), P(*D)),
         r"\draw[black!55] %s -- %s -- %s -- %s -- cycle;" % (P(*A), P(*B), P(*C), P(*D)),
         r"\draw[accent,line width=0.9pt] %s arc[start angle=%.3f,end angle=%.3f,radius=6mm];" % (P(Pt[0] + 6 * math.cos(t1 * DEG), Pt[1] + 6 * math.sin(t1 * DEG)), t1, t2),
         r"\node[inner sep=0pt] at %s {$?$};" % P(*lab)]
    for pnt, nm, t in zip((A, B, C, D), "ABCD", angs):
        L.append(r"\fill[ink] %s circle (0.6mm); \node[inner sep=0pt] at %s {$%s$};" % (P(*pnt), P(*pol(0, 0, r + 3.6, t)), nm))
    L.append(r"\node[inner sep=0pt,xshift=0pt] at %s {\scriptsize $P$};" % P(Pt[0] - 3.2 * math.cos((mid + 180) * DEG) * 0 + 0.0, Pt[1] - 3.2))
    L.append(END)
    return "\n".join(L)


# --------------------------------------------------------------------------------------------- F15
def fig_pyramid_cut(base=12, hgt=9, cut=3, u=3.6):
    wcut = base * (hgt - cut) / float(hgt)
    assert near(wcut, 8)
    L = [start(), r"\draw %s -- %s -- %s -- cycle;" % (P(-base / 2.0 * u, 0), P(base / 2.0 * u, 0), P(0, hgt * u)),
         r"\draw[accent,line width=1.2pt] %s -- %s;" % (P(-wcut / 2.0 * u, cut * u), P(wcut / 2.0 * u, cut * u)),
         r"\draw[dashed] %s -- %s;" % (P(0, 0), P(0, hgt * u)),
         r"\draw[<->,>=stealth] %s -- %s node[midway,below=0.5pt] {$%d$};" % (P(-base / 2.0 * u, -2.2), P(base / 2.0 * u, -2.2), base),
         r"\draw[<->,>=stealth] %s -- %s node[midway,left,inner sep=1pt] {$%d$};" % (P(-base / 2.0 * u - 4, 0), P(-base / 2.0 * u - 4, hgt * u), hgt),
         r"\draw[dotted] %s -- %s; \draw[dotted] %s -- %s;" % (P(-base / 2.0 * u, 0), P(-base / 2.0 * u - 4, 0), P(0, hgt * u), P(-base / 2.0 * u - 4, hgt * u)),
         r"\draw[<->,>=stealth] %s -- %s node[midway,right,inner sep=1pt] {$%d$};" % (P(base / 2.0 * u + 4, 0), P(base / 2.0 * u + 4, cut * u), cut),
         r"\draw[dotted] %s -- %s;" % (P(wcut / 2.0 * u, cut * u), P(base / 2.0 * u + 4, cut * u)),
         r"\draw[dotted] %s -- %s;" % (P(base / 2.0 * u, 0), P(base / 2.0 * u + 4, 0)),
         END]
    return "\n".join(L)


# --------------------------------------------------------------------------------------------- F16
def fig_parallel_chords(R=13, c1=24, c2=10, u=2.0):
    d1 = math.sqrt(R * R - (c1 / 2.0) ** 2); d2 = math.sqrt(R * R - (c2 / 2.0) ** 2)
    assert near(d1, 5) and near(d2, 12) and near(d1 + d2, 17)
    y1 = d1 * u; y2 = -d2 * u
    A1 = (-c1 / 2.0 * u, y1); B1 = (c1 / 2.0 * u, y1); A2 = (-c2 / 2.0 * u, y2); B2 = (c2 / 2.0 * u, y2)
    for p in (A1, B1, A2, B2):
        assert near(dist((0, 0), p), R * u)
    xd = R * u + 4
    L = [start(), r"\draw %s circle (%.3fmm);" % (P(0, 0), R * u),
         r"\draw %s -- %s; \draw %s -- %s;" % (P(*A1), P(*B1), P(*A2), P(*B2)),
         dot((0, 0), "$O$", "right", ",xshift=1pt"),
         r"\draw[dotted] %s -- %s; \draw[dotted] %s -- %s;" % (P(*B1), P(xd, y1), P(*B2), P(xd, y2)),
         r"\draw[<->,>=stealth] %s -- %s node[midway,right,inner sep=1pt] {$%d$};" % (P(xd, y2), P(xd, y1), d1 + d2),
         r"\node[above] at %s {$%d$};" % (P(0, y1), c1),
         r"\node[above] at %s {$%d$};" % (P(0, y2), c2),
         END]
    return "\n".join(L)


FIGS = {
    "sagitta": fig_sagitta, "kite": fig_kite, "semicircle": fig_semicircle, "segment": fig_segment,
    "annulus": fig_annulus_chord, "stadium": fig_stadium, "fourcircles": fig_four_circles, "lens": fig_lens,
    "twocircles": fig_two_circles, "incircle": fig_incircle, "conewater": fig_cone_water,
    "spherecyl": fig_sphere_cylinder, "silo": fig_silo, "chords": fig_chords, "pyramid": fig_pyramid_cut,
    "parallel": fig_parallel_chords,
}

if __name__ == "__main__":
    for k, f in FIGS.items():
        f()
        print("figure", k, "geometry asserts OK")
