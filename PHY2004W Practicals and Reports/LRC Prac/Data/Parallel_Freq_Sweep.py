from matplotlib import pyplot as plt
import numpy as np
from scipy.signal import find_peaks
from numpy import cos, pi, sin, sqrt, exp, random
import matplotlib
#matplotlib.use('pgf')
matplotlib.rcParams.update({
    'pgf.texsystem': 'pdflatex',
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
})
# Extracting all the relevant data, sorting it into our data array, for use later
file = open('PHY2004W Practicals and Reports\LRC Prac\Data\Parallel_Freq_Sweep.txt', 'r')
header = file.readline()
lines = file.readlines()
N = len(lines)
i=0
# data[0] is the frequency
# data[1] is the voltage
data = np.zeros((2,N))
# Reading the file, getting the data into the data array
for line in lines:
    line = line.strip()
    columns = line.split()
    data[0][i] = float(columns[0])
    data[1][i] = float(columns[1])
    i += 1
file.close()
# Determining the resonant frequency and Q, the quality factor
# Finding the extremum and the "voltage" at that freq
resonantIndex=find_peaks(1*data[1])[0][0]
resFreq=data[0][resonantIndex]
resFreqVoltage=data[1][resonantIndex]
# Returns an array of indices for which the value of the function is less than max/sqrt(2)
# For parallel must be <=, for series must be >=
indices=np.where(data[1]<=(resFreqVoltage/sqrt(2)))
# Finding the first and last indices of the above array, aka roughly the points at which 
# the function is equal to max/sqrt(2)
A=indices[0][0]
B=indices[0][-1]
deltaF2=data[0][B]-data[0][A]
Q=resFreq/deltaF2
print('Resistance is 1000')
print('The Resonant Frequency is',resFreq,'Hz')
print('The Quality Factor is',Q)
print(A,B)
print(data[0][A],data[0][B],data[1][A],data[1][B])
print(data[1])

# Plotting the data
plt.figure()
plt.plot(data[0],data[1],color='b',linewidth=0.7,label='Parallel Sweep Data for 1000 Hz')
plt.plot(resFreq,resFreqVoltage,'gs',ms=3)
plt.plot(data[0][A],data[1][A],'rs',ms=3)
plt.plot(data[0][B],data[1][B],'rs',ms=3)
plt.xlabel('Frequency (Hz)')
plt.ylabel('$V_{out}/V_{in}$')
plt.legend()
plt.show()