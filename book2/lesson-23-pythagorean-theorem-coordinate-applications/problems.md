# Book 2 — Lesson 23: Pythagorean Theorem & Coordinate Applications — Problem Sets

**Source content file**, paired with `concepts.md`. This is Book 2's final
lesson — Set 7 deliberately combines this lesson's content with slope
(Lesson 3) and equation-solving (Lesson 1). All numeric answers verified by
Python script (`sympy`), not hand-computed.

---

## Set 1 — Basic Pythagorean Theorem (right angle always given)

Each triangle below has a right angle explicitly between the two legs
named.

1. A right triangle has legs of length $3$ and $4$. What is the length of the hypotenuse?
2. A right triangle has legs of length $6$ and $8$. What is the length of the hypotenuse?
3. A right triangle has legs of length $5$ and $12$. What is the length of the hypotenuse?
4. A right triangle has a hypotenuse of length $10$ and one leg of length $6$. What is the length of the other leg?
5. A right triangle has a hypotenuse of length $13$ and one leg of length $5$. What is the length of the other leg?
6. A right triangle has a hypotenuse of length $17$ and one leg of length $8$. What is the length of the other leg?

## Set 2 — Apply or Don't Apply? (the core skill of this lesson)

For each item, first decide: *does the Pythagorean theorem apply here?*
Only compute if it does.

1. In a right triangle, a right angle is marked between two legs measuring $9$ and $12$. What is the length of the hypotenuse?
2. A triangle has sides of length $7$, $8$, and $10$, with no right angle marked or stated anywhere. Can the Pythagorean theorem be used to find or confirm a side of this triangle? Explain why or why not.
3. A triangle has sides of length $8$, $15$, and $17$, with no right angle marked. Using the converse of the Pythagorean theorem, is this a right triangle? If so, which side is the hypotenuse?
4. A triangle has sides of length $6$, $8$, and $11$, with no right angle marked. Using the converse of the Pythagorean theorem, is this a right triangle?
5. In a right triangle, a right angle is marked between two legs measuring $7$ and $24$. What is the length of the hypotenuse?
6. An isosceles triangle has two sides of length $10$ and a base of length $12$, with no right angle marked anywhere. Is this a right triangle?

## Set 3 — Distance Formula Drill

1. What is the distance between the points $(0,0)$ and $(3,4)$ in the xy-plane?
2. What is the distance between the points $(2,3)$ and $(7,15)$ in the xy-plane?
3. What is the distance between the points $(-4,1)$ and $(4,7)$ in the xy-plane?
4. What is the distance between the points $(1,1)$ and $(1,9)$ in the xy-plane?
5. What is the distance between the points $(-2,-3)$ and $(3,-3)$ in the xy-plane?
6. What is the distance between the points $(0,0)$ and $(1,1)$ in the xy-plane?

## Set 4 — Pythagorean Triples Speed Set (recognize, don't compute from scratch)

1. A right triangle has legs of length $9$ and $12$. What is the length of the hypotenuse?
2. A right triangle has legs of length $8$ and $15$. What is the length of the hypotenuse?
3. A right triangle has legs of length $20$ and $21$. What is the length of the hypotenuse?
4. A right triangle has a hypotenuse of length $25$ and one leg of length $7$. What is the length of the other leg?
5. A right triangle has legs of length $9$ and $40$. What is the length of the hypotenuse?
6. A right triangle has legs of length $10$ and $24$. What is the length of the hypotenuse?

## Set 5 — Mixed Real-World Word Problems

1. A ladder is positioned so that its base is $5$ meters from a wall and the ladder reaches $12$ meters up the wall. What is the length of the ladder, in meters?
2. A television screen measures $24$ inches wide and $10$ inches tall. What is the length of the screen's diagonal, in inches?
3. A ship sails $9$ kilometers east and then $12$ kilometers north. What is the straight-line distance from the ship's final position to its starting point, in kilometers?
4. In a coordinate system where distances are measured in kilometers, two cities are located at the points $(0,0)$ and $(8,15)$. What is the straight-line distance between the two cities, in kilometers?
5. A rectangular park measures $16$ meters by $30$ meters. What is the length of a diagonal path that cuts across the park, in meters?
6. A baseball diamond is a square with each side measuring $90$ feet. What is the exact distance from home plate to second base, which lies along the diagonal of the square, in feet?

## Set 6 — Spot the Error

Each item shows a flawed solution. Name the error and give the correct
answer.

1. Sides $6$, $10$, $11$ are given, with no right angle marked. *"Solution:
   $6^2+10^2=136$, and $11^2=121$ — these are close enough, so this is
   effectively a right triangle; we can ignore the small discrepancy."*
2. The hypotenuse is $25$ and one leg is $7$; find the other leg. *"Solution:
   $x=\sqrt{7^2+25^2}=\sqrt{674}\approx25.96$."*
3. What is the distance between $(1,5)$ and $(4,1)$? *"Solution:
   $\sqrt{3^2+(-4)}=\sqrt{9-4}=\sqrt5$."*
4. Sides $5$, $6$, $10$ are given, with no right angle marked. *"Solution: the
   longest side is $10$, so it must be the hypotenuse, and since
   $5^2+6^2=10^2$, this must be a right triangle."*
5. A right triangle has legs $9$ and $12$. *"Solution: $9^2+12^2=81+144=225$.
   The hypotenuse is $225$."*

## Set 7 — Bonus / Capstone (combines with Lessons 1 and 3 — closes Book 2)

1. In the xy-plane, points $A(1,2)$ and $B(7,10)$ are given. What is the distance $AB$, and what is the slope of segment $AB$?
2. In the xy-plane, the line $y=3x$ passes through the origin. A point $P=(x,9)$ lies on this line, where $x>0$. What is the value of $x$, and what is the distance $OP$ from the origin to point $P$?
3. In the xy-plane, a triangle has vertices at $(0,0)$, $(4,0)$, and $(4,3)$. What is the perimeter of the triangle? (Two sides can be found directly; find the third using the distance formula.)
4. Two points in the xy-plane are $13$ units apart, and the horizontal distance between them is $5$ units. What is the vertical distance between the two points?
5. In the xy-plane, a triangle has vertices at $(1,1)$, $(9,7)$, and $(9,1)$. Confirm that this is a right triangle (two of its sides are horizontal and vertical), and then find its area.

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
