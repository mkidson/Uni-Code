from matplotlib import pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from numpy import cos, pi, sin, sqrt, exp, random
import matplotlib, scipy.signal
# matplotlib.use('pgf')
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

for name in {'22Na'}:
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
    plt.hist(data[0], bins=data[0], weights=data[1], label=r'Counts per Channel', histtype='step')
    plt.xlabel(r'Channel Number')
    plt.ylabel(r'Counts per unit time')
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
            # Need a new N for each region since the size is changing
            newN=len(xFit)
            # Approximates the median to be in the middle of the two endpoint, it's a reasonable guess
            approxCentroid=(minima[p]+minima[p+1])/2
            p0=[approxCentroid,50,1]
            numParams=len(p0)

            popt, pcov = curve_fit(gaussian, xFit, yFit, p0, method='trf')
            # Finding if the fit was poggers or cringe
            toPlot=gaussian(xFit, *popt)
            chi_sq=sum((yFit-toPlot)**2)
            dof = newN-numParams

            # if p==7:
            print(f'Fit: {p}\nMu: {popt[0]}\nSigma: {popt[1]}\nAmplitude: {popt[2]}\nChi Squared per dof: {chi_sq/dof}\n')
            plt.plot(xFit, toPlot, linewidth=1, label=f'Gaussian fit')
            # arrowProps = dict(arrowstyle='->')
            # str661='661.657 keV photopeak\n$\mu=417.37$\n$\sigma=15.28$'
            # plt.annotate(str661, (419,5.9), (20,-60), textcoords='offset points', arrowprops=arrowProps)
            # plt.annotate('Compton Edge\nfor 661.657 keV', (273,1.4), (5,20), textcoords='offset points', arrowprops=arrowProps)
            # plt.annotate('Backscatter', (131, 2.1), (0,20), textcoords='offset points', arrowprops=arrowProps)
        except RuntimeError as identifier:
            print(identifier)

    plt.legend()
plt.show()
# plt.savefig(r'3rd Year\PHY3004W\Labs\Gamma Spectroscopy\Report\Data\137Cs.pgf')