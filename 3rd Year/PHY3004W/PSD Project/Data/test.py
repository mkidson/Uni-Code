from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
from scipy.interpolate import pade
from scipy.signal import residue
from numpy import cos, pi, sin, sqrt, exp, random
import matplotlib, math
from scipy.fft import rfft, rfftfreq
# matplotlib.use('pgf')
matplotlib.rcParams.update({
    'pgf.texsystem': 'pdflatex',
    'font.family': 'sans-serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
    'figure.constrained_layout.use': True,
    'savefig.bbox': 'tight',
    #'axes.labelsize': 16,
    #'legend.fontsize': 16
    #'xtick.labelsize': 12,
    #'ytick.labelsize': 12
})

sampleTime = 0.001
tArr = np.arange(0,10,sampleTime)
lambda1 = 5
lambda2 = 1
signal1 = np.exp(-lambda1*tArr)
signal2 = np.exp(-lambda2*tArr)
signal = 0.2*np.exp(-lambda1*tArr)+0.4*np.exp(-lambda2*tArr)
# signal = 3*sin(lambda1*tArr)+4*sin(lambda2*tArr)

# region trying pade laplace
halfMaxIndex = np.where(signal<=signal[0]/2)[0][0]
p0 = 1/(tArr[halfMaxIndex])
ds=np.zeros(4)

for c in np.arange(0,4):
    ds[c]=(sampleTime * (1/math.factorial(c)) * (0.5*((((-tArr[0])**c) * np.exp(-p0 * tArr[0]) * signal[0]) + (((-tArr[-1])**c) * np.exp(-p0 * tArr[-1]) * signal[-1])) + np.sum(((-tArr[1:-1])**c) * np.exp(-p0 * tArr[1:-1]) * signal[1:-1])))

numerator, denominator = pade(ds, 2, 1)
residues, p, k = residue(list(numerator), list(denominator))
poles = -(p+p0)

residues = residues[::-1]
poles = poles[::-1]

print('\nPade Laplace:')
print(f'Decay Constants: {poles}')
print(f'Amplitudes: {residues}')
padeLaplaceFit = residues[0]*np.exp(-poles[0]*tArr) + residues[1]*np.exp(-poles[1]*tArr)
# endregion

# region trying fourier
# transform = rfft(signal)
# freqs = rfftfreq(len(signal), sampleTime)
# plt.figure()
# plt.plot(2*pi*freqs, np.abs(transform), color='blue', lw=1)
# plt.xlabel('frequency')
# plt.ylabel('amplitude?')
# endregion

# region trying curve_fit
# def twoExponentials(t, l1, l2, a1, a2):
#     """
#     time, lambda1, lambda2, amplitude1, amplitude2
#     """
#     return a1*np.exp(-l1*t) + a2*np.exp(-l2*t)

# popt, pcov = curve_fit(twoExponentials, tArr, signal, p0=[1,1,1,1])

# print('\ncurve_fit:')
# print(f'Decay Constants: {popt[:2]}')
# print(f'Amplitudes: {popt[2:]}')
# curveFit = twoExponentials(tArr, *popt)
# endregion

plt.figure()
plt.plot(tArr, signal, color='blue', lw=1, label='signal')
# plt.plot(tArr, signal1, color='red', lw=1)
# plt.plot(tArr, signal2, color='green', lw=1)
plt.plot(tArr, padeLaplaceFit, color='red', lw=1, label='Pade Laplace Fit', ls='--')
# plt.plot(tArr, curveFit, color='green', lw=1, label='curve Fit')
plt.xlabel('time')
plt.ylabel('signal')
plt.legend()
plt.show()