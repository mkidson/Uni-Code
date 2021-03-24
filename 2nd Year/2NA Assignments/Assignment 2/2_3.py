from matplotlib import pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from numpy import cos, pi, sin, sqrt, exp, random
import matplotlib
matplotlib.use('pgf')
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
zeros = np.zeros(1000)
axis = np.linspace(-10, 10, 1000)

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

plt.plot(axis, zeros, '#000000')
plt.plot(zeros, axis, '#000000')
plt.plot(xs, ys, label='Lagrange Approximation of $\sin(x)$')
plt.grid(color='#CCCCCC', linestyle=':')
plt.xlabel('x')
plt.ylabel('y', rotation=0)
plt.legend()
plt.xlim(-0.2, (2*pi)+0.5)
plt.ylim(-1.5, 1.5)
# plt.show()
plt.savefig('2NA Assignments\Assignment 2\LagrangeExpanded.pgf')
plt.plot(axis, zeros, '#000000')
plt.plot(zeros, axis, '#000000')
plt.plot(xs, ys-sin(xs), label='$P_3(x)-\sin(x)$')
plt.grid(color='#CCCCCC', linestyle=':')
plt.xlabel('x')
plt.ylabel('y', rotation=0)
plt.legend()
plt.xlim(-0.2, (2*pi)+0.5)
plt.ylim(-.003, .003)
# plt.show()
plt.savefig('2NA Assignments\Assignment 2\LagrangeError.pgf')