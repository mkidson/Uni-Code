from matplotlib import pyplot as plt
import numpy as np
from numpy import cos, pi, sin, sqrt, exp, random
import matplotlib
matplotlib.use('pgf')
matplotlib.rcParams.update({
    'pgf.texsystem': 'pdflatex',
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
})

freqs=['100', '200', '500', '1000']
resistances=['5k6', '8k2', '15k']

for freq in freqs:
    for res in resistances:
        filename='Cap_'+freq+'Hz_'+res
        file = open('PHY2004W Practicals and Reports\Capacitor Prac\Freq_Resis\\'+ filename + '.txt', 'r')
        header = file.readline()
        lines = file.readlines()
        N = len(lines)
        i=0
        # data[0] is Time [s] - Voltage Capacitor
        # data[1] is Voltage [V] - Voltage Capacitor
        # data[2] is Time [s] - Voltage Source
        # data[3] is Voltage [V] - Voltage Source
        data = np.zeros((4, N))
        # Reading the file, getting the data into the data array
        for line in lines:
            line = line.strip()
            columns = line.split()
            data[0][i] = float(columns[0])
            data[1][i] = float(columns[1])
            data[2][i] = float(columns[2])
            data[3][i] = float(columns[3])
            i += 1
        file.close()
        # Plotting both the applied voltage and the voltage measured across the capacitor against time
        plt.figure()
        plt.plot(data[2], data[3], label='Applied Voltage', color='red', lw=0.5)
        plt.plot(data[0], data[1], label='Capacitor Voltage', color='blue', lw=1)
        # Making it all look better
        plt.legend(loc=1)
        plt.xlabel("Time (s)")
        plt.ylabel("Voltage (V)")
        # plt.show()
        plt.savefig('PHY2004W Practicals and Reports\Capacitor Prac\Freq_Resis\Plots\\'+filename+'.pgf')