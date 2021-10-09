from matplotlib import pyplot as plt, colors
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
from numpy import cos, pi, sin, sqrt, exp, random
import matplotlib
# matplotlib.use('pgf')
matplotlib.rcParams.update({
    'pgf.texsystem': 'pdflatex',
    'font.family': 'sans-serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
    'figure.constrained_layout.use': True,
    'savefig.bbox': 'tight',
    'axes.labelsize': 14,
    'legend.fontsize': 14,
    'xtick.labelsize': 12,
    'ytick.labelsize': 12
})
def npIndexOf(arr, element):
    """
    Returns the index of the first element in arr with the value of element
    """
    return np.where(arr==element)[0][0]

def gaussian(x, mu, sigma, A):
    return (A*(1/(sigma*sqrt(2*pi)))*exp(-(1/2)*((x-mu)/sigma)**2))

def gaussian2(x, mu1, sigma1, A1, mu2, sigma2, A2):
    return (A1*(1/(sigma1*sqrt(2*pi)))*exp(-(1/2)*((x-mu1)/sigma1)**2))+(A2*(1/(sigma2*sqrt(2*pi)))*exp(-(1/2)*((x-mu2)/sigma2)**2))

def Breit_Wigner(x, x_0, gamma, A):
    return A/(pi*gamma*(1+((x-x_0)/gamma)**2))

energyCutoff = 1

# region STNG data
longInts = np.load('STNG_CCM_longInts.npy')
CCM_PSDs = np.load('STNG_CCM_PSDs.npy')
STNGSortingArr = longInts.argsort()
longIntsSorted = longInts[STNGSortingArr]
CCM_PSDsSorted = CCM_PSDs[STNGSortingArr]
longIntsGreater1 = longIntsSorted[(longIntsSorted < 10)&(longIntsSorted>energyCutoff)]
CCM_PSDsGreater1 = CCM_PSDsSorted[(longIntsSorted < 10)&(longIntsSorted>energyCutoff)]
longIntsFinal = longIntsGreater1[(CCM_PSDsGreater1<1.1)&(CCM_PSDsGreater1>0.6)]
CCM_PSDFinal = CCM_PSDsGreater1[(CCM_PSDsGreater1<1.1)&(CCM_PSDsGreater1>0.6)]
# endregion

# region AmBe data
# longInts = np.load('AmBe_CCM_longInts.npy')
# CCM_PSDs = np.load('AmBe_CCM_PSDs.npy')
# AmBeSortingArr = longInts.argsort()
# longIntsSorted1 = longInts[AmBeSortingArr]
# CCM_PSDsSorted1 = CCM_PSDs[AmBeSortingArr]
# longIntsSorted = longIntsSorted1[(CCM_PSDsSorted1>0.5)&(longIntsSorted1>0.3)]
# CCM_PSDsSorted = CCM_PSDsSorted1[(CCM_PSDsSorted1>0.5)&(longIntsSorted1>0.3)]
# longIntsGreater1 = longIntsSorted[longIntsSorted > energyCutoff]
# CCM_PSDsGreater1 = CCM_PSDsSorted[longIntsSorted > energyCutoff]
# endregion

# plt.figure()
# plt.hist2d(longIntsGreater1[(CCM_PSDsGreater1<1.2)&(CCM_PSDsGreater1>0.45)], CCM_PSDsGreater1[(CCM_PSDsGreater1<1.2)&(CCM_PSDsGreater1>0.45)], bins=500, norm=colors.LogNorm())
# plt.hist2d(longInts[(CCM_PSDs>0.4)&(longInts<=8)], CCM_PSDs[(CCM_PSDs>0.4)&(longInts<=8)], bins=500, norm=colors.LogNorm())
# plt.xlabel('$L$ (MeVee)')
# plt.ylabel('$S_{CCM}$ (a.u.)')
# plt.hist2d(longInts[CCM_PSDs<5], CCM_PSDs[CCM_PSDs<5], bins=1000, norm=colors.LogNorm())
# plt.axvline(energyCutoff)

# region STNG
STNGcutoff = 0.032*np.log(longIntsFinal)+0.75
# plt.plot(longIntsFinal, STNGcutoff, color='black', lw=1.5)
# plt.annotate('deuteron recoil', (6,0.7), fontsize=16)
# plt.annotate('alpha particle recoil', (1.2,0.6), fontsize=16)

photonsPSDs = CCM_PSDFinal[CCM_PSDFinal>STNGcutoff]
neutronsPSDs = CCM_PSDFinal[CCM_PSDFinal<STNGcutoff]

# photonsPSDs = CCM_PSDsGreater1[CCM_PSDsGreater1>STNGcutoff]
# neutronsPSDs = CCM_PSDsGreater1[CCM_PSDsGreater1<STNGcutoff]

# photonsPSDs = CCM_PSDsSorted[CCM_PSDsSorted>STNGcutoff]
# neutronsPSDs = CCM_PSDsSorted[CCM_PSDsSorted<STNGcutoff]

# photonLongInts = longIntsSorted[CCM_PSDsSorted>STNGcutoff]
# neutronLongInts = longIntsSorted[CCM_PSDsSorted<STNGcutoff]

# endregion

