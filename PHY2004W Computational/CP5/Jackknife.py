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
# Some starting constants and arrays needed, as well as opening the DampedData file
file = open('PHY2004W Computational\CP5\DampedData1.txt', 'r')
header = file.readline()
lines = file.readlines()
i = 0
N = len(lines)
data = np.zeros((2, N))
jackknifeData = np.zeros((2, N, N-1))
u = [0.001]*(N-1)
p0 = [0.28, 0.04, 0.4, 30, 0]
# Reading the file, getting the data into the data array
for line in lines:
    line = line.strip()
    columns = line.split()
    data[0, i] = float(columns[0])
    data[1, i] = float(columns[1])
    i += 1
file.close()
# The function that we give to curve_fit
def f(t, A, B, gamma, omega, alpha):
    return A+(B*np.exp(-gamma*t))*np.cos((omega*t)-alpha)
# Removes random values from the data sets
for c in range(N):
    r = random.randint(0, 250)
    jackknifeData[0, c] = np.delete(data[0], r)
    jackknifeData[1, c] = np.delete(data[1], r)
# Fitting to the jackknifed datasets
tmodel = np.linspace(0.0, 5.0, N-1)
jackknifeFits = np.zeros((N, N-1))
popts = []
for k in range(N):
    popt, pcov = curve_fit(f, jackknifeData[0, k], jackknifeData[1, k], p0, sigma=u, absolute_sigma=True)
    jackknifeFits[k] = f(tmodel, *popt)
    popts.append(popt)
# Isolating arrays of each optimal fitting parameters
poptNp = np.zeros((5, N))
for d, ds in enumerate(popts):
    poptNp[0, d] = ds[0]
    poptNp[1, d] = ds[1]
    poptNp[2, d] = ds[2]
    poptNp[3, d] = ds[3]
    poptNp[4, d] = ds[4]
AMean = np.mean(poptNp[0])
AUn = sqrt(np.var(poptNp[0]))/(N-1)
BMean = np.mean(poptNp[1])
BUn = sqrt(np.var(poptNp[1]))/(N-1)
gammaMean = np.mean(poptNp[2])
gammaUn = sqrt(np.var(poptNp[2]))/(N-1)
omegaMean = np.mean(poptNp[3])
omegaUn = sqrt(np.var(poptNp[3]))/(N-1)
alphaMean = np.mean(poptNp[4])
alphaUn = sqrt(np.var(poptNp[4]))/(N-1)

print(AUn, BUn, gammaUn, omegaUn, alphaUn)