import dso1kb
import numpy as np
import matplotlib.pyplot as plt
import time

# dso=dso1kb.Dso('10.10.0.20:3001', True)
dso=dso1kb.Dso('/dev/ttyACM2')
t1 = time.time()
dso.getRawData(True, 1)
dso.getRawData(True, 2)
dso.getRawData(True, 3)
t2 = time.time()
fwave1 = []
fwave2 = []
fwave3 = []
fwave1 = dso.convertWaveform(1, 1)
fwave2 = dso.convertWaveform(2, 1)
fwave3 = dso.convertWaveform(3, 1)
t3 = time.time()

print('time to get data: ', t2-t1)
print('time to convert waveforms: ', t3-t2)
print('total time: ', t3-t1)

tArr = np.arange(0,len(fwave1))
plt.plot(tArr, fwave1, label='ch1')
plt.plot(tArr, fwave2, label='ch2')
plt.plot(tArr, fwave3, label='ch3')
plt.legend()
plt.savefig('testplot.png')