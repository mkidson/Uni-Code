#!/usr/bin/env python3

from gw_com_1kb import com
from gw_lan import lan
import dso1kb_1
import matplotlib.pyplot as plt

#Check interface according to config file or command line argument.
#port=com.scanComPort()

#Connecting to a DSO.
# dso=dso1kb.Dso("COM3")
# dso=dso1kb.Dso("localhost:3001")
dso=dso1kb.Dso("localhost")
# dso=dso1kb.Dso("127.0.0.1:3001")
# dso=dso1kb.Dso("10.10.0.77:3001")

# for i in range(1,5):
#     print(i, dso.isChannelOn(i))
#
# dso.write(":CHAN1:DISP ON\n")
# dso.write(":CHAN2:DISP ON\n")
# dso.write(":CHAN3:DISP OFF\n")
# dso.write(":CHAN4:DISP OFF\n")

dso.getRawData(True, 1)
# dso.getRawData(True, 2)
fwave1 = dso.convertWaveform(1,1)
# fwave2 = dso.convertWaveform(2,1)

plt.plot(fwave1)
plt.show()
