from matplotlib import pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from numpy import cos, pi, sin, sqrt, exp, random
import matplotlib
#matplotlib.use('pgf')
matplotlib.rcParams.update({
    'pgf.texsystem': 'pdflatex',
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
})

numRuns = 1000
N = 100000
approxPi = np.zeros(numRuns)
for c in range(numRuns):
    xs = random.uniform(-1, 1, N)
    ys = random.uniform(-1, 1, N)
    inCircle = 0
    for i in range(N):
        if sqrt((xs[i]**2) + (ys[i]**2)) <= 1:
            inCircle += 1

    approxPi[c] = ((inCircle/N)*4)

print(np.mean(approxPi), sqrt(np.var(approxPi)))
approxPi.sort()
def gaussian(x, mu, sigma):
    return (1/(sigma*sqrt(2*pi)))*exp(-((x-mu)**2)/(2*sigma**2))
dataMean = np.mean(approxPi)
dataSigma = sqrt(np.var(approxPi))
xplot = approxPi
yplot = gaussian(xplot, dataMean, dataSigma)
trueGaussian = gaussian(xplot, 40, 2)

binwidth = 0.0001
bins = np.arange(np.floor(min(approxPi)), np.floor(max(approxPi))+1, binwidth)
# Creates and plots the histogram
plt.hist(approxPi, bins, density=True)
plt.xlabel('x')
plt.ylabel('Occurrence')
plt.draw()
plt.xlim(3.1, 3.2)

plt.plot(xplot, yplot, 'r-')
plt.show()