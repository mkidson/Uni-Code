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
file = open(r'PHY2004W Practicals and Reports\Skin Effect Prac\Report\Data\Skin_Data_Text.txt', 'r')
header = file.readline()
lines = file.readlines()
N = len(lines)
i=0
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
# Some constants
R=20e-3
RUn=0.1e-3
d=1e-3
dUn=0.1e-3
mu=1.256629e-6
# Converting to SI and amplitudes
data[0]*=2*pi
data[1]*=0.5*1e-3
data[2]*=0.5*1e-3
# Ratio of mag fields = ratio of emfs
yData=data[2]/data[1]
# Uncertainties on these measured values
omegaUn=0.02*2000*pi
emfUn=sqrt(0.02**2 + (0.0001/(2*sqrt(3)))**2)*0.5
yDataUn=np.zeros(N)
for m,ms in enumerate(yData):
    yDataUn[m]=ms*sqrt((emfUn/data[1][m])**2 + (emfUn/data[2][m])**2)
# Function for curve_fit
def func(omega,sigma):
    return 1/(sqrt(1+((R*d)/((2)/(mu*sigma*omega)))**2))
# Array used to plot the optimised function and initial guess
xModel=np.linspace(data[0][0],data[0][-1],N,endpoint=True)
p0=[1e7]
numParams=len(p0)
# Jackknife Curve Fitting
jackknifeData = np.zeros((4, N, N-1))
popts=np.zeros((numParams,N))
for c in range(N):
    # Removing random values from each array
    r = random.randint(0, N)
    jackknifeData[0][c] = np.delete(data[0], r)
    jackknifeData[1][c] = np.delete(yData, r)
    jackknifeData[2][c] = np.delete(yDataUn, r)
    jackknifeData[3][c] = np.delete(xModel, r)
    # Fitting N times
    popt, pcov = curve_fit(func, jackknifeData[0][c], jackknifeData[1][c], p0, sigma=jackknifeData[2][c], absolute_sigma=True)
    popts[0][c]=popt
# Means and standard uncertainties of the parameters
pOptimals=np.zeros((2,numParams))
for j, js in enumerate(popts):
    pMean=np.mean(js)
    pOptimals[0][j]=pMean
    sumI=0
    for i in js:
        sumI+=(i-pMean)**2
    # Jackknife method for determining uncertainties of fitted parameters
    pOptimals[1][j]=sqrt(float(((N-1)/N)*sumI))/sqrt(N-1)
# Printing optimal parameters
print('sigma =',pOptimals[0][0],'+/-',pOptimals[1][0])
# Plotting the function with the optimal parameters
yfit=func(xModel,*pOptimals[0])
plt.errorbar(data[0],yData,yerr=yDataUn,fmt='bs',ms=3,elinewidth=1,capsize=4,label='Experimental Data')
plt.plot(xModel,yfit,'r',label='curve\_fit Approximation')
plt.xlabel('Angular Frequency $\omega$ (rad/s)')
plt.ylabel('$\epsilon(d)/\epsilon(0)$')
plt.grid(color='#CCCCCC', linestyle=':')    
plt.legend()
# plt.show()
plt.savefig(r'PHY2004W Practicals and Reports\Skin Effect Prac\Report\Data\SkinEffect.pgf')