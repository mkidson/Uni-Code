import numpy as np
import scipy.stats as stats

#creates a numpy array to hold the data
N = 60
data = np.zeros(N)
i = 0

#reads the data and puts it into the array
f = open('PHY2004W Computational\CP1\Activity1Data.txt', 'r')
header = f.readline()
for line in f:
    line = line.strip()
    columns = line.split()
    data[i] = float(columns[1])
    i += 1

f.close()

#calculating the mean and variance from their definitions
mean = sum(data)/N

data2 = np.zeros(N)
for i in range(N):
    data2[i] = (data[i]-mean)**2

varianceB = sum(data2)/(N)
varianceU = sum(data2)/(N-1)

print("Mean:", round(mean, 5))
print("Biased Variance:", round(varianceB, 5))
print("Unbiased Variance:", round(varianceU, 5))

