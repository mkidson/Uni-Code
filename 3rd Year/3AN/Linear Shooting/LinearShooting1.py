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
t_eval=np.arange(a,b,dt)
# tspan=[a,b]
C=()

def particular(t, y):
    u=y[0]
    z=y[1]
    du=[0,0]
    du[0]=z
    du[1]=(-z/(t+2))+(2*u/((t+2)**2))-(4/((t+2)**3))
    return du

def homog(t, y):
    v=y[0]
    w=y[1]
    dv=[0,0]
    dv[0]=w
    dv[1]=(-w/(t+2))+(2*v/((t+2)**2))
    return dv

uSol=solve_ivp(particular, [t_eval[0],t_eval[-1]], u0, t_eval=t_eval)
vSol=solve_ivp(homog, [t_eval[0],t_eval[-1]], v0, t_eval=t_eval)

plt.plot(uSol.t, uSol.y[1], label='u')
plt.plot(vSol.t, vSol.y[1], label='v')
plt.legend()
plt.show()