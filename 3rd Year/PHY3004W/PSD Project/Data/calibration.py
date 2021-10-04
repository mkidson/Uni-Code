from matplotlib import pyplot as plt, colors
import numpy as np
import matplotlib, readRaw, analysePulse
from math import factorial
from scipy.optimize import curve_fit
import time, scipy
np.set_printoptions(threshold=np.inf)
# matplotlib.use('pgf')
matplotlib.rcParams.update({
    'pgf.texsystem': 'pdflatex',
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
    'figure.constrained_layout.use': True,
    'savefig.bbox': 'tight',
})

maxEvents = 1000000
fileName = r'Raw\Na22'

# conversion factors
bitsToVolt = 2.0 / 2.0**14 # in V
sampleToTime = 1.0 / 500e6 * 1e9 # in ns

# print(sampleToTime)

# open file stream, read preamble and initialise
ipf = readRaw.readFile(fileName)
eventCounter=0

longs = []

while eventCounter < maxEvents:
    # read from file event-by-event
    eventCounter, timestamp, traces, endFile = ipf.readEvent()

    try: 
        traces.any()

        # read the waveforms from the traces array for event where ch0 is anode
        anode = np.array(traces[0], dtype=float)*bitsToVolt
        tArr = np.arange(len(anode))*sampleToTime # Time values, scaled as chloe does it
        # maxes.append(min(anode[:160]))
        # Calculates the baseline signal from < 25% of the total event time. Exactly 25% is 375, so this is just a bit lower to be safe. This section also transforms the signal so it goes up and starts from 0. I like this better than how it is in the data for RMS reasons
        baseline = np.mean(anode[:365])
        anode -= baseline
        anode *= -1
        # Calculates the RMS of the background after the signal has been transformed. Not sure if I'll use this to do the integral window start. Might use tanya's method below
        # baselineRMS = np.sqrt(np.mean(np.square(anode[:350])))
        maxIndex = np.where(anode==max(anode))[0][0]

        intervalStart = maxIndex - (round(10/sampleToTime))
        intervalLongEnd = maxIndex + (round(100/sampleToTime))
        longIntegral = np.trapz(anode[intervalStart:intervalLongEnd], tArr[intervalStart:intervalLongEnd])

        longs.append(longIntegral)

    except Exception as e: 
        print(f'EOF at {eventCounter}\nError is {e}')
        break

def gaussian(x, mu, sigma, A):
    return (A*(1/(sigma*np.sqrt(2*np.pi)))*np.exp(-(1/2)*((x-mu)/sigma)**2))

longs = np.array(longs)
histData, histBins = np.histogram(longs[(longs<0.5)&(longs>0.26)], bins='auto') #[(longs<2)&(longs>0.75)],[(longs<0.8)&(longs>0.4)],[(longs<1.5)&(longs>1.07)]
plt.step(histBins[:-1], histData)
# plt.axvline(1.1035574567183923,c='red')
# smooth = scipy.signal.savgol_filter(histData, 51, 5)

# plt.step(histBins[:-1], smooth)
# plt.step(histBins[:-1], np.gradient(smooth))

xFit = histBins[:-1]
grad = np.gradient(histData)

popt, pcov = curve_fit(gaussian, xFit, grad, [1,0.5,-1])
print(popt[0])
plt.step(xFit, grad)
plt.plot(xFit, gaussian(xFit, *popt))
plt.show()

# 22Na 1.274537 MeV compton edge at 1.1035574567183923
# Energy is 1.0617027983 MeV
# 22Na 0.511 MeV compton edge at 0.34515502437962947
# Energy is 0.340666666 MeV
# 137Cs 0.661657 MeV compton edge at 0.4877006303285822
# Energy is 0.47733374509 MeV
# 60Co 1.332492 MeV compton edge at 1.1481204129710332
# Energy is 1.1181006769 MeV