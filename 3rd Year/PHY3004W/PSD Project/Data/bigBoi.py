from matplotlib import pyplot as plt, colors
import numpy as np
import matplotlib, readRaw, analysePulse
from math import factorial
from scipy.optimize import curve_fit
import time
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
maxEvents = 1000000
# fileName = r"3rd Year\PHY3004W\PSD Project\Data\Raw\STNG"
# fileName = r"Raw\STNG"
fileName = r"Raw\AmBe"

# conversion factors
bitsToVolt = 2.0 / 2.0**14 # in V
sampleToTime = 1.0 / 500e6 * 1e9 # in ns

# print(sampleToTime)

# open file stream, read preamble and initialise
ipf = readRaw.readFile(fileName)
eventCounter=0

maxes=[]
CCM_PSDs = []
optimiseCCM = []
laplace_PSDs = []
voltages = []
longInts = []

shorts = np.arange(25,27,0.2)

t1 = time.time()

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

        # tempPSD = []

        # for i in shorts:
        #     tempPSD.append(CCM_PSD)

        CCM_PSD, voltage, longInt = analysePulse.CCM(anode, tArr, i)
        # optimiseCCM.append(tempPSD)
        CCM_PSDs.append(CCM_PSD)
        # voltages.append(voltage)
        longInts.append(longInt)


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

    # region testing out pade laplace
    nDecays = 5
    # res, poles, fit, tNew = analysePulse.PadeLaplace(anode, tArr, nDecays)
    # res, poles, n = analysePulse.PadeLaplace(anode, tArr, nDecays)

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
    # endregion


# close file stream (important)
ipf.closeFile()

t2 = time.time()
print(f'time taken is {t2-t1:.4} seconds')

# plt.figure()
# plt.hist2d(voltages, CCM_PSDs, bins=2000, norm=colors.LogNorm())
# plt.title('Voltage')
# plt.hist2d(voltages, laplace_PSDs, bins=2000, norm=colors.LogNorm())
# plt.figure()
# plt.hist2d(longInts, CCM_PSDs, bins=2000, norm=colors.LogNorm())
# plt.title('Long Integral')
# plt.show()
optimiseCCM = np.array(optimiseCCM)
longInts = np.array(longInts)
FoMs = []

# for p, ps in enumerate(shorts):
# CCM_PSDs = np.array(optimiseCCM[:,p])
CCM_PSDs = np.array(CCM_PSDs)

forFoM = CCM_PSDs[longInts > 2.2]
# print(gammas)
histData, histBins = np.histogram(forFoM, bins=512)

# print(histBins)

cutoff = np.where(histBins >= 0.8555)[0][0]

p0N = [histBins[np.where(histData==max(histData[:cutoff]))[0][0]],0.01,1]
poptN, pcovN = curve_fit(analysePulse.gaussian, histBins[:cutoff], histData[:cutoff], p0=p0N)
xModelN = np.linspace(histBins[0], histBins[cutoff], 1000)
# print(p0N)
# print(poptN)

p0P = [histBins[np.where(histData==max(histData[cutoff:]))[0][0]],0.01,1]
poptP, pcovP = curve_fit(analysePulse.gaussian, histBins[cutoff:-1], histData[cutoff:], p0=p0P, maxfev=5000)
xModelP = np.linspace(histBins[cutoff], histBins[-1], 1000)
# print(p0P)
# print(poptP)

# FoM = (poptP[0]-poptP[1])/(poptP[1]*2.35 + poptN[1]*2.35)
# FoMs.append(FoM)
# print(ps, FoM)

# histData1, histBins1 = np.histogram(CCM_PSDs, bins=1000)

# plt.step(histBins[:-1], histData)
# plt.plot(xModelN, analysePulse.gaussian(xModelN, *poptN))
# plt.plot(xModelP, analysePulse.gaussian(xModelP, *poptP))

# plt.step(histBins1[:-1], histData1)
# plt.show()

# 0.8555

plt.step(shorts, FoMs)
plt.show()