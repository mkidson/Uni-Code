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
x = np.array([0.34515502437962947, 1.1035574567183923, 0.4877006303285822, 1.1481204129710332])
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

# m: 0.9603817487213419 +/- 0.009490966753604687
# c: 0.008868546534848159 +/- 0.008071512642620725


# 22Na 0.511 MeV compton edge at 0.34515502437962947
# Energy is 0.340666666 MeV
# 22Na 1.274537 MeV compton edge at 1.1035574567183923
# Energy is 1.0617027983 MeV
# 137Cs 0.661657 MeV compton edge at 0.4877006303285822
# Energy is 0.47733374509 MeV
# 60Co 1.332492 MeV compton edge at 1.1481204129710332
# Energy is 1.1181006769 MeV