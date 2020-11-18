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

file = open(r'PHY2004W Practicals and Reports\Hall Effect Prac\Report\Data\Forward Data.txt', 'r')
lines = file.readlines()
N = len(lines)
i=0
# 0 is current, 1 is Vparallel, 2 is Vperpendicular
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
# SI units
data[0]*=1e-3
data[2]*=1e-3
# Plotting the V things
plt.figure()
plt.plot(data[0],data[1],label='$V_\parallel$')
plt.plot(data[0],data[2],label='$V_\perp$')
plt.ylabel('$V$',rotation=0)
plt.xlabel('$I_S$')
plt.legend()
plt.show()
# V_H/I and V_\perp/V_\parallel
VH_I=data[2]/data[0]
VPerp_VParallel=data[2]/data[1]
# print(VH_I)
# print(VPerp_VParallel)
print(data[1]/data[0])
print(data[2]/data[0])