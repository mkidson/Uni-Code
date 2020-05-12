from numpy import cos,pi,linspace
from pylab import plot,show,subplot

a = [1,4,2] # plotting the curves for
b = [2,1,1] # different values of a/b
delta = [pi/3, -pi/4, 0]
t = linspace(-pi,pi,300)

for i in range(0,3):
 x = cos(a[i] * t)
 y = cos(b[i] * t + delta[i])
 subplot(2,2,i+1)
 plot(x,y)

show()