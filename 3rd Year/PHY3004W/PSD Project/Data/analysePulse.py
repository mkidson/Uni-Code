# 02-07-2021
# Methods for PSD 
# Miles Kidson KDSMIL001

import numpy as np
import readRaw, math
from numpy import zeros, asarray, eye, poly1d, hstack, r_
from scipy import linalg
from scipy.interpolate import pade
from scipy.signal import residue
from matplotlib import pyplot as plt, colors


def CCM(pulse, t):
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
    intervalShortEnd = maxIndex + (round(25/sampleToTime))
    # Integrates the pulse from the start to the long or short end
    longIntegral = np.trapz(pulse[intervalStart:intervalLongEnd], t[intervalStart:intervalLongEnd])
    shortIntegral = np.trapz(pulse[intervalStart:intervalShortEnd], t[intervalStart:intervalShortEnd])

    return longIntegral/shortIntegral

# def myPade(an):
#     mat = 


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
    # Slices the two arrays so they start at the peak of the pulse, as in this method we are only interested in the shape of the tail.
    pulse = pulse[maxIndex:]
    t = t[:-maxIndex]

    # N = 3
    # cumsum, moving_aves = [0], []

    # for i, x in enumerate(pulse, 1):
    #     cumsum.append(cumsum[i-1] + x)
    #     if i>=N:
    #         moving_ave = (cumsum[i] - cumsum[i-N])/N
    #         #can do stuff with moving_ave here
    #         moving_aves.append(moving_ave)
    
    # pulse = moving_aves

    ds = []
    nDecays = 2

    for n in np.arange(1,nDecays+1):
        # print('n = ',n)
        ds=zeros(2*n)

        for c in np.arange(0,2*n):
            ds[c]=(dt * (1/math.factorial(c)) * (0.5*((((-t[0])**c) * np.exp(-p0 * t[0]) * pulse[0]) + (((-t[-1])**c) * np.exp(-p0 * t[-1]) * pulse[-1])) + np.sum(((-t[1:-1])**c) * np.exp(-p0 * t[1:-1]) * pulse[1:-1])))
        
        num, denom = pade(ds, n, n-1)
        
        residues, p, k = residue(list(num), list(denom))
        poles = -(p+p0)

        residues = residues[::-1]
        poles = poles[::-1]

        # print(f'Poles are {poles}')
        # print(f'Residues are {residues}')
    
    return residues, poles