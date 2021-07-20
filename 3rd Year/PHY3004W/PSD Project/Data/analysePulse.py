# 02-07-2021
# Methods for PSD for neutron/photons
# Miles Kidson KDSMIL001

import numpy as np
import readRaw


def CCM(pulse, t):
    """
    Integrates over "short" and "long" windows for a pulse and returns a discrimination parameter given by PSD_{CCM} = I_{long}/I_{short}. This is the Charge Comparison Method.

    Parameters
    ---
    pulse : array_like
        Array of voltages over a time period `t`, should contain one pulse only. Should start at the start of the integration window, for now. Might change this.
    
    t : array_like
        Array of the time period that `pulse` runs over. Needs to be scaled as in exampleRead.py, in nanoseconds.

    Returns
    ---
    out : float
        Discrimination parameter PSD_{CCM}
    """

    longInterval = 1 # These need to be determined as in Lang. The start point is something about when the waveform exceeds 3*sigma of the baseline rms
    shortInterval = 1

    tLong = t[1:2]
    tShort = t[1:2]

    longIntegral = np.trapz(pulse, tLong)
    shortIntegral = np.trapz(pulse, tShort)

    return longIntegral/shortIntegral