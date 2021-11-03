#!/usr/bin/env python3
"""
Takes a screeshot of the current oscilloscope screen and saves it to the folder under the name given by the user.
"""
from oscilloscopeRead import scopeRead
import datetime
import time
import os
import argparse
import numpy as np

scope = scopeRead.Reader()

trig_count_1 = int(os.popen('trdbox reg-read 0x102').read().split('\n')[0])
os.system('trdbox unblock')
trig_count_2 = 0
i = 0
while i < 2:
    trig_count_2 = int(os.popen('trdbox reg-read 0x102').read().split('\n')[0])

    if trig_count_2 != trig_count_1:
        i += 1
        print(i)
        now = datetime.datetime.now()
        nowString = now.strftime('%Y.%m.%d.%H.%M.%S')

        waveform = scope.getData([1,2,3], True)

        trig_count_1 = trig_count_2

        os.system('trdbox unblock')
    else:
        pass
