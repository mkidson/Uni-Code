import numpy as np
import scipy.stats as stats
from math import sqrt

f = open('PHY2004W Computational\CP1\LinearNoErrors.txt', 'r')
header = f.readline()
N = 12
data = np.zeros([2, N])
i = 0

for line in f:
    data[0, i] = line.split()[0]
    data[1, i] = line.split()[1]
    i += 1

xy = []
for c in range(N):
    xy.append(round(data[0, c]*data[1,c], 3))

x2 = []
for t in range(N):
    x2.append(round(data[0,t]**2, 3))

x = data[0]
y = data[1]
d = []
d2 = []

m = ((N*sum(xy)) - sum(x)*sum(y))/((N*sum(x2))-(sum(x))**2)
c = ((sum(x2)*sum(y))-(sum(xy)*sum(x)))/((N*sum(x2))-(sum(x)**2))

for r in range(N):
    d.append(y[r] - ((m*x[r]) + c))
    d2.append(d[r]**2)

um = sqrt(((sum(d2)/((N*sum(x2))-(sum(x)**2)))*(N/(N-2))))
uc = sqrt((((sum(d2)*sum(x2))/(N*((N*sum(x2))-(sum(x)**2))))*(N/(N-2))))

print("m:", round(m, 5))
print("u(m):", round(um, 5))
print("c:", round(c, 5))
print("u(c):", round(uc, 5))

f.close()

