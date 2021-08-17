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

mean = np.array([6562.884677998162, 6563.095540354904, 6562.9995793933285, 4859.941512289506, 4338.767459274166, 4338.898310590096, 4338.980668235516, 4100.030455931825, 4100.122795661184, 4099.951889085272])
meanUns = np.array([1.3260220396402362, 0.7962571005011349, 0.4910962250135318, 0.6565135211790716, 1.518214289808576, 0.8485307907163656, 0.5011640882936601, 1.130327000507779, 0.686458807052474, 0.4529533829228385])
# expected = [6562.79]*3 + [4861.35] + [4340.472]*3 + [4101.734]*3
# expectedUns = [0.03]*3 + [0.05] + [0.006]*3 + [0.006]*3

meanWeights = 1/(meanUns**2)

H3 = sum(mean[:3]*meanWeights[:3])/sum(meanWeights[:3])
H3Un = sqrt((sum(meanWeights[:3]*mean[:3]**2)/sum(meanWeights[:3]))-H3**2)*(1/sqrt(len(mean[:3])-1))
H4 = mean[3]
H4Un = meanWeights[3]
H5 = sum(mean[4:7]*meanWeights[4:7])/sum(meanWeights[4:7])
H5Un = sqrt((sum(meanWeights[4:7]*mean[4:7]**2)/sum(meanWeights[4:7]))-H5**2)*(1/sqrt(len(mean[4:7])-1))
H6 = sum(mean[7:]*meanWeights[7:])/sum(meanWeights[7:])
H6Un = sqrt((sum(meanWeights[7:]*mean[7:]**2)/sum(meanWeights[7:]))-H6**2)*(1/sqrt(len(mean[7:])-1))

weightedMeans = np.array([H3, H4, H5, H6])*1e-10
weightedMeansUn = np.array([H3Un, H4Un, H5Un, H6Un])*1e-10

fitX = np.array([0.25 - 1/(3**2), 0.25 - 1/(4**2), 0.25 - 1/(5**2), 0.25 - 1/(6**2)])
fitY = 1/weightedMeans
fitYErr = weightedMeansUn/(weightedMeans**2)

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

