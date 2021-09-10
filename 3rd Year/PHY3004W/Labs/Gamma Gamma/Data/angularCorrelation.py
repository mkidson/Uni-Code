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
    'axes.labelsize': 16,
    'legend.fontsize': 16,
    'xtick.labelsize': 12,
    'ytick.labelsize': 12
})

names = ['PHY3004W_gglab_Angular_Scan1.csv', 'PHY3004W_gglab_Angular_Scan2.csv', 'PHY3004W_gglab_Angular_Scan3.csv']

for name in names:
    data = np.genfromtxt(f'PHY3004W_gglab_angular_scans/{name}', delimiter=',', skip_header=8, unpack=True)


    plt.figure()
    # print(data)
    plt.scatter(data[0], data[1], label='Red', c='red', s=8)
    plt.scatter(data[0], data[2], label='Blue', c='blue', s=8)
    plt.plot(data[0], data[3], label='Coincident Events', color='g')
    plt.legend()
plt.xlabel('Angle (degrees)')
plt.ylabel('Coincident gammas count')
# plt.xlim(-100, 95)
plt.show()