# KDSMIL001
# 21-04-2022

import math as m
import numpy as np
from matplotlib import pyplot as plt
from scipy.special import factorial
from scipy.integrate import quad
import time, random

def radioactiveDecay(N0, Lambda, T, dt=None, numRuns=1):
    """
    # Radioactive Decay

    Simulates the decay process for a sample of `N0` nuclei, with activity `Lambda`, for a counting interval of `T` seconds, with time step `dt`. This process can be run multiple times by changing `numRuns`.

    Parameters
    ----------
    N0 : (int) Number of particles present

    Lambda : (float) Sample decay rate
    
    T : (int) Counting period, i.e. how long to run the simulation for eaech time

    dt : (float) Time step, defaults to 1/1000 of the Counting Period
    
    numRuns : (int) Number of times to run the simulation in order to get the mean decays per counting period T

    Returns
    -------
    decaysPerRun (array)(int) Array of number of decays counted each time the process starts a new run

    timesBetweenDecays (array)(float) Array of the time between each decay, ignoring those which decay at the same time step, as that seems like it's not good data
    """

    lambda1 = Lambda/N0     # Getting decay constant
    if dt is None:
        dt = T / 1000
    Ts = np.arange(0, T, dt)

    decaysPerRun = []
    timesBetweenDecays = []

    for k in range(numRuns):    # Iterates the decay process numRuns times
        N = N0
        lastDecayTime = 0       # Badly named but it keeps track of the last time a decay happened that wasn't in the same time step as the step we're in

        for t in Ts:            # Iterates over the time steps
            for j in range(N):  # Iterates over each nucleus and checks if it decays
                rand = random.random()
                decayProb = lambda1*dt

                if rand <= decayProb:
                    N -= 1      # If a decay occurs, reduce N by one

                    if lastDecayTime != t:  # If this is the first decay in this time step, calculate the time since the last time step that had a decay, but if this is not the first in this step, do nothing
                        timesBetweenDecays.append(t-lastDecayTime)
                        lastDecayTime = t

        decaysPerRun.append(N0-N)   # Appends the number of decays seen in this run

        print(k)        # Prints the run number, mostly useful for checking where we are if it's taking a while
    
    return decaysPerRun, timesBetweenDecays

def rejectionMethod(N, probDist, yMin=0.0, yMax=1.0):
    """
    # Rejection Method

    Generates `N` random numbers according to the probability distribution `probDist`, on interval `[yMin, yMax]`

    Parameters
    -----------
    N : (int) Number of random numbers to generate

    probDist : (function) The probability distribution function according to which the random numbers must be generated

    yMin : (float) Minimum of the range of generated numbers

    yMax : (float) Maximum of the range of generated numbers

    Returns
    -------
    ys : (array)(float) Array of the first `N` values generated according to `probDist` in the interval `[yMin, yMax]`
    """
    yRange = np.arange(yMin, yMax, 0.01)
    zMax = np.max(probDist(yRange))         # Finds the max of probDist in the interval
    pHit = 1/(np.max(probDist(yRange))*(yMax-yMin)) # Finds the hit probability, requires probDist to be normalised. Could probably use quad here to just always get it right
    print(f'pHit: {pHit}')

    # Generates the random pair needed for rejection method, using the hit probability to account for rejections in order to end up with enough numbers at the end such that we can return N numbers. 1.5* is simply for safety
    zRand = np.random.uniform(0, zMax, int(np.ceil(1.5 * N / pHit)))
    yRand = np.random.uniform(yMin, yMax, int(np.ceil(1.5 * N / pHit)))

    # Lovely bit of conditional numpy array indexing to find all those elements in yRand for which their pair in zRand is less than the probability function value at that yRand
    ys = yRand[zRand <= probDist(yRand)]

    return ys[:N] # Slices it down to N values

