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
})

names = ['PHY3004W_gglab_Angular_Scan1.csv', 'PHY3004W_gglab_Angular_Scan2.csv', 'PHY3004W_gglab_Angular_Scan3.csv']

for name in names:
    data = np.genfromtxt(f'PHY3004W_gglab_angular_scans/{name}', delimiter=',', skip_header=8, unpack=True)


    # plt.figure()
    # print(data)
    # plt.plot(data[0], data[1])
    # plt.plot(data[0], data[2])
    plt.plot(data[0], data[3]/max(data[3]))
plt.show()