# Book 2 — Lesson 23: Pythagorean Theorem & Coordinate Applications — Problem Sets

**Source content file**, paired with `concepts.md`. This is Book 2's final
lesson — Set 7 deliberately combines this lesson's content with slope
(Lesson 3) and equation-solving (Lesson 1). All numeric answers verified by
Python script (`sympy`), not hand-computed.

---

## Set 1 — Basic Pythagorean Theorem (right angle always given)

Each triangle below has a right angle explicitly between the two legs
named. Find the missing side.

1. Legs $3$ and $4$. Find the hypotenuse.
2. Legs $6$ and $8$. Find the hypotenuse.
3. Legs $5$ and $12$. Find the hypotenuse.
4. Hypotenuse $10$, one leg $6$. Find the other leg.
5. Hypotenuse $13$, one leg $5$. Find the other leg.
6. Hypotenuse $17$, one leg $8$. Find the other leg.

## Set 2 — Apply or Don't Apply? (the core skill of this lesson)

For each item, first decide: *does the Pythagorean theorem apply here?*
Only compute if it does.

1. A right angle is marked between two legs measuring $9$ and $12$. Find
   the hypotenuse.
2. A triangle has sides $7$, $8$, and $10$. No right angle is marked or
   stated anywhere. Can the Pythagorean theorem be used to check or find a
   side here? Explain.
3. A triangle has sides $8$, $15$, and $17$, with no right angle marked.
   Using the converse check, is this a right triangle? If so, which side
   is the hypotenuse?
4. A triangle has sides $6$, $8$, and $11$, with no right angle marked.
   Using the converse check, is this a right triangle?
5. A right angle is marked between two legs measuring $7$ and $24$. Find
   the hypotenuse.
6. An isosceles triangle has two sides of $10$ and a base of $12$, with no
   right angle marked anywhere. Is this a right triangle?

## Set 3 — Distance Formula Drill

Find the distance between each pair of points.

1. $(0,0)$ and $(3,4)$
2. $(2,3)$ and $(7,15)$
3. $(-4,1)$ and $(4,7)$
4. $(1,1)$ and $(1,9)$
5. $(-2,-3)$ and $(3,-3)$
6. $(0,0)$ and $(1,1)$

## Set 4 — Pythagorean Triples Speed Set (recognize, don't compute from scratch)

1. Legs $9$ and $12$. Hypotenuse?
2. Legs $8$ and $15$. Hypotenuse?
3. Legs $20$ and $21$. Hypotenuse?
4. Hypotenuse $25$, one leg $7$. Other leg?
5. Legs $9$ and $40$. Hypotenuse?
6. Legs $10$ and $24$. Hypotenuse?

## Set 5 — Mixed Real-World Word Problems

1. A ladder's base is $5$ m from a wall, and it reaches $12$ m up the
   wall. How long is the ladder?
2. A TV screen measures $24$ in wide and $10$ in tall. Find the length of
   its diagonal.
3. A ship sails $9$ km east, then $12$ km north. How far is it from its
   starting point in a straight line?
4. Two cities are located at coordinates $(0,0)$ and $(8,15)$ (in km).
   Find the straight-line distance between them.
5. A rectangular park is $16$ m by $30$ m. Find the length of a diagonal
   path cutting across it.
6. A baseball diamond is a square with each side $90$ ft. Find the exact
   distance from home plate to second base (the diagonal).

## Set 6 — Spot the Error

Each item shows a flawed solution. Name the error and give the correct
answer.

1. Sides $6$, $10$, $11$ are given, no right angle marked. *"Yechim:
   $6^2+10^2=136$, va $11^2=121$ — bular juda yaqin, demak bu amalda
   to'g'ri burchakli uchburchak, xatoni e'tiborsiz qoldiramiz."*
2. Hypotenuse $25$, one leg $7$, find the other leg. *"Yechim:
   $x=\sqrt{7^2+25^2}=\sqrt{674}\approx25.96$."*
3. Find the distance between $(1,5)$ and $(4,1)$. *"Yechim:
   $\sqrt{3^2+(-4)}=\sqrt{9-4}=\sqrt5$."*
4. Sides $5$, $6$, $10$ are given, no right angle marked. *"Yechim: eng
   uzun tomon $10$ ekan, demak u gipotenuza, va $5^2+6^2=10^2$ deb
   hisoblab, bu to'g'ri burchakli uchburchak deb e'lon qilamiz."*
5. Legs $9$ and $12$. *"Yechim: $9^2+12^2=81+144=225$. Javob: $225$."*

