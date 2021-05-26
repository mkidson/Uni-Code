from matplotlib import pyplot as plt
import numpy as np
from scipy.stats import poisson
from scipy.special import gamma
from numpy import cos, pi, sin, sqrt, exp, random
import matplotlib
# matplotlib.use('pgf')
matplotlib.rcParams.update({
    'pgf.texsystem': 'pdflatex',
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False
})


# cole function: feed np.histogram the bins array with the ends calculated by you iteratively and the centre bins just based on step. use np.concatenate

file = open(f'3rd Year\PHY3004W\Labs\Poisson Statistics\Data\Actual\mu4.txt', 'r')
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
data=data

def newBinEdges(arr, step):
    tempBinEdges = np.arange(np.min(arr), np.max(arr), step)
    h, edges = np.histogram(arr,tempBinEdges)
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
                
        h, edges = np.histogram(arr,tempBinEdges)

        if h[0]>=5 and h[-1]>=5:
            done=True
    return edges
step=1
newEdges=newBinEdges(data,step)
histData, histBins=np.histogram(data, newEdges)

binMiddles=np.concatenate(([0.5*(histBins[1] + histBins[2])-step],0.5*(histBins[2:-1] + histBins[1:-2]),[0.5*(histBins[-3] + histBins[-2])+step]))
print(histBins)
print(binMiddles)

xTicks=np.concatenate(([f'$<${histBins[1]}'],[str(x) for x in binMiddles[1:-1]],[f'$\geq${histBins[-2]}']))

plt.errorbar(binMiddles, histData, sqrt(histData*(1-histData/N)), fmt='.', capsize=2, elinewidth=1)
plt.xticks(binMiddles, xTicks)
plt.show()