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

file = open('PHY2004W Practicals and Reports\Induction\Report\Data\FieldAxisData.txt', 'r')
header = file.readline()
lines = file.readlines()
N = len(lines)
i=0
data = np.zeros((2,N))
# Reading the file, getting the data into the data array
for line in lines:
    line = line.strip()
    columns = line.split()
    data[0][i] = float(columns[0])
    data[1][i] = float(columns[1])
    i += 1
file.close()
# Converting the data to SI
data[0]*=1e-2
data[1]*=1e-3*0.5
# Defining some useful constants
mu0=pi*4e-7
omega=1000*2*pi
omegaUn=0.02*omega
primaryCoilWinds=120
secondaryCoilWinds=175
# Radius measured in m
primaryCoilRadius=3.4e-2
primaryCoilRadiusUn=0.05e-2
secondaryCoilRadius=6.5e-3
SecondaryCoilRadiusUn=0.05e-2
# Area measured in m^2
primaryCoilArea=pi*primaryCoilRadius**2
primaryCoilAreaUn=2*pi*primaryCoilRadius*primaryCoilRadiusUn
secondaryCoilArea=pi*secondaryCoilRadius**2
secondaryCoilAreaUn=2*pi*secondaryCoilRadius*SecondaryCoilRadiusUn
# Current measured in amps
measuredCurrent=0.494975
measuredCurrentUn=0.02857738033
# An array used for plotting the theoretical values
distances=np.linspace(-0.1,0.05,1000)
# The Functions used to calculate B in different ways
def experimentalMagField(emf):
    return emf/(secondaryCoilWinds*secondaryCoilArea*omega)
def theoreticalMagField(z):
    return (mu0*primaryCoilWinds*measuredCurrent/2)*(((primaryCoilRadius)**2)/((primaryCoilRadius**2 + z**2)**(3/2)))

experimentalMax=max(experimentalMagField(data[1]))
theoreticalMax=max(theoreticalMagField(data[0]))
scaleFactor=experimentalMax/theoreticalMax
print(experimentalMax,theoreticalMax)
# Uncertainty calculations, my favourite
calibrationFactor=1/(secondaryCoilWinds*secondaryCoilArea*omega)
# This is 2% of the scale that the oscilloscope was at, 1 V
experimentalEmfUn=sqrt((1e-5/(2*sqrt(3)))**2 + (0.02)**2)*0.5
experimentalBUn=[]
for emf in data[1]:
    experimentalBUn.append((emf*calibrationFactor)*sqrt((experimentalEmfUn/emf)**2 + (secondaryCoilAreaUn/secondaryCoilArea)**2 + (omegaUn/omega)))

plt.errorbar(data[0],experimentalMagField(data[1]),yerr=experimentalBUn,fmt='bs',ms=3,elinewidth=1,capsize=4,label='Experimental Data')
plt.plot(distances,theoreticalMagField(distances),'r',label='Theoretical Model')
plt.xlabel('Distance Along the Primary Axis (m)')
plt.ylabel('Amplitude of the Magnetic Field (T)')
plt.legend()
plt.grid(color='#CCCCCC', linestyle=':')
plt.show()
# plt.savefig(r'PHY2004W Practicals and Reports\Induction\Report\Data\FieldAxisData.pgf')