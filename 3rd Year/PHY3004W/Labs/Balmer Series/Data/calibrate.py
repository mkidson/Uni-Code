from matplotlib import pyplot as plt
import numpy as np
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

# region Ingest Data
data0, data1 = np.genfromtxt(r'3rd Year\PHY3004W\Labs\Balmer Series\Data\BalmerCalibrationJoJoSaSaMiMi.csv', delimiter=',', skip_header=14, unpack=True)

data = np.array((data0, data1))
# endregion

data[1] /= sum(data[1])

def gaussian(x, mu, sigma):
    return (1/(sigma*sqrt(2*pi)))*exp(-(1/2)*((x-mu)/sigma)**2)

popt, pcov = curve_fit(gaussian, data[0], data[1], p0=[6328,1])
xmodel = np.linspace(min(data[0]), max(data[0]), 1000)

print(popt)

plt.plot(xmodel, gaussian(xmodel, *popt))
plt.step(data[0], data[1])
plt.show()