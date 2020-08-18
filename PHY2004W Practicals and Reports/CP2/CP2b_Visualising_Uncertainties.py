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
p0 = np.array([1, 1])
name = np.array(['m', 'c'])
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
ncols = 400
c = 0
for mpar in np.linspace(0.5, 0.7, 100, True):
    for cpar in np.linspace(0.5, 1.7, 100, True):
        mscan[c] = mpar
        cscan[c] = cpar
        dymin = (data[1]-f(data[0], mpar, cpar))/data[2]
        chi_dof[c] = sum(dymin*dymin)/dof
        c += 1
plt.figure(1)
# Plots the contour and saves it
plt.title('$\\frac{\\chi^2}{\\texttt{dof}}$ for various values of m and c', pad=15)
plt.xlabel('m')
plt.ylabel('c', rotation = 0)
cntPlt = plt.tricontourf(mscan, cscan, chi_dof, ncols, cmap='jet', levels=np.linspace(0, 40, 41))
for r in cntPlt.collections:
    r.set_edgecolor("face")
cbar = plt.colorbar()
cbar.set_label('$\\frac{\\chi^2}{\\texttt{dof}}$', rotation=0)
plt.savefig('PHY2004W Computational\CP2\CP2b_Contour_Plot.pgf')

plt.figure(2)
plt.errorbar(data[0], data[1], data[2], fmt='_b', lw=0.5, capsize=2, capthick=0.5, markersize=4, markeredgewidth=0.5, label='Data')
# Beginning of analysis of parameters
tmodel = np.linspace(1, 12, 1000)
yfit = f(tmodel, *popt)
plt.plot(tmodel, yfit, '-r', lw=0.5, label='Best Fit')
# Calculates chi squared and does magic to work out the fit paramters
dymin = (data[1]-f(data[0], *popt))/data[2]
min_chisq = sum(dymin*dymin)
dof = len(data[0]) - len(popt)

print('Chi Squared:', round(min_chisq, 5))
print('Number of Degrees of Freedom:', round(dof, 5))
print('Chi Squared per Degree of Freedom:', round(min_chisq/dof, 5))
print()

print('Fitted paramters with 68% C.I.:')
for i, pmin in enumerate(popt):
    print('%2i %-10s %12f +/- %10f'%(i, name[i], pmin, np.sqrt(pcov[i,i])*np.sqrt(min_chisq/dof)))
print()
perr = np.sqrt(np.diag(pcov))
print('Perr:', perr)
# Calculates and prints the Correlation matrix
print('Correlation matrix:')
print('          ', end='')
for i in range(len(popt)): print('%10s'%(name[i],), end=''),
print()
for i in range(len(popt)):
    print('%10s'%(name[i]), end=''),
    for j in range(i+1):
        print('%10f'%(pcov[i,j]/np.sqrt(pcov[i,i]*pcov[j,j]),), end=''),
    print()

plt.legend()
plt.savefig('PHY2004W Computational\CP2\CP2b_Data_Plot.pgf')