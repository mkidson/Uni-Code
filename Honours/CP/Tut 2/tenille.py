#SPI using Gaussian kernal function
from cProfile import label
import pprint
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp

#Function we are interpolating:
def f(x):
    return 3*(x**4)-3*(x**2)

#Our so called 'data':
x_data = np.linspace(-10,10,60)
y_data = f(x_data)
#Number of interpolated points:
N = 1000
#smoothing length:
h = 0.5

#Interpolation values:
x_int = np.linspace(-5,5,N) #Interpolating on the interval [-5,5], a subset of the data interval
# x_int = 0.707
y_int = np.zeros(N)
# y_int = 0

for j in range(N):
    y = 0
    for i in np.arange(1,59): #x_i is the second data points, so that we don't get weird edge things
        #Gaussian Kernal
        W = (1/(h*np.sqrt(np.pi)))*np.exp(-(((x_data[i]-x_int[j])/h)**2))
        del_x = ((x_data[i]+x_data[i+1])/2) - ((x_data[i]+x_data[i-1])/2)
        y = y + del_x*y_data[i]*W
    y_int[j] = y

plt.plot(x_data,y_data,label= 'Actual Function')
plt.plot(x_data, [0]*60, 'rs', ms=4)
plt.plot(x_int,y_int, label = 'SPI')
plt.show()
