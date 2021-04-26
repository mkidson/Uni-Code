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

a=0
b=4
dt=0.2
u0=[1,0]
v0=[0,1]
t=np.arange(a,b,dt)
# tspan=[a,b]

def particular(t, y):
    u=y[0]
    z=y[1]
    return [z, (-z/(t+2))+(2*u/((t+2)**2))-(4/((t+2)**3))]

def homog(t, y):
    v=y[0]
    w=y[1]
    return [w, (-w/(t+2))+(2*v/((t+2)**2))]

uSol=solve_ivp(particular, [t[0],t[-1]], u0, t_eval=t)
vSol=solve_ivp(homog, [t[0],t[-1]], v0, t_eval=t)
C=(1/3 - uSol.y[1][-1])/(vSol.y[1][-1])
print(C)
ySol=uSol.y[0]+C*vSol.y[0]

plt.figure(1)
plt.plot(uSol.t, uSol.y[0], label='u', c='r')
plt.plot(vSol.t, vSol.y[0], label='v', c='b')
plt.legend()
plt.xlabel('t')
plt.ylabel('y')
plt.figure(2)
plt.plot(uSol.t, ySol, label='y', c='orange')
plt.legend()
plt.xlabel('t')
plt.ylabel('y')
plt.show()
