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
    #'legend.fontsize': 16
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
longInts = np.load('STNG_Laplace_longInts.npy')
Laplace_Res = np.load('STNG_Laplace_Res.npy')
Laplace_Poles = np.load('STNG_Laplace_Poles.npy')

Laplace_PSDs = Laplace_Poles[:,1]/Laplace_Poles[:,0]
STNGSortingArr = longInts.argsort()
longIntsSorted = longInts[STNGSortingArr]
Laplace_PSDsSorted = Laplace_PSDs[STNGSortingArr]
# longIntsGreater1 = longIntsSorted[longIntsSorted > energyCutoff]
# CCM_PSDsGreater1 = CCM_PSDsSorted[longIntsSorted > energyCutoff]
# endregion

# region AmBe data
# longInts = np.load('AmBe_Laplace_longInts.npy')
# Laplace_Res = np.load('AmBe_Laplace_Res.npy')
# Laplace_Poles = np.load('AmBe_Laplace_Poles.npy')

# Laplace_PSDs = Laplace_Poles[:,1]/Laplace_Poles[:,0]
# AmBeSortingArr = longInts.argsort()
# longIntsSorted = longInts[AmBeSortingArr]
# Laplace_PSDsSorted = Laplace_PSDs[AmBeSortingArr]
# longIntsGreater1 = longIntsSorted[longIntsSorted > energyCutoff]
# Laplace_PSDsGreater1 = Laplace_PSDsSorted[longIntsSorted > energyCutoff]
# endregion

plt.figure()
# plt.hist2d(longInts[Laplace_PSDs<100], Laplace_PSDs[Laplace_PSDs<100], bins=2000, norm=colors.LogNorm())
plt.hist2d(longInts, Laplace_Res[:,0], bins=2000, norm=colors.LogNorm())
plt.show()

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
