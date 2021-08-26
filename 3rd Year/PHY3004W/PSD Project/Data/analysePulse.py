# 02-07-2021
# Methods for digital PSD 
# Miles Kidson KDSMIL001

import numpy as np
import readRaw, math
from numpy import zeros, asarray, eye, poly1d, hstack, r_
from scipy import linalg
from scipy.interpolate import pade
from scipy.signal import residue
from matplotlib import pyplot as plt, colors


def CCM(pulse, t, short=26):
    """
    Integrates over "short" and "long" windows for a pulse and returns a discrimination parameter given by PSD_{CCM} = I_{long}/I_{short}. This is the Charge Comparison Method. 

    Parameters
    ---
    pulse : array_like
        Array of voltages over a time period `t`, should contain one pulse only. 
    
    t : array_like
        Array of the time period that `pulse` runs over. Needs to be scaled as in exampleRead.py, in nanoseconds.

    Returns
    ---
    out : float
        Discrimination parameter PSD_{CCM}
    """
    sampleToTime = 1.0 / 500e6 * 1e9 # in ns
    # The index of the peak of the pulse
    maxIndex = np.where(pulse==max(pulse))[0][0]
    # Finds the index of the starts and ends of the integration windows. The values it shifts by need to be optimised in some way. I think this method effectively centers every event on the peak of the pulse. Not sure if that's correct and if it's correct not sure if that's what we want
    intervalStart = maxIndex - (round(10/sampleToTime))
    intervalLongEnd = maxIndex + (round(100/sampleToTime))
    intervalShortEnd = maxIndex + (round(short/sampleToTime))
    # Integrates the pulse from the start to the long or short end
    longIntegral = np.trapz(pulse[intervalStart:intervalLongEnd], t[intervalStart:intervalLongEnd])
    shortIntegral = np.trapz(pulse[intervalStart:intervalShortEnd], t[intervalStart:intervalShortEnd])

    return shortIntegral/longIntegral, max(pulse), longIntegral


def PadeLaplace(pulse, t, nDecays=2):
    """
    something
    """
    sampleToTime = 1.0 / 500e6 * 1e9 # in ns
    # The index of the peak of the pulse and of the pulse when it has decayed to half the height of the peak
    maxIndex = np.where(pulse==max(pulse))[0][0]
    # halfMaxIndex = np.where(pulse <= pulse[maxIndex]/2)
    halfMaxIndices = np.where(pulse<=pulse[maxIndex]/2)[0]
    halfMaxIndicesIndex = np.where(halfMaxIndices > maxIndex)[0][0]
    halfMaxIndex = halfMaxIndices[halfMaxIndicesIndex]
    # print(maxIndex, halfMaxIndex)
    # The inverse of the time taken to decay to half the peak voltage. Scaled to ns
    p0 = 1/((halfMaxIndex-maxIndex)*sampleToTime)
    # print(p0)
    dt = sampleToTime
    # nDecays = 5
    # Slices the two arrays so they start at the peak of the pulse, as in this method we are only interested in the shape of the tail.
    pulse = pulse[maxIndex:]
    t = t[:-maxIndex]
    polesMain = []
    residuesMain = []

    # region didn't work 
    # N = 3
    # cumsum, moving_aves = [0], []

    # for i, x in enumerate(pulse, 1):
    #     cumsum.append(cumsum[i-1] + x)
    #     if i>=N:
    #         moving_ave = (cumsum[i] - cumsum[i-N])/N
    #         #can do stuff with moving_ave here
    #         moving_aves.append(moving_ave)
    
    # pulse = moving_aves
    
    # ds=zeros(2*nDecays)
    # for c in np.arange(0,2*nDecays):
    #     ds[c]=(dt * (1/math.factorial(c)) * (0.5*((((-t[0])**c) * np.exp(-p0 * t[0]) * pulse[0]) + (((-t[-1])**c) * np.exp(-p0 * t[-1]) * pulse[-1])) + np.sum(((-t[1:-1])**c) * np.exp(-p0 * t[1:-1]) * pulse[1:-1])))
    
    # p = np.arange(0.01,1,0.001)
    # transform = [np.sum(ds_i*(p_i-p0)**(ds_enum) for ds_enum, ds_i in enumerate(ds)) for p_i in p]

    # return transform, p
    # endregion
    finished = False
    for n in np.arange(1,nDecays+1):
        # print('n = ',n)
        ds=zeros(2*n)

        for c in np.arange(0,2*n):
            ds[c]=(dt * (1/math.factorial(c)) * (0.5*((((-t[0])**c) * np.exp(-p0 * t[0]) * pulse[0]) + (((-t[-1])**c) * np.exp(-p0 * t[-1]) * pulse[-1])) + np.sum(((-t[1:-1])**c) * np.exp(-p0 * t[1:-1]) * pulse[1:-1])))
        
        num, denom = pade(ds, n, n-1)
        # print('a')
        
        residues, p, k = residue(list(num), list(denom))
        poles = -(p+p0)

        residues = residues[::-1]
        poles = poles[::-1]

        # if n==3:
        for i in residues:
            if residues.dtype == 'complex128':
                if np.conjugate(np.around(i,7)) in np.around(residues,7):
                    finished = True
            elif residues.dtype == 'float64':
                pass # needs some check to see if one of the values is smaller than the other by a considerable amount. can't think of one rn

        if finished:
            print(f'total decay constants is: {n-1}')
            for k in range(len(polesMain[n-2])):
                print(f'lambda: {polesMain[n-2][k]:12.8} A: {residuesMain[n-2][k]:12.8}')
            break
        
        polesMain.append(poles)
        residuesMain.append(residues)

    fit=zeros(len(t),dtype=complex)         #Create fit from poles and residues
    for i in np.arange(0,n-1):
        fit = fit + residuesMain[-1][i]*np.exp(-polesMain[-1][i]*t)

    # print(polesMain[-1])
    # print(residuesMain[-1])
    return residuesMain[-1], polesMain[-1], n-1#, fit, t
    # return fit

def gaussian(x, mu, sigma, A):
    return (A*(1/(sigma*np.sqrt(2*np.pi)))*np.exp(-(1/2)*((x-mu)/sigma)**2))