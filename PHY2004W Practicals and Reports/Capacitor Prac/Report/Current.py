from matplotlib import pyplot as plt
import numpy as np
from numpy import cos, pi, sin, sqrt, exp, random
from scipy.signal import find_peaks
import matplotlib
matplotlib.use('pgf')
matplotlib.rcParams.update({
    'pgf.texsystem': 'pdflatex',
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
})

file = open('PHY2004W Practicals and Reports\Capacitor Prac\Current\Res_100Hz_15k.txt', 'r')
header = file.readline()
lines = file.readlines()
N = len(lines)
i=0
# data[0] is Time [s] - Resistor Voltage
# data[1] is Current [I] - Resistor Voltage
# data[2] is Time [s] - Voltage Source
# data[3] is Voltage [V] - Voltage Source
data = np.zeros((4, N))
# Reading the file, getting the data into the data array
for line in lines:
    line = line.strip()
    columns = line.split()
    data[0][i] = float(columns[0])
    data[1][i] = float(columns[1])
    data[2][i] = float(columns[2])
    data[3][i] = float(columns[3])
    i += 1
file.close()
# data[1]=data[1]/15000
# Finding the peaks of each
ResPeaks=find_peaks(data[1], distance=3)
AppPeaks=find_peaks(data[3], distance=3)
pi2Arr=np.concatenate((data[0][ResPeaks[0][1]]-data[0][ResPeaks[0][0]], data[0][ResPeaks[0][2]]-data[0][ResPeaks[0][1]], data[0][ResPeaks[0][3]]-data[0][ResPeaks[0][2]], data[0][AppPeaks[0][1]]-data[0][AppPeaks[0][0]], data[0][AppPeaks[0][2]]-data[0][AppPeaks[0][1]], data[0][AppPeaks[0][3]]-data[0][AppPeaks[0][2]]),axis=None)
pi2=np.average(pi2Arr)
print(pi2)
diffs=np.concatenate((data[0][AppPeaks[0][0]]-data[0][ResPeaks[0][0]], data[0][AppPeaks[0][1]]-data[0][ResPeaks[0][1]], data[0][AppPeaks[0][2]]-data[0][ResPeaks[0][2]], data[0][AppPeaks[0][3]]-data[0][ResPeaks[0][3]]), axis=None)
diff=np.average(diffs)
print(diff)
print(diff/pi2)
print(2*diff/pi2)

# Plotting both the applied voltage and the voltage measured across the resistor against time
plt.figure()
plt.plot(data[2], data[3], label='Applied Voltage', color='red', lw=0.5)
plt.plot(data[0], data[1], label='Resistor Voltage', color='blue', lw=1)
# Making it all look better
plt.legend(loc=1)
plt.xlabel("Time (s)")
plt.ylabel("Voltage (V)")
# plt.show()
plt.savefig('PHY2004W Practicals and Reports\Capacitor Prac\Current\Res_100Hz_15k.pgf')