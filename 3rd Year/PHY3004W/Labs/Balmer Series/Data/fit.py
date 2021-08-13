from matplotlib import pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from numpy import cos, pi, sin, sqrt, exp, random
import matplotlib
# matplotlib.use('pgf')
matplotlib.rcParams.update({
    'pgf.texsystem': 'pdflatex',
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
    'figure.constrained_layout.use': True,
    'savefig.bbox': 'tight',
})

mean = np.array([6563.3, 6563.5, 6563.4, 4860.3, 4338.5, 4339.3, 4339.3, 4100.3, 4100.5, 4100.3])*1e-10
meanUns = np.array([5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 4.9, 5.0, 5.0, 5.1])*1e-10
# expected = [6562.79]*3 + [4861.35] + [4340.472]*3 + [4101.734]*3
# expectedUns = [0.03]*3 + [0.05] + [0.006]*3 + [0.006]*3

fitX = np.array([0.25 - 1/(3**2)]*3 + [0.25 - 1/(4**2)] + [0.25 - 1/(5**2)]*3 + [0.25 - 1/(6**2)]*3)
fitY = 1/mean
fitYErr = meanUns/(mean**2)

def f(x,m,c):
    return m*x+c

Delta=sum(1/(fitYErr**2))*sum((fitX**2)/(fitYErr**2))-(sum(fitX/(fitYErr**2)))**2

m=(sum(1/(fitYErr**2))*sum((fitX*fitY)/(fitYErr**2))-sum(fitX/(fitYErr**2))*sum(fitY/(fitYErr**2)))/Delta
um=sqrt((sum(1/(fitYErr**2)))/Delta)

c=(sum((fitX**2)/(fitYErr**2))*sum(fitY/(fitYErr**2))-sum(fitX/(fitYErr**2))*sum((fitX*fitY)/(fitYErr**2)))/Delta
uc=sqrt((sum((fitX**2)/(fitYErr**2)))/Delta)

kirkupFit=m*fitX+c

chiSqKirk=sum(((fitY-kirkupFit)/fitYErr)**2)
dofKirk=len(fitX)-2

print(f'Chi Squared per d.o.f = {chiSqKirk/dofKirk}\n')

print(f'c = {c} +/- {uc}\nlambda = {m} +/- {um}')



plt.scatter(fitX, fitY)
plt.plot(fitX, kirkupFit)
plt.show()

