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
    #'axes.labelsize': 16,
    #'legend.fontsize': 16,
    #'xtick.labelsize': 12,
    #'ytick.labelsize': 12
})
def npIndexOf(arr, element):
    """
    Returns the index of the first element in arr with the value of element
    """
    return np.where(arr==element)[0][0]

energyCutoff = 0#0.25

# region STNG data
longInts1 = np.load('STNG_Laplace_longInts.npy')
Laplace_Res1 = np.load('STNG_Laplace_Res.npy')
Laplace_Poles1 = np.load('STNG_Laplace_Poles.npy')
Laplace_ChiSq = np.load('STNG_Laplace_chisq2.npy')

longInts = longInts1[Laplace_ChiSq<1]
Laplace_Res = Laplace_Res1[Laplace_ChiSq<1]
Laplace_Poles = Laplace_Poles1[Laplace_ChiSq<1]

# Laplace_PSDs = Laplace_Poles[:,1]/Laplace_Poles[:,0]
# STNGSortingArr = longInts.argsort()
# longIntsSorted = longInts[STNGSortingArr]
# Laplace_PSDsSorted = Laplace_PSDs[STNGSortingArr]
# endregion

# region AmBe data
# longInts = np.load('AmBe_Laplace_longInts.npy')
# Laplace_Res = np.load('AmBe_Laplace_Res.npy')
# Laplace_Poles = np.load('AmBe_Laplace_Poles.npy')

# Laplace_PSDs = (np.abs(Laplace_Res[:,1])*np.abs(Laplace_Poles[:,1]))/(np.abs(Laplace_Res[:,0])*np.abs(Laplace_Poles[:,0]))
Laplace_PSDs = np.where(Laplace_Poles[:,0]>=Laplace_Poles[:,1], Laplace_Res[:,1]/Laplace_Res[:,0], Laplace_Res[:,0]/Laplace_Res[:,1])
# Laplace_PSDs = Laplace_Res[:,0]
# AmBeSortingArr = longInts.argsort()
# longIntsSorted = longInts[AmBeSortingArr]
# Laplace_PSDsSorted = Laplace_PSDs[AmBeSortingArr]
# endregion

# region comparing to CCM AmBe
# CCM_longInts = np.load('AmBe_CCM_longInts.npy')
# CCM_PSDs = np.load('AmBe_CCM_PSDs.npy')
# CCM_SortingArr = np.load('AmBe_CCM_SortingArr.npy')

# Laplace_PSDs_Sorted = Laplace_PSDs[CCM_SortingArr]
# longInts_Sorted = longInts[CCM_SortingArr]
# CCM_longInts_Sorted = CCM_longInts[CCM_SortingArr]
# CCM_PSDs_Sorted = CCM_PSDs[CCM_SortingArr]

# AmBecutoff = 0.015*np.log(longInts_Sorted-0.05)+0.84
# laplacePhotonsPSDs = Laplace_PSDs_Sorted[CCM_PSDs_Sorted>AmBecutoff]
# laplacePhotonsLongInts = longInts[CCM_PSDs_Sorted>AmBecutoff]
# laplaceNeutronsPSDs = Laplace_PSDs_Sorted[CCM_PSDs_Sorted<AmBecutoff]
# laplaceNeutronsLongInts = longInts[CCM_PSDs_Sorted<AmBecutoff]
# endregion

# region comparing to CCM STNG
# CCM_longInts = np.load('STNG_CCM_longInts.npy')
# CCM_PSDs = np.load('STNG_CCM_PSDs.npy')
# CCM_SortingArr = np.load('STNG_CCM_SortingArr.npy')

# Laplace_PSDs_Sorted = Laplace_PSDs[CCM_SortingArr]
# longInts_Sorted = longInts[CCM_SortingArr]
# CCM_longInts_Sorted = CCM_longInts[CCM_SortingArr]
# CCM_PSDs_Sorted = CCM_PSDs[CCM_SortingArr]

