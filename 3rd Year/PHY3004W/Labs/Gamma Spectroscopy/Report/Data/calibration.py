from matplotlib import pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from numpy import cos, pi, sin, sqrt, exp, random
import matplotlib
matplotlib.use('pgf')
matplotlib.rcParams.update({
    'pgf.texsystem': 'pdflatex',
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
})

def linear(x, m, c):
    return m*x+c
# region Data
# xData is the expected energies, coming from nudat2, in keV
xData=np.array([511, 1274.537, 1173.228, 1332.492, 88.0336, 80.9979, 356.0129, 661.657, 121.7817, 244.6974, 344.2785])
# yData is the mean voltage for each peak. we're getting it from the other program in channel number so we need the conversion
yData=(5/1024)*np.array([319.6533485546973, 781.9981845211427, 734.8359790306333, 835.6149327429337, 55.15979050752576, 49.09566045153678, 228.56531071809022, 416.98938465306423, 76.22835232015214, 154.71027390398143, 218.6496819516902])
# u is the sigma from the gaussian fit for each peak, acting as a standard uncertainty, also converted to voltage
u=(5/1024)*np.array([15.30681758032915, 24.039233361270966, 25.72860760912807, 22.97389382574074, 5.878731197356799, 8.23644485780789, 15.786840703524405, 15.579503245987384, 10.11388999318153, 19.645559270497074, 15.650589896871189])
# endregion

p0=[1,1]
popt, pcov = curve_fit(linear, xData, yData, p0, u, absolute_sigma=True)
xModel=np.arange(0, max(xData)+200)
stDev = sqrt(np.diag(pcov))

print(f'\nm: {popt[0]} +/- {stDev[0]}\nc: {popt[1]} +/- {stDev[1]}\n')
unknownY=526.6962170441554*(5/1024)
unknownX=((unknownY)-popt[1])/popt[0]
unknownU=16.765567075414058*(5/1024)
uUnknownX=unknownX*sqrt(((sqrt(unknownU**2 + stDev[1]**2))/((unknownY)-popt[1]))**2 + ((stDev[0])/(popt[0]))**2)
print(f'Energy of unknown source photopeak: {unknownX} +/- {uUnknownX}')

notToPlot=linear(np.sort(xData), *popt)
SS_total = np.sum((np.sort(yData) - np.average(yData))**2)
SS_res = np.sum((np.sort(yData) - notToPlot)**2)
R2=1-(SS_res)/(SS_total)
print(f'R-Squared: {R2}\n')

plt.plot(xModel, linear(xModel, *popt), 'red', linewidth=1, label=f'Linear Best Fit Line \nm=0.003049(56) \nc=0.002(22) \n$R^2$={R2:.6}')
plt.errorbar(xData[:2], yData[:2], u[:2], label='22Na', fmt='s', capsize=3)
plt.errorbar(xData[2:4], yData[2:4], u[2:4], label='60Co', fmt='s', capsize=3)
plt.errorbar(xData[4:5], yData[4:5], u[4:5], label='109Cd', fmt='s', capsize=3)
plt.errorbar(xData[5:7], yData[5:7], u[5:7], label='133Ba', fmt='s', capsize=3)
plt.errorbar(xData[7:8], yData[7:8], u[7:8], label='137Cs', fmt='s', capsize=3)
plt.errorbar(xData[8:], yData[8:], u[8:], label='152Eu', fmt='s', capsize=3)
plt.errorbar(unknownX, unknownY, unknownU, label='Unknown Source', fmt='s', capsize=3)
plt.legend()
plt.xlabel('Energy (keV)')
plt.ylabel('Voltage (V)')
# plt.show()
plt.savefig(r'3rd Year\PHY3004W\Labs\Gamma Spectroscopy\Report\Plots\linearRegression.pgf')