## Set 7 — Bonus / Capstone (combines with Lessons 1 and 3 — closes Book 2)

1. Points $A(1,2)$ and $B(7,10)$. Find the distance $AB$ and the slope of
   segment $AB$.
2. A line $y=3x$ passes through the origin. A point $P=(x,9)$ lies on this
   line, with $x>0$. Find $x$, then find the distance $OP$ (from the
   origin to $P$).
3. A triangle has vertices $(0,0)$, $(4,0)$, and $(4,3)$. Find its
   perimeter (two sides are given directly; find the third with the
   distance formula).
4. Two points are $13$ units apart. The horizontal distance between them
   is $5$ units. Find the vertical distance between them.
5. A triangle has vertices $(1,1)$, $(9,7)$, and $(9,1)$. Confirm this is
   a right triangle (two of its sides are perfectly horizontal/vertical),
   then find its area.

---

## Answer Key

**Set 1:** 1) $5$  2) $10$  3) $13$  4) $8$  5) $12$  6) $15$

**Set 2:**
1. Apply — right angle given. $9^2+12^2=225$, hypotenuse $=15$.
2. Cannot apply — no right angle is given or marked anywhere in the
   triangle, so the Pythagorean theorem has nothing to attach to.
3. Converse check: $8^2+15^2=64+225=289=17^2$. Yes, it's a right triangle;
   $17$ is the hypotenuse (it's the side the check confirms against).
4. Converse check: $6^2+8^2=36+64=100\ne121=11^2$. No, not a right
   triangle.
5. Apply — right angle given. $7^2+24^2=625$, hypotenuse $=25$.
6. Converse check across all pairings: $10^2+10^2=200\ne12^2=144$, and
   $10^2+12^2=244\ne10^2=100$. No combination works — not a right
   triangle.

**Set 3:** 1) $5$  2) $13$  3) $10$  4) $8$  5) $5$  6) $\sqrt2$

**Set 4:** 1) $15$  2) $17$  3) $29$  4) $24$  5) $41$  6) $26$

**Set 5:** 1) $13$ m  2) $26$ in  3) $15$ km  4) $17$ km  5) $34$ m
6) $90\sqrt2$ ft (exact — it's an irrational distance, don't force a
decimal)

**Set 7:**
1. $AB=10$; slope $=\dfrac{10-2}{7-1}=\dfrac43$.
2. On $y=3x$ with $y=9$: $9=3x$, so $x=3$ — point $P=(3,9)$. Distance
   $OP=\sqrt{3^2+9^2}=\sqrt{90}=3\sqrt{10}$.
3. Legs: $(0,0)$-$(4,0)=4$; $(4,0)$-$(4,3)=3$. Hypotenuse (distance
   formula): $(0,0)$-$(4,3)=\sqrt{16+9}=5$. Perimeter $=4+3+5=12$.
4. $5^2+b^2=13^2 \Rightarrow b^2=144 \Rightarrow b=12$.
5. $(1,1)$-$(9,1)$ is horizontal, length $8$; $(9,1)$-$(9,7)$ is vertical,
   length $6$ — these meet at $(9,1)$ at a right angle by construction.
   Hypotenuse $(1,1)$-$(9,7)=\sqrt{64+36}=10$. Area
   $=\frac12(8)(6)=24$.

**Set 6:**
1. Error — treating $136$ and $121$ as "close enough" to call it a right
   triangle. The Pythagorean check requires *exact* equality, not an
   approximation; since $136\ne121$, this is definitively not a right
   triangle, and the theorem can't be used on it at all. (No "correct
   answer" to compute — the right response is to reject the setup.)
2. Error — treated the hypotenuse ($25$) as if it were a leg, squaring and
   adding it to the other leg instead of subtracting. Correct: hypotenuse
   is the longest side, so $7^2+x^2=25^2$, $x^2=625-49=576$, $x=24$.
3. Error — forgot to square the second difference before combining (used
   $-4$ directly instead of $(-4)^2$). Correct:
   $\sqrt{3^2+(-4)^2}=\sqrt{9+16}=\sqrt{25}=5$.
4. Error — assumed the longest side must be the hypotenuse of a right
   triangle without first confirming a right angle exists, then forced
   the equation to "work" without actually checking it ($25+36=61\ne100$
   — it fails). This is not a right triangle, and the Pythagorean theorem
   cannot be applied to it to find or confirm any side.
5. Error — forgot to take the final square root, stopping at $c^2=225$
   instead of solving for $c$. Correct: $c=\sqrt{225}=15$.
