# finding the electric field due to two point charges
# kdsmil001
# 18-07-19

from vpython import *

Q1 = sphere(pos=(0,0,0), radius=.3e-2, color=color.red, charge=6e-9)
Q2 = sphere(pos=(0,05,0.08,0), radius=.3e2, color=color.blue, charge=-5e-9)

obsloc = vector(-0.04,0.08,0)
k = 9e9

r1 = location - Q1.pos
E1 = k*Q1.charge*((r1.x/mag(r1))/mag(r1)**2
                  