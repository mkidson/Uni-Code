from matplotlib import pyplot as plt, colors
import numpy as np
import matplotlib, readRaw, analysePulse
from math import factorial
from scipy.optimize import curve_fit
from scipy.fft import rfft, rfftfreq
import time
np.set_printoptions(threshold=np.inf)
# matplotlib.use('pgf')
matplotlib.rcParams.update({
    'pgf.texsystem': 'pdflatex',
    'font.family': 'sans-serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
    'figure.constrained_layout.use': True,
    'savefig.bbox': 'tight',
    'axes.labelsize': 18,
    'legend.fontsize': 18,
    'xtick.labelsize': 16,
    'ytick.labelsize': 16,
    'axes.titlesize': 18
})

maxEvents = 1000000
fileName = r"Raw\STNG"
# fileName = r"Raw\AmBe"

# conversion factors
bitsToVolt = 2.0 / 2.0**14 # in V
sampleToTime = 1.0 / 500e6 * 1e9 # in ns
# long integral to MeVee conversion
m = 0.9177884481407862
c = 0.005787603530313204

# print(sampleToTime)

# open file stream, read preamble and initialise
ipf = readRaw.readFile(fileName)
eventCounter=0

maxes=[]
CCM_PSDs = []
laplace_PSDs = []
laplace_Res = []
laplace_Poles = []
laplace_chisq = []
voltages = []
longInts = []
curve_fit_params = []

# Used for optimisation of short integral window
# optimiseCCM = []
# shorts = np.arange(20,25,0.2)

t1 = time.time()

while eventCounter < maxEvents:
    # read from file event-by-event
    eventCounter, timestamp, traces, endFile = ipf.readEvent()

    try: 
        traces.any()

        # read the waveforms from the traces array for event where ch0 is anode
        anode = np.array(traces[0], dtype=float)*bitsToVolt
        tArr = np.arange(len(anode))*sampleToTime # Time values, scaled as chloe does it
        # maxes.append(min(anode[:160]))
        # Calculates the baseline signal from < 25% of the total event time. Exactly 25% is 375, so this is just a bit lower to be safe. This section also transforms the signal so it goes up and starts from 0. I like this better than how it is in the data for RMS reasons
        baseline = np.mean(anode[:365])
        anode -= baseline
        anode *= -1
        # Calculates the RMS of the background after the signal has been transformed. Not sure if I'll use this to do the integral window start. Might use tanya's method below
        # baselineRMS = np.sqrt(np.mean(np.square(anode[:350])))
        maxIndex = np.where(anode==max(anode[365:400]))[0][0]
        intervalStart = maxIndex - (round(10/sampleToTime))
        intervalLongEnd = maxIndex + (round(250/sampleToTime))
        intervalShortEnd = maxIndex + (round(22/sampleToTime))

        # more optimising things
        # tempPSD = []
        # for i in shorts:
        #     CCM_PSD, longInt = analysePulse.CCM(anode, tArr, i)
        #     # CCM_PSDs.append(CCM_PSD)
        #     tempPSD.append(CCM_PSD)
        # longInts.append(longInt)
        # optimiseCCM.append(tempPSD)

        CCM_PSD, longInt = analysePulse.CCM(anode, tArr)
        CCM_PSDs.append(CCM_PSD)
        longInts.append(longInt)

        # residues, poles, longInt, chiSqDof = analysePulse.PadeLaplace(anode, tArr)
        # laplace_PSDs.append((poles[1])/(poles[0]))
        # laplace_Res.append(residues)
        # laplace_Poles.append(poles)
        # longInts.append(longInt)
        # laplace_chisq.append(chiSqDof)



        # region plotting for sanity checking - remove if using large number of events
        # if True:
        #     plt.figure()
            
        #     plt.title(f'Event {eventCounter}')
            
        #     plt.plot(tArr, anode, label='anode', alpha=1, color='blue', lw='1')
        #     plt.axvline(tArr[intervalStart], linestyle='dashed', color='black', linewidth=1)
        #     plt.axvline(tArr[intervalLongEnd], linestyle='dashed', color='black', linewidth=1)
        #     plt.axvline(tArr[intervalShortEnd], linestyle='dashed', color='black', linewidth=1)

        #     plt.text(tArr[intervalStart], 0.05, 'Integral window start', rotation='vertical', horizontalalignment='right', size=18)
        #     plt.text(tArr[intervalShortEnd], 0.05, 'Short integral window', rotation='vertical', horizontalalignment='left', size=18)
        #     plt.text(tArr[intervalLongEnd], 0.05, 'Long integral window', rotation='vertical', horizontalalignment='right', size=18)

        #     # # plt.plot(tArr[maxIndex:], fit, color='red', lw=1)


        #     # # # plt.plot(tArr, anode)
        #     plt.grid(color='#CCCCCC', linestyle=':')
            
        #     plt.xlabel('Time (ns)')
        #     plt.ylabel('Voltage (V)')
            
        #     plt.legend()
        #     plt.xlim(725, 1200)
        #     plt.show()
            # plt.savefig(r'anode_flipped.pgf')
        # endregion



    except Exception as e: 
        print(f'EOF at {eventCounter}\nError is {e}')
        break


# close file stream (important)
ipf.closeFile()
longInts = m*np.array(longInts)+c

CCM_PSDs = np.array(CCM_PSDs)
# laplace_Res = np.array(laplace_Res)
# laplace_Poles = np.array(laplace_Poles)
# laplace_PSDs = np.array(laplace_PSDs)
# laplace_chisq = np.array(laplace_chisq)

