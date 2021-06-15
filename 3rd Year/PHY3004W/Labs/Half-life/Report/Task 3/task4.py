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


halfLifeData=np.zeros(180)

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


    halfLifeData[n-1]=sum(nData[1][537:627])
    # print(np.where(nData >= 1555))
    # halfLifeData[n-1]=sum(np.where(nData[1] >= 1555 and nData[1] <= 1825))

halfLifeXData=np.arange(0,180)*10
halfLifeDataErr=sqrt(halfLifeData)
halfLifeDataLinear=np.log(halfLifeData)
halfLifeDataErrLinear=halfLifeDataErr/halfLifeData

# region Linear fitting to the half-life curve

print('------------------------------------------------')
print('Kirkup Weighted Linear Fit')
print('------------------------------------------------')
Delta=sum(1/(halfLifeDataErrLinear**2))*sum((halfLifeXData**2)/(halfLifeDataErrLinear**2))-(sum(halfLifeXData/(halfLifeDataErrLinear**2)))**2

m=(sum(1/(halfLifeDataErrLinear**2))*sum((halfLifeXData*halfLifeDataLinear)/(halfLifeDataErrLinear**2))-sum(halfLifeXData/(halfLifeDataErrLinear**2))*sum(halfLifeDataLinear/(halfLifeDataErrLinear**2)))/Delta
um=sqrt((sum(1/(halfLifeDataErrLinear**2)))/Delta)

c=(sum((halfLifeXData**2)/(halfLifeDataErrLinear**2))*sum(halfLifeDataLinear/(halfLifeDataErrLinear**2))-sum(halfLifeXData/(halfLifeDataErrLinear**2))*sum((halfLifeXData*halfLifeDataLinear)/(halfLifeDataErrLinear**2)))/Delta
uc=sqrt((sum((halfLifeXData**2)/(halfLifeDataErrLinear**2)))/Delta)

kirkupFit=m*halfLifeXData+c

chiSqKirk=sum(((halfLifeDataLinear-kirkupFit)/halfLifeDataErrLinear)**2)
dofKirk=len(halfLifeXData)-2

print(f'Chi Squared per d.o.f = {chiSqKirk/dofKirk}\n')

print(f'c = {c} +/- {uc}\nlambda = {m} +/- {um}')

# endregion

# region plotting shit

ax=plt.axes()
ax.set_box_aspect(5/14)

# ax.step(halfLifeXData, halfLifeData+halfLifeDataErr, linewidth=1, linestyle='--', color='r')
# ax.step(halfLifeXData, halfLifeData-halfLifeDataErr, linewidth=1, linestyle='--', color='r')
# ax.step(halfLifeXData, halfLifeData, linewidth=2)

ax.step(halfLifeXData, halfLifeDataLinear+halfLifeDataErrLinear, linewidth=0.5, linestyle='--', color='r', label='Uncertainty')
ax.step(halfLifeXData, halfLifeDataLinear-halfLifeDataErrLinear, linewidth=0.5, linestyle='--', color='r')
ax.step(halfLifeXData, halfLifeDataLinear, linewidth=1, label='Number of detector events')
ax.plot(halfLifeXData, m*halfLifeXData+c, linewidth=1)


ax.set_xlabel(r'Time (s)')
ax.set_ylabel(r'Number of detector events')
ax.set_xlim(left=0)
ax.set_ylim(bottom=0)

ax.legend()
# plt.yscale('log')

plt.show()
# plt.savefig(r'3rd Year\PHY3004W\Labs\Half-life\Report\Task 3\Plots\task4.pgf')


'''
Details about doing wide figures for latex:
    I like the ratio of 5:14 height to width. to get this when plotting I use
    ax.set_box_aspect(5/14) as well as 
    'figure.constrained_layout.use': True,
    Then the most important thing, to make sure the figure doesn't have shitty whitespace in the pdf, 
    do 'savefig.bbox': 'tight' in rcparams
'''

# endregion