# region AmBe
# AmBecutoff = 0.022*np.log(longIntsSorted)+0.75
# plt.plot(longIntsSorted, AmBecutoff, color='black', lw=1.5)
# for i in np.arange(2,6,2):
#     longIntsGreater1 = longIntsSorted[(longIntsSorted > i-2) & (longIntsSorted < i)]
#     CCM_PSDsGreater1 = CCM_PSDsSorted[(longIntsSorted > i-2) & (longIntsSorted < i)]

#     photonsPSDs = CCM_PSDsGreater1[CCM_PSDsGreater1>AmBecutoff[(longIntsSorted > i-2) & (longIntsSorted < i)]]
#     neutronsPSDs = CCM_PSDsGreater1[CCM_PSDsGreater1<AmBecutoff[(longIntsSorted > i-2) & (longIntsSorted < i)]]

    # photonsPSDs = CCM_PSDsSorted[CCM_PSDsSorted>AmBecutoff]
    # neutronsPSDs = CCM_PSDsSorted[CCM_PSDsSorted<AmBecutoff]

# photonLongInts = longIntsSorted[CCM_PSDsSorted>AmBecutoff]
# neutronLongInts = longIntsSorted[CCM_PSDsSorted<AmBecutoff]
# endregion

photonsData, photonsBins = np.histogram(photonsPSDs, bins=1000)
neutronsData, neutronsBins = np.histogram(neutronsPSDs, bins=1000)


# splitting the data and flipping it
newData = neutronsData[neutronsBins[:-1]>neutronsBins[:-1][np.where(neutronsData==max(neutronsData))[0][0]]]
newDataFlipped = newData[::-1]
newData2 = np.concatenate((newDataFlipped[:-1], newData))
newBins = neutronsBins[np.where(neutronsData==max(neutronsData))[0][0]-len(newData)+2:-1]

# photonsData, photonsBins = np.histogram(photonLongInts, bins=1000)
# neutronsData, neutronsBins = np.histogram(neutronLongInts, bins=1000)

# fitting to the two histograms
photonsPopt, photonsPcov = curve_fit(gaussian, photonsBins[:-1], photonsData, p0=[photonsBins[np.where(photonsData==max(photonsData))[0][0]],1,1], sigma=np.where(photonsData!=0,sqrt(photonsData), 1), absolute_sigma=True)
# neutronsPopt, neutronsPcov = curve_fit(gaussian, neutronsBins[:-1], neutronsData, p0=[neutronsBins[np.where(neutronsData==max(neutronsData))[0][0]],1,1], sigma=np.where(neutronsData!=0,sqrt(neutronsData), 1), absolute_sigma=True)
neutronsPopt1, neutronsPcov1 = curve_fit(gaussian, newBins, newData2, p0=[newBins[np.where(newData2==max(newData2))[0][0]],1,1], sigma=np.where(newData2!=0,sqrt(newData2), 1), absolute_sigma=True)
# neutronsDataNew = neutronsData-gaussian(neutronsBins[:-1], *neutronsPopt1)
# neutronsPopt, neutronsPcov = curve_fit(gaussian, neutronsBins[:-1], neutronsDataNew, p0=[neutronsBins[np.where(neutronsDataNew==max(neutronsDataNew))[0][0]],1,1], sigma=np.where(neutronsDataNew!=0,sqrt(abs(neutronsDataNew)), 1), absolute_sigma=True)

plt.figure()
plt.step(photonsBins[:-1], photonsData, label='gamma-rays')
plt.step(neutronsBins[:-1], neutronsData, label='neutrons')
# plt.step(newBins, newData2)
plt.plot(photonsBins[:-1], gaussian(photonsBins[:-1], *photonsPopt), lw=1, label='Gaussian shape \nfitted to gamma-ray data')
plt.plot(newBins, gaussian(newBins, *neutronsPopt1), lw=1, label='Gaussian shape fitted \nto neutron data')
# plt.plot(neutronsBins[:-1], gaussian(neutronsBins[:-1], *neutronsPopt), lw=1, label='Gaussian shape fitted \nto neutron data')
# photonsData, photonsBins = np.histogram(photonsPSDs2, bins=1000)
# neutronsData, neutronsBins = np.histogram(neutronsPSDs2, bins=1000)
# plt.step(photonsBins[:-1], photonsData, label='photons2')
# plt.step(neutronsBins[:-1], neutronsData, label='neutrons2')
plt.fill_between(photonsBins[:-1], photonsData+sqrt(photonsData), photonsData-sqrt(photonsData), alpha=0.3, color='C0', step='pre')
plt.fill_between(neutronsBins[:-1], neutronsData+sqrt(neutronsData), neutronsData-sqrt(neutronsData), alpha=0.3, color='C1', step='pre')
plt.legend()

# plt.title('Long Integral')
plt.xlabel('$S_{CCM}$ (a.u.)')
plt.ylabel('Counts')
# plt.xlim(0.6,0.9)
# plt.show()
# plt.savefig(f'Plots/CCM_AmBe_separation_hist_{i}.pdf')

FoM = (photonsPopt[0]-neutronsPopt1[0])/(2*photonsPopt[1]+2.35*neutronsPopt1[1])
print(FoM)

# plt.show()
plt.savefig('Plots/CCM_STNG_separation_hist.png')