# np.savetxt('residues.txt', laplace_Res)
# np.savetxt('poles.txt', laplace_Poles)
# np.save('AmBe_Laplace_Res2.npy', laplace_Res)
# np.save('AmBe_Laplace_Poles2.npy', laplace_Poles)
# np.save('AmBe_Laplace_longInts2.npy', longInts)

# np.save('STNG_Laplace_Res2.npy', laplace_Res)
# np.save('STNG_Laplace_Poles2.npy', laplace_Poles)
# np.save('STNG_Laplace_longInts2.npy', longInts)
# np.save('STNG_Laplace_chisq2.npy', laplace_chisq)

np.save('STNG_CCM_longInts3.npy', longInts)
np.save('STNG_CCM_PSDs3.npy', CCM_PSDs)

# np.save('AmBe_CCM_longInts3.npy', longInts)
# np.save('AmBe_CCM_PSDs3.npy', CCM_PSDs)

t2 = time.time()
print(f'time taken is {t2-t1:.4} seconds')

# plt.figure()
# plt.plot(tArr, anode)
# plt.plot()

# plt.figure()
# plt.hist2d(voltages, CCM_PSDs, bins=2000, norm=colors.LogNorm())
# plt.title('Voltage')
# plt.hist2d(longInts, laplace_Res[:,0], bins=2000, norm=colors.LogNorm())
# plt.scatter(longInts, laplace_PSDs)
# plt.figure()
# plt.hist2d(longInts, CCM_PSDs, bins=2000, norm=colors.LogNorm())
# plt.title('Long Integral')
# plt.xlabel('Energy (MeVee)')
# plt.ylabel('Short integral/Long integral')

# plt.figure()
# plt.scatter(laplace_Res[:,0], laplace_Poles[:,0], label='first constant', s=2)
# plt.scatter(laplace_Res[:,1], laplace_Poles[:,1], label='second constant', s=2)
# plt.legend()


# plt.show()

# region optimising the short integral window using FoM. found best to be 26
# optimiseCCM = np.array(optimiseCCM)
# FoMs = []

# for p, ps in enumerate(shorts):
#     CCM_PSDs = np.array(optimiseCCM[:,p])


#     AmBeSortingArr = longInts.argsort()
#     longIntsSorted = longInts[AmBeSortingArr]
#     CCM_PSDsSorted = CCM_PSDs[AmBeSortingArr]

#     cutoff = 0.015*np.log(longIntsSorted-0.05)+0.79
#     # plt.figure()
#     # plt.hist2d(longInts[longInts<14], CCM_PSDs[longInts<14], bins=2000, norm=colors.LogNorm())
#     # plt.plot(longIntsSorted, cutoff)

#     photonsPSDs = CCM_PSDsSorted[CCM_PSDsSorted>cutoff]
#     neutronsPSDs = CCM_PSDsSorted[CCM_PSDsSorted<cutoff]

#     photonsData, photonsBins = np.histogram(photonsPSDs, bins=1000)
#     neutronsData, neutronsBins = np.histogram(neutronsPSDs, bins=1000)

#     photonsPopt, photonsPcov = curve_fit(analysePulse.Breit_Wigner, photonsBins[:-1], photonsData, p0=[photonsBins[np.where(photonsData==max(photonsData))[0][0]],1,1], sigma=np.where(photonsData!=0,np.sqrt(photonsData), 1), absolute_sigma=True)
#     neutronsPopt, neutronsPcov = curve_fit(analysePulse.gaussian, neutronsBins[:-1], neutronsData, p0=[neutronsBins[np.where(neutronsData==max(neutronsData))[0][0]],1,1], sigma=np.where(neutronsData!=0,np.sqrt(neutronsData), 1), absolute_sigma=False)

#     FoM = (photonsPopt[0]-neutronsPopt[0])/(2*photonsPopt[1]+2.35*neutronsPopt[1])

#     FoMs.append(FoM)
#     print(ps, FoM)

# # p0N = [histBins[np.where(histData==max(histData[:cutoff]))[0][0]],0.01,1]
# # poptN, pcovN = curve_fit(analysePulse.gaussian, histBins[:cutoff], histData[:cutoff], p0=p0N)
# # xModelN = np.linspace(histBins[0], histBins[cutoff], 1000)
# # # print(p0N)
# # # print(poptN)

# # p0P = [histBins[np.where(histData==max(histData[cutoff:]))[0][0]],0.01,1]
# # poptP, pcovP = curve_fit(analysePulse.gaussian, histBins[cutoff:-1], histData[cutoff:], p0=p0P, maxfev=5000)
# # xModelP = np.linspace(histBins[cutoff], histBins[-1], 1000)
# # # print(p0P)
# # # print(poptP)

# # FoM = (poptP[0]-poptP[1])/(poptP[1]*2.35 + poptN[1]*2.35)


# # histData1, histBins1 = np.histogram(CCM_PSDs, bins=1000)

# # plt.step(histBins[:-1], histData)
# # plt.plot(xModelN, analysePulse.gaussian(xModelN, *poptN))
# # plt.plot(xModelP, analysePulse.gaussian(xModelP, *poptP))

# # plt.step(histBins1[:-1], histData1)
# # plt.show()

# # 0.8555

# plt.figure()
# plt.step(shorts, FoMs)
# plt.show()
# endregion