# KDSMIL001
# 21-04-2022

import random as r
import math as m
import numpy as np
from matplotlib import pyplot as plt
from scipy.special import factorial


def radioactiveDecay(N0, Lambda, T, numRuns):
    """
    Parameters
    ----------
    N0 : (int) Number of particles present

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
                # timesBetweenDecays.append(cs)
                pass
            else:
                timesBetweenDecays.append(cs-decayTimes[c-1])

        print(k)
    
    return decaysPerRun, timesBetweenDecays

def poisson(n, mu):
    return (mu**n)*(np.exp(-mu))/factorial(n)

def gaussian(x, mu, sigma, A):
    return (A*(1/(sigma*np.sqrt(2*np.pi)))*np.exp(-(1/2)*((x-mu)/sigma)**2))

def q1b():
    decaysPerRun1, timesBetweenDecays1 = radioactiveDecay(100, 1.2, 10, 1000)
    xs = np.arange(min(decaysPerRun1), max(decaysPerRun1), 0.1)
    plt.figure()
    plt.hist(decaysPerRun1, max(decaysPerRun1)-min(decaysPerRun1), density=True)

    plt.plot(xs, poisson(xs, np.mean(decaysPerRun1)), label='poisson')
    plt.plot(xs, gaussian(xs, np.mean(decaysPerRun1), np.std(decaysPerRun1), 1), label='gaussian')
    
    plt.legend()
    plt.show()

def q1c():
    decaysPerRun2, timesBetweenDecays2 = radioactiveDecay(1000, 1.2, 1, 1000)
    plt.figure()
    plt.hist(timesBetweenDecays2)
    print(np.mean(timesBetweenDecays2))
    plt.show()

def q2a(subsection):
    x = np.random.rand(100000)

    if subsection == 1:
        y = 0.5 * np.arcsin(2 * x - 1)
    elif subsection == 2:
        y = np.sqrt((x * (np.sqrt(8) - np.sqrt(3)) + np.sqrt(3))**2 + 1)
    elif subsection == 3:
        y = np.sqrt(8 * x**2 + 1)
    
    plt.figure()
    plt.hist(x, 50, label='x')
    plt.title("X")
    
    # plt.figure()
    plt.hist(y, 50, label='y')
    plt.title("Y")
    
    plt.legend()
    plt.show()

def q2b(N):
    """
    Parameters
    ----------
    N : (int) Number of random points to generate
    """
    yMin = -np.pi/4
    yMax = np.pi/4
    yRange = np.arange(yMin, yMax, 0.01)
    zMin = np.min(np.cos(2*yRange))
    zMax = np.max(np.cos(2*yRange))

    zRand = (np.random.rand(N) * (zMax - zMin) + zMin)
    yRand = (np.random.rand(N) * (yMax - yMin) + yMin)
        
    acceptedY = yRand[zRand<=np.cos(2*yRand)]

    plt.figure()
    plt.hist(acceptedY, yRange)
    plt.show()
    # return acceptedY

if __name__ == "__main__":
    # q1b()

    # q1c()

    # q2a(3)

    q2b(500000)







    pass
    