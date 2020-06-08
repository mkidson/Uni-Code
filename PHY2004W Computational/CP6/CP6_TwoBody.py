import numpy as np
from numpy import cos, pi, sin, sqrt, exp, random
from vpython import *
# Constants to be used later, such as start positions and start momenta
r1 = vector(1,0,0)
rStar = vector(0,0,0)
p1 = vector(0,0.5,0)
pStar = vector(0,0,0)
mStar = 1
m1 = 1
# More constants, physical
deltaT = 0.01
t = 0
G = 1
rCoM = (m1*r1+mStar*rStar)/(m1+mStar)
# Creating the objects to be drawn on the canvas, as well as settings for the canvas
star = sphere(pos=rStar, radius=0.1, color=color.yellow)
planet1 = sphere(pos=r1, radius=0.05, color=color.blue)
CoM = sphere(pos=rCoM, radius=0.01, color=color.red)
starTrail = curve(color=vector(99,99,59), radius=0.005)
planet1Trail = curve(color=color.cyan, radius=0.005)
CoMTrail = curve(color=vector(99,0,0), radius=0.005)
scene.autoscale = 0
scene.camera.follow(CoM)
scene.title = 'Planet Initial Momentum: '+str(p1)+'\nStar Initial Momentum: '+str(pStar)+'\nSystem Initial Momentum: '+str(p1+pStar)
# The loop that calculates new positions based on forces
while t < 100:
    rate(100)
    # Updating positions and trails
    starTrail.append(pos=rStar)
    planet1Trail.append(pos=r1)
    CoMTrail.append(pos=rCoM)
    star.pos=rStar
    planet1.pos=r1
    CoM.pos=rCoM
    # Force calculations
    F1Star = -G*mStar*m1*(r1-rStar)/(mag(r1-rStar)**3)
    # Updating star stuff
    pStar += deltaT*(-F1Star)
    rStar += pStar*deltaT/mStar
    # Updating planet1 stuff
    p1 += F1Star*deltaT
    r1 += p1*deltaT/m1
    # Finding new CoM position from position of masses
    rCoM = (m1*r1+mStar*rStar)/(m1+mStar)
    # Housekeeping
    t += deltaT
    scene.caption = 't = '+str(round(t,3))+'\nSystem Momentum at time t: '+str(p1+pStar)