import numpy as np
from numpy import cos, pi, sin, sqrt, exp
from scipy.integrate import odeint
import matplotlib
from matplotlib import pyplot as plt
matplotlib.use('pgf')
matplotlib.rcParams.update({
    'pgf.texsystem': 'pdflatex',
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
})

a = 0.05
c = 2e3
k = 7e4
m = 800

def dU_dx(U, x, v):
    z = pi*v/5
    return [U[1], (-(c/m)*U[1])-((k/m)*U[0])+((c*a*z/m)*cos(z*x))+((k*a/m)*sin(z*x))]

U0 = [0.2, 1]
Vs = np.linspace(1, 30, 500)
ts = np.linspace(0, 100, 500)

# Us = odeint(dU_dx, U0, ts, args=(14,))
# ys = Us[:,0]

# plt.plot(ts[25:], ys[25:])
# plt.show()

maxY = []
for i in Vs:
    Us = odeint(dU_dx, U0, ts, args=(i,))
    ys = Us[:,0]
    maxY.append(max(abs(ys[25:])))

maxMaxY = max(maxY)
print(maxMaxY, Vs[maxY.index(maxMaxY)])

plt.plot(Vs, maxY)
plt.xlabel("Velocity ($\\frac{m}{s}$)")
plt.ylabel("Amplitude ($m$)")
# plt.show()
plt.savefig('2ODE Projects\Project 1\The Numerical Plot.pgf')

maxs = [0.19510861846800925, 14.68937875751503]