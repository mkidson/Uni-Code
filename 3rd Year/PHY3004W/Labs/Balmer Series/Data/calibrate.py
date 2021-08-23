from matplotlib import pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from numpy import cos, pi, sin, sqrt, exp, random
import matplotlib
matplotlib.use('pgf')
matplotlib.rcParams.update({
    'pgf.texsystem': 'pdflatex',
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
    'figure.constrained_layout.use': True,
    'savefig.bbox': 'tight',
    'axes.labelsize': 16,
    'legend.fontsize': 16
})

names = ['HeNe_0.2A_200ms_05um_6300to6400.csv','HeNe_0.2A_200ms_10um_6300to6400.csv','HeNe_0.2A_200ms_15um_6300to6400.csv','HeNe_0.5A_200ms_05um_6300to6400.csv','HeNe_0.5A_200ms_10um_6300to6400.csv','HeNe_0.5A_200ms_15um_6300to6400.csv','HeNe_0.8A_200ms_05um_6300to6400.csv','HeNe_0.8A_200ms_10um_6300to6400.csv','HeNe_0.8A_200ms_15um_6300to6400.csv','HeNe_1.0A_200ms_05um_6300to6400.csv','HeNe_1.0A_200ms_10um_6300to6400.csv','HeNe_1.0A_200ms_15um_6300to6400.csv']

# names = ['HeNe_0.5A_200ms_10um_6300to6400.csv']
corrs = []
corrsUn = []

for name in names:
    # region Ingest Data
    data0, data1 = np.genfromtxt(f'THRSAM005/{name}', delimiter=',', skip_header=14, unpack=True)

    data = np.array((data0, data1))
    # endregion

    # normalising
    # data[1] /= sum(data[1])

    def gaussian(x, mu, sigma, A, y):
        return A*(1/(sigma*sqrt(2*pi)))*exp(-(1/2)*((x-mu)/sigma)**2)+y

    p0 = [data[0][np.where(data[1]==max(data[1]))[0][0]],0.5,1000,100]

    popt, pcov = curve_fit(gaussian, data[0], data[1], p0=p0, sigma=sqrt(data[1]))
    xmodel = np.linspace(min(data[0]), max(data[0]), 1000)

    fit = gaussian(data[0], *popt)
    chiSq=sum(((data[1]-fit)/1)**2)
    dof=len(data[0])-2

    # print(f'\nMean at {popt[0]} +/- {popt[1]} A')
    # print(f'Laser is expected to have wavelength of 6328 A, so our correction factor is:\n-{popt[0]-6328} +/- {popt[1]} A\n')
    # print(f'Chi Squared per d.o.f = {chiSq/dof}\n')
    corrs.append(popt[0]-6328)
    corrsUn.append(popt[1])

    plt.figure()
    plt.step(data[0], data[1], label='Data')
    plt.plot(xmodel, gaussian(xmodel, *popt), label=f'Gaussian Fit:\n$\mu={np.around(popt[0],decimals=3)}$\n$\sigma={np.around(popt[1],decimals=3)}$')
    plt.legend()
    plt.xlabel('Wavelength $\lambda$ (A)')
    plt.ylabel('Counts')
    plt.savefig(f'Calibration/{name}.pgf')
# plt.show()
# corrs = np.array(corrs)
# corrsUn = np.array(corrsUn)
# corrsWeights = 1/(corrsUn**2)

# correction = sum(corrs*corrsWeights)/sum(corrsWeights)
# correctionUn = sqrt((sum(corrsWeights*corrs**2)/sum(corrsWeights))-correction**2)*(1/sqrt(len(corrs)-1))

# print(f'Correction is -{correction} +/- {correctionUn}')