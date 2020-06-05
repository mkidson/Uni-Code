import numpy as np
# Setting constants to allow for modification if need be
a = 0
b = 1
n = 1000
h = (b-a)/n
xs = np.linspace(a, b, n)
I = 0
# Looping through the summation, setting a new w at each iteration
for i in xs:
    w = a+(i+(1/2))*h
    I += 4/(1+(i**2))
# Multiplying by h as per the formula
I *= h
print(I)