def combinationRejection(N, probDist, transform, Cf, yMin=0.0, yMax=1.0):
    """
    # Combination Rejection-Transformation Method

    Generates `N` random numbers according to the probability distribution `probDist` using the combination Rejection and Transformation methods, in the interval `[yMin, yMax]`. Requires the input of the transformed approximate function to `probDist`, as well as the approximate function multiplied by the appropriate constant.

    Parameters
    ----------
    N : (int) Number of random numbers to generate

    probDist : (function) The probability distribution function according to which the random numbers must be generated

    transform : (function) The function obtained by the transformation method from the approximating function to `probDist`

    Cf : (function) The approximating function to `probDist` multiplied by the appropriate factor C such that `Cf > probDist` for all values in `[yMin, yMax]`

    yMin : (float) Minimum of the range of generated numbers

    yMax : (float) Maximum of the range of generated numbers

    Returns
    -------
    ys : (array)(float) Array of the first `N` values generated according to `probDist` in the interval `[yMin, yMax]`
    """
    acceptanceRate = quad(probDist, yMin, yMax)[0] / quad(Cf, yMin, yMax)[0] # Finds the proportion of generated numbers that is expected to be accepted by this method
    print(f'rejectionRate {acceptanceRate}')

    safeNum = int(np.ceil(2 * N / acceptanceRate))  # The number to start with such that we have a good chance of getting N generated values out the other end

    initialY = transform(np.random.rand(safeNum))   # Generates random numbers according to the transformation method

    zs = np.random.rand(safeNum) * Cf(initialY)     # Generates random numbers in the interval [0, Cf(initialY)] where initialY are distributed according to the approximate function

    # Selects only those values in initialY for which the zs generated in the interval [0, Cf(initialY)] are less than the expected distribution evaluated at that initialY
    ys = initialY[zs <= probDist(initialY)]

    return ys[:N]       # Slices the first N of the generated values

def metropolisMethod(N, probDist, xMin, xMax, Delta=1, sepConstant=1, ignoreInitial=0):
    
    acceptedXs = []
    x0 = np.max(probDist(np.linspace(xMin, xMax, 1000)))
    xi = x0
    numAccepted = 0

    while len(acceptedXs) < (N*sepConstant)-ignoreInitial/sepConstant:
        deltaI = random.uniform(-Delta, Delta)
        xTrial = xi + deltaI
        w = probDist(xTrial)/probDist(xi)
        acceptedXs.append(xi)

        # dataSquareMean = np.mean(np.array(acceptedXs)**2)
        # sigmaSquare = 1
        # if np.abs(dataSquareMean - sigmaSquare) <= 1e-4:
        #     break

        if w >= 1:
            xi = xTrial
            numAccepted += 1
            continue
        else:
            r = random.random()

            if r <= w:
                xi = xTrial
                numAccepted += 1
                continue
            else:
                continue

    return acceptedXs[sepConstant*ignoreInitial::sepConstant], numAccepted

def autocorrelation(x, j):
    return (np.mean(x[:-j]*x[j:])-np.mean(x[:-j])**2)/(np.mean(x[:-j]**2)-np.mean(x[:-j])**2)

# A few functions that I found useful to define here
def poisson(n, mu):
    return (mu**n)*(np.exp(-mu))/factorial(n)

def gaussian(x, mu, sigma, A):
    return (A*(1/(sigma*np.sqrt(2*np.pi)))*np.exp(-(1/2)*((x-mu)/sigma)**2))

def exponentialDecay(t, lmbda, N):
    return N*np.exp(-lmbda*t)

def exponentialDistribution(x, lmbda):
    return lmbda*np.exp(-lmbda*x)

# A collection of equations needed for specific questions, vaguely labelled in a logical way
def q2ieqn(y):
    return np.cos(2*y)

def q2ieqnInverse(x):
    return 0.5 * np.arcsin(2 * x - 1)

def q2iieqn(y):
    return (1 / (np.sqrt(8) - np.sqrt(3))) * (y / (np.sqrt(y**2 - 1)))

def q2iieqnInverse(x):
    return np.sqrt((x * (np.sqrt(8) - np.sqrt(3)) + np.sqrt(3))**2 + 1)

def q2iiieqn(y):
    return (1 / np.sqrt(8)) * (y / (np.sqrt(y**2 - 1)))

def q2iiieqnInverse(x):
    return np.sqrt(8 * x**2 + 1)

def q3eqn1(y):
    return (1 / 4.6997309) * (np.sin(y)**2 + 1) / (y**(4/3))

