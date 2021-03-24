from matplotlib import pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from scipy.integrate import odeint
from numpy import cos, pi, sin, sqrt, exp, random
import matplotlib
matplotlib.use('pgf')
matplotlib.rcParams.update({
    'pgf.texsystem': 'pdflatex',
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
})

N = 1000
step = 2.4/N
nu = np.linspace(3.75, 4.5, N, endpoint=False)
epsilon = np.linspace(1.6, 4, N, endpoint=False)
ts = np.linspace(0, 100, 500)
U0 = [1, 0]

def dU_dx(U, t, nu, epsilon):
    return [U[1], (-nu*U[0]-epsilon*cos(2*t)*U[0])]

epsilons = []
hasMax = True
for i in nu:
    print(i)
    for c in epsilon:
        Us = odeint(dU_dx, U0, ts, args=(i,c,))
        ys = Us[:,0]
        if max(ys) >= 100:
            epsilons.append(c-step)
            hasMax = False
            break

    if hasMax:
        epsilons.append(c)
        hasMax = True

plt.plot(nu, epsilons, 'b', label='Numerical Solution')
# plt.plot(nu, (abs((2*nu)-2)), 'r', label='Analytical Solution')
plt.xlabel(r"$\nu$")
plt.ylabel(r"$\epsilon$", rotation=0)
plt.legend()
# plt.show()
plt.savefig(r'2ODE Projects\Project 2\Nu4Numerical.pgf')