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
def gaussian(x, mu, sigma, A, shift):
    return (A*(1/(sigma*sqrt(2*pi)))*exp(-(1/2)*((x-mu)/sigma)**2))+shift

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
    print(N)
    # 0th index is channel number, 1st index is count
    data=np.zeros((2,N))
    uncertainty=np.zeros(N)
    i=0
    for line in lines:
        line = line.strip()
        columns = line.split(',')
        data[0][i] = float(columns[0])
        data[1][i] = float(columns[1])
        if data[1][i]==0:
            uncertainty[i]=1
        else:
            uncertainty[i]=1/sqrt(data[1][i])
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
            # Isolates the regions of interest 
            xFit=data[0][minima[p]:minima[p+1]]
            yFit=data[1][minima[p]:minima[p+1]]
            uncertaintyFit=uncertainty[minima[p]:minima[p+1]]
            # Need a new N for each region since the size is changing
            newN=len(xFit)
            # Approximates the median to be in the middle of the two endpoint, it's a reasonable guess
            approxCentroid=(minima[p]+minima[p+1])/2

            #region Jackknife method for uncertainties of curve_fit
            p0=[approxCentroid,50,1,1]
            numParams=len(p0)
            # Jackknife Curve Fitting
            jackknifeData = np.zeros((3, newN, newN-1))
            popts=[]
            for c in range(newN):
                # Removing random values from each array
                r = random.randint(0, newN)
                jackknifeData[0][c] = np.delete(xFit, r)
                jackknifeData[1][c] = np.delete(yFit, r)
                jackknifeData[2][c] = np.delete(uncertaintyFit, r)
                # Fitting newN times
                popt, pcov = curve_fit(gaussian, jackknifeData[0][c], jackknifeData[1][c], p0, jackknifeData[2][c], absolute_sigma=True, method='trf')
                popts.append(popt)
            # Isolating arrays of each optimal fitting parameter
            poptNp = np.zeros((numParams, newN))
            for d, ds in enumerate(popts):
                poptNp[0, d] = ds[0]
                poptNp[1, d] = ds[1]
                poptNp[2, d] = ds[2]
                poptNp[3, d] = ds[3]
            # Means and standard uncertainties of the parameters
            pOptimals=np.zeros((2,numParams))
            for j, js in enumerate(poptNp):
                pMean=np.mean(js)
                pOptimals[0][j]=pMean
                sumI=0
                for i in js:
                    sumI+=(i-pMean)**2
                # Jackknife method for determining uncertainties of fitted parameters
                pOptimals[1][j]=sqrt(float(((newN-1)/newN)*sumI))/sqrt(newN-1)
            #endregion
            toPlot=gaussian(xFit, *pOptimals[0])
            chi_sq=sum(((yFit-toPlot)/uncertaintyFit)**2)
            dof = newN-numParams

            # if 0.5<(min_chisq/dof)<1.5:
            print(f'Fit: {p}\nMu: {pOptimals[0][0]} +/- {pOptimals[1][0]}\nSigma: {pOptimals[0][1]} +/- {pOptimals[1][1]}\nAmplitude: {pOptimals[0][2]} +/- \
                {pOptimals[1][2]}\ny-shift: {pOptimals[0][3]} +/- {pOptimals[1][3]}\nChi Squared per dof: {chi_sq/dof}\n')
            plt.plot(xFit, gaussian(xFit, *pOptimals[0]), linewidth=2, label=f'Fit {p}')
        except RuntimeError as identifier:
            print(identifier)

    plt.legend()
    # plt.hist(xFit, bins=xFit, weights=yFit)
    # plt.plot(data[0], smootherData, label=r'Smoothed Data')
    # plt.hist(bData[0], bins=bData[0], weights=bData[1], label=r'Background')
plt.show(block=True)