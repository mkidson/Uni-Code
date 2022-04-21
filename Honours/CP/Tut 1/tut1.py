# KDSMIL001
# 21-04-2022
import random as r
import math as m
import numpy as np
from matplotlib import pyplot as plt


def radioactiveDecay(N0, Lambda, T, numRuns):
    """
    Parameters
    ----------
    N0 : (int) Number of particles present. Should be on the order of avaagadro
    Lambda : (float) Sample decay rate
    T : (int) Counting period, i.e. how long to run the simulation for eaech time
    numRuns : (int) Number of times to run the simulation in order to get the mean decays per counting period T
    """

    lambda1 = Lambda/N0
    dt = 1e-3
    Ts = np.arange(0, T, dt)
    decaysPerRun = []
    timesBetweenDecays = []


    for k in range(numRuns):
        N = N0
        decayTimes = []

        for i in Ts:
            for j in range(N):
                rand = r.random()
                dProb = lambda1*dt

                if rand <= dProb:
                    N -= 1
                    decayTimes.append(i)

        decaysPerRun.append(N0-N)
        for c, cs in enumerate(decayTimes):
            if c == 0:
                pass
            else:
                timesBetweenDecays.append(cs-decayTimes[c-1])

        print(k)
    
    return decaysPerRun, timesBetweenDecays



if __name__ == "__main__":
    # 1. a)
    # decaysPerRun1, timesBetweenDecays1 = radioactiveDecay(1000, 1.2, 10, 100)
    # histData, histBins = np.histogram(decaysPerRun, max(decaysPerRun)-min(decaysPerRun))
    # plt.figure()
    # plt.step(histBins[:-1], histData)
    # plt.show()

    # 1. c)
    decaysPerRun2, timesBetweenDecays2 = radioactiveDecay(1000, 1.2, 10, 10)
    histData, histBins = np.histogram(timesBetweenDecays2)
    plt.figure()
    plt.step(histBins[:-1], histData)
    # plt.plot(timesBetweenDecays2)
    # print(np.mean(timesBetweenDecays2))
    plt.show()
    