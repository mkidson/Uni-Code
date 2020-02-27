import numpy as np
import scipy.stats as stats

#creates a numpy array to hold the data
data = np.zeros(60)
i = 0

#reads the data and puts it into the array
f = open('PHY2004W Computational\CP1\Activity1Data.txt', 'r')
header = f.readline()
for line in f:
    line = line.strip()
    columns = line.split()
    data[i] = float(columns[1])
    # print(i, data[i])
    i += 1

f.close()

#computing the mean and variance using numpy
npMean = np.mean(data)
npVariance = np.var(data)

#computing using scipy
n, (xmin, xmax), spMean, spVariance, s, k = stats.describe(data)

#printing out the results
print("Numpy Mean:", round(npMean, 5))
print("Numpy Variance:", round(npVariance, 5))
print("Scipy Mean:", round(spMean, 5))
print("Scipy Variance:", round(spVariance, 5))

