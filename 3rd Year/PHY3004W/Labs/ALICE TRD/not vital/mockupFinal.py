#!/usr/bin/env python3
"""
A mockup of the program I think should be run when we want to take a run of data. It should run through the number of events we want to take, saving the relevant data at each step before moving to the next event. 
"""
import ALICE_LAB_2021.dso1kb
import datetime
import os
import argparse
import numpy as np


# ------------------------------------------------------------------------
# generate a parser for the command line arguments. required so a run number can be passed to the file.
parser = argparse.ArgumentParser(description='Send triggers for a synchronized data run.')
parser.add_argument('run', help='the current TRD run')
parser.add_argument('n_events', help='number of events to be taken')
parser.add_argument('--printargs', action='store_true',
                    help='print arguments and exit')

args = parser.parse_args()
# ------------------------------------------------------------------------


if args.printargs:
    print(args)
    exit(0)

# Connects to the oscilloscope over USB and then gets the time of the event
dso=dso1kb.Dso('/dev/ttyACM2')
# dso = dso1kb.Dso('10.10.0.20:3001')

# Makes a new directory for the data. You will need to change the path to this for when you save data. This checks if the run exists and if it does, exits, else it creates a directory for the data and carries on
if os.system(f'test -d ~/prac2021/data/oscilloscopeData/run_{args.run}') == 0:
    print('That run already exists, change run number to avoid writing over data')
    exit(0)
else:
    os.system(f'mkdir ~/prac2021/data/oscilloscopeData/run_{args.run}')
# similar thing for TRD data 

for i in range(int(args.n_events)):
    now = datetime.datetime.now()
    nowString = now.strftime('%Y.%m.%d.%H.%M.%S')

    # unblock trigger
    # read event (minidaq)
    # could even run the TRD and scope data collection in parallel. wouldn't be too hard to code in.
    
    # Gets the raw data from the oscilloscope, which then gets saved to a variable in the dso object
    dso.getRawData(True, 1)
    dso.getRawData(True, 2)
    dso.getRawData(True, 3)

    waveform = []

    # The convertWaveForm function takes the raw data from the dso object, formats it as a list of floats, and then returns that list
    waveform.append(dso.convertWaveform(1, 1))
    waveform.append(dso.convertWaveform(2, 1))
    waveform.append(dso.convertWaveform(3, 1))
    dso.resetChList()

    waveform = np.array(waveform)
    np.savetxt(f'/home/trd/prac2021/data/oscilloscopeData/run_{args.run}/{i}.csv', waveform, header=nowString, delimiter=',')