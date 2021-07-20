import readRaw
import numpy as np 
import matplotlib.pyplot as plt 

maxEvents = 1
fileName = r"3rd Year\PHY3004W\PSD Project\Data\Raw\STNG"

# conversion factors
bitsToVolt = 2.0 / 2.0**14 # in V
sampleToTime = 1.0 / 500e6 * 1e9 # in ns

# open file stream, read preamble and initialise
ipf = readRaw.readFile(fileName)
eventCounter=0

while eventCounter < maxEvents:
    # read from file event-by-event
    eventCounter, timestamp, traces, endFile = ipf.readEvent()

    try: 
        traces.any()

        # read the waveforms from the traces array for event, where ch0 is anode, and ch1 is dynode
        anode = np.array(traces[0], dtype=float)
        dynode = np.array(traces[1], dtype=float)
                
        # plotting for sanity checking - remove if using large number of events
        plt.figure()
        
        plt.title('Event %d'%eventCounter)
        
        plt.plot(np.arange(len(anode)) * sampleToTime, anode * bitsToVolt, label='anode')
        plt.plot(np.arange(len(dynode)) * sampleToTime, dynode * bitsToVolt, label='dynode')
        
        plt.xlabel('Time (ns)')
        plt.ylabel('Voltage (V)')
        
        plt.legend()
    
    except: 
        print('EOF at %d'%eventCounter)
        break
     
# close file stream (important)
ipf.closeFile()
plt.show()  


