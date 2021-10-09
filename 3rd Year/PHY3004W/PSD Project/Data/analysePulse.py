# 02-07-2021
# Methods for digital PSD 
# Miles Kidson KDSMIL001

import numpy as np
import readRaw, math
from numpy import zeros, asarray, eye, poly1d, hstack, r_
from scipy import linalg
from scipy.interpolate import pade
from scipy.signal import residue
from scipy.optimize import curve_fit
from matplotlib import pyplot as plt, colors


def CCM(pulse, t, short=22):
    """
    Integrates over "short" and "long" windows for a pulse and returns a discrimination parameter given by PSD_{CCM} = I_{short}/I_{long}. This is the Charge Comparison Method. 

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
    maxIndex = np.where(pulse==max(pulse[365:400]))[0][0]
    # Finds the index of the starts and ends of the integration windows. The values it shifts by need to be optimised in some way. I think this method effectively centers every event on the peak of the pulse. Not sure if that's correct and if it's correct not sure if that's what we want
    intervalStart = maxIndex - (round(10/sampleToTime))
    intervalLongEnd = maxIndex + (round(250/sampleToTime))
    intervalShortEnd = maxIndex + (round(short/sampleToTime))
    # Integrates the pulse from the start to the long or short end
    longIntegral = np.trapz(pulse[intervalStart:intervalLongEnd], t[intervalStart:intervalLongEnd])
    shortIntegral = np.trapz(pulse[intervalStart:intervalShortEnd], t[intervalStart:intervalShortEnd])

    return shortIntegral/longIntegral, longIntegral

def PadeLaplace(pulse, t):
    """
    something
    """
    sampleToTime = 1.0 / 500e6 * 1e9 # in ns
    # The index of the peak of the pulse and of the pulse when it has decayed to half the height of the peak
    maxIndex = np.where(pulse==max(pulse[365:400]))[0][0]
    intervalStart = maxIndex - (round(10/sampleToTime))
    intervalLongEnd = maxIndex + (round(250/sampleToTime))
    longIntegral = np.trapz(pulse[intervalStart:intervalLongEnd], t[intervalStart:intervalLongEnd])
    # halfMaxIndex = np.where(pulse <= pulse[maxIndex]/2)
    halfMaxIndices = np.where(pulse<=pulse[maxIndex]/2)[0]
    halfMaxIndicesIndex = np.where(halfMaxIndices > maxIndex)[0][0]
    halfMaxIndex = halfMaxIndices[halfMaxIndicesIndex]
    # print(maxIndex, halfMaxIndex)
    # The inverse of the time taken to decay to half the peak voltage. Scaled to ns
    p0 = 1/((halfMaxIndex-maxIndex)*sampleToTime)
    # print(p0)
    dt = sampleToTime
    nDecays = 2
    # Slices the two arrays so they start at the peak of the pulse, as in this method we are only interested in the shape of the tail.
    pulse = pulse[maxIndex:]
    t = t[:-maxIndex]
    polesMain = []
    residuesMain = []

    ds=zeros(2*nDecays)

    for c in np.arange(0,4):
        ds[c]=(dt * (1/math.factorial(c)) * (0.5*((((-t[0])**c) * np.exp(-p0 * t[0]) * pulse[0]) + (((-t[-1])**c) * np.exp(-p0 * t[-1]) * pulse[-1])) + np.sum(((-t[1:-1])**c) * np.exp(-p0 * t[1:-1]) * pulse[1:-1])))

    numerator, denominator = pade(ds, 2, 1)
    residues, p, k = residue(list(numerator), list(denominator))
    poles = -(p+p0)

    fit = exponential(t, poles[0], residues[0], poles[1], residues[1])
    chiSq=sum(((pulse-fit)/1)**2)
    dof=len(t)-4


    return residues, poles, longIntegral, chiSq/dof, halfMaxIndex

def gaussian(x, mu, sigma, A):
    return (A*(1/(sigma*np.sqrt(2*np.pi)))*np.exp(-(1/2)*((x-mu)/sigma)**2))

def exponential(x, lambda1, A1, lambda2, A2):
    return A1*np.exp(-lambda1*x)+A2*np.exp(-lambda2*x)

def exponentialFit(pulse, t):
    sampleToTime = 1.0 / 500e6 * 1e9 # in ns
    # The index of the peak of the pulse and of the pulse when it has decayed to half the height of the peak
    maxIndex = np.where(pulse==max(pulse))[0][0]
    intervalStart = maxIndex - (round(10/sampleToTime))
    intervalLongEnd = maxIndex + (round(100/sampleToTime))
    longIntegral = np.trapz(pulse[intervalStart:intervalLongEnd], t[intervalStart:intervalLongEnd])
    halfMaxIndices = np.where(pulse<=pulse[maxIndex]/2)[0]
    halfMaxIndicesIndex = np.where(halfMaxIndices > maxIndex)[0][0]
    halfMaxIndex = halfMaxIndices[halfMaxIndicesIndex]
    # print(maxIndex, halfMaxIndex)
    # The inverse of the time taken to decay to half the peak voltage. Scaled to ns
    p = 1/((halfMaxIndex-maxIndex)*sampleToTime)

    pulse = pulse[maxIndex:]
    t = t[:-maxIndex]

    popt, pcov = curve_fit(exponential, t, pulse, p0=[p, 1, p, 1])

    return popt, t, longIntegral

def Breit_Wigner(x, x_0, gamma, A):
    return A/(np.pi*gamma*(1+((x-x_0)/gamma)**2))