from matplotlib import pyplot as plt
import numpy as np
import matplotlib, readRaw, analysePulse
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

maxEvents = 10000
fileName = r"3rd Year\PHY3004W\PSD Project\Data\Raw\STNG"

# conversion factors
bitsToVolt = 2.0 / 2.0**14 # in V
sampleToTime = 1.0 / 500e6 * 1e9 # in ns

# open file stream, read preamble and initialise
ipf = readRaw.readFile(fileName)
eventCounter=0

maxes=[]
CCM_PSDs = []

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

        intStart = maxIndex - (round(10/sampleToTime))
        intShort = maxIndex + (round(25/sampleToTime))
        intLong = maxIndex + (round(100/sampleToTime))

        shortIntegral = np.trapz(anode[intStart:intShort], tArr[intStart:intShort])
        longIntegral = np.trapz(anode[intStart:intLong], tArr[intStart:intLong])

        CCM_PSD = longIntegral/shortIntegral
        # print(CCM_PSD)
        CCM_PSDs.append(CCM_PSD)
                
        # plotting for sanity checking - remove if using large number of events
        # plt.figure()
        
        # plt.title(f'Event {eventCounter}')
        
        # plt.plot(tArr, anode, label='anode', alpha=1, color='blue', lw='1')
        # plt.plot(tArr, [baselineRMS]*len(anode), color='red', ls='--', lw=0.6)
        # plt.plot(tArr, [baselineRMS*3]*len(anode), color='green', ls='--', lw=0.6)
        # plt.grid(color='#CCCCCC', linestyle=':')
        # plt.vlines(tArr[intStart], 0, 0.08)
        # plt.vlines(tArr[intShort], 0, 0.08)
        # plt.vlines(tArr[intLong], 0, 0.08)
        
        # plt.xlabel('Time (ns)')
        # plt.ylabel('Voltage (V)')
        
        # plt.legend()
    
    except: 
        print(f'EOF at {eventCounter}')
        break
     
# close file stream (important)
ipf.closeFile()
# print(np.array(maxes))
# plt.show()

# print(CCM_PSDs)

# Actually got CCM working, no 2d hist yet but the concept is there. Do need to optimise the integral windows
histData, histBins = np.histogram(CCM_PSDs, bins=100)
plt.step(histBins[:-1], histData)
plt.show()