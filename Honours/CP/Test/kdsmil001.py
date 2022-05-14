# KDSMIL001
# 14-05-2022

from cProfile import label
import numpy as np
import matplotlib.pyplot as plt
import random

def gaussLaguerreIntegration(numRoots, func, const=1, *funcArgs):
    """Blindingly simple implementation of Gauss-Laguerre quadrature integration. 
    
        Args
        ----
            numRoots (int):
        Number of roots of the Laguerre polynomials to use in the integration
    
            func (function):
        Name of the function q(t) in the integrand of the integral, where the entire integrand is q(t) e^-t

            const (float):
        Constant to multiply the integral by

            *funcArgs (optional):
        Arguments of `func` if any are needed. Obviously need to be fed in the order that they appear in `func`
    
        Returns
        -------
            int (float):
        Value of the integral that has been esimated using Gauss-Laguerre quadrature
    """
    points, weights = np.polynomial.laguerre.laggauss(numRoots)     # Finds the roots of the Laguerre polynomials to use in the method

    int = np.sum(func(points, *funcArgs) * weights)

    return const * int

def q1iNumerator(x):
    # f(x_i) for the integral in the numerator, for gauss-laguerre integration
    return ( (x + 1) / 4) * ( ( (x**2 + 2 * x) / 4 )**2 + 1 ) * np.exp(-1)

def q1iDenominator(x):
    # f(x_i) for the integral in the denominator, for gauss-laguerre integration
    return ( (x + 1) / 4) * np.exp(-1)

def q1i():
    roots = 16

    # Using gauss-laguerre to find the numerator and denominator integrals
    numeratorI = gaussLaguerreIntegration(roots, q1iNumerator)
    denominatorI = gaussLaguerreIntegration(roots, q1iDenominator)

    totI = numeratorI / denominatorI

    print()
    print(f'Gauss-Laguerre integration gives:\nI = {totI}')
    print('---------------------------')

def metropolisMethod(N, probDist, xMin, xMax, x0, Delta=1):
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
    xi = x0     # Sets current step to initial guess
    numAccepted = 0     # Will be used to keep track of acceptance ratio

    while len(acceptedXs) < N:
        deltaI = random.uniform(-Delta, Delta)
        xTrial = xi + deltaI        # Generates new trial step randomly
        w = probDist(xTrial)/probDist(xi)
        acceptedXs.append(xi)       # Appends current step to the chain. Done here since we always want to add to the chain, regardless of if we accept or not, so this cuts down on unnecessary logic later on

        if np.logical_or(xTrial < xMin, xTrial > xMax):     # Check if the trial is within the bounds and if not, starts again, importantly we have still added the current step to the chain
            continue
        
        # Pretty self-explanatory method for accepting or rejecting. Not sure if generating r here is a good idea, might be quicker to generate a whole list of them before we loop
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

    acceptanceRatio = numAccepted / len(acceptedXs)

    return acceptedXs, acceptanceRatio

def autocorrelation(x, j):
    return (np.mean(x[:-j]*x[j:])-np.mean(x[:-j])**2)/(np.mean(x[:-j]**2)-np.mean(x[:-j])**2)

def movingAvg(xArr):
    # Returns the moving average for some array `xArr`

    xArrCumsum = np.cumsum(xArr)
    xArrMovingAvg = []

    for i in range(len(xArr)):
        xArrMovingAvg.append(xArrCumsum[i] / (i + 1))
    
    return np.array(xArrMovingAvg)

