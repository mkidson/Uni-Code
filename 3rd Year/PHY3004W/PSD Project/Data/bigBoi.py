from matplotlib import pyplot as plt, colors
import numpy as np
import matplotlib, readRaw, analysePulse
from math import factorial
from scipy.interpolate import pade
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

# maxEvents = 218796
maxEvents = 4
# fileName = r"3rd Year\PHY3004W\PSD Project\Data\Raw\STNG"
fileName = r"Raw\STNG"

# conversion factors
bitsToVolt = 2.0 / 2.0**14 # in V
sampleToTime = 1.0 / 500e6 * 1e9 # in ns

# print(sampleToTime)

# open file stream, read preamble and initialise
ipf = readRaw.readFile(fileName)
eventCounter=0

maxes=[]
CCM_PSDs = []
laplace_PSDs = []
voltages = []

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
        baselineRMS = np.sqrt(np.mean(np.square(anode[:350])))
        maxIndex = np.where(anode==max(anode))[0][0]

        # intervalStart = maxIndex - (round(10/sampleToTime))
        # intervalLongEnd = maxIndex + (round(100/sampleToTime))
        # intervalShortEnd = maxIndex + (round(25/sampleToTime))

        # CCM_PSD = analysePulse.CCM(anode, tArr)
        # CCM_PSDs.append(CCM_PSD)
        voltages.append(max(anode))

        # if eventCounter % 100 == 0:
        #     print(eventCounter)
        #     print(max(anode))

        # region plotting for sanity checking - remove if using large number of events
        # plt.figure()
        
        # plt.title(f'Event {eventCounter}')
        
        # plt.plot(tArr, anode, label='anode', alpha=1, color='blue', lw='1')
        # # plt.plot(tArr, [baselineRMS]*len(anode), color='red', ls='--', lw=0.6)
        # # plt.plot(tArr, [baselineRMS*3]*len(anode), color='green', ls='--', lw=0.6)
        # plt.axvline(tArr[intervalStart], linestyle='dashed', color='black', linewidth=1)
        # plt.axvline(tArr[intervalLongEnd], linestyle='dashed', color='black', linewidth=1)
        # plt.axvline(tArr[intervalShortEnd], linestyle='dashed', color='black', linewidth=1)


        # # plt.plot(tArr, anode)
        # plt.grid(color='#CCCCCC', linestyle=':')
        
        # plt.xlabel('Time (ns)')
        # plt.ylabel('Voltage (V)')
        
        # plt.legend()
        # endregion

    except Exception as e: 
        print(f'EOF at {eventCounter}\nError is {e}')
        break

    # testing out pade laplace
    nDecays = 5
    # res, poles, fit, tNew = analysePulse.PadeLaplace(anode, tArr, nDecays)
    res, poles, n = analysePulse.PadeLaplace(anode, tArr, nDecays)

    # plt.figure()
    # plt.plot(tArr[maxIndex:],fit,linewidth=2)
    # plt.semilogx(); plt.grid(True); plt.legend()

    # print(poles, res)

    # fit = 0
    # for i in range(nDecays):
    #     fit += res[i]*np.exp(-poles[i]*tArr[:-maxIndex])

    # plt.plot(tArr[maxIndex:750], movingAves[:750-maxIndex])

    # laplace_PSDs.append(res[1]/res[0])
    # print(res[0]/res[1])
    # print(res)

    # transform, p = analysePulse.PadeLaplace(anode, tArr)
    # plt.plot(p,transform)
    # print(transform)


# close file stream (important)
ipf.closeFile()

# plt.hist2d(voltages, CCM_PSDs, bins=2000, norm=colors.LogNorm())
# plt.hist2d(voltages, laplace_PSDs, bins=2000, norm=colors.LogNorm())
plt.show()