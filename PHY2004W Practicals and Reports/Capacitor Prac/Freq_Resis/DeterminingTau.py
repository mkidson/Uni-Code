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

file = open('PHY2004W Practicals and Reports\Capacitor Prac\Freq_Resis\Cap_100Hz_5k6.txt', 'r')
header = file.readline()
lines = file.readlines()
N = len(lines)
i=0
# data[0] is Time [s] - Voltage Capacitor
# data[1] is Voltage [V] - Voltage Capacitor
# data[2] is Time [s] - Voltage Source
# data[3] is Voltage [V] - Voltage Source
data = np.zeros((4,N))
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
# Splitting the data into purely charging and discharging data for 5k6100Hz
chargingVE=np.concatenate((data[3][2:67],data[3][133:198],data[3][263:328],data[3][393:459]), axis=None)
chargingVC=np.concatenate((data[1][2:67],data[1][133:198],data[1][263:328],data[1][393:459]),axis=None)
dischargingVE=np.concatenate((data[3][0:2],data[3][67:133],data[3][198:263],data[3][328:393],data[3][459:520]),axis=None)
dischargingVC=np.concatenate((data[1][0:2],data[1][67:133],data[1][198:263],data[1][328:393],data[1][459:520]),axis=None)
chargingT=np.concatenate((data[0][2:67],data[0][133:198],data[0][263:328],data[0][393:459]),axis=None)
dischargingT=np.concatenate((data[0][0:2]+data[0][67:133]+data[0][198:263]+data[0][328:393]+data[0][459:520]),axis=None)
# Splitting the data into purely charging and discharging data for 15k100Hz
# chargingVE=data[3][12:77]+data[3][142:206]+data[3][271:338]+data[3][400:423]
# chargingVC=data[1][12:77]+data[1][142:206]+data[1][271:338]+data[1][400:423]
# dischargingVE=data[3][0:12]+data[3][77:142]+data[3][206:271]+data[3][338:400]
# dischargingVC=data[1][0:12]+data[1][77:142]+data[1][206:271]+data[1][338:400]
# chargingT=data[0][12:77]+data[0][142:206]+data[0][271:338]+data[0][400:423]
# dischargingT=data[0][0:12]+data[0][77:142]+data[0][206:271]+data[0][338:400]

# Creating the arrays that will hold the final scatter plot data
chargingXY=np.zeros((2, np.size(chargingVC)))
dischargingXY=np.zeros((2, np.size(dischargingVC)))



def charging(VC, VE, t):
    pass

print(chargingVE)
print(chargingVC)
print(dischargingVE)
print(dischargingVC)