from matplotlib import pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from numpy import cos, pi, sin, sqrt, exp, random
import matplotlib
#matplotlib.use('pgf')
matplotlib.rcParams.update({
    'pgf.texsystem': 'pdflatex',
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
})

def Lagrange(x):
    return ((x**3)*((90-(54*sqrt(3)))/(pi**3)))+((x**2)*((-63+(36*sqrt(3)))/(pi**2)))+((x)*((22-(9*sqrt(3)))/(2*pi)))

xs = np.linspace(0, 2*pi, 2000)
ys = np.zeros(2000)

for i in range(xs.size):
    mod = xs[i]-np.floor(xs[i]/(2*pi))*(2*pi)
    if 0 < mod <= (pi/2):
        ys[i] = Lagrange(mod)
    elif (pi/2) < mod <= (pi):
        ys[i] = Lagrange(pi-mod)
    elif (pi) < mod <= (3*pi/2):
        ys[i] = Lagrange(mod-pi)*(-1)
    elif (3*pi/2) < mod <= (2*pi):
        ys[i] = Lagrange((2*pi)-mod)*(-1)

plt.plot(xs, ys)
plt.grid(color='#CCCCCC', linestyle=':')
plt.xlabel('x')
plt.ylabel('y', rotation=0)
plt.show()
plt.plot(xs, ys-sin(xs))
plt.grid(color='#CCCCCC', linestyle=':')
plt.xlabel('x')
plt.ylabel('y', rotation=0)
plt.show()