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
    'figure.constrained_layout.use': True,
    'savefig.bbox': 'tight',
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


# data[0]=(nData[0]-0.6)/0.333
data[0]=nData[0]
data[1]/=1800 

# region plotting shit
ax=plt.axes()
ax.set_box_aspect(5/14) # for wide boys use 5/14

ax.step(data[0], data[1], linewidth=1)

ax.set_xlabel(r'Gamma ray energy (keV)')
ax.set_ylabel(r'Event rate ($s^{-1}$)')
ax.set_xlim(left=0)
ax.set_ylim(bottom=0)

ax.fill_between(data[0][0:130], data[1][0:130], step='pre', color='green', alpha=0.5, label='Bremsstrahlung')
ax.fill_between(data[0][180:235], data[1][180:235], step='pre', color='blue', alpha=0.5, label='843.76 keV $\gamma$ Compton continuum')
ax.axvline(data[0][279], linestyle='dashed', color='black', linewidth=1)
ax.text(data[0][279], 0.15, '843.76 $\gamma$ photopeak', rotation='vertical', horizontalalignment='right')
ax.axvline(data[0][336], linestyle='dashed', color='black', linewidth=1)
ax.text(data[0][336], 0.15, '1014.52 $\gamma$ photopeak', rotation='vertical', horizontalalignment='right')
ax.fill_between(data[0][460:535], data[1][460:535], step='pre', color='red', alpha=0.5, label='1778.987 keV $\gamma$ Compton continuum')
ax.axvline(data[0][583], linestyle='dashed', color='black', linewidth=1)
ax.text(data[0][583], 0.15, '1778.987 $\gamma$ photopeak', rotation='vertical', horizontalalignment='right')


ax.legend()

plt.show()
# plt.savefig(r'3rd Year\PHY3004W\Labs\Half-life\Report\Task 3\task3Plot.pgf')

# endregion

# region Gaussian stuff, not needed after calibration
# Fits a gaussian to the data for each region between a local minimum. Slightly overkill since not all of those regions are photopeaks but i'm lazy
# for p in range(1):
#     try:
#         # Isolates the regions of interest 
#         xFit=data[0][551:615]
#         yFit=data[1][551:615]
#         # Need a new N for each region since the size is changing
#         newN=len(xFit)
#         # Approximates the median to be in the middle of the two endpoint, it's a reasonable guess
#         approxCentroid=(data[0][551]+data[0][615])/2
#         p0=[approxCentroid,50,1]
#         numParams=len(p0)

#         popt, pcov = curve_fit(gaussian, xFit, yFit, p0, method='trf')
#         # Finding if the fit was poggers or cringe
#         toPlot=gaussian(xFit, *popt)
#         chi_sq=sum((yFit-toPlot)**2)
#         dof = newN-numParams

#         print(f'Fit: {p}\nMu: {popt[0]}\nSigma: {popt[1]}\nAmplitude: {popt[2]}\nChi Squared per dof: {chi_sq/dof}\n')
#         ax.plot(xFit, toPlot, linewidth=1, label=f'Gaussian fit {p}')
#     except RuntimeError as identifier:
#         print(identifier)
# endregion