def q3eqn2(x):
    return 1/((1 - x)**(3))

def q3eqn3(y):
    return (6 / 4.6997309) * 1 / (3 * y**(4 / 3))

def q4gaussian(x):
    return (1/(np.sqrt(2*np.pi)))*np.exp((-x**2)/(2))

# Code used for specific questions
def q1b(numNuclei, Lambda, T, numRuns): # This snippet is for q1a and q1b, as they kind of mushed together in terms of their output. Takes in the same arguments as the radioactiveDecay function

    decaysPerRun, timesBetweenDecays = radioactiveDecay(numNuclei, Lambda, T, 1e-3, numRuns)
    xs = np.arange(min(decaysPerRun)+0.5, max(decaysPerRun)+0.5)        # Generating a range of x-values that I use to plot the poisson and gaussian distributions later on, shifted by 0.5 in order to line up the dots with the center of the histogram bins

    plt.figure()
    plt.hist(decaysPerRun, max(decaysPerRun)-min(decaysPerRun), density=True, alpha=0.8, fc='C0', ec='blue')    # Histogram of the number of decays seen in each run

    meanDecays = np.mean(decaysPerRun)  # Mean value of the decaysPerRun, used in both the poisson and gaussian plotting
    stdevDecays = np.std(decaysPerRun)  # Standard Deviation 
    plt.plot(xs, poisson(xs, meanDecays), label='Poisson', marker='o')
    plt.plot(xs, gaussian(xs, meanDecays, stdevDecays, 1), label='Gaussian', marker='o')
    
    print(f'mean: {meanDecays}')
    print(f'std uncertainty: {stdevDecays}')
    plt.legend(title=f'mean = {meanDecays:.4}\nstd dev = {stdevDecays:.4}')
    plt.xlabel('Number of Decays')
    plt.ylabel('Probability')
    plt.title(f'Distribution of Decays per Counting Interval - T = {T}')

def q1c(numNuclei, Lambda, T, numRuns): # Takes in the same arguments as the radioactiveDecay function
    decaysPerRun, timesBetweenDecays = radioactiveDecay(numNuclei, Lambda, T, 1e-3, numRuns)

    meanTime = np.mean(timesBetweenDecays)      # Mean of the times between successive decays, expected to be 1/Lambda

    plt.figure()
    plt.hist(timesBetweenDecays, int(np.ceil(np.max(timesBetweenDecays)))*10, density=True, alpha=0.8, fc='C0', ec='blue')      # Histogram of the times between decays. Bin number is the maximum, rounded up to a whole second, then split into 1/10 of a second per bin
    
    timeRange = np.linspace(0, np.max(timesBetweenDecays), 1000)        # Range of times needed to plot the expected distribution
    plt.plot(timeRange, exponentialDistribution(timeRange, Lambda), label='Exponential Distribution')

    plt.legend(title=f'mean = {meanTime:.3} s')
    plt.xlabel('Time Between Successive Decays (s)')
    plt.ylabel('Probability')
    plt.title('Distribution of Times between Decays')

    print(meanTime)

def q2a(subsection, N): # Takes the subsection as an argument, just to shorten things, as well as the number of points to generate
    x = np.random.rand(N)       # Generates N random numbers in [0,1)

    # All these things do the same but for different equation. They find y from the transform of the probability function, then just find the actual function in order to compare the distribution with the random numbers
    if subsection == 1:
        y = q2ieqnInverse(x)
        yRange = np.linspace(-np.pi/4, np.pi/4, 100)
        pExpected = q2ieqn(yRange)

    elif subsection == 2:
        y = q2iieqnInverse(x)
        yRange = np.linspace(2, 3, 100)
        pExpected = q2iieqn(yRange)

    elif subsection == 3:
        y = q2iiieqnInverse(x)
        yRange = np.linspace(1, 3, 100)
        pExpected = q2iiieqn(yRange)


    plt.figure()
    plt.hist(x, 25, alpha=0.8, fc='C0', ec='blue', density=True)
    plt.title('Distribution of X-values; Uniform')
    # plt.savefig('.\Plots\q2aiiix.pdf')

    plt.figure()
    plt.hist(y, 25, alpha=0.8, fc='#ff7f0e', ec='#ce670d', density=True)
    plt.title('Distribution of Y-values According to Associated Equation')
    plt.plot(yRange, pExpected, color='red', label='Expected Height')
    plt.legend()
    # plt.savefig('.\Plots\q2aiiiy.pdf')

