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

# region Ingest data
file = open(r'CV100Days.txt', 'r')
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
# endregion

# region Slicing and Dicing
first100=data[:100]
first100Err=sqrt(first100)
first100CumSum=first100
first100CumSumErr=first100Err
first100Linear=np.log(first100CumSum)
first100LinearErr=first100CumSumErr/first100CumSum
t=np.arange(100)

# endregion

# region Exponential curve_fit
print('------------------------------------------------')
print('Exponential Curve Fitting')
print('------------------------------------------------')
def exponential(t,c,lam):
    return c*np.exp(lam*t)

poptExp, pcovExp=curve_fit(exponential, t, first100CumSum, p0=[1,0.1], sigma=first100CumSumErr, absolute_sigma=True)
xmodel=np.linspace(0,100,1000)

expFit=exponential(xmodel, *poptExp)

chiSqExp=sum(((first100CumSum-exponential(t, *poptExp))/first100CumSumErr)**2)
dofExp=len(t)-len(poptExp)

print(f'Chi Squared per d.o.f = {chiSqExp/dofExp}\n')

print(f'c = {poptExp[0]} +/- {sqrt(pcovExp[0][0])}\nlambda = {poptExp[1]} +/- {sqrt(pcovExp[1][1])}')

plt.figure()
plt.title('Exponential curve\_fit')
plt.errorbar(t, first100CumSum, fmt='s', ms=3, yerr=first100CumSumErr)
plt.plot(xmodel, expFit)

# endregion

# region Linear curve_fit
print('------------------------------------------------')
print('Linear Curve Fitting')
print('------------------------------------------------')
def linear(t,c,lam):
    return lam*t + c

poptLin, pcovLin=curve_fit(linear, t, first100Linear, p0=[1,0.1], sigma=first100LinearErr, absolute_sigma=True)

linFit=linear(t, *poptLin)

chiSqLin=sum(((first100Linear-linear(t, *poptLin))/first100LinearErr)**2)
dofLin=len(t)-len(poptLin)

print(f'Chi Squared per d.o.f = {chiSqLin/dofLin}\n')

print(f'c = {poptLin[0]} +/- {sqrt(pcovLin[0][0])}\nlambda = {poptLin[1]} +/- {sqrt(pcovLin[1][1])}')

plt.figure()
plt.title('Linear curve\_fit')
plt.errorbar(t, first100Linear, fmt='s', ms=3, yerr=first100LinearErr)
plt.plot(xmodel, linear(xmodel, *poptLin))

# endregion

# region Kirkup Weighted Linear Fit
print('------------------------------------------------')
print('Kirkup Weighted Linear Fit')
print('------------------------------------------------')
Delta=sum(1/(first100LinearErr**2))*sum((t**2)/(first100LinearErr**2))-(sum(t/(first100LinearErr**2)))**2

m=(sum(1/(first100LinearErr**2))*sum((t*first100Linear)/(first100LinearErr**2))-sum(t/(first100LinearErr**2))*sum(first100Linear/(first100LinearErr**2)))/Delta
um=sqrt((sum(1/(first100LinearErr**2)))/Delta)

c=(sum((t**2)/(first100LinearErr**2))*sum(first100Linear/(first100LinearErr**2))-sum(t/(first100LinearErr**2))*sum((t*first100Linear)/(first100LinearErr**2)))/Delta
uc=sqrt((sum((t**2)/(first100LinearErr**2)))/Delta)

kirkupFit=m*t+c

chiSqKirk=sum(((first100Linear-kirkupFit)/first100LinearErr)**2)
dofKirk=len(t)-2

print(f'Chi Squared per d.o.f = {chiSqKirk/dofKirk}\n')

print(f'c = {c} +/- {uc}\nlambda = {m} +/- {um}')

plt.figure()
plt.title('Kirkup Weighted Linear Fit')
plt.errorbar(t, first100Linear, fmt='s', ms=3, yerr=first100LinearErr)
plt.plot(t, m*t+c)

# endregion

plt.show()