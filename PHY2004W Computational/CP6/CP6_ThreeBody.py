from matplotlib import pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from numpy import cos, pi, sin, sqrt, exp, random
import matplotlib
from vpython import *
#matplotlib.use('pgf')
matplotlib.rcParams.update({
    'pgf.texsystem': 'pdflatex',
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
})
# Constants to be used later, such as start positions and start momenta
r1 = vector(1,0,0)
rStar = vector(0.5,0,0)
phi = -pi/6
p1 = vector(0.5,0.5,0)
pStar = vector(-0.5,-0.5,0)
mStar = 1
m1 = 1

deltaT = 0.0001
t = 0
G = 1
rCoM = (m1*r1+mStar*rStar)/(m1+mStar)

star = sphere(pos=rStar, radius=0.1, color=color.yellow)
planet1 = sphere(pos=r1, radius=0.05, color=color.blue)
CoM = sphere(pos=rCoM, radius=0.01, color=color.red)
starTrail = curve(color=vector(99,99,59), radius=0.001)
planet1Trail = curve(color=color.cyan, radius=0.001)
CoMTrail = curve(color=vector(99,0,0), radius=0.001)
scene.autoscale = 0

while t < 100:
    # rate(100)
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

    rCoM = (m1*r1+mStar*rStar)/(m1+mStar)
    t += deltaT

exit()