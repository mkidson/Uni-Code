from matplotlib import pyplot as plt
import numpy as np
from numpy import cos, pi, sin, sqrt, exp, random
import matplotlib
# matplotlib.use('pgf')
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
# 5k6 data for the first charging/discharging cycle
chargingVE=data[3][2:45]
chargingVC=data[1][2:45]
dischargingVE=data[3][67:96]
dischargingVC=data[1][67:96]+4
chargingT=data[0][2:45]
dischargingT=data[0][67:96]
# 15k data for the first charging/discharging cycle
# chargingVE=data[3][12:77]
# chargingVC=data[1][12:77]
# dischargingVE=data[3][77:141]
# dischargingVC=data[1][77:141]+4
# chargingT=data[0][12:77]
# dischargingT=data[0][77:141]
# Creating the arrays that will hold the final scatter plot data
chargingY=[]
dischargingY=[]
# Calculating the y values for charging
for i in range(np.size(chargingT)):
    x=chargingVE[i]-chargingVC[i]
    chargingY.append(np.log(x))
# And discharging
for c in range(np.size(dischargingT)):
    v=dischargingVC[c]
    dischargingY.append(np.log(v))
# Fitting the linear least squares line for charging
def linearLeastSquares(x, y):
    Ni=np.size(x)
    m = ((Ni*sum(x*y)) - sum(x)*sum(y))/((Ni*sum(x**2))-(sum(x))**2)
    c = ((sum(x**2)*sum(y))-(sum(x*y)*sum(x)))/((Ni*sum(x**2))-(sum(x)**2))
    di=y-((m*x)+c)
    um = sqrt(((sum(di**2)/((Ni*sum(x**2))-(sum(x)**2)))*(Ni/(N-2))))
    uc = sqrt((((sum(di**2)*sum(x**2))/(Ni*((Ni*sum(x**2))-(sum(x)**2))))*(Ni/(Ni-2))))
    print('m=',m,'+/-',um)
    print('c=',c,'+/-',uc)
    return [m,c,um,uc]
chargingFit=linearLeastSquares(chargingT,chargingY)
dischargingFit=linearLeastSquares(dischargingT,dischargingY)
# Calculating tau and its uncertainty then printing
chargingTau=-1/chargingFit[0]
chargingTauUn=chargingTau*sqrt((chargingFit[2]/chargingFit[0])**2)
dischargingTau=-1/dischargingFit[0]
dischargingTauUn=(dischargingTau)*sqrt((dischargingFit[2]/dischargingFit[0])**2)
tau=(chargingTau+dischargingTau)/2
tauUn=sqrt(chargingTauUn**2 + dischargingTauUn**2)/2
print('tau =',tau,'+/-',tauUn)
# Plotting the charging scatterplot 
plt.errorbar(chargingT, chargingY, fmt='bs', ecolor='black', label='Data', markersize=3)
plt.xlabel('Time (s)')
plt.ylabel('$\ln(V_\epsilon -V_C)$')
plt.plot(chargingT, chargingFit[0]*chargingT+chargingFit[1], label='Best Fit Line')
plt.legend()
# Plotting the discharging scatterplot
plt.figure()
plt.errorbar(dischargingT, dischargingY, fmt='bs', ecolor='black', label='Data', markersize=3)
plt.xlabel('Time (s)')
plt.ylabel('$\ln(V_C)$')
plt.plot(dischargingT, dischargingFit[0]*dischargingT+dischargingFit[1], label='Best Fit Line')
plt.legend()
# plt.show()