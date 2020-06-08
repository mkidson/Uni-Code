import numpy as np
from numpy import cos, pi, sin, sqrt, exp, random
from vpython import *
# Constants to be used later, such as start positions and start momenta
# r1 = vector(0.97000436, -0.24308753, 0)
# r2 = vector(-0.97000436, 0.24308753, 0)
# rStar = vector(0,0,0)
# pStar = vector (-0.93240737, -0.86473146, 0)
# p1 = -pStar/2
# p2 = -pStar/2
# m1 = 1
# m2 = 1
# mStar = 1
r1 = vector(1,0,0)
r2 = vector(-1,0,0)
rStar = vector(0,0,0)
p1 = vector(0,0.1,0)
p2 = vector(0,-0.1,0)
pStar = vector (0,0,0)
m1 = 0.1
m2 = 0.1
mStar = 1
rCoM = ((m1*r1)+(m2*r2)+(mStar*rStar))/(m1+m2+mStar)
# More constants, physical
deltaT = 0.01
t = 0
G = 1
# Creating the objects to be drawn on the canvas, as well as settings for the canvas
planet1 = sphere(pos=r1, radius=0.05, color=color.blue)
planet2 = sphere(pos=r2, radius=0.05, color=color.green)
star = sphere(pos=rStar, radius=0.1, color=color.yellow)
CoM = sphere(pos=rCoM, radius=0.01, color=color.red)
planet1Trail = curve(color=color.blue, radius=0.005)
planet2Trail = curve(color=color.green, radius=0.005)
starTrail = curve(color=color.yellow, radius=0.005)
CoMTrail = curve(color=color.red, radius=0.005)
scene.autoscale = 0
scene.camera.follow(CoM)
scene.title = 'Planet1 Initial Momentum: '+str(p1)+' Planet1 Mass: '+str(m1)+'\nPlanet2 Initial Momentum: '+str(p2)+' Planet2 Mass: '+str(m2)+\
    '\nStar Initial Momentum: '+str(pStar)+' Star Mass: '+str(mStar)+'\nSystem Initial Momentum: '+str(p1+p2+pStar)
# The loop that calculates new positions based on forces
while t < 100:
    rate(100)
    # Updating positions and trails
    planet1Trail.append(pos=r1)
    planet2Trail.append(pos=r2)
    starTrail.append(pos=rStar)
    CoMTrail.append(pos=rCoM)
    planet1.pos=r1
    planet2.pos=r2
    star.pos=rStar
    CoM.pos=rCoM
    # Force calculations
    F1Star = -G*mStar*m1*(r1-rStar)/(mag(r1-rStar)**3)
    F12 = -G*m1*m2*(r1-r2)/(mag(r1-r2)**3)
    F2Star = -G*m2*mStar*(r2-rStar)/(mag(r2-rStar)**3)
    # Updating planet1 position and momentum
    p1 += (F1Star+F12)*deltaT
    r1 += p1*deltaT/m1
    # Updating planet2 position and momentum
    p2 += (F2Star-F12)*deltaT
    r2 += p2*deltaT/m2
    # Updating star position and momentum
    pStar += (-F1Star-F2Star)*deltaT
    rStar += pStar*deltaT/mStar
    # Finding new CoM position from positions of masses
    rCoM = ((m1*r1)+(m2*r2)+(mStar*rStar))/(m1+m2+mStar)
    # Housekeeping
    t += deltaT
    scene.caption = 't = '+str(round(t,3))+'\nSystem Momentum at time t: '+str(p1+p2+pStar)