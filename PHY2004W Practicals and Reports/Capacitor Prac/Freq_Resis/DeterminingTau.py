from matplotlib import pyplot as plt
import numpy as np
from numpy import cos, pi, sin, sqrt, exp, random
from scipy.optimize import leastsq
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

# Using only one cycle instead of all of them
chargingVE=data[3][2:45]
chargingVC=data[1][2:45]
dischargingVE=data[3][73:102]
dischargingVC=data[1][73:102]
chargingT=data[0][2:45]
dischargingT=data[0][73:102]

# Creating the arrays that will hold the final scatter plot data
chargingY=[]
dischargingY=[]
# Calculating the y values for charging
for i in range(np.size(chargingT)):
    x=chargingVE[i]-chargingVC[i]
    chargingY.append(np.log(x))
# And discharging
for i in range(np.size(dischargingT)):
    v=-dischargingVC[i]
    dischargingY.append(np.log(v))

# Fitting the linear least squares line for charging
def linearLeastSquares(x, y):
    Ni=np.size(x)
    m = ((Ni*sum(x*y)) - sum(x)*sum(y))/((Ni*sum(x**2))-(sum(x))**2)
    c = ((sum(x**2)*sum(y))-(sum(x*y)*sum(x)))/((Ni*sum(x**2))-(sum(x)**2))
    di=y-((m*x)+c)
    um = sqrt(((sum(di**2)/((Ni*sum(x**2))-(sum(x)**2)))*(Ni/(N-2))))
    uc = sqrt((((sum(di**2)*sum(x**2))/(Ni*((Ni*sum(x**2))-(sum(x)**2))))*(Ni/(Ni-2))))
    print(m,c,um,uc)
    return [m,c,um,uc]

chargingFit=linearLeastSquares(chargingT,chargingY)
dischargingFit=linearLeastSquares(dischargingT,dischargingY)


# Plotting the charging scatterplot 
plt.errorbar(chargingT, chargingY, fmt='bs', ecolor='black', label='', markersize=3)
plt.xlabel('Time (s)')
plt.ylabel('$\ln(V_\epsilon -V_C)$')
plt.plot(chargingT, chargingFit[0]*chargingT+chargingFit[1])
plt.show()

plt.figure()
plt.plot(dischargingT,np.log(dischargingVC/dischargingVE))

plt.figure()
# Plotting the discharging scatterplot
plt.errorbar(dischargingT, dischargingY, fmt='bs', ecolor='black', label='', markersize=3)
plt.xlabel('Time (s)')
plt.ylabel('$\ln(V_C)$')
plt.plot(dischargingT, dischargingFit[0]*dischargingT+dischargingFit[1])
plt.show()

# print(chargingVE)
# print(chargingVC)
# print(dischargingVE)
# print(dischargingVC)



# Splitting the data into purely charging and discharging data for 5k6100Hz
# chargingVE=np.concatenate((data[3][2:45],data[3][133:175],data[3][263:305],data[3][393:436]),axis=None)
# chargingVC=np.concatenate((data[1][2:45],data[1][133:175],data[1][263:305],data[1][393:436]),axis=None)
# dischargingVE=np.concatenate((data[3][67:102],data[3][198:232],data[3][328:363],data[3][459:493]),axis=None)
# dischargingVC=np.concatenate((data[1][67:102],data[1][198:232],data[1][328:363],data[1][459:493]),axis=None)
# chargingT=np.concatenate((data[0][2:45],data[0][133:175],data[0][263:305],data[0][393:436]),axis=None)
# dischargingT=np.concatenate((data[0][67:102],data[0][198:232],data[0][328:363],data[0][459:493]),axis=None)
# Splitting the data into purely charging and discharging data for 15k100Hz
# chargingVE=np.concatenate((data[3][12:77],data[3][142:206],data[3][271:338],data[3][400:423]), axis=None)
# chargingVC=np.concatenate((data[1][12:77],data[1][142:206],data[1][271:338],data[1][400:423]), axis=None)
# dischargingVE=np.concatenate((data[3][0:12],data[3][77:142],data[3][206:271],data[3][338:400]), axis=None)
# dischargingVC=np.concatenate((data[1][0:12],data[1][77:142],data[1][206:271],data[1][338:400]), axis=None)
# chargingT=np.concatenate((data[0][12:77],data[0][142:206],data[0][271:338],data[0][400:423]), axis=None)
# dischargingT=np.concatenate((data[0][0:12],data[0][77:142],data[0][206:271],data[0][338:400]), axis=None)