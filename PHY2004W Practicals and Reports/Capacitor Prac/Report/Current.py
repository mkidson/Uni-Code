from matplotlib import pyplot as plt
import numpy as np
from numpy import cos, pi, sin, sqrt, exp, random
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
# data[0] is Time [s] - Current Resistor
# data[1] is Current [I] - Current Resistor
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
# Plotting both the applied voltage and the current measured through the resistor against time
plt.figure()
plt.plot(data[2], data[3], label='Applied Voltage', color='red', lw=0.5)
plt.plot(data[0], data[1], label='Resistor Current', color='blue', lw=1)
# Making it all look better
plt.legend(loc=1)
plt.xlabel("Time (s)")
plt.ylabel("Current (I)/Voltage (V)")
# plt.show()
plt.savefig('PHY2004W Practicals and Reports\Capacitor Prac\Current\Res_100Hz_15k.pgf')