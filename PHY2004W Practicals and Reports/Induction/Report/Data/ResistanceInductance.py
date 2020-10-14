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
# The usual stripping of data from the files
file = open('PHY2004W Practicals and Reports\Induction\Report\Data\InductanceData.txt', 'r')
header = file.readline()
lines = file.readlines()
N = len(lines)
i=0
# data[0] is frequency (not omega), data[1] is primary coil emf. data[2] is axial coil emf
data = np.zeros((3,N))
# Reading the file, getting the data into the data array
for line in lines:
    line = line.strip()
    columns = line.split()
    data[0][i] = float(columns[0])
    data[1][i] = float(columns[1])
    data[2][i] = float(columns[2])
    i += 1
file.close()
# Converting to Volts and rad/s, now data[0] is omega, not f
data[1]*=0.5
data[0]*=2*pi
# Current measured in amps
theoreticalCurrent=0.8
measuredCurrent=0.806101
measuredCurrentUn=0.02857738033
# The function for curve_fit
def emfFromFreq(omega,R,L):
    return theoreticalCurrent*sqrt(R**2 + (L**2)*(omega**2))
# Things needed for curve_fit
freqs=np.linspace(200*pi,4000*pi,N,endpoint=True)
u=[sqrt((1e-2/(2*sqrt(3)))**2 + (2)**2)*0.5]*N
print(u)
p0=[10,0.01]
# Jackknife curve_fitting
jackknifeData = np.zeros((4, N, N-1))
for c in range(N):
    r = random.randint(0, N)
    jackknifeData[0, c] = np.delete(data[0], r)
    jackknifeData[1, c] = np.delete(data[1], r)
    jackknifeData[2, c] = np.delete(u, r)
    jackknifeData[3, c] = np.delete(freqs, r)
# Fitting to the jackknifed datasets
jackknifeFits = np.zeros((N, N-1))
popts = []
for k in range(N):
    popt, pcov = curve_fit(emfFromFreq, jackknifeData[0, k], jackknifeData[1, k], p0, sigma=jackknifeData[2, k], absolute_sigma=True)
    jackknifeFits[k] = emfFromFreq(jackknifeData[3, k], *popt)
    popts.append(popt)
# Isolating arrays of each optimal fitting parameter
poptNp = np.zeros((2, N))
for d, ds in enumerate(popts):
    poptNp[0, d] = ds[0]
    poptNp[1, d] = ds[1]
# Calculating means and standard uncertainties
pOptimals = np.zeros((2, 2))
for j, js in enumerate(poptNp):
    mean = np.mean(js)
    pOptimals[0][j] = mean
    sumI = 0
    for i in js:
        sumI += (i-mean)**2
    pOptimals[1][j] = sqrt(float(((N-1)/N)*sumI))/sqrt(N-1)
# Plotting the function with the optimal parameters
yfit=emfFromFreq(freqs,*pOptimals[0])
print('Resistance of the Large Coil:',pOptimals[0][0],'+/-',pOptimals[1][0])
print('Inductance of the Large Coil:',pOptimals[0][1],'+/-',pOptimals[1][1])
# Plotting but more
plt.errorbar(data[0],data[1],yerr=u,fmt='bs',ms=3,elinewidth=0.7,capsize=3,label='Experimental Data')
plt.plot(freqs,yfit,'r',label='curve\_fit Approximation')
plt.xlabel('Angular Frequency $\omega$ (rad/s)')
plt.ylabel('Amplitude of Voltage Across the Large Coil (V)')
plt.legend()
plt.show()
# plt.savefig(r'PHY2004W Practicals and Reports\Induction\Report\Data\ResistanceInductance.pgf')