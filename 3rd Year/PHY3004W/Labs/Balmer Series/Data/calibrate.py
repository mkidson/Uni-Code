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

# region Ingest Data
data0, data1 = np.genfromtxt(r'BalmerCalibrationJoJoSaSaMiMi.csv', delimiter=',', skip_header=14, unpack=True)

data = np.array((data0, data1))
# endregion

# normalising
# data[1] /= sum(data[1])

def gaussian(x, mu, sigma, A, y):
    return A*(1/(sigma*sqrt(2*pi)))*exp(-(1/2)*((x-mu)/sigma)**2)+y

p0 = [data[0][np.where(data[1]==max(data[1]))[0][0]],1,1000,100]

popt, pcov = curve_fit(gaussian, data[0], data[1], p0=p0, sigma=sqrt(data[1]))
xmodel = np.linspace(min(data[0]), max(data[0]), 1000)

fit = gaussian(data[0], *popt)
chiSq=sum(((data[1]-fit)/1)**2)
dof=len(data[0])-2

print(f'\nMean at {popt[0]} +/- {popt[1]} A')
print(f'Laser is expected to have wavelength of 6328 A, so our correction factor is:\n-{popt[0]-6328} +/- {popt[1]} A\n')
print(f'Chi Squared per d.o.f = {chiSq/dof}\n')

plt.plot(xmodel, gaussian(xmodel, *popt))
plt.step(data[0], data[1])#/sum(data[1]))
plt.show()