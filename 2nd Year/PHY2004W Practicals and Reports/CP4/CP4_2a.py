from matplotlib import pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from numpy import cos, pi, sin, sqrt, exp, random
import matplotlib
matplotlib.use('pgf')
matplotlib.rcParams.update({
    'pgf.texsystem': 'pdflatex',
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
})
# Creates a numpy array to hold the data
data = np.zeros(60)
i = 0
# Reads the data and puts it into the array
f = open(r'PHY2004W Computational\CP4\Activity1Data.txt', 'r')
header = f.readline()
for line in f:
    line = line.strip()
    columns = line.split()
    data[i] = float(columns[1])
    i += 1
f.close()
data.sort()
# A function to compute a Gaussian
def gaussian(x, mu, sigma):
    return (1/(sigma*sqrt(2*pi)))*exp(-((x-mu)**2)/(2*(sigma**2)))
# Computes values for the gaussian plot
dataMu = np.mean(data)
dataSigma = sqrt(np.var(data))
xplot = data
yplot = gaussian(xplot, dataMu, dataSigma)
gaussianMax = gaussian(dataMu, dataMu, dataSigma)
trueGaussian = gaussian(xplot, 40, 2)
# Defines some things for the histogram plotting
binwidth = 0.5
bins = np.arange(np.floor(min(data)), np.floor(max(data))+1, binwidth)
# Creates and plots the histogram
hist = plt.hist(data, bins, density=True, label='Activity1Data')
plt.xlabel('x')
plt.ylabel('Occurrence')
plt.draw()
# Plots the gaussian
gaussian = plt.plot(xplot, yplot, 'r-', label='Actual Gaussian')
trueGaussian = plt.plot(xplot, trueGaussian, 'g-', label='Expected Gaussian')
# Plots the graph
plt.legend()
plt.annotate(r'$\mu=$'+str(round(dataMu, 3))+'$; \sigma=$'+str(round(dataSigma, 3)), (dataMu, gaussianMax), textcoords='offset points', bbox=dict(facecolor='orange', edgecolor='black', boxstyle='round'))
# plt.show()
plt.savefig('PHY2004W Computational\CP4\Activity1DataHist.pgf')