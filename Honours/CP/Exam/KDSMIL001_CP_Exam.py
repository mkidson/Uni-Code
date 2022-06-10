# KDSMIL001
# 10-06-2022

import numpy as np
import random
import matplotlib.pyplot as plt
from scipy.integrate import quad

def rejectionMethod(N, probDist, yMin=0.0, yMax=1.0):
    """Generates `N` random numbers according to the probability distribution `probDist`, on interval `[yMin, yMax]`. Onlt really works for good rejection rates.
    
        Args
        ----
            N (int):
        Number of random values to generate
    
            probDist (function):
        The probability distribution function according to which the random numbers must be generated. Must have one input only as I'm too lazy to do a funcArgs thing
    
            yMin (float, optional): 
        Minimum of the range of generated numbers. Defaults to 0.0.
    
            yMax (float, optional): 
        Maximum of the range of generated numbers. Defaults to 1.0.
    
        Returns
        -------
            ys (array, float):
        Array of the first `N` values generated according to `probDist` in the interval `[yMin, yMax]`
    """

    yRange = np.linspace(yMin, yMax, 2000)
    zMax = np.max(probDist(yRange))         # Finds the max of probDist in the interval
    pHit = 1/(np.max(probDist(yRange))*(yMax-yMin)) # Finds the hit probability, requires probDist to be normalised. Could probably use quad here to just always get it right
    print(f'pHit: {pHit}')

    # Generates the random pair needed for rejection method, using the hit probability to account for rejections in order to end up with enough numbers at the end such that we can return N numbers. 1.5* is simply for safety
    zRand = np.random.uniform(0, zMax, int(np.ceil(1.5 * N / pHit)))
    yRand = np.random.uniform(yMin, yMax, int(np.ceil(1.5 * N / pHit)))

    # Lovely bit of conditional numpy array indexing to find all those elements in yRand for which their pair in zRand is less than the probability function value at that yRand
    ys = yRand[zRand <= probDist(yRand)]

    return ys[:N] # Slices it down to N values

def gaussian(N):
    return (( 1 / ( np.sqrt( 2 * np.pi * 10000 ))) * np.exp( - (( N - 10000 )**2 / ( 2 * 10000 ))))

def boltzmann(p):
    return p**2 * np.exp(- p / 2)

def boltzmannNorm(p):
    return p**2 * np.exp(- p / 2) / 15.999371064829049

def thetaDist(x):
    return np.arccos(1 - 2 * x)

def phiDist(x):
    return 2 * np.pi * ( x - 0.5 )



def q1a():
    # Using rejection method to generate gaussian distribution
    photonYields = rejectionMethod(20000, gaussian, 9500, 10500)

    yieldAvg = np.mean(photonYields)
    print(f'Average yield: {yieldAvg}')
    yieldVar = np.var(photonYields)
    print(f'Variance of yields: {yieldVar}')

    xRange = np.linspace(9500, 10500, 1000)
    plt.hist(photonYields, bins=200, density=True, alpha=0.8, fc='C0', ec='blue', label='Rejection Method')
    plt.plot(xRange, gaussian(xRange), color='red', label='Expected Heights')
    plt.legend()
    plt.title('Distribution of photon yields')
    plt.xlabel('Number of photons')
    plt.show()

def q1b():
    pRange = np.linspace(0, 30, 1000)

    plt.figure()
    plt.plot(pRange, boltzmann(pRange))
    plt.xlabel('p (MeV)')
    plt.title('Unnormalised Boltzmann distribution for momentum')

    norm = quad(boltzmann, 0, 30)
    print(norm)

    plt.figure()
    plt.plot(pRange, boltzmannNorm(pRange))
    plt.xlabel('p (MeV)')
    plt.title('Normalised Boltzmann distribution for momentum')

    plt.show()

def q1cf():
    numPhotons = 10000      # Change this on the final run
    pRange = np.linspace(0, 30, 1000)

    photonMomenta = rejectionMethod(numPhotons, boltzmannNorm, 0, 30)
    momentaAvg = np.mean(photonMomenta)

    print(f'Average momenum magnitude: {momentaAvg}')
    
    thetas = thetaDist(np.random.rand(numPhotons))
    phis = phiDist(np.random.rand(numPhotons))

    avgZMomentum = np.mean(photonMomenta * np.cos(thetas))

    print(f'Average momentum in z direction: {avgZMomentum}')


    plt.hist(photonMomenta, bins=30, density=True, alpha=0.8, fc='C0', ec='blue', label='Rejection Method')
    plt.plot(pRange, boltzmannNorm(pRange), color='red', label='Expected Heights')
    plt.legend()
    plt.title('Distribution of photon momenta')
    plt.xlabel('p (MeV)')


    plt.figure()
    plt.hist(thetas, 50, alpha=0.8, fc='C0', ec='blue')
    plt.title(r'Distribution of $\theta$')
    plt.xlabel(r'$\theta$')
    
    
    plt.figure()
    plt.hist(phis, 50, alpha=0.8, fc='C0', ec='blue')
    plt.title(r'Distribution of $\phi$')
    plt.xlabel(r'$\phi$')


    plt.show()


def q2a():
    pass



##############################################################

# q1a()

# q1b()

# q1cf()

