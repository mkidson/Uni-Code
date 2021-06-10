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

def linear(x, m, c):
    return m*x+c
# region Data

names=['22Na', '60Co', '137Cs']

# xData is the expected energies, coming from nudat2, in keV
xData=np.array([511, 1274.537, 1173.228, 1332.492, 661.657])
# yData is the mean voltage for each peak. we're getting it from the other program in channel number so we need the conversion
yData=np.array([169.86368098834947, 424.7286533105192, 390.34252298697703, 442.35419727097764, 219.1754550304657])
# u is the sigma from the gaussian fit for each peak, acting as a standard uncertainty, also converted to voltage
u=np.array([6.264735765344269, 10.143503819527698, 10.865582922597806, 10.093158168933954, 6.916299725573073])
# endregion

Delta=sum(1/(u**2))*sum((xData**2)/(u**2))-(sum(xData/(u**2)))**2

m=(sum(1/(u**2))*sum((xData*yData)/(u**2))-sum(xData/(u**2))*sum(yData/(u**2)))/Delta
um=sqrt((sum(1/(u**2)))/Delta)

c=(sum((xData**2)/(u**2))*sum(yData/(u**2))-sum(xData/(u**2))*sum((xData*yData)/(u**2)))/Delta
uc=sqrt((sum((xData**2)/(u**2)))/Delta)

kirkupFit=m*xData+c

chiSqKirk=sum(((yData-kirkupFit)/u)**2)
dofKirk=len(xData)-2

print(f'Chi Squared per d.o.f = {chiSqKirk/dofKirk}\n')

print(f'c = {c} +/- {uc}\nm = {m} +/- {um}')

xModel=np.arange(min(xData)-100, max(xData)+100)
# p0=[1,1]
# popt, pcov = curve_fit(linear, xData, yData, p0, u, absolute_sigma=True)
# stDev = sqrt(np.diag(pcov))

# print(f'\nm: {popt[0]} +/- {stDev[0]}\nc: {popt[1]} +/- {stDev[1]}\n')

notToPlot=linear(np.sort(xData), m, c)
SS_total = np.sum((np.sort(yData) - np.average(yData))**2)
SS_res = np.sum((np.sort(yData) - notToPlot)**2)
R2=1-(SS_res)/(SS_total)
print(f'R-Squared: {R2}\n')

plt.plot(xModel, linear(xModel, m, c), 'red', linewidth=1, label=f'Linear Best Fit Line \nm=0.333(11) \nc=-0.6(9.8) \n$R^2$={R2:.6}')
plt.errorbar(xData[:2], yData[:2], u[:2], label='22Na', fmt='s', capsize=3)
plt.errorbar(xData[2:4], yData[2:4], u[2:4], label='60Co', fmt='s', capsize=3)
plt.errorbar(xData[4:], yData[4:], u[4:], label='137Cs', fmt='s', capsize=3)
plt.legend()
plt.xlabel('Energy (keV)')
plt.ylabel('Channel Number')
plt.show()
# plt.savefig(r'3rd Year\PHY3004W\Labs\Gamma Spectroscopy\Report\Plots\linearRegression.pgf')