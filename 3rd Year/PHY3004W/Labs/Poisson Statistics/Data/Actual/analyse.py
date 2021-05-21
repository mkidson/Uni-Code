from matplotlib import pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from scipy.special import gamma
from numpy import cos, pi, sin, sqrt, exp, random
import matplotlib, math
matplotlib.use('pgf')
matplotlib.rcParams.update({
    'pgf.texsystem': 'pdflatex',
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
    'axes.labelsize': 14,
    'axes.titlesize': 15,
    'legend.fontsize': 14
})
# region Background
file = open(r'3rd Year\PHY3004W\Labs\Poisson Statistics\Data\Actual\background.txt', 'r')
blines = file.readlines()
bN = len(blines)
bi=0
bkgData = np.zeros(bN, dtype=int)
# Reading the file, getting the data into the data array
for line in blines:
    line = line.strip()
    columns = line.split()
    bkgData[bi] = float(columns[0])
    bi += 1
file.close()
bMean=np.mean(bkgData)
bUncertainty=sqrt(np.var(bkgData))
# print(bMean)
# print(bUncertainty)

# endregion

names=[4, 10, 30, 100]
steps=[1,1,3,4]
sampleVarianceArr=np.array([])
sampleVarianceUncertaintyArr=np.array([])
meanCountArr=np.array([])
meanCountUncertaintyArr=np.array([])
for q, name in enumerate(names):

# region Reads data in
    file = open(f'3rd Year\PHY3004W\Labs\Poisson Statistics\Data\Actual\mu{name}.txt', 'r')
    head=file.readline()
    lines = file.readlines()
    N = len(lines)
    i=0
    data = np.zeros(N, dtype=int)
    # Reading the file, getting the data into the data array
    for line in lines:
        line = line.strip()
        columns = line.split()
        data[i] = float(columns[0])
        i += 1
    file.close()
    data=data#-bMean
# endregion

# region Poisson plots
    def determine_bin_edges(arr, step):
        tempBinEdges = np.arange(np.min(arr), np.max(arr), step)
        i = 0
        while (True):
            binnedData, edges = np.histogram(arr, bins=tempBinEdges)
            if i >= len(tempBinEdges)-1:
                break
            if binnedData[i] < 5:
                if i <= len(tempBinEdges)/2:
                    tempBinEdges = np.delete(tempBinEdges, 0)
                else:
                    tempBinEdges = np.delete(tempBinEdges, len(tempBinEdges)-1)
                i=-1
            i+=1
        binnedData, edges = np.histogram(arr, bins=tempBinEdges)
        return tempBinEdges
    step=steps[q]
    binEdges=determine_bin_edges(data, step)
    # print(binEdges)
    histData, histBins=np.histogram(data, bins=binEdges, density=False)
    # print(histData)

    def poisson(x, mu):
        return ((mu**x)/(gamma(x+1)))*exp(-mu)

    xmodel=np.linspace(histBins[0], histBins[-1], 1000)
    meanCount=np.mean(data)
    # print(meanCount)
    meanCountUncertainty=sqrt(meanCount/N)
    # print(meanCountUncertainty)

    binMiddles=0.5*(histBins[1:] + histBins[:-1])
    xTicks=np.concatenate(([f'$\leq${histBins[1]}'],[str(x) for x in binMiddles[1:-1]],[f'$\geq${histBins[-2]}']))
    # plt.figure()
    # plt.errorbar(binMiddles, histData, sqrt(histData*(1-histData/N)), fmt='.', capsize=2, elinewidth=1)
    # plt.plot(xmodel, N*step*poisson(xmodel, meanCount), label=f'Poisson Distribution\nwith $\mu={meanCount}$')
    # plt.xticks(binMiddles, xTicks)
    # plt.xlabel('Counts per Trial')
    # plt.ylabel('Number of Trials with Given Number of Counts')
    # plt.title(f'Approximate Count Rate of {name}/10s')
    # plt.legend(loc='upper right')
    # plt.savefig(f'3rd Year\PHY3004W\Labs\Poisson Statistics\Report\Plots\poisson_mu{name}.pgf')
    
