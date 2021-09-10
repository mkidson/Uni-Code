from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
from numpy import cos, pi, sin, sqrt, exp, random
import matplotlib
matplotlib.use('pgf')
matplotlib.rcParams.update({
    'pgf.texsystem': 'pdflatex',
    'font.family': 'sans-serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
    'figure.constrained_layout.use': True,
    'savefig.bbox': 'tight',
    'legend.handlelength': 1,
    'axes.labelsize': 14,
    'legend.fontsize': 12,
    'xtick.labelsize': 12,
    'ytick.labelsize': 12
})


# names = ["PHY3004W_gglab_BlueCo60_gated1.csv", "PHY3004W_gglab_BlueCo60_gated2.csv", "PHY3004W_gglab_BlueNa22_gated1.csv", "PHY3004W_gglab_BlueNa22_gated2.csv", "PHY3004W_gglab_RedCo60_gated1.csv", "PHY3004W_gglab_RedNa22_gated1.csv"]

name = "PHY3004W_gglab_RedCo60_gated1.csv"


# for name in names:
# region Ingest Data
dataDf = pd.read_csv(f'PHY3004W_gglab_coinc_spectra/{name}', header=0, skiprows=[0,1,2,4,5])
liveTime = int(dataDf.columns[1])
data = dataDf.T.to_numpy(dtype='float')
if name[15:19]=='Blue':
    data[0] = (data[0]+0.0001325744712578748)/0.3488421803288909
elif name[15:18]=='Red':
    data[0] = (data[0]+0.00013939501839624682)/0.34919335675192653
# data[1] /= liveTime

# endregion
plt.figure()
ax=plt.axes()
ax.set_box_aspect(5/14) # for wide boys use 5/14

ax.set_xlabel('Energy (keV)')
ax.set_ylabel('Counts')

ax.step(data[0], data[1], lw=1)
ax.fill_between(data[0][0:330],data[1][0:330], step='pre', color='green', alpha=0.5, label='Compton continuum for 1172 keV photopeak')
ax.axvline(data[0][58], linestyle='dashed', color='black', linewidth=1)
ax.axvline(data[0][68], linestyle='dashed', color='black', linewidth=1)
ax.text(data[0][57], 800, 'Possible 1172 keV \ndouble escape peak', rotation='vertical', horizontalalignment='right', size=12)


ax.set_xlim(left=0,right=1700)
# ax.set_xlim(left=0,right=600)
ax.set_ylim(bottom=0)


ax.legend()
# plt.show()
plt.savefig(r'Plots/60Co_Gated.pgf')