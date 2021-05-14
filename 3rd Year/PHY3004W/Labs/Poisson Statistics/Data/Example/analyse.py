from matplotlib import pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from scipy.special import gamma
from numpy import cos, pi, sin, sqrt, exp, random
import matplotlib, math
# matplotlib.use('pgf')
matplotlib.rcParams.update({
    'pgf.texsystem': 'pdflatex',
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
})

file = open(r'3rd Year\PHY3004W\Labs\Poisson Statistics\Data\Example\mu100.txt', 'r')
lines = file.readlines()
N = len(lines)
i=0
data = np.zeros(N)
# Reading the file, getting the data into the data array
for line in lines:
    line = line.strip()
    columns = line.split()
    data[i] = float(columns[0])
    i += 1
file.close()

dataDict={}
for i in data:
    if i in dataDict.keys():
        dataDict[i]+=1
    else:
        dataDict[i]=1

sortedDataDict=sorted(dataDict.items())

finX=np.array([x[0] for x in sortedDataDict])
finY=np.array([x[1] for x in sortedDataDict])
finY=finY/np.sum(finY) # normalising data because poisson is a pmf

def poisson(x, mu):
    return ((mu**x)/(gamma(x+1)))*exp(-mu)

popt, pcov=curve_fit(poisson, finX, finY, p0=[100])
print(f'mu: {popt[0]} +/- {sqrt(pcov[0][0])}')
xmodel=np.linspace(finX[0], finX[-1], 1000)

toPlot=poisson(finX, *popt)
chi_sq=sum((finY-toPlot)**2)
dof=len(finX)-1
print(f'chi squared/dof: {chi_sq/dof}')

plt.hist(finX, bins=finX, weights=finY)
plt.plot(xmodel, poisson(xmodel, *popt))
plt.show()