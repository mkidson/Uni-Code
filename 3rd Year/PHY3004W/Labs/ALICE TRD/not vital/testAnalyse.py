from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
from numpy import cos, pi, sin, sqrt, exp, random
import matplotlib
# matplotlib.use('pgf')
matplotlib.rcParams.update({
    'pgf.texsystem': 'pdflatex',
    'font.family': 'sans-serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
    'figure.constrained_layout.use': True,
    'savefig.bbox': 'tight',
    #'axes.labelsize': 16,
    #'legend.fontsize': 16,
    #'xtick.labelsize': 12,
    #'ytick.labelsize': 12
})

data = np.genfromtxt('1.csv', delimiter=',')


t = np.arange(0,1000)
plt.plot(t, data[0])
plt.plot(t, data[1])
plt.plot(t, data[2])

plt.show()