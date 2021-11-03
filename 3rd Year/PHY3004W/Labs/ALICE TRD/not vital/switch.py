#!/usr/bin/env python3
"""
Just a little program that will probably never need to be used again but it saves me the bother of switching between scope modes when taking TRD data and time resolution data
"""

import dso1kb
import os
import argparse

# ------------------------------------------------------------------------
# generate a parser for the command line arguments. required so a run number can be passed to the file.
parser = argparse.ArgumentParser(description='Send triggers for a synchronized data run.')
parser.add_argument('mode', help='the mode you want to switch to')
parser.add_argument('--printargs', action='store_true',
                    help='print arguments and exit')

args = parser.parse_args()
# ------------------------------------------------------------------------

if args.printargs:
    print(args)
    exit(0)

# Connects to the oscilloscope over USB
dso=dso1kb.Dso('/dev/ttyACM2')

if args.mode == 'timeResolution':
    dso.write(':CHAN3:DISP OFF\n')
    dso.write(':TRIG:SOUR CH1\n')
    dso.write(':TRIG:LEV -3E-1\n')
    dso.write(':TRIG:EDG:SLOP FALL\n')
elif args.mode == 'TRD':
    dso.write(':CHAN3:DISP ON\n')
    dso.write(':TRIG:SOUR CH3\n')
    dso.write(':TRIG:LEV 3E\n')
    dso.write(':TRIG:EDG:SLOP RIS\n')
else:
    exit(0)