# endregion

# region Running mean
    runningMeans=[]
    runningMeansUncertainty=[]
    for i in range(N):
        currRunningMean=np.mean(data[:i+1])
        runningMeans.append(currRunningMean)
        currRunningMeanUncertainty=sqrt(currRunningMean/(i+1))
        runningMeansUncertainty.append(currRunningMeanUncertainty)

    # plt.figure()
    # plt.plot(list(range(N)), [name]*N, label=f'Expected value: {name}', color='C1')
    # plt.errorbar(list(range(N)), runningMeans, runningMeansUncertainty, fmt='.', elinewidth=1, capsize=2, ms=3, label='Running mean', color='C0')
    # plt.xlabel('Trial Number $j$')
    # plt.ylabel(r'Arithmetic Mean $\bar{x}_j$')
    # plt.title(f'Running mean for approximate count rate of {name}/10s')
    # plt.legend()
    # plt.savefig(f'3rd Year\PHY3004W\Labs\Poisson Statistics\Report\Plots\mu{name}_runningMean.pgf')
# endregion

# region Sample variance
    sampleVariance=sum((data-meanCount)**2)/(N-1)
    sampleVarianceUncertainty=sqrt((2*N*meanCount**2+(N-1)*meanCount)/(N*(N-1)))
    # print('---------------------------------------')
    # print(name)
    # print(sampleVariance)
    # print(sampleVarianceUncertainty)
    # print(meanCount)
    # print(meanCountUncertainty)
    sampleVarianceArr=np.append(sampleVarianceArr, sampleVariance)
    sampleVarianceUncertaintyArr=np.append(sampleVarianceUncertaintyArr, sampleVarianceUncertainty)
    meanCountArr=np.append(meanCountArr, meanCount)
    meanCountUncertaintyArr=np.append(meanCountUncertaintyArr, meanCountUncertainty)

# endregion

# Everything before this point is in the big for loop

# region s^2/x
sampleVar_meanCount=sampleVarianceArr/meanCountArr
sampleVar_meanCountUncertainty=sampleVar_meanCount*sqrt((sampleVarianceUncertaintyArr/sampleVarianceArr)**2 + (meanCountUncertaintyArr/meanCountArr)**2)
# plt.figure()
# plt.errorbar(meanCountArr, sampleVar_meanCount, xerr=meanCountUncertaintyArr, yerr=sampleVar_meanCountUncertainty, fmt='.', elinewidth=1, capsize=2, ms=3, label=r'$s^2/\bar{x}$')
# plt.plot(np.linspace(meanCountArr[0], meanCountArr[-1], 20), [1]*20, label='Expected value of 1')
# plt.xlabel(r'$\bar{x}$')
# plt.ylabel(r'$s^2/\bar{x}$')
# plt.title(r'Plot of $s^2/\bar{x}$ against sample mean for each approximate count rate')
# plt.legend()
# plt.savefig(r'3rd Year\PHY3004W\Labs\Poisson Statistics\Report\Plots\s2_x.pgf')
# endregion

# region Agreeing bins

numTotalBins=np.array([8,9,7,8])
numAgreeBins=np.array([5,6,6,6])
plt.figure()
plt.errorbar(meanCountArr, numAgreeBins/numTotalBins, sqrt(numAgreeBins*(1-(numAgreeBins/numTotalBins)))/numTotalBins, fmt='.', elinewidth=1, capsize=2, ms=3)
plt.plot(np.linspace(4,100,10), [0.68]*10, label='Expected value: 0.68')
plt.xlabel('Arithmetic Mean Count Rate')
plt.ylabel('$n_a/N_{bins}$')
plt.title('Fraction of bins that agree with the Poisson curve')
plt.legend(loc='upper right')
plt.savefig(r'3rd Year\PHY3004W\Labs\Poisson Statistics\Report\Plots\binAgree.pgf')

# endregion


# plt.show()