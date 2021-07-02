#25/02/2019
#read in raw waveform from dat files 
#Chloe Sole

import numpy as np
import matplotlib.pyplot as plt

# Open file and skip over header preamble
class readFile(object):
    headerSize = 72
    maxChannels = 64
    preambleSize = 4+20+4*maxChannels
    def __init__(self,file_name):
        self.inputFile = open(file_name, "rb")
        self.header = self.inputFile.read(self.headerSize)
        #traces = np.empty(maxChannels)
        self.eventCounter=0
        self.eventTimeStamp=0
        self.endFile = False
        print('init complete')
        
    def readEvent(self):
        
        preamble = np.frombuffer(self.inputFile.read(self.preambleSize),dtype=np.uint32)
        
        if not preamble.any(): #check end of file
            self.endFile = True
            return self.eventCounter,0, 0, self.endFile
        
        #convert timestamp to microseconds
        eventTimeStamp = preamble[5]*8e-3 #us 
        self.channelSizes = preamble[6:]
        
        #array of all channels 0 if that channel isn't active, int value being equal to the 
        #number of samples in that active channel
        self.chActive = np.argwhere(self.channelSizes>0).flatten()
        
        #init trace array
        traces = np.empty((len(self.chActive),self.channelSizes[self.chActive[0]]))
        self.eventCounter+=1
        
        #read traces for only active channels
        for i in range(len(self.chActive)):
            y = np.array(np.frombuffer(self.inputFile.read(self.channelSizes[self.chActive[i]]*2), dtype=np.uint16),dtype=int)
            traces[i]=y
        
        return self.eventCounter,eventTimeStamp, traces, self.endFile
    
    def closeFile(self):
        self.inputFile.close()
        
