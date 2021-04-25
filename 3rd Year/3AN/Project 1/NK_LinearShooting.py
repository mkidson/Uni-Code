from matplotlib import pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp
from numpy import cos, pi, sin, sqrt, exp, random
import matplotlib
matplotlib.rcParams.update({
    'pgf.texsystem': 'pdflatex',
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
})

n=1
a=0 #might need to be 0.001
b=10

N=50
h=(b-a)/N
print('h',h)

r_span=np.array([a,b])
rs=np.arange(a,b,h)
u_0=0.1*rs

alpha=0
beta=1

def f(r,u,v):
    return -((1/r)*v + (u/(1-u**2))*(v**2 - (n**2)/(r**2)) + u*(1-u**2))

def Q(r,u,v):
    return -((1+u**2)/((1-u**2)**2)*(v**2 - (n**2)/(r**2)) + (1-3*u**2))

def P(r,u,v):
    return -((1/r) + u/(1-u**2)*(2*v))

def N(r,u,v):
    return -v+f(r,u,v)

def homog(r,u):
    pass

def particular(r,u):
    pass

u_1=0 #just used so the while doesn't break the first loop around
tol=1e-5
maxIter=200
k=1
while k <= maxIter and (abs(u_1-b)>tol):
    break

