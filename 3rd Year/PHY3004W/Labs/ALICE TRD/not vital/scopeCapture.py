#!/usr/bin/env python3
"""
This program is designed to be run every time a new event is taken using minidaq. It takes the run number as an argument in order to better organise the output.

We only used 3 of the channels but if more or less are needed, just change those lines.

The output should be a csv containing all the waveforms of the triggering event, as well as the trigger pulse itself. The header and filename are the time of the event in YEAR.MONTH.DAY.HOUR.MINUTE.SECOND format.

Created: OCT 2021

Author: Miles Kidson
"""

import dso1kb
import datetime
import os
import argparse
import numpy as np

# ------------------------------------------------------------------------
# generate a parser for the command line arguments. required so a run number can be passed to the file.
parser = argparse.ArgumentParser(description='Send triggers for a synchronized data run.')
parser.add_argument('run', help='the current TRD run')
parser.add_argument('--printargs', action='store_true',
                    help='print arguments and exit')

args = parser.parse_args()
# ------------------------------------------------------------------------

if args.printargs:
    print(args)
    exit(0)

# Connects to the oscilloscope over USB and then gets the time of the event
# dso = dso1kb.Dso('10.10.0.20:3001')
dso=dso1kb.Dso('/dev/ttyACM2')
now = datetime.datetime.now()
nowString = now.strftime('%Y.%m.%d.%H.%M.%S')

# Makes a new directory for the data. You will need to change the path to this for when you save data
os.system(f'mkdir ~/prac2021/data/oscilloscopeData/run_{args.run}')

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
# change the output to just be a number starting from 1
np.savetxt(f'~/prac2021/data/oscilloscopeData/run_{args.run}/{nowString}.csv', waveform, header=nowString, delimiter=',')