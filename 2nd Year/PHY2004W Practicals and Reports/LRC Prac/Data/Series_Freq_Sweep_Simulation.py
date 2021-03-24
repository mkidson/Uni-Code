from matplotlib import pyplot as plt
import numpy as np
from scipy.signal import find_peaks
from scipy. optimize import curve_fit
from numpy import cos, pi, sin, sqrt, exp, random, power
import matplotlib
matplotlib.use('pgf')
matplotlib.rcParams.update({
    'pgf.texsystem': 'pdflatex',
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
})
# Extracting all the relevant data, sorting it into our data array, for use later
resistances=['100','200','400','1000']
print('Series Circuit')
for res in resistances:
    file = open('PHY2004W Practicals and Reports\LRC Prac\Data\Series_Freq_Sweep_'+res+'.txt', 'r')
    header = file.readline()
    lines = file.readlines()
    N = len(lines)
    i=0
    # data[0] is the frequency
    # data[1] is the "voltage"
    data = np.zeros((2,N))
    # Reading the file, getting the data into the data array
    for line in lines:
        line = line.strip()
        columns = line.split()
        data[0][i] = float(columns[0])
        data[1][i] = float(columns[1])
        i += 1
    file.close()
    # Using the jackknife method to calculate uncertainties on curve_fir determined optimal parameters
    p0=[70e-3,int(res),96.51e-9,0.5]
    pNames=['L','R','C','scaleFactor']
    u=data[1]*0.02
    tmodel = np.linspace(data[0][0], data[0][-1], N, endpoint=True)
    def transfer(omega,L,R,C,scaleFactor):
        # return scaleFactor*(R*2*pi*omega*C)/sqrt((power(1-C*L*power(2*pi*omega,2),2))+power(C*2*pi*omega*R,2))
        return scaleFactor*(R*2*pi*omega*C)/sqrt(((1-C*L*power(2*pi*omega,2))**2) + ((C*2*pi*omega*R)**2))
    # Removes random values from the data sets
    jackknifeData = np.zeros((4, N, N-1))
    for c in range(N):
        r = random.randint(0, N)
        jackknifeData[0, c] = np.delete(data[0], r)
        jackknifeData[1, c] = np.delete(data[1], r)
        jackknifeData[2, c] = np.delete(u, r)
        jackknifeData[3, c] = np.delete(tmodel, r)
    # Fitting to the jackknifed datasets
    jackknifeFits = np.zeros((N, N-1))
    popts = []
    for k in range(N):
        popt, pcov = curve_fit(transfer, jackknifeData[0, k], jackknifeData[1, k], p0, sigma=jackknifeData[2, k], absolute_sigma=True)
        jackknifeFits[k] = transfer(jackknifeData[3, k], *popt)
        popts.append(popt)
    # Isolating arrays of each optimal fitting parameter
    poptNp = np.zeros((4, N))
    for d, ds in enumerate(popts):
        poptNp[0, d] = ds[0]
        poptNp[1, d] = ds[1]
        poptNp[2, d] = ds[2]
        poptNp[3, d] = ds[3]
    # Calculating means and standard uncertainties
    pOptimals = np.zeros((2, 4))
    for j, js in enumerate(poptNp):
        mean = np.mean(js)
        pOptimals[0][j] = mean
        sumI = 0
        for i in js:
            sumI += (i-mean)**2
        pOptimals[1][j] = sqrt(float(((N-1)/N)*sumI))/sqrt(N-1)
    # Plotting the function with the optimal parameters
    yfit=transfer(tmodel,*pOptimals[0])
    # Printing fit parameters
    print('-'*25)
    print('Results below are for',res,'Ohms')
    for p in range(len(p0)):
        print(pNames[p],'=',pOptimals[0][p],'+/-',pOptimals[1][p])
    # Determining some values and uncertainties
    resIndex=find_peaks(yfit)[0][0]
    resFreq=tmodel[resIndex]
    resAngularFreq=2*pi*resFreq
    resAngularFreqUn=0.02*resAngularFreq
    # Printing stuff
    print('The Resonant Frequency is',resFreq,'+/-',resFreq*0.02)
    print('The Resonant Angular Frequency is',resAngularFreq,'+/-',resAngularFreqUn)
    # Plotting the data 
    plt.figure()
    plt.plot(data[0],data[1],color='b',linewidth=0.7,label='Series LRC Circuit '+res+' Hz')
    plt.plot(tmodel, yfit,c='r',label='curve\_fit')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('$V_{out}/V_{in}$')
    plt.legend()
    plt.savefig('PHY2004W Practicals and Reports\LRC Prac\Data\Series_Freq_Sweep_'+res+'.pgf')
# plt.show()