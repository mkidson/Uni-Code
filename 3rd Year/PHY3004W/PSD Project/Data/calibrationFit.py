from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
from numpy import cos, pi, sin, sqrt, exp, random
import matplotlib
# matplotlib.use('pgf')
matplotlib.rcParams.update({
    'pgf.texsystem': 'pdflatex',
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
    'figure.constrained_layout.use': True,
    'savefig.bbox': 'tight',
    #'axes.labelsize': 16,
    #'legend.fontsize': 16
    #'xtick.labelsize': 12,
    #'ytick.labelsize': 12
})

# long integral values
x = np.array([0.3643005509235264, 1.1591246830476258, 0.5139275454596316, 1.2037573894699727])
# energies of compton edges in MeV
y = np.array([0.340666666, 1.0617027983, 0.47733374509, 1.1181006769])
N = 4

m = ((N*sum(x*y)) - sum(x)*sum(y))/((N*sum(x**2))-(sum(x))**2)
c = ((sum(x**2)*sum(y))-(sum(x*y)*sum(x)))/((N*sum(x**2))-(sum(x)**2))
di=y-((m*x)+c)
um = sqrt(((sum(di**2)/((N*sum(x**2))-(sum(x)**2)))*(N/(N-2))))
uc = sqrt((((sum(di**2)*sum(x**2))/(N*((N*sum(x**2))-(sum(x)**2))))*(N/(N-2))))

print(f'm: {m} +/- {um}\nc: {c} +/- {uc}')

xmodel = np.linspace(min(x), max(x), 100)
plt.plot(xmodel, m*xmodel+c)
plt.errorbar(x, y, fmt='s')
plt.show()

# m: 0.9177884481407862 +/- 0.010299086583261487
# c: 0.005787603530313204 +/- 0.009196568624832134


# 22Na 1.274537 MeV compton edge at 1.1591246830476258
# Energy is 1.0617027983 MeV
# 22Na 0.511 MeV compton edge at 0.3643005509235264
# Energy is 0.340666666 MeV
# 137Cs 0.661657 MeV compton edge at 0.5139275454596316
# Energy is 0.47733374509 MeV
# 60Co 1.332492 MeV compton edge at 1.2037573894699727
# Energy is 1.1181006769 MeV