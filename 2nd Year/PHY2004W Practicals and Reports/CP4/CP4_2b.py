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
# Creates random data to use, with specific mean and standard deviation and writes it to a file
N = 600
data = random.normal(40, 2, N)
writeFile = open(r"PHY2004W Computational\CP4\RandomisedData.txt", 'w+')
writeFile.write("Random numbers drawn from Gaussian with mu = 40.0 and sigma = 2.0\n")
c = 0
for i in data:
    c+=1
    writeFile.write(str(c)+" "+str(round(i, 3))+"\n")
writeFile.close()
# Creates a numpy array to hold the data
data2 = np.zeros(N)
i = 0
# Reads the data and puts it into the array
f = open(r"PHY2004W Computational\CP4\RandomisedData.txt", 'r')
header = f.readline()
for line in f:
    line = line.strip()
    columns = line.split()
    data2[i] = float(columns[1])
    i += 1
f.close()
data2.sort()
# A function to compute a Gaussian
def gaussian(x, mu, sigma):
    return (1/(sigma*sqrt(2*pi)))*exp(-((x-mu)**2)/(2*sigma**2))
# Computes values for the gaussian plot
dataMu = np.mean(data2)
dataSigma = sqrt(np.var(data2))
xplot = data2
yplot = gaussian(xplot, dataMu, dataSigma)
gaussianMax = gaussian(dataMu, dataMu, dataSigma)
trueGaussian = gaussian(xplot, 40, 2)
# Defines some things for the histogram plotting
binwidth = 0.5
bins = np.arange(np.floor(min(data2)), np.floor(max(data2))+1, binwidth)
# Creates and plots the histogram
hist = plt.hist(data2, bins, density=True, label='Randomised Data')
plt.xlabel('x')
plt.ylabel('Occurrence')
plt.draw()
# Plots the gaussian and the expected gaussian
gaussian = plt.plot(xplot, yplot, 'r-', label='Actual Gaussian')
trueGaussian = plt.plot(xplot, trueGaussian, 'g-', label='Expected Gaussian')
# plt.show()
plt.legend(loc='upper left')
plt.annotate(r'$\mu=$'+str(round(dataMu, 3))+'$; \sigma=$'+str(round(dataSigma, 3)), (dataMu, gaussianMax), textcoords='offset points', bbox=dict(facecolor='orange', edgecolor='black', boxstyle='round'))
plt.savefig('PHY2004W Computational\CP4\RandomisedDataHist600_1.pgf')