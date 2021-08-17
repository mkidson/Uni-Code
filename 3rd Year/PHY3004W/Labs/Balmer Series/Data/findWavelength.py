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

names = ['H3 (6563 A)/H3-210808-1304-100um-300ms-6562-6600A-0.2A-lightsOff.csv','H3 (6563 A)/H3-210808-1308-050um-300ms-6561-6600A-0.2A-lightsOff.csv','H3 (6563 A)/H3-210808-1311-020um-300ms-6557-6600A-0.2A-lightsOff.csv','H4 (4861 A)/H4-210808-1300-020um-300ms-4861-4900A-0.2A-lightsOff.csv','H5 (4341 A)/H5-210808-1239-100um-300ms-4338-4380A-0.2A-lightsOff.csv','H5 (4341 A)/H5-210808-1244-050um-300ms-4332-4380A-0.2A-lightsOff.csv','H5 (4341 A)/H5-210808-1247-020um-300ms-4340-4380A-0.2A-lightsOff.csv','H6 (4102 A)/H6-210808-1201-100um-300ms-4099-4150A-0.2A-lightsOff.csv','H6 (4102 A)/H6-210808-1210-050um-300ms-4099-4150A-0.2A-lightsOff.csv','H6 (4102 A)/H6-210808-1218-020um-300ms-4102-4150A-0.2A-lightsOff.csv']

# names = ['H3 (6563 A)\H3-210808-1306-050um-300ms-6559-6600A-1.0A-lightsOff.csv']
means = []
uns = []
for name in names:
    data0, data1 = np.genfromtxt(f'{name}', delimiter=',', skip_header=14, unpack=True)
    data = np.array((data0, data1))

    def gaussian(x, mu, sigma, A, y):
        return A*(1/(sigma*sqrt(2*pi)))*exp(-(1/2)*((x-mu)/sigma)**2)+y
    
    p0=[data[0][np.where(data[1]==max(data[1]))[0][0]],1,1000,100]

    popt, pcov = curve_fit(gaussian, data[0], data[1], p0=p0, sigma=sqrt(data[1]))
    mean = popt[0]-22.462101126143132
    meanUn = sqrt(popt[1]**2 + 0.1410598624822681**2)

    fit = gaussian(data[0], *popt)
    chiSq=sum(((data[1]-fit)/1)**2)
    dof=len(data[0])-2

    means.append(mean)
    uns.append(meanUn)

    # print('--------------------------------')
    # print(f'[{mean}, {meanUn}]')
    # print(f'Chi Squared per d.o.f = {chiSq/dof}')
    plt.figure()

    xmodel = np.linspace(min(data[0]), max(data[0]), 1000)
    plt.step(data[0], data[1])
    plt.plot(xmodel, gaussian(xmodel, *popt))

# plt.show()

print(means)
print(uns)

"""
the literature values of the wavelengths of the spectral lines

in A

4101.734 +/- 0.006 
4340.472 +/- 0.006
4861.35 +/- 0.05  
6562.79 +/- 0.03  

Correction:
+22.5 +/- 4.0 

"""