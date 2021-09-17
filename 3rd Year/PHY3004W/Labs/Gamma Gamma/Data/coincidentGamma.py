from matplotlib import pyplot as plt
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
    'legend.handlelength': 1,
    'axes.labelsize': 14,
    'legend.fontsize': 12,
    'xtick.labelsize': 12,
    'ytick.labelsize': 12
})


# names = ["PHY3004W_gglab_BlueCo60_gated1.csv", "PHY3004W_gglab_BlueCo60_gated2.csv"] 
# names = ["PHY3004W_gglab_BlueNa22_gated1.csv", "PHY3004W_gglab_BlueNa22_gated2.csv"]#, "PHY3004W_gglab_RedCo60_gated1.csv", "PHY3004W_gglab_RedNa22_gated1.csv"]

name = "PHY3004W_gglab_RedCo60_gated1.csv"

plt.figure()
ax=plt.axes()

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
ax.set_box_aspect(5/14) # for wide boys use 5/14

ax.set_xlabel('Energy (keV)')
ax.set_ylabel('Counts')

# if names.index(name)==0:
#     label='TSCA window wide open'
# elif names.index(name)==1:
#     label='TSCA window centred on \n511 keV photopeak'

ax.step(data[0], data[1], lw=1)#, label=label)


# ax.set_xlim(left=140,right=1400)
ax.set_xlim(left=0,right=1700)
# ax.set_xlim(left=0,right=278)
ax.set_ylim(bottom=0)


ax.legend()
plt.show()
# plt.savefig(r'Plots/.pgf')

# region red_60Co_gated
# ax.fill_between(data[0][0:330],data[1][0:330], step='pre', color='green', alpha=0.5, label='Compton continuum for 1172 keV photopeak')
# ax.axvline(data[0][58], linestyle='dashed', color='black', linewidth=1)
# ax.axvline(data[0][68], linestyle='dashed', color='black', linewidth=1)
# ax.text(data[0][72], 800, 'Possible 1172 keV \ndouble escape peak', rotation='horizontal', horizontalalignment='left', size=12)
# ax.axvline(data[0][412], linestyle='dashed', color='black', linewidth=1)
# ax.text(data[0][420], 1200, '1172 keV photopeak', rotation='horizontal', horizontalalignment='left', size=12)
# ax.axvline(data[0][466], ymax=0.5, linestyle='dashed', color='black', linewidth=1)
# ax.text(data[0][470], 500, 'Remnants of the \n1332 keV \nphotopeak', rotation='horizontal', horizontalalignment='left', size=12)
# ax.set_xlim(left=0,right=1700)
# endregion

# region red_22Na_gated
# ax.fill_between(data[0][0:115],data[1][0:115], step='pre', color='green', alpha=0.5, label='Compton continuum for \n511 keV photopeak')
# ax.axvline(data[0][178], linestyle='dashed', color='black', linewidth=1)
# ax.text(data[0][185], 25000, '511 keV photopeak', rotation='horizontal', horizontalalignment='left', size=12)
# ax.set_xlim(left=0,right=800)
# endregion

