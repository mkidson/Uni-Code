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

def L0(x):
    return ((-36*(x**3))/(pi**3))+((36*(x**2))/(pi**2))-((11*x)/(pi))+1
def L1(x):
    return ((108*(x**3))/(pi**3))-((90*(x**2))/(pi**2))+((18*x)/(pi))
def L2(x):
    return ((-108*(x**3))/(pi**3))+((72*(x**2))/(pi**2))-((9*x)/(pi))
def L3(x):
    return ((36*(x**3))/(pi**3))-((18*(x**2))/(pi**2))+((2*x)/(pi))
def Lagrange(x):
    return ((x**3)*((90-(54*sqrt(3)))/(pi**3)))+((x**2)*((-63+(36*sqrt(3)))/(pi**2)))+((x)*((22-(9*sqrt(3)))/(2*pi)))
def Newton(x):
    return (3*x/pi)+(((9*(sqrt(3)-2))/(pi**2))*((x**2)-(x*pi/6)))+(((18*(5-(3*sqrt(3))))/(pi**3))*((x**3)-((x**2)*pi/2)+(x*(pi**2)/18)))

xs = np.linspace(0, pi/2, 100)
zeros = np.zeros(1000)
axis = np.linspace(-10, 10, 1000)

plt.plot(axis, zeros, '#000000')
plt.plot(zeros, axis, '#000000')
plt.plot(xs, Lagrange(xs), 'b-', label='Lagrange(x)')
plt.plot(xs, L0(xs), 'r-', label='$L_0(x)$')
plt.plot(xs, L1(xs), 'g-', label='$L_1(x)$')
plt.plot(xs, L2(xs), 'y-', label='$L_2(x)$')
plt.plot(xs, L3(xs), label='$L_3(x)$')
plt.legend()
plt.grid(color='#CCCCCC', linestyle=':')
plt.xlim(-0.2, (pi/2)+0.5)
plt.ylim(-0.5, 1.5)
plt.xlabel('x')
plt.ylabel('y', rotation=0)
# plt.show()
plt.savefig(r'2NA Assignments\Assignment 2\LagrangePlot.pgf')

plt.plot(axis, zeros, '#000000')
plt.plot(zeros, axis, '#000000')
plt.plot(xs, Newton(xs), 'b-', label='Newton(x)')
plt.legend()
plt.grid(color='#CCCCCC', linestyle=':')
plt.xlim(-0.2, (pi/2)+0.5)
plt.ylim(-0.5, 1.5)
plt.xlabel('x')
plt.ylabel('y', rotation=0)
# plt.show()
plt.savefig(r'2NA Assignments\Assignment 2\NewtonPlot.pgf')