def q2b(N):

    acceptedY = rejectionMethod(N, q2ieqn, -np.pi/4, np.pi/4)

    # Range of ys to plot the expected function
    yRange = np.linspace(-np.pi/4, np.pi/4, 1000)

    plt.figure()
    plt.hist(acceptedY, 25, density=True, alpha=0.8, fc='C0', ec='blue')
    plt.plot(yRange, np.cos(2*yRange), color='red', label='Expected Heights')
    plt.title('Distribution of Y-values Determined using Rejection Method')
    plt.legend()

def q3():
    # Timing the rejection method
    t1 = time.time()
    rejectionYs = rejectionMethod(1000000, q3eqn1, 1, 100)
    t2 = time.time()
    tRejection = t2 - t1

    plt.figure()
    plt.hist(rejectionYs, 200, density=False, alpha=0.5, fc='C0', label='Rejection')
    # plt.title('Distribution Generated Using Rejection Method')
    # plt.legend(title=f'Time Taken: {tRejection:.5} s')

    # Timing the combo method
    t3 = time.time()
    comboRejectionYs = combinationRejection(1000000, q3eqn1, q3eqn2, q3eqn3, 1.0, 100.0)
    t4 = time.time()
    tCombo = t4 - t3

    print(f'rejection average: {np.mean(rejectionYs)}')
    print(f'combo average: {np.mean(comboRejectionYs[comboRejectionYs<100])}')
    print(f'number of combo above 100: {len(comboRejectionYs[comboRejectionYs>100])}')
    print(f'Time taken for Rejection Method: {tRejection}')
    print(f'Time taken for Combination Method: {tCombo}')


    # plt.figure()
    plt.hist(comboRejectionYs, 200, (1,100), density=False, alpha=0.5, fc='#ff7f0e', label='Combination')
    plt.title('Comparison of Rejection and Combination Methods')
    plt.legend()

    # plt.title('Distribution Generated Using Combination Method')
    # plt.legend(title=f'Time Taken: {tCombo:.5} s')

def q4a():

    acceptedX, numAccepted = metropolisMethod(100000, q4gaussian, -5, 5, 4)

    print(f'Acceptance Ratio: {numAccepted/len(acceptedX)}')
    print(f'Number of Iterations: {len(acceptedX)}')
    print(f'Number of Accepted: {numAccepted}')
    print(f'Mean: {np.mean(acceptedX)}')
    print(f'stddev: {np.std(acceptedX)}')

    plt.hist(acceptedX, 50, density=True, alpha=0.8, fc='C0', ec='blue')
    xRange = np.linspace(-5, 5, 1000)
    plt.plot(xRange, q4gaussian(xRange), color='red', label='Gaussian\n$\langle x \\rangle=0$\n$\sigma=1$')
    plt.legend()
    plt.title('Gaussian Distribution using Metropolis Method')
    plt.xlabel('x')
    plt.ylabel('Probability')

def q4c():

    acceptedX, numAccepted = metropolisMethod(100000, q4gaussian, -5, 5, 4)

    autoCors = []
    for i in np.arange(1,100):
        autoCor = autocorrelation(np.array(acceptedX), i)
        autoCors.append(autoCor)
        if np.abs(autoCor) <= 1e-3:
            print(f'C(j={i}) = 0')
    
    plt.plot(np.arange(1,100), autoCors)
    plt.title('Autocorrelation Function for Metropolis Method Gaussian')
    plt.xlabel('j')
    plt.ylabel('C(j)')



if __name__ == "__main__":
    # q1b(100, 1.2, 10, 1000)

    # q1c(100, 1.2, 10, 1000)

    # q2a(3, 500000)

    # q2b(500000)

    # q3()

    # q4a()

    q4c()

    plt.show()
    # plt.savefig('.\Plots\q4c.pdf')






    pass
    