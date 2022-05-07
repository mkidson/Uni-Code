# KDSMIL001
# 05-05-2022

from matplotlib import pyplot as plt
import numpy as np
import random
from scipy.integrate import nquad

def xInverse(u):
    return -3 * np.log(-u / 3 + np.exp(1 / 3))

def X(ux, uy, uz):
    return np.exp(-ux / 3)

def q1eqn(x, y, z):
    return np.exp(-x / 3) * (1 + 0.1 * np.log(np.sqrt(x**2 + y**2 + z**2 + 1)))

def q1():
    N = 1000000

    ux = np.random.rand(N)
    xs = xInverse(ux)
    ys = np.random.uniform(0, 5, N)
    zs = np.random.uniform(0, 5, N)

    normConst = -3 * (np.exp(-2) - np.exp(1/3)) * 25

    I = (normConst / N) * np.sum(q1eqn(xs, ys, zs) / X(xs, ys, zs))

    print(I)

def q2eqn(x):
    return np.exp(-x)

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

    return acceptedXs[sepConstant*ignoreInitial::sepConstant], numAccepted

def q2():
    N = 10000000
    ran = (0, 10000)
    # plotRange = np.linspace(minPlot, maxPlot,1000)
    xs, num = metropolisMethod(N, q2eqn, ran[0], ran[1], 0, 2)

    I = np.sum(xs) / N
    print(I)

    # print(np.max(q2eqn(np.linspace(0, 100, 1000))))
    # print(num/N)
    # plt.hist(xs, 20, (0, 10), density=True)
    # plt.plot(plotRange, q2eqn(plotRange))
    # plt.show()

if __name__ == "__main__":
    
    q1()
    
    # q2()
    
    I = nquad(q1eqn, [[-1, 6], [0, 5], [0, 5]])
    print(I)
    
    pass