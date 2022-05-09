# KDSMIL001
# 05-05-2022

import numpy as np
import random

def metropolisMethod(N, probDist, xMin, xMax, x0, Delta=1, sepConstant=1, ignoreInitial=0):
    """Metropolis Method
    
        Args
        ----
            N (int):
        Number of random values to be generated
    
            probDist (function):
        The probability distribution that the numbers should be generated according to
    
            xMin (float):
        Lower bound of the interval on which to generate values
    
            xMax (float):
        Upper bound of the interval on which to generate values

            x0 (float):
        x-value to start the method at, should be the point at which `probDist` is at its max.

            Delta (int, optional): 
        Half the range over which to generate numbers when determining a trial point. Defaults to 1.
    
            sepConstant (int, optional): 
        Number of points to skip between output points, to avoid correlation. Defaults to 1.
    
            ignoreInitial (int, optional): 
        Number of initial points in those generated that should be skipped, to avoid transient terms. Defaults to 0.

        Returns
        -------
            acceptedXs (array, float):
        Array of 
    
    
    """
    acceptedXs = []
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

        if np.logical_or(xTrial < xMin, xTrial > xMax):
            continue

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

    numAccepted = numAccepted/sepConstant + ignoreInitial

    return acceptedXs[sepConstant*ignoreInitial::sepConstant], numAccepted

def autocorrelation(x, j):
    return (np.mean(x[:-j]*x[j:])-np.mean(x[:-j])**2)/(np.mean(x[:-j]**2)-np.mean(x[:-j])**2)

def xInverse(u):
    return -3 * np.log(-u * (-3 * (np.exp(-2) - np.exp(1/3))) / 3 + np.exp(1 / 3))

def X(ux, uy, uz):
    return np.exp(-ux / 3)

def q1eqn(x, y, z):
    return np.exp(-x / 3) * (1 + 0.1 * np.log(np.sqrt(x**2 + y**2 + z**2 + 1)))

def q2eqn(x):
    return np.exp(-x)

def q1():
    N = 1000000     # Number of points to generate for x, y, and z

    numRuns = 100   # Number of runs to do
    ints = []       # Array for integral values
    ints2 = []

    for i in range(numRuns):
        ux = np.random.rand(N)
        xs = xInverse(ux)       # Generates values distributed according to e^{-x/3}
        ys = np.random.uniform(0, 5, N)     # Uniform on [0,5]
        zs = np.random.uniform(0, 5, N)

        normConst = -3 * (np.exp(-2) - np.exp(1/3)) * 25    # Defining the normalisation constant so that w(x,y,z) is normalised over the interval

        I = (normConst / N) * np.sum(q1eqn(xs, ys, zs) / X(xs, ys, zs))     # Calculating I

        ints.append(I)

    intMean = np.mean(ints)
    intStd = np.std(ints)
    intUnc = intStd / np.sqrt(numRuns)

    print(f'I = {intMean} +/- {intUnc}')

def q2():
    N = 30000       # Number of points to generate
    ran = (0, np.inf)   # range over which metropolis will run

    numRuns = 100       # Number of runs to perform
    ints = []       # Array for integral values

    for i in range(numRuns):

        xs, num = metropolisMethod(N, q2eqn, ran[0], ran[1], 0, 2, 58, 100)

        # autoCors = []
        # for i in np.arange(1,1000):
        #     autoCor = autocorrelation(np.array(xs), i)
        #     autoCors.append(autoCor)
        #     if np.abs(autoCor) <= 1e-3:
        #         # print(f'C(j={i}) = 0')
        #         seps.append(i)
        #         break

        I = np.sum(xs) / len(xs)    # Calculating the integral
        ints.append(I)



    intMean = np.mean(ints)
    intStd = np.std(ints)

    print(f'I = {intMean} +/- {intStd/np.sqrt(numRuns)}')


if __name__ == "__main__":
    
    q1()

    # q2()

    pass