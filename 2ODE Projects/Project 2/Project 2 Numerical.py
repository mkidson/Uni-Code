from matplotlib import pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from scipy.integrate import odeint
from numpy import cos, pi, sin, sqrt, exp, random
import matplotlib
#matplotlib.use('pgf')
matplotlib.rcParams.update({
    'pgf.texsystem': 'pdflatex',
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
})

step = 0.01
nu = np.arange(3.7, 4.3, step)
epsilon = np.arange(0, 1, step)
ts = np.linspace(0, 100, 500)
U0 = [1, 0]

def dU_dx(U, t, nu, epsilon):
    return [ U[1], (-nu*U[0]-epsilon*cos(2*t)*U[0])]

# Us = odeint(dU_dx, U0, ts, args=(nu,epsilon,))
# ys = Us[:,0]

# plt.plot(ts[:], ys[:])
# plt.show()

epsilons = []
for i in nu:
    print(i)
    for c in epsilon:
        Us = odeint(dU_dx, U0, ts, args=(i,c,))
        ys = Us[:,0]
        if max(ys) >= 100:
            epsilons.append(c-step)
            break

    epsilons.append(c)

print(epsilons)

plt.plot(nu, epsilons)
plt.xlabel(r"$\nu_1$")
plt.ylabel(r"$\epsilon_1$", rotation=0)
plt.show()