# STNGcutoff = 0.016*np.log(longInts_Sorted)+0.836
# laplacePhotonsPSDs = Laplace_PSDs_Sorted[CCM_PSDs_Sorted>STNGcutoff]
# laplacePhotonsLongInts = longInts[CCM_PSDs_Sorted>STNGcutoff]
# laplaceNeutronsPSDs = Laplace_PSDs_Sorted[CCM_PSDs_Sorted<STNGcutoff]
# laplaceNeutronsLongInts = longInts[CCM_PSDs_Sorted<STNGcutoff]
# endregion

CCM_longInts1 = np.load('STNG_CCM_longInts.npy')
CCM_PSDs1 = np.load('STNG_CCM_PSDs.npy')
# CCM_SortingArr1 = np.load('STNG_CCM_SortingArr.npy')

CCM_longInts = CCM_longInts1[Laplace_ChiSq<1]
CCM_PSDs = CCM_PSDs1[Laplace_ChiSq<1]
CCM_SortingArr = CCM_longInts.argsort()

Laplace_Poles_Sorted = Laplace_Poles[CCM_SortingArr]
Laplace_Res_Sorted = Laplace_Res[CCM_SortingArr]
Laplace_PSDs_Sorted = Laplace_PSDs[CCM_SortingArr]
longInts_Sorted = longInts[CCM_SortingArr]
CCM_longInts_Sorted = CCM_longInts[CCM_SortingArr]
CCM_PSDs_Sorted = CCM_PSDs[CCM_SortingArr]

STNGcutoff = 0.016*np.log(longInts_Sorted)+0.836
laplacePhotonsPoles = Laplace_Poles_Sorted[CCM_PSDs_Sorted>STNGcutoff]
laplacePhotonsRes = Laplace_Res_Sorted[CCM_PSDs_Sorted>STNGcutoff]
laplacePhotonsLongInts = longInts[CCM_PSDs_Sorted>STNGcutoff]
laplacePhotonsPSDs = Laplace_PSDs_Sorted[CCM_PSDs_Sorted>STNGcutoff]
laplaceNeutronsPoles = Laplace_Poles_Sorted[CCM_PSDs_Sorted<STNGcutoff]
laplaceNeutronsRes = Laplace_Res_Sorted[CCM_PSDs_Sorted<STNGcutoff]
laplaceNeutronsLongInts = longInts[CCM_PSDs_Sorted<STNGcutoff]
laplaceNeutronsPSDs = Laplace_PSDs_Sorted[CCM_PSDs_Sorted<STNGcutoff]

plt.figure()
# plt.hist2d(laplacePhotonsLongInts[np.abs(laplacePhotonsPSDs)<100], laplacePhotonsPSDs[np.abs(laplacePhotonsPSDs)<100], bins=2000, norm=colors.LogNorm())
# plt.figure()
# plt.hist2d(laplaceNeutronsLongInts[np.abs(laplaceNeutronsPSDs)<100], laplaceNeutronsPSDs[np.abs(laplaceNeutronsPSDs)<100], bins=2000, norm=colors.LogNorm())
# plt.hist2d(longInts[np.abs(Laplace_PSDs)<100], Laplace_PSDs[np.abs(Laplace_PSDs)<100], bins=2000, norm=colors.LogNorm())

# plt.hist2d(laplacePhotonsRes[:,0][(np.abs(laplacePhotonsRes[:,0])<0.2)&(np.abs(laplacePhotonsRes[:,1])<1)], laplacePhotonsRes[:,1][(np.abs(laplacePhotonsRes[:,0])<0.2)&(np.abs(laplacePhotonsRes[:,1])<1)], bins=2000, norm=colors.LogNorm())
# plt.figure()
# plt.hist2d(laplaceNeutronsRes[:,0][(np.abs(laplaceNeutronsRes[:,0])<0.2)&(np.abs(laplaceNeutronsRes[:,1])<1)], laplaceNeutronsRes[:,1][(np.abs(laplaceNeutronsRes[:,0])<0.2)&(np.abs(laplaceNeutronsRes[:,1])<1)], bins=2000, norm=colors.LogNorm())


