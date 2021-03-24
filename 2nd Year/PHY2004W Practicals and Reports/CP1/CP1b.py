from matplotlib import pyplot as plt
import matplotlib
from scipy.optimize import curve_fit
import numpy as np
matplotlib.use("pgf")
matplotlib.rcParams.update({
    "pgf.texsystem": "pdflatex",
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
})

x = np.array([1.21, 2.04, 3.57])
xUn = np.array([0.16, 0.10, 0.13])
y = np.array([10.2, 15.3, 19.8])
yUn = np.array([2.1, 3.2, 2.6])
p0 = np.array([1, 1])
name = np.array(['m', 'c'])
N = 3

plt.errorbar(x, y, yUn, xUn, 'rs', 'black', 0.5, capsize=3, label="PHY2004W Data", \
    markersize=5, capthick=0.5)


xy = []
for c in range(N):
    xy.append(round(x[c]*y[c], 3))
x2 = []
for t in range(N):
    x2.append(round(x[t]**2, 3))

m = ((N*sum(xy)) - sum(x)*sum(y))/((N*sum(x2))-(sum(x))**2)
c = ((sum(x2)*sum(y))-(sum(xy)*sum(x)))/((N*sum(x2))-(sum(x)**2))

xLine = np.arange(0.5, 4, 0.1)
yLine = []
for i in xLine:
    yLine.append((m*i)+c)
# Plots the line of best fit determined from the calculations above
plt.plot(xLine, yLine, color='blue', label="Best Fit", lw=0.5)
plt.legend(numpoints=2)
plt.savefig('CP1b Plot.pgf')