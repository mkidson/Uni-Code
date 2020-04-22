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

V = np.linspace(1, 100, 500)
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
    A = (k*a*(k-m*z**2)+c**2*a*z**2)/((k-m*(z**2))**2+(c*z)**2)
    B = (c*a*z*(k-m*z**2)-k*a*c*z)/((k-m*(z**2))**2+(c*z)**2)
    return exp((-5/4)*x)*(C1*cos(p*x)+C2*sin(p*x))+A*sin(z*x)+B*cos(z*x)

maxY = []
for i in V:
    maxY.append(max(abs(Y(i, t))))

maxMaxY = max(maxY)
print(maxMaxY, V[maxY.index(maxMaxY)])

plt.plot(V, maxY)
plt.show()