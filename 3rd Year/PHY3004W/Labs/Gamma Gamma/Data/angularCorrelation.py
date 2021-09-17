from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
from numpy import cos, pi, sin, sqrt, exp, random
import matplotlib
matplotlib.use('pgf')
matplotlib.rcParams.update({
    'pgf.texsystem': 'pdflatex',
    'font.family': 'sans-serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
    'figure.constrained_layout.use': True,
    'savefig.bbox': 'tight',
    'axes.labelsize': 16,
    'legend.fontsize': 16,
    'xtick.labelsize': 12,
    'ytick.labelsize': 12,
    # 'text.latex.preamble': r'\usepackage{amsmath}'
})

names = ['PHY3004W_gglab_Angular_Scan1.csv', 'PHY3004W_gglab_Angular_Scan2.csv', 'PHY3004W_gglab_Angular_Scan3.csv']

for name in names:
    data = np.genfromtxt(f'PHY3004W_gglab_angular_scans/{name}', delimiter=',', skip_header=8, unpack=True)
    # data[1:3]/=30

    plt.figure()
    # print(data)
    plt.scatter(data[0], data[1], label=r'$N_{\mathrm{red}}$', c='red', s=8)
    plt.scatter(data[0], data[2], label=r'$N_{\mathrm{blue}}$', c='blue', s=8)
    plt.plot(data[0], data[3], label=r'$N_{\mathrm{coincident}}$', color='g')
    plt.legend(loc='lower right')
    plt.xlabel('Angle (degrees)')
    plt.ylabel('Counts of gammas')
    plt.grid(color='#CCCCCC', linestyle=':')
    # print('--------------------------------')
    # print(f'Run {name[-5]}')
    # ratio = data[3]/data[1]
    # ratioUn = ratio*sqrt((sqrt(data[3])/data[3])**2 + (sqrt(data[1])/data[1])**2)
    # for i in range(len(data[0])):
    #     print(f'{data[0][i]}: {ratio[i]} +/- {ratioUn[i]}')
    plt.savefig(f'Plots/angular_{name[-5]}.pgf')
# plt.xlim(-100, 95)
# plt.show()