from matplotlib import pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from numpy import cos, pi, sin, sqrt, exp, random
import matplotlib
matplotlib.rcParams.update({
    'pgf.texsystem': 'pdflatex',
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
})

file = open(r'PHY2004W Practicals and Reports\Hall Effect Prac\Report\Data\Backward Data.txt', 'r')
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
# Uncertainties
u=np.zeros((3,N))
for cIndex in range(N):
    u[0][cIndex]=sqrt(((0.1e-3)/(2*sqrt(3)))**2 + (0.01*100e-3)**2)
    u[1][cIndex]=sqrt(((0.01)/(2*sqrt(3)))**2 + (0.01*10)**2)
    u[2][cIndex]=sqrt(((0.1e-3)/(2*sqrt(3)))**2 + (0.01*100e-3)**2)
# Straight line with gradient from first 2 values
iModel=np.linspace(0,40e-3,200)
parallelGradient=(data[1][1]-data[1][0])/(data[0][1]-data[0][0])
perpGradient=(data[2][1]-data[2][0])/(data[0][1]-data[0][0])
# Plotting the V things
# plt.figure()
# plt.plot(iModel, parallelGradient*iModel, label='Linear model based on first 2 points')
# plt.errorbar(data[0],data[1],xerr=u[0],yerr=u[1],fmt='rs',markersize=1.5,elinewidth=0.7,capsize=3,capthick=0.7,label='$V_\parallel$')
# plt.ylabel('$V$',rotation=0)
# plt.xlabel('$I$')
# plt.legend()
# plt.grid(color='#CCCCCC', linestyle=':')
# # plt.savefig(r'PHY2004W Practicals and Reports\Hall Effect Prac\Report\Data\ForwardParallel.pgf')
# # plt.show()
# plt.figure()
# plt.plot(iModel, perpGradient*iModel, label='Linear model based on first 2 points')
# plt.errorbar(data[0],data[2],xerr=u[0],yerr=u[2],fmt='rs',markersize=1.5,elinewidth=0.7,capsize=3,capthick=0.7,label='$V_\perp$')
# plt.ylabel('$V$',rotation=0)
# plt.xlabel('$I$')
# plt.legend()
# plt.grid(color='#CCCCCC', linestyle=':')
# plt.show()
# plt.savefig(r'PHY2004W Practicals and Reports\Hall Effect Prac\Report\Data\ForwardPerp.pgf')
# V_H/I and V_\perp/V_\parallel
VH_I=data[2][1:]/data[0][1:]
VPerp_VParallel=data[2][1:]/data[1][1:]
# print(VH_I)
# print(VPerp_VParallel)
print(VPerp_VParallel)
print(VH_I)
print(np.var(VPerp_VParallel))
print(np.mean(VPerp_VParallel))
print(np.var(VH_I))
print(np.mean(VH_I))