# plt.hist2d(Laplace_Res[:,0][(np.abs(Laplace_Res[:,0])<0.2)&(np.abs(Laplace_Res[:,1])<1)], Laplace_Res[:,1][(np.abs(Laplace_Res[:,0])<0.2)&(np.abs(Laplace_Res[:,1])<1)], bins=2000, norm=colors.LogNorm())
# plt.hist2d(Laplace_Poles[:,0][Laplace_Poles[:,1]<2], Laplace_Poles[:,1][Laplace_Poles[:,1]<2], bins=2000, norm=colors.LogNorm())
# plt.hist2d(longInts[np.abs(Laplace_PSDs)<4], Laplace_PSDs[np.abs(Laplace_PSDs)<4], bins=2000, norm=colors.LogNorm())
plt.show()
# [np.abs(Laplace_PSDs)<10]


# plt.figure()
# plt.hist2d(laplacePhotonsPoles[:,0], laplacePhotonsPoles[:,0]/laplacePhotonsPoles[:,1], bins=2000, norm=colors.LogNorm())
# plt.figure()
# plt.hist2d(laplaceNeutronsPoles[:,0], laplaceNeutronsPoles[:,0]/laplaceNeutronsPoles[:,1], bins=2000, norm=colors.LogNorm())
# plt.figure()
# plt.hist2d(Laplace_Poles[:,0], Laplace_Poles[:,0]/Laplace_Poles[:,1], bins=2000, norm=colors.LogNorm())
# plt.scatter(Laplace_ChiSq[Laplace_ChiSq<1], Laplace_Poles[:,0][Laplace_ChiSq<1], c='red', s=1)
# plt.show()



# plt.axvline(energyCutoff)
# xmodel = np.linspace(min(longInts), 14, 2000)

# region STNG
# STNGcutoff = 0.016*np.log(longIntsSorted)+0.836
# STNGcutoff = 0.02*np.log(longIntsSorted)+0.834
# plt.plot(longIntsSorted, STNGcutoff)

# photonsPSDs = CCM_PSDsSorted[CCM_PSDsSorted>STNGcutoff]
# neutronsPSDs = CCM_PSDsSorted[CCM_PSDsSorted<STNGcutoff]

# # photonsPSDs2 = CCM_PSDsGreater1[CCM_PSDsGreater1>STNGcutoff[longIntsSorted > energyCutoff]]
# # neutronsPSDs2 = CCM_PSDsGreater1[CCM_PSDsGreater1<STNGcutoff[longIntsSorted > energyCutoff]]

# endregion

# region AmBe
# AmBecutoff = 0.015*np.log(longIntsSorted-0.05)+0.84
# plt.plot(longIntsSorted, AmBecutoff)

# photonsPSDs = Laplace_PSDsSorted[Laplace_PSDsSorted>AmBecutoff]
# neutronsPSDs = Laplace_PSDsSorted[Laplace_PSDsSorted<AmBecutoff]

# photonsPSDs2 = CCM_PSDsGreater1[CCM_PSDsGreater1>AmBecutoff[longIntsSorted > 1]]
# neutronsPSDs2 = CCM_PSDsGreater1[CCM_PSDsGreater1<AmBecutoff[longIntsSorted > 1]]
# endregion

# photonsData, photonsBins = np.histogram(photonsPSDs, bins=1000)
# neutronsData, neutronsBins = np.histogram(neutronsPSDs, bins=1000)

# plt.figure()
# plt.step(photonsBins[:-1], photonsData, label='photons')
# plt.step(neutronsBins[:-1], neutronsData, label='neutrons')
# photonsData, photonsBins = np.histogram(photonsPSDs2, bins=1000)
# neutronsData, neutronsBins = np.histogram(neutronsPSDs2, bins=1000)
# plt.step(photonsBins[:-1], photonsData, label='photons2')
# plt.step(neutronsBins[:-1], neutronsData, label='neutrons2')
# plt.legend()

# plt.title('Long Integral')
# plt.xlabel('Energy (MeVee)')
# plt.ylabel('Short integral/Long integral')
# plt.xlim(0,14)
# plt.show()

