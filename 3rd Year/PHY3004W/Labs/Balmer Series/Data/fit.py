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

mean = np.array([6562.6940630841655, 6562.904925440907, 6562.808964479332, 4859.750897375509, 4338.576844360169, 4338.707695676099, 4338.790053321519, 4099.839841017828, 4099.932180747187, 4099.7612741712755])*1e-10
meanUns = np.array([2.7177651982593303, 2.5023865795189195, 2.422620218994398, 2.4614880106855828, 2.816538274733167, 2.519507437189195, 2.4246811474198293, 2.6278417667992944, 2.469643479743145, 2.4151770101504293])*1e-10
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

