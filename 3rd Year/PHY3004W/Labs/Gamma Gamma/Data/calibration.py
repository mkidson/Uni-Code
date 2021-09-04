from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import scipy.signal
from scipy.optimize import curve_fit
from numpy import cos, pi, sin, sqrt, exp, random
import matplotlib
# matplotlib.use('pgf')
matplotlib.rcParams.update({
    'pgf.texsystem': 'pdflatex',
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
    'figure.constrained_layout.use': True,
    'savefig.bbox': 'tight',
})

# region bkg
bkgBlueDf = pd.read_csv(r'PHY3004W_gglab_singles_spectra/PHY3004W_gglab_BlueBack_single.csv', header=0, skiprows=[0,1,2,4,5])
blueLiveTime = int(bkgBlueDf.columns[1])
blueData = bkgBlueDf.T.to_numpy(dtype='float')
blueData[1] /= blueLiveTime

bkgRedDf = pd.read_csv(r'PHY3004W_gglab_singles_spectra/PHY3004W_gglab_RedBack_single.csv', header=0, skiprows=[0,1,2,4,5])
redLiveTime = int(bkgRedDf.columns[1])
redData = bkgRedDf.T.to_numpy(dtype='float')
redData[1] /= redLiveTime
# endregion

def gaussian(x, mu, sigma, A):
    return (A*(1/(sigma*sqrt(2*pi)))*exp(-(1/2)*((x-mu)/sigma)**2))

blueNames = ['PHY3004W_gglab_BlueCo60_single.csv','PHY3004W_gglab_BlueCs137_single.csv','PHY3004W_gglab_BlueNa22_single.csv']
# blueNames = ['PHY3004W_gglab_BlueCs137_single.csv']
redNames = ['PHY3004W_gglab_RedCo60_single.csv','PHY3004W_gglab_RedCs137_single.csv','PHY3004W_gglab_RedNa22_single.csv']

# region Finding mu and sigma for all peaks
# for name in blueNames:
#     csvRead = pd.read_csv(f'PHY3004W_gglab_singles_spectra/{name}', header=0, skiprows=[0,1,2,4,5])

#     data = csvRead.T.to_numpy(dtype='float')
#     liveTime = float(csvRead.columns[1])
#     data[1] /= liveTime
#     data[1] -= blueData[1]
    
#     plt.figure()
#     plt.step(data[0], data[1])

#     smoothData = scipy.signal.savgol_filter(data[1], 51, 5)
#     smootherData = scipy.signal.savgol_filter(smoothData, 51, 5)
#     # Finds the minima
#     minima = scipy.signal.find_peaks(smootherData*-1)[0]
#     # print(minima)
#     # Fits a gaussian to the data for each region between a local minimum. Slightly overkill since not all of those regions are photopeaks but i'm lazy
#     for p in range(len(minima)-1):
#         try:
#             # Isolates the regions of interest 
#             xFit = data[0][minima[p]:minima[p+1]]
#             yFit = data[1][minima[p]:minima[p+1]]
#             # Need a new N for each region since the size is changing
#             newN = len(xFit)
#             # Approximates the median to be in the middle of the two endpoint, it's a reasonable guess
#             approxCentroid = (minima[p]+minima[p+1])/2
#             p0 = [approxCentroid,10,1]
#             numParams=len(p0)

#             popt, pcov = curve_fit(gaussian, xFit, yFit, p0, method='trf')
#             # Finding if the fit was poggers or cringe
#             toPlot=gaussian(xFit, *popt)
#             chi_sq=sum((yFit-toPlot)**2)
#             dof = newN-numParams

#             # if p==7:
#             print(f'Fit: {p}\nMu: {popt[0]}\nSigma: {popt[1]}\nAmplitude: {popt[2]}\nChi Squared per dof: {chi_sq/dof}\n')
#             plt.plot(xFit, toPlot, linewidth=1, label=f'Gaussian fit {p}')
#         except RuntimeError as identifier:
#             print(identifier)
    
#     plt.legend()
# plt.show()

# endregion

# 2 from 60-Co, 1 from 137-Cs, 2 from 22-Na

blueMus = np.array([409.38117891475815, 463.62983693327425, 227.26646405723562, 180.08530122005803, 446.71621199598826])*1e-3
blueSigmas = np.array([11.212339044335359, 10.597477037188037, 7.560240660823334, 6.458363395520904, 10.486407306946038])*1e-3
redMus = np.array([410.2599433027199, 465.0799334506383, 230.5812314159163, 178.4743740112304, 444.59425670740745])*1e-3
redSigmas = np.array([11.509809363155421, 10.858149774040802, 7.362937915494044, 6.5885236801044185, 10.812913719556672])*1e-3
fitX=np.array([1173.228, 1332.492, 661.657, 511, 1274.537])*1e-3

fitY = blueMus
fitYErr = blueSigmas

Delta=sum(1/(fitYErr**2))*sum((fitX**2)/(fitYErr**2))-(sum(fitX/(fitYErr**2)))**2

m=(sum(1/(fitYErr**2))*sum((fitX*fitY)/(fitYErr**2))-sum(fitX/(fitYErr**2))*sum(fitY/(fitYErr**2)))/Delta
um=sqrt((sum(1/(fitYErr**2)))/Delta)

c=(sum((fitX**2)/(fitYErr**2))*sum(fitY/(fitYErr**2))-sum(fitX/(fitYErr**2))*sum((fitX*fitY)/(fitYErr**2)))/Delta
uc=sqrt((sum((fitX**2)/(fitYErr**2)))/Delta)

kirkupFit=m*fitX+c

SS_total = np.sum((fitY - np.average(fitY))**2)
SS_res = np.sum((fitY - kirkupFit)**2)
R2=1-(SS_res)/(SS_total)
print(f'c = {c} +/- {uc}\nm = {m} +/- {um}')
print(f'R-Squared: {R2}')
plt.errorbar(fitX, fitY, yerr=fitYErr, fmt='.')
plt.plot(np.sort(fitX), m*np.sort(fitX)+c)
# plt.show()

# blue: m = 0.3488421803288909 +/- 0.011242627314320509, c = -0.0001325744712578748 +/- 0.010195728439634526, R2 = 0.9996883132391094
# red: m = 0.34919335675192653 +/- 0.01148026252472518, c = c = -0.00013939501839624682 +/- 0.010324622974044462, R2 = 0.9999890226156749

blueCorrected = (blueMus+0.0001325744712578748)/0.3488421803288909
blueCorrectedUn = blueCorrected*sqrt((sqrt(blueSigmas**2+0.010195728439634526**2)/(blueMus+0.0001325744712578748))**2 + (0.011242627314320509/0.3488421803288909)**2)
redCorrected = (redMus+0.00013939501839624682)/0.34919335675192653
redCorrectedUn = redCorrected*sqrt((sqrt(redSigmas**2+0.010324622974044462**2)/(redMus+0.00013939501839624682))**2 + (0.01148026252472518/0.34919335675192653)**2)


print(blueCorrected)
print(blueCorrectedUn)
print(redCorrected)
print(redCorrectedUn)
print(fitX)