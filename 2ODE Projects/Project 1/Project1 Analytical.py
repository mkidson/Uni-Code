from matplotlib import pyplot as plt
import numpy as np
from numpy import cos, pi, sin, sqrt, exp
from scipy.optimize import curve_fit
import matplotlib
# matplotlib.use('pgf')
matplotlib.rcParams.update({
    'pgf.texsystem': 'pdflatex',
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
})

Vs = np.linspace(1, 30, 500)
t = np.linspace(5, 100, 500)

C1 = 0.2
C2 = sqrt(55)/55
a = 0.05
c = 2e3
k = 7e4
m = 800
p = sqrt(1375/16)

def Y(v, x):
    z = pi*v/5
    sinAlpha = (k*(k-m*z**2)+c**2*z**2)/sqrt((k-m*(z**2))**2+(c*z)**2)
    cosAlpha = (c*m*z**3)/sqrt((k-m*(z**2))**2+(c*z)**2)
    A = (a)/sqrt((k-m*(z**2))**2+(c*z)**2)
    return A*(cos(z*x)*cosAlpha+sin(z*x)*sinAlpha)

# maxY = max(abs(Y(14.88758171, t)))
# plt.plot(t, Y(14.88758171, t))
# print(maxY)

# exp(-5*x/4)*(0.2*cos(p*t)+(sqrt(55)/55)*sin(p*t))+

maxY = []
for i in Vs:
    maxY.append(max(abs(Y(i, t))))

maxMaxY = max(maxY)
print(maxMaxY, Vs[maxY.index(maxMaxY)])

plt.plot(Vs, maxY)
plt.xlabel("Velocity ($\\frac{m}{s}$)")
plt.ylabel("Amplitude ($m$)")

plt.show()
# plt.savefig('2ODE Projects\Project 1\Analytical Plot.pgf')

maxs = [0.19509896745635577, 14.68937875751503]