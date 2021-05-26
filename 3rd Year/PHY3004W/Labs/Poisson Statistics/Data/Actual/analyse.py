from matplotlib import pyplot as plt
import numpy as np
from scipy.special import gamma
from scipy.stats import poisson
from numpy import cos, pi, sin, sqrt, exp, random
import matplotlib, math
matplotlib.use('pgf')
matplotlib.rcParams.update({
    'pgf.texsystem': 'pdflatex',
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
    # 'axes.labelsize': 10*2,
    # 'axes.titlesize': 10*2,
    # 'legend.fontsize': 8*2
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
steps=[1,2,3,4]
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
    def newBinEdges(arr, step):
        tempBinEdges = np.arange(np.min(arr), np.max(arr), step)
        h, edges = np.histogram(arr, tempBinEdges)
        tempBinEdges=edges
        newLow=[edges[0],edges[1]]
        newHigh=[edges[-2],edges[-1]]

        done=False
        while not done:
            if h[0]<5:
                newLow[1]=edges[2]
                tempBinEdges=np.concatenate((newLow, tempBinEdges[3:]))

            if h[-1]<5:
                newHigh[0]=edges[-3]
                tempBinEdges=np.concatenate((tempBinEdges[:-3],newHigh))
                    
            h, edges = np.histogram(arr, tempBinEdges)

            if h[0]>=5 and h[-1]>=5:
                done=True
        return edges    
    
    step=steps[q]
    binEdges=newBinEdges(data, step)
    histData, histBins=np.histogram(data, binEdges)


    def myPoisson(x, mu):
        return ((mu**x)/(gamma(x+1)))*exp(-mu)

    xmodel=np.linspace(histBins[1], histBins[-2], 1000)

    meanCount=np.mean(data)
    meanCountUncertainty=sqrt(meanCount/N)

    yUpper=[(1-poisson.cdf(histBins[-2], meanCount))*N]*2
    yLower=[(poisson.cdf(histBins[1], meanCount))*N]*2

    binMiddles=np.concatenate(([0.5*(histBins[1] + histBins[2])-step],0.5*(histBins[2:-1] + histBins[1:-2]),[0.5*(histBins[-3] + histBins[-2])+step]))
    xTicks=np.concatenate(([f'$<${histBins[1]}'],[f'[{x},{x+step})' for x in histBins[1:-2]],[f'$\geq${histBins[-2]}']))
    # plt.figure()
    # plt.errorbar(binMiddles, histData, sqrt(histData*(1-histData/N)), fmt='.', capsize=2, elinewidth=1)
    # plt.plot(xmodel, N*step*myPoisson(xmodel, meanCount), label=f'Poisson Distribution\nwith $\mu={meanCount}$')
    # plt.plot([histBins[-2], histBins[-2]+step], yUpper, color='C1')
    # plt.plot([histBins[1]-step, histBins[1]], yLower, color='C1')
    # # plt.plot(xmodelLower, poisson(xmodelLower, meanCount))
    # plt.xticks(binMiddles, xTicks)
    # plt.xlabel('Counts per Trial')
    # plt.ylabel('No. Trials with Given No. Counts')
    # plt.title(f'Approximate Count Rate of {name}/10s')
    # plt.legend()
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
    # plt.plot(list(range(N)), [meanCount]*N, label=f'Arithmetic Mean: {meanCount}', color='C1')
    # plt.errorbar(list(range(N)), runningMeans, runningMeansUncertainty, fmt='.', elinewidth=1, capsize=2, ms=3, label='Running mean', color='C0')
    # plt.xlabel('Trial Number $j$')
    # plt.ylabel(r'Arithmetic Mean $\bar{x}_j$')
    # plt.title(f'Approximate Count Rate of {name}/10s')
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

numTotalBins=np.array([8,6,7,8])
numAgreeBins=np.array([5,3,6,7])
# print(np.mean(numAgreeBins/numTotalBins))
# binsAgreeMean=np.mean(numAgreeBins/numTotalBins)
# binsAgreeUncertainty=sum(((numAgreeBins/numTotalBins)-binsAgreeMean)**2)/(np.sum(numTotalBins)-1)
# print(f'{binsAgreeMean} +/- {binsAgreeUncertainty}')

# plt.figure()
# plt.errorbar(meanCountArr, numAgreeBins/numTotalBins, sqrt(numAgreeBins*(1-(numAgreeBins/numTotalBins)))/numTotalBins, fmt='.', elinewidth=1, capsize=2, ms=3)
# plt.plot(np.linspace(4,100,10), [0.68]*10, label='Expected value: 0.68')
# plt.xlabel('Arithmetic Mean')
# plt.ylabel('$n_a/N_{bins}$')
# plt.title('Fraction of bins that agree with the Poisson curve')
# plt.legend()
# plt.savefig(r'3rd Year\PHY3004W\Labs\Poisson Statistics\Report\Plots\binAgree.pgf')

# endregion


# plt.show()
