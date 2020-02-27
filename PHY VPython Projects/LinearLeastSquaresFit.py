# This example code does a Linear Least Squares Fit for a data set.
# To use, enter your data in the 'xdata' and 'ydata' lists then run.
# The output is the slope (m) and the intercept (c) of the fit line
#   with uncertainties on the fitted quantities
# Code by S. Wheaton, modified by A. Hamilton

import math

# enter your data here
# be sure xdata and ydata have the same number of entries

xdata = [0.3, 0.6, 0.9, 1.2, 1.5]                
ydata = [0.2646168, 0.38934573, 0.515001, 0.77110872, 0.86156583]

t = []
r = []

for i in range(len(t)):
        xdata.append(r[i]**2)
        ydata.append(t[i]**2 * r[i])



# this gets the number of data points
N = len(xdata)


# this initializes the sums needed for the least squares fit

sum_xy = 0.0
sum_x = 0.0
sum_y = 0.0
sum_xx = 0.0
sum_dd = 0.0


# this calculates the sums needed for the least squares fit

for j in range(N):
       
        sum_xy += xdata[j]*ydata[j]
        sum_x += xdata[j]
        sum_y += ydata[j]
        sum_xx += xdata[j]*xdata[j]


# this does the linear least squares fit
# (compare these to equations on page 110 of the measurement manual)

mfit = (N*sum_xy - sum_x * sum_y) / (N*sum_xx - sum_x * sum_x)
cfit = (sum_xx*sum_y - sum_xy*sum_x) / (N*sum_xx - sum_x * sum_x)

for j in range(N):
        d = ydata[j] - (mfit * xdata[j] + cfit)
        sum_dd += d*d

umfit = math.sqrt((sum_dd)/(N*sum_xx - sum_x * sum_x)*N/(N-2))
ucfit = math.sqrt((sum_dd * sum_xx)/(N*(N*sum_xx - sum_x * sum_x))*N/(N-2))



# this prints the results

print("m = %6.2f +/- %5.2f"%(mfit,umfit))
print("c = %6.2f +/- %5.2f"%(cfit,ucfit))



# plot the model prediction with the best-fit parameters 
# (you will need matplotlib and numpy installed to do this)

import numpy as np
import matplotlib.pyplot as plt

xdata_array = np.array(xdata)
ydata_array = np.array(ydata)

plt.plot(xdata_array, ydata_array, 'bs', label = "Data")

yfit = mfit*xdata_array + cfit
plt.plot(xdata_array, yfit, '-r', label = "Unweighted Best Fit")

plt.title("The result of the model fit to the linear data")
plt.ylabel("y")
plt.xlabel("x")
plt.legend()
plt.show()
