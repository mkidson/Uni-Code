from matplotlib import pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import matplotlib 
matplotlib.use("pgf")
matplotlib.rcParams.update({
    "pgf.texsystem": "pdflatex",
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
})
# File reading and initialisation of variables
file = open('PHY2004W Computational\CP2\LinearWithErrors.txt', 'r')
header = file.readline()
lines = file.readlines()
i = 0
N = len(lines)
data = np.zeros((3, N))
p0 = [1, 1] # Initial guess, not that significant as long as it's reasonable
for line in lines:
    line = line.strip()
    columns = line.split()
    data[0, i] = float(columns[0])
    data[1, i] = float(columns[1])
    data[2, i] = float(columns[2])
    i += 1
file.close()
# Defines the function that the curve_fit function uses
def f(x, m, c):
    return m*x+c
# Plots the Levenberg-Marquardt best fit
popt, pcov = curve_fit(f, data[0], data[1], p0, sigma=data[2], absolute_sigma=True)
dof = len(data[1])-len(popt)
# Initialises variables used for plotting the contour plot and plots it
Npts = 10000
mscan = np.zeros(Npts)
cscan = np.zeros(Npts)
chi_dof = np.zeros(Npts)
ncols = 1000
c = 0
for mpar in np.linspace(0.5, 0.7, 100, True):
    for cpar in np.linspace(0.5, 1.7, 100, True):
        mscan[c] = mpar
        cscan[c] = cpar
        dymin = (data[1]-f(data[0], mpar, cpar))/data[2]
        chi_dof[c] = sum(dymin*dymin)/dof
        c += 1
plt.figure()
# Plots the contour and saves it
plt.tricontourf(mscan, cscan, chi_dof, ncols)
plt.colorbar()
plt.savefig('PHY2004W Computational\CP2\CP2b_Contour_Plot.pgf')