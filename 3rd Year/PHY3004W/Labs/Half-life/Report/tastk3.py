from matplotlib import pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from numpy import cos, pi, sin, sqrt, exp, random
import matplotlib, scipy.signal
np.set_printoptions(threshold=np.inf)
# matplotlib.use('pgf')
matplotlib.rcParams.update({
    'pgf.texsystem': 'pdflatex',
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
})


def gaussian(x, mu, sigma, A):
    return (A*(1/(sigma*sqrt(2*pi)))*exp(-(1/2)*((x-mu)/sigma)**2))

data=np.zeros((2,1024))

for n in range(1,181):

    # region Ingest data
    file = open(f'3rd Year\PHY3004W\Labs\Half-life\Data\\28Al_{n}.tsv', 'r')
    lines = file.readlines()
    N = len(lines)
    liveTime=float(lines[13].strip().split()[3])
    i=0
    # 0th index is channel number, 1st index is count
    nData=np.zeros((2,N-22))
    # Reading the file, getting the data into the data array
    for line in lines[22:]:
        line = line.strip()
        columns = line.split()
        nData[0][i] = float(columns[0])
        nData[1][i] = float(columns[1])
        i += 1
    file.close()
    # endregion

    # Normalise the data with respect to the time the detector was on for. We do this in order to subtract the normalised background data
    nData[1]/=liveTime
    # Sum up each run to make a whole nice long spectrum
    data[1]+=nData[1]

data[0]=(nData[0]-0.6)/0.333
# data[1]/=180 not sure about this one. makes it look like her plot but idk if it's the right way to do it

# Plots the histogram now
plt.hist(data[0], bins=data[0], weights=data[1], label=r'Counts per Channel', histtype='step')
plt.xlabel(r'Gamma ray energy (keV)')
plt.ylabel(r'Event rate ($s^{-1}$)')

# region Gaussian stuff, not needed anymore
# Fits a gaussian to the data for each region between a local minimum. Slightly overkill since not all of those regions are photopeaks but i'm lazy
# for p in range(len(minima)-1):
#     try:
#         # Isolates the regions of interest 
#         xFit=data[0][minima[p]:minima[p+1]]
#         yFit=data[1][minima[p]:minima[p+1]]
#         # Need a new N for each region since the size is changing
#         newN=len(xFit)
#         # Approximates the median to be in the middle of the two endpoint, it's a reasonable guess
#         approxCentroid=(minima[p]+minima[p+1])/2
#         p0=[approxCentroid,50,1]
#         numParams=len(p0)

#         popt, pcov = curve_fit(gaussian, xFit, yFit, p0, method='trf')
#         # Finding if the fit was poggers or cringe
#         toPlot=gaussian(xFit, *popt)
#         chi_sq=sum((yFit-toPlot)**2)
#         dof = newN-numParams

#         print(f'Fit: {p}\nMu: {popt[0]}\nSigma: {popt[1]}\nAmplitude: {popt[2]}\nChi Squared per dof: {chi_sq/dof}\n')
#         plt.plot(xFit, toPlot, linewidth=1, label=f'Gaussian fit {p}')
#         # arrowProps = dict(arrowstyle='->')
#         # str661='661.657 keV photopeak\n$\mu=417.37$\n$\sigma=15.28$'
#         # plt.annotate(str661, (419,5.9), (20,-60), textcoords='offset points', arrowprops=arrowProps)
#         # plt.annotate('Compton Edge\nfor 661.657 keV', (273,1.4), (5,20), textcoords='offset points', arrowprops=arrowProps)
#         # plt.annotate('Backscatter', (131, 2.1), (0,20), textcoords='offset points', arrowprops=arrowProps)
#     except RuntimeError as identifier:
#         print(identifier)
# endregion

# plt.plot(data[0], smootherData)
plt.legend()
plt.show()