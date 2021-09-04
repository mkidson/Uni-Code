from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
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


names = ["PHY3004W_gglab_BlueCo60_gated1.csv", "PHY3004W_gglab_BlueCo60_gated2.csv", "PHY3004W_gglab_BlueNa22_gated1.csv", "PHY3004W_gglab_BlueNa22_gated2.csv", "PHY3004W_gglab_RedCo60_gated1.csv", "PHY3004W_gglab_RedNa22_gated1.csv"]

for name in names:
    # region Ingest Data
    dataDf = pd.read_csv(f'PHY3004W_gglab_coinc_spectra/{name}', header=0, skiprows=[0,1,2,4,5])
    liveTime = int(dataDf.columns[1])
    data = dataDf.T.to_numpy(dtype='float')
    if name[15:19]=='Blue':
        data[0] = (data[0]+0.0001325744712578748)/0.3488421803288909
    elif name[15:19]=='Red':
        data[0] = (data[0]+0.00013939501839624682)/0.34919335675192653
    data[1] /= liveTime

    # endregion
    plt.figure()
    plt.step(data[0], data[1])

plt.show()