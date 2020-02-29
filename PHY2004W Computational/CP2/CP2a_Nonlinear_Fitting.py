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
file = open('PHY2004W Computational\CP2\DampedData1.txt', 'r')
header = file.readline()
lines = file.readlines()
i = 0
N = len(lines)
data = np.zeros((2, N))
u = [0.001]*N
p0 = [0.28, 0.04, 0.4, 30, 0] # My best guess for the parameters, by observation
name = ['A', 'B', 'gamma', 'omega', 'alpha']

for line in lines:
    line = line.strip()
    columns = line.split()
    data[0, i] = float(columns[0])
    data[1, i] = float(columns[1])
    i += 1
file.close()
# Plots the data
plt.errorbar(data[0], data[1], u, fmt='_b', lw=0.5, capsize=2, capthick=0.5, markersize=4, markeredgewidth=0.5, label='Data')
# Defines the function that the curve_fit function uses
def f(t, A, B, gamma, omega, alpha):
    return A+(B*np.exp(-gamma*t))*np.cos((omega*t)-alpha)

# Plots my best guess
tmodel = np.linspace(0.0, 5.0, 1000)
ystart = f(tmodel, *p0)
plt.plot(tmodel, ystart, '-g', lw=0.5, label='Initial Guess')
plt.legend()
plt.savefig('PHY2004W Computational/CP2/CP2a_Initial_Guess.pgf')

# Plots the Levenberg-Marquardt best fit
popt, pcov = curve_fit(f, data[0], data[1], p0, sigma=u, absolute_sigma=True)
yfit = f(tmodel, *popt)
plt.plot(tmodel, yfit, '-r', lw=0.5, label='Best Fit [1.03]')

# Calculates chi squared and does magic to work out the fit paramters
dymin = (data[1]-f(data[0], *popt))/u
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
# Finally saves the best fit curve
plt.legend()
plt.savefig('PHY2004W Computational/CP2/CP2a_Best_Fit.pgf')