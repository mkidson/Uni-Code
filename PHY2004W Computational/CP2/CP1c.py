import scipy.stats as stats
from math import sqrt
from matplotlib import pyplot as plt
import matplotlib
from scipy.optimize import curve_fit
import numpy as np
matplotlib.use("pgf")
matplotlib.rcParams.update({
    "pgf.texsystem": "pdflatex",
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
})

f = open('PHY2004W Computational\CP2\LinearNoErrors.txt', 'r')
header = f.readline()
N = 12
data = np.zeros([3, N])
i = 0
p0 = np.array([1, 1])
name = np.array(['m', 'c'])
for line in f:
    data[0, i] = line.split()[0]
    data[1, i] = line.split()[1]
    data[2, i] = 1
    i += 1
f.close()

xy = []
for c in range(N):
    xy.append(round(data[0, c]*data[1,c], 3))
x2 = []
for t in range(N):
    x2.append(round(data[0,t]**2, 3))

x = data[0]
y = data[1]
d = []
d2 = []
m = ((N*sum(xy)) - sum(x)*sum(y))/((N*sum(x2))-(sum(x))**2)
c = ((sum(x2)*sum(y))-(sum(xy)*sum(x)))/((N*sum(x2))-(sum(x)**2))

for r in range(N):
    d.append(y[r] - ((m*x[r]) + c))
    d2.append(d[r]**2)
um = sqrt(((sum(d2)/((N*sum(x2))-(sum(x)**2)))*(N/(N-2))))
uc = sqrt((((sum(d2)*sum(x2))/(N*((N*sum(x2))-(sum(x)**2))))*(N/(N-2))))

print("m:", round(m, 5))
print("u(m):", round(um, 5))
print("c:", round(c, 5))
print("u(c):", round(uc, 5))
print()
# Plots the data and the line of best fit calculated above
xLine = np.arange(1, 12.5, 0.1)
yLine = []
for i in xLine:
    yLine.append((m*i)+c)
plt.figure(1)
plt.plot(xLine, yLine, color='blue', label="Best Fit", lw=1)
plt.errorbar(data[0], data[1], fmt='ob', lw=0.5, capsize=2, capthick=0.5, markersize=4, markeredgewidth=0.5, label='Data')
# Plots the line of best fit using curve_fit
def f(x, m, c):
    return (m*x)+c
popt, pcov = curve_fit(f, data[0], data[1], p0, sigma=data[2], absolute_sigma=True)
dof = len(y)-len(popt)
tmodel = np.linspace(1, 12, 1000)
ystart = f(tmodel, *p0)
yfit = f(tmodel, *popt)
plt.plot(tmodel, yfit, '-r', lw=0.5, label='curve fit Best Fit')
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.title("Comparison of Experimental Data with Theoretical Prediction")
plt.xlim(0,13)
plt.legend()
plt.savefig('PHY2004W Computational\CP2\CP1c_Data_Plot.pgf')
# Calculates chi squared and does magic to work out the fit paramters
dymin = (y-f(x, *popt))/data[2]
min_chisq = sum(dymin*dymin)
dof = len(x) - len(popt)

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
# Initialises variables 
Npts = 10000
mscan = np.zeros(Npts)
cscan = np.zeros(Npts)
chi_dof = np.zeros(Npts)
ncols = 25
c = 0
for mpar in np.linspace(0.5, 0.7, 100, True):
    for cpar in np.linspace(0.5, 1.7, 100, True):
        mscan[c] = mpar
        cscan[c] = cpar
        dymin = (data[1]-f(data[0], mpar, cpar))/data[2]
        chi_dof[c] = sum(dymin*dymin)/dof
        c += 1
plt.figure(2)
# Plots the contour and saves it
plt.title('$\\frac{\\chi^2}{\\texttt{dof}}$ for various values of m and c', pad=15)
plt.xlabel('m')
plt.ylabel('c', rotation = 0)
cntPlt = plt.tricontourf(mscan, cscan, chi_dof, ncols, cmap='jet', levels=np.linspace(0, 40, 41))
for r in cntPlt.collections:
    r.set_edgecolor("face")
cbar = plt.colorbar()
cbar.set_label('$\\frac{\\chi^2}{\\texttt{dof}}$', rotation=0)
plt.savefig('PHY2004W Computational\CP2\CP1c_Contour_Plot.pgf')