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
data[2]*=1e-3*0.5
data[0]*=2*pi
# Defining some useful constants
mu0=pi*4e-7
primaryCoilWinds=120
secondaryCoilWinds=175
# Radius measured in m
primaryCoilRadius=3.4e-2
primaryCoilRadiusUn=0.05e-2
secondaryCoilRadius=6.5e-3
SecondaryCoilRadiusUn=0.05e-2
# Area measured in m^2
secondaryCoilArea=pi*secondaryCoilRadius**2
secondaryCoilAreaUn=2*pi*secondaryCoilRadius*SecondaryCoilRadiusUn
# Current measured in amps
measuredCurrent=0.806101
measuredCurrentUn=0.02857738033
# Linear least squares fit to find slope of correlation
x=data[0]
y=data[2]
m = ((N*sum(x*y)) - sum(x)*sum(y))/((N*sum(x**2))-(sum(x))**2)
c = ((sum(x**2)*sum(y))-(sum(x*y)*sum(x)))/((N*sum(x**2))-(sum(x)**2))
di=y-((m*x)+c)
um = sqrt(((sum(di**2)/((N*sum(x**2))-(sum(x)**2)))*(N/(N-2))))
uc = sqrt((((sum(di**2)*sum(x**2))/(N*((N*sum(x**2))-(sum(x)**2))))*(N/(N-2))))
# Calculating B from the induced voltages (expression 1) and its uncertainty (easier here)
Bs=np.zeros(N)
experimentalBUn=np.zeros(N)
experimentalEmfUn=sqrt((1e-5/(2*sqrt(3)))**2 + (0.02)**2)*0.5
for index,freq in enumerate(data[0]):
    calibrationFactor=1/(secondaryCoilWinds*secondaryCoilArea*freq)
    Bs[index]=(data[2][index]*calibrationFactor)
    experimentalBUn[index]=((data[2][index]*calibrationFactor)*sqrt((experimentalEmfUn/data[2][index])**2 + (secondaryCoilAreaUn/secondaryCoilArea)**2 + (1000*2*pi*0.02/freq)))
BAverage=np.mean(Bs)
# Calculating B from expression 2
B2=(mu0*primaryCoilWinds*measuredCurrent)/(2*primaryCoilRadius)
# Finding "expected" gradient value
expectedM1=secondaryCoilArea*secondaryCoilWinds*BAverage
expectedM2=secondaryCoilArea*secondaryCoilWinds*B2
# Uncertainties
BAverageUn=(1/N)*sqrt(np.sum(experimentalBUn**2))
B2Un=B2*sqrt((measuredCurrentUn/measuredCurrent)**2 + (primaryCoilRadiusUn/primaryCoilRadius)**2)
expectedM1Un=expectedM1*sqrt((BAverageUn/BAverage)**2 + (secondaryCoilAreaUn/secondaryCoilArea)**2)
expectedM2Un=expectedM2*sqrt((B2Un/B2)**2 + (secondaryCoilAreaUn/secondaryCoilArea)**2)
axialEmfUn=0.02*np.mean(data[2])
# Printing results
print('Gradient from Linear fit:',m,'+/-',um)
print('Average B amplitude from axial emf:',BAverage,'+/-',BAverageUn)
print('B determined from expression 2:',B2,'+/-',B2Un)
print('Gradient expected, from expression 1:',expectedM1,'+/-',expectedM1Un)
print('Gradient expected, from expression 2:',expectedM2,'+/-',expectedM2Un)
# Plotting
freqs=np.linspace(200*pi,4000*pi,10000,endpoint=True)
plt.errorbar(data[0],data[2],yerr=axialEmfUn,fmt='bs',ms=2,elinewidth=0.7,capsize=3,label='Axial (induced) emf')
plt.plot(freqs,(freqs*m)+c,'r',label='Linear Least Squares Fit')
plt.xlabel('Angular Frequency $\omega$ (rad/s)')
plt.ylabel('Amplitude of the Induced emf (V)')
plt.legend()
plt.show()
# plt.savefig(r'PHY2004W Practicals and Reports\Induction\Report\Data\EmfPropToFreq.pgf')