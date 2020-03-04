from matplotlib import pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import matplotlib
matplotlib.use('pgf')
matplotlib.rcParams.update({
    'pgf.texsystem': 'pdflatex',
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
})

x = np.linspace(-10, 10, 500)
y = np.linspace(-10, 10, 500)

def y1(x):
    return (x**2)-2
def y2(x):
    return np.sqrt(np.abs(x)+2)
def y3(x):
    return 2/(x-1)
def y4(x):
    return (2/x)+1

y32 = y3(x)[~np.isnan(y3(x))]

plt.plot(x, y1(x), color='r', lw=0.5, label='$y = x^2-2$')
plt.plot(np.abs(x), y2(x), color='b', lw=0.5, label='$y = \sqrt{x+2}$')
plt.plot(x, y32, color='y', lw=0.5, label='$y = \\frac{2}{x-1}$')
plt.plot(x, y4(x), color='g', lw=0.5, label='$y = \\frac{2}{x}+1$')
plt.plot(x, np.zeros(500), color='black')
plt.plot(np.zeros(500), y, color='black')
plt.plot(x, y, label='$y = x$')

plt.ylim(-10, 10)
plt.xlim(-10, 10)
plt.legend()
plt.savefig('2NA Assignments\Assignment 1\Q2_Plot.pgf')
# plt.show()