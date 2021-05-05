from matplotlib import pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from numpy import cos, pi, sin, sqrt, exp, random
import matplotlib, scipy.signal
matplotlib.rcParams.update({
    'pgf.texsystem': 'pdflatex',
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
})
#region Ingesting background data, only needs to be done once
backgroundFile=open(r'3rd Year\PHY3004W\Labs\Gamma Spectroscopy\Data\Background.csv','r')
bLiveTime=float(backgroundFile.readline().strip())
# Gets info from top of file: ,Low,High,Gross,Net,FWHM,Centroid
bVitals=backgroundFile.readline().strip().split(',')
# Gets actual data
bLines=backgroundFile.readlines()
bN=len(bLines)
# 0th index is channel number, 1st index is count
bData=np.zeros((2,bN))
i=0
for line in bLines:
    line = line.strip()
    columns = line.split(',')
    bData[0][i] = float(columns[0])
    bData[1][i] = float(columns[1])
    i += 1
backgroundFile.close()
# Normalise background wrt live time
bData[1]/=bLiveTime
#endregion

# Function for curve fit, defining here to be more efficient, rather than doing it in the loop
def gaussian(x, mu, sigma, A):
    return (A*(1/(sigma*sqrt(2*pi)))*exp(-(1/2)*((x-mu)/sigma)**2))

names=['22Na', '60Co', '109Cd', '133Ba', '137Cs', '152Eu', 'Unknown']

for name in names:
    print('----------------------------------------------------------------------------------------')
    print(name)
    #region Ingesting data
    f=open(f'3rd Year\PHY3004W\Labs\Gamma Spectroscopy\Data\{name}.csv','r')
    liveTime=float(f.readline().strip())
    # Gets info from top of file: ,Low,High,Gross,Net,FWHM,Centroid
    vitals=f.readline().strip().split(',')
    # Gets actual data
    lines=f.readlines()
    N=len(lines)
    # 0th index is channel number, 1st index is count
    data=np.zeros((2,N))
    i=0
    for line in lines:
        line = line.strip()
        columns = line.split(',')
        data[0][i] = float(columns[0])
        data[1][i] = float(columns[1])
        i += 1
    f.close()
    #endregion
    # Normalise the data with respect to the time the detector was on for. We do this in order to subtract the normalised background data
    data[1]/=liveTime
    data[1]-=bData[1]
    # Plots the histogram now, just makes things easier later on since python layers plots chronologically
    plt.figure(name)
    plt.hist(data[0], bins=data[0], weights=data[1], label=r'Counts per Channel')
    plt.xlabel(r'Channel')
    plt.ylabel(r'Count')
    # Both these just help smooth the data out so that we can find the minima, which we will use as start and end points for curve_fit to fit the gaussian to the data
    smoothData = scipy.signal.savgol_filter(data[1], 51, 5)
    smootherData = scipy.signal.savgol_filter(smoothData, 51, 5)
    # Finds the minima
    minima=scipy.signal.find_peaks(smootherData*-1)[0]
    # print(minima)
    # Fits a gaussian to the data for each region between a local minimum. Slightly overkill since not all of those regions are photopeaks but i'm lazy
    for p in range(len(minima)-1):
        try:
            xFit=data[0][minima[p]:minima[p+1]]
            yFit=data[1][minima[p]:minima[p+1]]
            approxCentroid=(minima[p]+minima[p+1])/2
            p0=[approxCentroid,50,1]
            popt, pcov=curve_fit(gaussian, xFit, yFit, p0, method='trf')

            #region Jackknife method for uncertainties of curve_fit
            # # Function for curve_fit
            # def func(omega,sigma):
            #     return 
            # # Array used to plot the optimised function and initial guess
            # xModel=np.linspace(data[0][0],data[0][-1],N,endpoint=True)
            # p0=[]
            # numParams=len(p0)
            # # Jackknife Curve Fitting
            # jackknifeData = np.zeros((4, N, N-1))
            # popts=np.zeros((numParams,N))
            # for c in range(N):
            #     # Removing random values from each array
            #     r = random.randint(0, N)
            #     jackknifeData[0][c] = np.delete(data[0], r)
            #     jackknifeData[1][c] = np.delete(data[1], r)
            #     jackknifeData[2][c] = np.delete(u, r)
            #     jackknifeData[3][c] = np.delete(xModel, r)
            #     # Fitting N times
            #     popt, pcov = curve_fit(func, jackknifeData[0][c], jackknifeData[1][c], p0, sigma=jackknifeData[2][c], absolute_sigma=True)
            #     popts[0][c]=popt
            # # Means and standard uncertainties of the parameters
            # pOptimals=np.zeros((2,numParams))
            # for j, js in enumerate(popts):
            #     pMean=np.mean(js)
            #     pOptimals[0][j]=pMean
            #     sumI=0
            #     for i in js:
            #         sumI+=(i-pMean)**2
            #     # Jackknife method for determining uncertainties of fitted parameters
            #     pOptimals[1][j]=sqrt(float(((N-1)/N)*sumI))/sqrt(N-1)
            # # Plotting the function with the optimal parameters
            # yfit=func(xModel,*pOptimals[0])
            #endregion

            if popt[2]>1:
                print(f'Fit: {p}\nMu: {popt[0]}\nSigma: {popt[1]}\nAmplitude: {popt[2]}\n')
                plt.plot(xFit, gaussian(xFit, *popt), linewidth=1, label=f'Fit {p}')
        except RuntimeError as identifier:
            print(identifier)

    plt.legend()
    # plt.hist(xFit, bins=xFit, weights=yFit)
    # plt.plot(data[0], smootherData, label=r'Smoothed Data')
    # plt.hist(bData[0], bins=bData[0], weights=bData[1], label=r'Background')
plt.show()