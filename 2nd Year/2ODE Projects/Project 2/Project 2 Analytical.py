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

N = 1000
step = 0.1/N
nu = np.linspace(0.7, 1.3, N)

plt.plot(nu, (abs((2*nu)-2)), 'r')
plt.xlabel(r"$\nu$")
plt.ylabel(r"$\epsilon$", rotation=0)
# plt.show()
plt.savefig(r'2ODE Projects\Project 2\Nu1Analytical.pgf')