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

def L0(x):
    return ((-36*(x**3))/(pi**3))+((36*(x**2))/(pi**2))-((11*x)/(pi))+1
def L1(x):
    return ((108*(x**3))/(pi**3))-((90*(x**2))/(pi**2))+((18*x)/(pi))
def L2(x):
    return ((-108*(x**3))/(pi**3))+((72*(x**2))/(pi**2))-((9*x)/(pi))
def L3(x):
    return ((36*(x**3))/(pi**3))-((18*(x**2))/(pi**2))+((2*x)/(pi))

# 1(a) Lagrange Interpolating Polynomial
xs = np.linspace(0, pi/2, 100)
def Lagrange(x):
    # return (0*L0(x))+((pi/6)*L1(x))+((pi/3)*L2(x))+((pi/2)*L3(x))
    return ((x**3)*((90-(54*sqrt(3)))/(pi**3)))+((x**2)*((-63+(36*sqrt(3)))/(pi**2)))+((x)*((22-(9*sqrt(3)))/(2*pi)))

def Newton(x):
    return (3*x/pi)+(((9*(sqrt(3)-2))/(pi**2))*((x**2)-(x*pi/6)))+(((18*(5-(3*sqrt(3))))/(pi**3))*((x**3)-((x**2)*pi/2)+(x*(pi**2)/18)))

# plt.plot(xs, Lagrange(xs))
plt.plot(xs, Newton(xs))
# plt.plot(xs, L0(xs), 'r-')
# plt.plot(xs, L1(xs), 'g-')
# plt.plot(xs, L2(xs), 'y-')
# plt.plot(xs, L3(xs), 'b-')
plt.show()