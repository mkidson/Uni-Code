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
})
# Quick note, this will take quite a while to run, for me it took around 2 hours, so watch out
# Creates the random coordinates
numRuns = 100
N = 10000000
approxPi = np.zeros(numRuns)
for c in range(numRuns):
    xs = random.uniform(-1, 1, N)
    ys = random.uniform(-1, 1, N)
    inCircle = 0
    for i in range(N):
        if sqrt((xs[i]**2) + (ys[i]**2)) <= 1:
            inCircle += 1
    approxPi[c] = ((inCircle/N)*4)
    print((c/numRuns)*100, "%")
# A function to find the gaussian distribution
def gaussian(x, mu, sigma):
    return (1/(sigma*sqrt(2*pi)))*exp(-((x-mu)**2)/(2*sigma**2))
# Sorts things out for analysis, getting values we need
approxPi.sort()
dataMu = np.mean(approxPi)
dataSigma = sqrt(np.var(approxPi))
xplot = approxPi
yplot = gaussian(xplot, dataMu, dataSigma)
gaussianMax = gaussian(dataMu, dataMu, dataSigma)
trueGaussian = gaussian(xplot, 40, 2)
print("pi = ", dataMu, " +/- ", dataSigma/sqrt(numRuns))
# Defines some constants needed to make the histogram
binwidth = 0.0001
bins = np.arange(np.floor(min(approxPi)), np.floor(max(approxPi))+1, binwidth)
# Creates and plots the histogram
plt.hist(approxPi, bins, density=True, label=r'Approximation of $\pi$')
plt.xlabel(r'Approximation of $\pi$')
plt.ylabel('Occurrence')
plt.draw()
plt.xlim(min(approxPi), max(approxPi))
# Plots the graph, along with the legend and an annotation of the mean and std dev
plt.plot(xplot, yplot, 'r-', label='Gaussian Distribution')
plt.legend(loc='upper left')
plt.annotate(r'$\mu=$'+str(round(dataMu, 5))+'$; \sigma=$'+str(round(dataSigma, 5)), (dataMu, gaussianMax), textcoords='offset points', xytext=(10, 10), bbox=dict(facecolor='orange', edgecolor='black', boxstyle='round'))
# plt.savefig('ApproxPi3a.pgf')
plt.show()