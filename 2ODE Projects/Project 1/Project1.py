from matplotlib import pyplot as plt
import numpy as np
from numpy import cos, pi, sin
from scipy.optimize import curve_fit
import matplotlib
# matplotlib.use('pgf')
matplotlib.rcParams.update({
    'pgf.texsystem': 'pdflatex',
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
})

V = np.linspace(1, 50, 500)
t = np.linspace(-10, 10, 500)
y = np.linspace(-10, 10, 500)

def Y(v, t):
    a = 0.05
    c = 2e3
    k = 7e4
    z = pi*v/5
    m = 800

    A1 = (a*(-((c*z)**2)-(k**2)+k*m*(z)**2))/(-((c*z)**2)-(k**2)-2*k*m*(z**2)+(m*(z**2))**2)
    B1 = (a*c*m*(z**3))/(-((c*z)**2)-(k**2)-2*k*m*(z**2)+(m*(z**2))**2)
    C1 = 5/(pi*v)
    C2 = 0.2
    return C1*sin(z*t)+C2*cos(z*t)+sin(z*t)*((k-m*(z**2))*A1-(c*z)*B1-(a*k))+cos(z*t)*((c*z)*A1+(k-m*(z**2)*B1)-(a*c*z))

maxY = []
for i in V:
    maxY.append(max(Y(i, t)))

maxMaxY = max(maxY)
print(maxMaxY, V[maxY.index(maxMaxY)])
plt.plot(V, maxY)
plt.show()