def correlationAndEquilibration(chain):
    """Finds the autocorrelation function for a Markov chain and returns the first `j` for which `C(j) <= 0.01`. Plots the autocorrelation function, as well as the moving average of the chain, then asks the user to input a number of steps after which it looks like equilibrium has been reached
    
        Args
        ----
            chain (array, float):
        Array of randomly generated numbers, hopefully a Markov chain produced from the Metropolis method
    
        Returns
        -------
            autoCorrSkip (int):
        Size of gap to skip each time a point is sampled from `chain`

            equilibrationSkip (int):
        Number of entries in `chain` to skip before starting to sample from it
    """
    autoCorrs = []
    for i in np.arange(1,50):
        autoCorr = autocorrelation(np.array(chain), i)
        autoCorrs.append(autoCorr)

    
    for c in autoCorrs:
        if np.abs(c) <= 1e-2:
            print(f'C(j={autoCorrs.index(c)}) = 0\n')
            autoCorrSkip = autoCorrs.index(c)
            break

    plt.figure()
    plt.plot(np.arange(1,50), autoCorrs, 'rs', ms=3)
    plt.axvline(autoCorrSkip, label=f'First C(j) < 0.01\nj = {autoCorrSkip}')
    plt.legend()
    plt.title('Plot of autocorrelation function')
    plt.xlabel('j')
    plt.ylabel('C(j)')

    finalAvg = np.mean(chain)
    xMovingAverage = movingAvg(chain)

    plt.figure()
    plt.plot(xMovingAverage, 'rs', ms=3, label='Moving average')
    plt.axhline(finalAvg, label='Final average')
    plt.legend()
    plt.title('Moving average of the Markov Chain')
    plt.xlabel('Number of points generated')
    plt.ylabel('Average of x')

    plt.show()

    equilibriumPosition = int(input('Input equilibrium position: '))
    # equilibriumPosition = 30000

    return autoCorrSkip, equilibriumPosition

def q1iiDistribution(x):
    # The distribution we will generate according to, using Metropolis method
    return x * np.exp( -np.sqrt( 4 * x**2 + 1) )

def q1iiIntegrand(x):
    return x**4 + 1

def q1ii():
    
    numPoints = 500000
    genXs, acceptanceRatio = metropolisMethod(numPoints, q1iiDistribution, 0, np.inf, 0.636, 2)

    print()
    print(f'Acceptance ratio: {acceptanceRatio:.5}\n')

    autoCorrSkip, equiPos = correlationAndEquilibration(genXs)

    finalXs = genXs[equiPos::autoCorrSkip]
    plotRange = np.linspace(0, np.max(finalXs), 1000)
    distPlot = 2 * np.exp(1) * q1iiDistribution(plotRange)

    plt.figure()
    plt.hist(finalXs, 200, density=True, label='Random values, histogrammed')
    plt.plot(plotRange, distPlot, label='Exact distribution, normalised')
    plt.legend()
    plt.title('Histogram of Metropolis-generated values compared to exact distribution')
    plt.xlabel('x')
    plt.show()

    plt.figure()
    plt.scatter(finalXs[:-1:2], finalXs[1::2], s=0.3, color='green', marker='.')
    plt.xlim(0,4)
    plt.ylim(0,4)
    plt.title('Plot of "randomness"')
    plt.xlabel('$x_{2i}$')
    plt.ylabel('$x_{2i+1}$')
    plt.show()

    I = np.sum(q1iiIntegrand(np.array(finalXs))) / len(finalXs)

    stdDev = np.sqrt( np.mean(q1iiIntegrand(np.array(finalXs))**2) - np.mean(q1iiIntegrand(np.array(finalXs)))**2 )

    print()
    print(f'Metropolis integration gives:\nI = {I} +/- {stdDev / np.sqrt(len(finalXs))}')
    print('---------------------------')

def q2():

    rMin = 1
    rMax = 3
    V0 = 20
    VNp1 = 55
    deltaR = 0.001
    numPoints = int((rMax - rMin) / deltaR)
    print(numPoints)
    rs = np.linspace(rMin, rMax, numPoints)
    alpha = (1 - deltaR / rs)
    beta = (1 + deltaR / rs)

    A = np.diag(alpha[2:-1], -1) + np.diag([-2] * (numPoints - 2), 0) + np.diag(beta[1:-2], 1)

    w = np.zeros(numPoints - 2)
    w[0] = -alpha[0] * V0
    w[-1] = -beta[0] * VNp1

    V = np.linalg.solve(A, w)
    V = np.insert(V, 0, V0)
    V = np.append(V, VNp1)

    plt.plot(rs, V, label='Finite Difference solution')
    plt.xlabel('$r$ (m)')
    plt.ylabel('$V(r)$ (V)')
    plt.legend()
    plt.title('Solution to Laplace\'s equation in a spherically symmetric region')
    plt.grid(color='#CCCCCC', linestyle=':')
    plt.show()




if __name__ == '__main__':

    # q1i()

    # q1ii()

    q2()

    pass
