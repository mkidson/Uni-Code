# KDSMIL001
# 10-06-2022

import wave
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
    return p**2 * np.exp(- p / 2) / 16

def thetaDist(x):
    return np.arccos(1 - 2 * x)

def phiDist(x):
    return 2 * np.pi * ( x - 0.5 )

def regulaFalsi(x1, x2, func, rootVal=0.0, tol=0.01, printIntermediate=True):
    """Returns the root of the function `func` that lies between `x1` and `x2`
    
        Args
        ----
            x1 (float):
        Leftmost inital guess
    
            x2 (float):
        Rightmost inital guess
    
            func (function):
        The function which calls the method to interpolate the data in `xs` and `ys`, at some point `x`. Needs to be of the form `func(x, xs, ys)`

            rootVal (float, optional): 
        Value of the function f(x) for which to find the corresponding x. Defaults to 0.
    
            tol (float, optional):
        The tolerance to which the root-finding method must reach before exiting and outputting the x-value at the root. Should be less than 1. Defaults to `0.01`

            printIntermediate (bool, optional):
        Tells the function whether it should print out the step number, x-value, and y-value at each step. Defaults to `True`

        Returns
        -------
            x0 (float):
        The x-value for the root of the function `func` in the interval [`x1`, `x2`]
    """
    y1 = func(x1)
    y2 = func(x2)
    
    x0 = x1 + (rootVal - y1) * ((x2 - x1) / (y2 - y1))      # Using the formula for linear interpolation with y(x) = 0 to find x
    y0 = func(x0)
    
    i = 0
    while np.abs(y0) >= tol:
        i += 1
        if y0 * y1 < 0:     # Checking if y0 and y1 are on opposite sides of the root, and if so setting y2 to y0
            y2 = y0
            x2 = x0
        elif y0 * y2 < 0:   # Same here
            y1 = y0
            x1 = x0
            
        x0 = x1 + (rootVal - y1) * ((x2 - x1) / (y2 - y1))      # Sets new x0 value as above
        y0 = func(x0)
        
        if printIntermediate:
            print(f'step {i}')
            print(f'x: {x0:.5}')
            print(f'y: {y0:.5}')
            print('---')
    
    return x0



def q1a():
    # Using rejection method to generate gaussian distribution
    photonYields = rejectionMethod(20000, gaussian, 9500, 10500)
    print(f'First yield generated: {photonYields[0]}')

    # Finding average and variance
    yieldAvg = np.mean(photonYields)
    print(f'Average yield: {yieldAvg}')
    yieldVar = np.var(photonYields)
    print(f'Variance of yields: {yieldVar}')

    xRange = np.linspace(9500, 10500, 1000)
    plt.hist(photonYields, bins=100, density=True, alpha=0.8, fc='C0', ec='blue', label='Rejection Method')
    plt.plot(xRange, gaussian(xRange), color='red', label='Expected Heights')
    plt.legend()
    plt.title('Distribution of photon yields,, normalised')
    plt.xlabel('Number of photons')
    plt.show()

def q1b():
    pRange = np.linspace(0, 30, 1000)       # Distribution drops off appreciably by p=30

    plt.figure()
    plt.plot(pRange, boltzmann(pRange))
    plt.xlabel('p (MeV)')
    plt.title('Unnormalised Boltzmann distribution for momentum')
    plt.grid(color='#CCCCCC', linestyle=':')

    norm = quad(boltzmann, 0, np.inf)       # Normalisation, might as well go to infinity if we can
    print(norm)

    plt.figure()
    plt.plot(pRange, boltzmannNorm(pRange))
    plt.xlabel('p (MeV)')
    plt.title('Normalised Boltzmann distribution for momentum')
    plt.grid(color='#CCCCCC', linestyle=':')

    plt.show()

def q1cf():
    # This is the code for both 1c and 1f as they kind of do the same thing/rely on the same inputs, namely the number of photons to generate

    numPhotons =  9759      
    pRange = np.linspace(0, 30, 1000)       # Range of momenta

    photonMomenta = rejectionMethod(numPhotons, boltzmannNorm, 0, 30)       # Using rejection to get the photon momentum distribution
    momentaAvg = np.mean(photonMomenta)

    print(f'Average momenum magnitude: {momentaAvg}')
    
    thetas = thetaDist(np.random.rand(numPhotons))      # Using inverse transform to find theta and phi distributions
    phis = phiDist(np.random.rand(numPhotons))

    avgZMomentum = np.mean(photonMomenta * np.cos(thetas))      # Average momentum in z direction is p*cos(theta)

    print(f'Average momentum in z direction: {avgZMomentum}')


    plt.hist(photonMomenta, bins=30, density=True, alpha=0.8, fc='C0', ec='blue', label='Random Numbers')
    plt.plot(pRange, boltzmannNorm(pRange), color='red', label='Expected Heights')
    plt.legend()
    plt.title('Distribution of photon momenta')
    plt.xlabel('p (MeV)')


    plt.figure()
    plt.hist(thetas, 50, density=True, alpha=0.8, fc='C0', ec='blue')
    plt.title(r'Distribution of $\theta$, normalised')
    plt.xlabel(r'$\theta$')
    
    
    plt.figure()
    plt.hist(phis, 50, density=True, alpha=0.8, fc='C0', ec='blue')
    plt.title(r'Distribution of $\phi$, normalised')
    plt.xlabel(r'$\phi$')


    plt.show()


def numerovDE0(E0):
    """Returns `dE0`, which is a measure of how well the solutions from the right and left match at the classical turning point, for the Numerov method on a quantum harmonic oscillator
    
        Args
        ----
            E0 (float):
        Energy for which to calculate `dE0`

        Returns
        -------
            dE0 (float):
        Difference in first derivatives at the classical turning point
    """
    mc2 = 5.11e5            # eV
    hc = 197.3              # eV nm
    hOmega = 1              # eV
    
    # Using symmetric guesses to start off with, just makes things easier
    psi_0 = 0
    psi_1 = 0.0001       # A complete guess as to what is reasonable

    psi_left = []           # Initialisation of the left and right solutions
    psi_left.append(psi_0)
    psi_left.append(psi_1)

    psi_right = []          # Note that the right solution is being done in the right order, with its leftmost value in terms of x being the first in the array
    psi_right.append(psi_1)
    psi_right.append(psi_0)

    # Chose -1 to 1 nm pretty arbitrarily, seemed to work well so I didn't change it
    xRange = np.linspace(-1, 1, 1000)
    deltaX = xRange[1] - xRange[0]

    potential = 0.5 * ( mc2 / hc**2 ) * hOmega**2 * xRange**2

    meetPointX = np.where(potential <= E0)[0][-1]       # Finds the index of the classical turning point. Chose the right hand one

    f = 2 * ( mc2 / hc**2 ) * ( E0 - potential )        # From the derivation of Numerov

    # Looping for the update equation. Took some thought to get the indexing right here but I'm happy with it
    for xl in xRange[1:meetPointX]:
        i = np.where(xRange == xl)[0][0]    # numpy arrays are really annoying sometimes but this works to get the index of an element. Could be an easier way to do this whole loop but it works
        psi_l_new = ( ( 2 - (5/6) * deltaX**2 * f[i] ) * psi_left[i] - ( 1 + (deltaX**2 / 12) * f[i-1] ) * psi_left[i-1] ) / ( 1 + (deltaX**2 / 12) * f[i+1])
        psi_left.append(psi_l_new)
    
    for xr in xRange[meetPointX:-1][::-1]:
        c = np.where(xRange == xr)[0][0]
        # The indexing in this bit is really weird because I'm trying to do it right to left and make it also be in that direction in the array, so the psi_right values we want are always the the first and second ones
        psi_r_new = ( ( 2 - (5/6) * deltaX**2 * f[c] ) * psi_right[0] - ( 1 + (deltaX**2 / 12) * f[c+1] ) * psi_right[1] ) / ( 1 + (deltaX**2 / 12) * f[c-1])
        psi_right.insert(0, psi_r_new)

    psi_left = np.array(psi_left) * ( psi_right[1] / psi_left[-2] )     # Adjusting left solution to match right at the turning point

    dE0 = ( ( psi_left[-1] - psi_left[-3] ) - ( psi_right[2] - psi_right[0] ) ) / ( 2 * deltaX * psi_right[1])      # Finding d(E_0)

    return dE0

def numerovWavefn(E0):
    # This does exactly the same thing as the other numerov, but it just returns the wavefunction instead of d(E_0). The way that I originally set this all up meant that it was easier to just duplicate this instead of modifying the other one etc
    mc2 = 5.11e5            # eV
    hc = 197.3              # eV nm
    hOmega = 1              # eV
    
    # Using symmetric guesses to start off with, just makes things easier
    psi_0 = 0
    psi_1 = 0.0001       # A complete guess as to what is reasonable

    psi_left = []
    psi_left.append(psi_0)
    psi_left.append(psi_1)

    psi_right = []
    psi_right.append(psi_1)
    psi_right.append(psi_0)

    # Will be going from -1 to 1 nm
    xRange = np.linspace(-1, 1, 1000)
    deltaX = xRange[1] - xRange[0]

    potential = 0.5 * ( mc2 / hc**2 ) * hOmega**2 * xRange**2

    meetPointX = np.where(potential <= E0)[0][-1]

    f = 2 * ( mc2 / hc**2 ) * ( E0 - potential )

    for xl in xRange[1:meetPointX]:
        i = np.where(xRange == xl)[0][0]
        psi_l_new = ( ( 2 - (5/6) * deltaX**2 * f[i] ) * psi_left[i] - ( 1 + (deltaX**2 / 12) * f[i-1] ) * psi_left[i-1] ) / ( 1 + (deltaX**2 / 12) * f[i+1])
        psi_left.append(psi_l_new)
    
    for xr in xRange[meetPointX:-1][::-1]:
        c = np.where(xRange == xr)[0][0]
        # The indexing in this bit is really weird because I'm trying to do it right to left and make it also be in that direction in the array, so the psi_right values we want are always the the first and second ones
        psi_r_new = ( ( 2 - (5/6) * deltaX**2 * f[c] ) * psi_right[0] - ( 1 + (deltaX**2 / 12) * f[c+1] ) * psi_right[1] ) / ( 1 + (deltaX**2 / 12) * f[c-1])
        psi_right.insert(0, psi_r_new)

    psi_left = np.array(psi_left) * ( psi_right[1] / psi_left[-2] )

    # plt.plot(xRange[:meetPointX-1], psi_left[:-2])
    # plt.plot(xRange[meetPointX-1:], psi_right)
    # plt.show()

    wavefunc = np.concatenate((psi_left[:-2], psi_right[1:]))

    return wavefunc


def q2a():
    ERanges = [(0.1, 0.62), (1.3, 1.6), (2.35, 2.6)]        # Found ranges by plotting d(E_0) against E_0 and seeing where it crossed 0

    # Simple regula falsi root finding
    E_0 = regulaFalsi(ERanges[0][0], ERanges[0][1], numerovDE0, tol=1e-4, printIntermediate=False)
    E_1 = regulaFalsi(ERanges[1][0], ERanges[1][1], numerovDE0, tol=1e-4, printIntermediate=False)
    E_2 = regulaFalsi(ERanges[2][0], ERanges[2][1], numerovDE0, tol=1e-4, printIntermediate=False)

    print(f'First three energies are: {E_0:.5} eV, {E_1:.5} eV, and {E_2:.5} eV')


def q2b():
    Es = [0.5007712065928163, 1.5010174165369703, 2.502924361232347]        # Values of E found from q2a. Note these will be different to the output from that function as it rounds to look nicer, but these are the actual values

    xRange = np.linspace(-1, 1, 1000)       # Same range of x values from earlier, in nm
    deltaX = xRange[1] - xRange[0]
    # For plotting the potential, just looks nice :)
    mc2 = 5.11e5            # eV
    hc = 197.3              # eV nm
    hOmega = 1              # eV
    potential = 0.5 * ( mc2 / hc**2 ) * hOmega**2 * xRange**2
    plt.plot(xRange, potential, color='black', lw='1', label='V(x)', ls='--')


    for E in Es:        # For each E value we find the wavefunction, normalise it, and plot
        wavefunc = numerovWavefn(E)
        normalisation = np.sum(wavefunc**2) * deltaX    # Seems like all that's needed for normalisation

        wavefuncNormed = wavefunc / np.sqrt(normalisation)       # Normalising
        wavefuncNormed += E     # Shifting up by their energy value, just think it makes it a bit more clear when plotting
        plt.plot(xRange[:-1], wavefuncNormed, label=f'$\psi_{Es.index(E)}$')
    
    plt.xlabel('x')
    plt.ylabel('$\psi(x)$')
    plt.legend()
    plt.title('First three normalised stationary state wavefunctions')
    plt.show()


def q2extra():
    # Finding the ranges on which to look for d(E_0)=0

    Es = np.linspace(0.1, 3, 100)
    dE0s = []
    for E in Es:
        dE0 = numerovDE0(E)
        dE0s.append(dE0)
    
    plt.plot(Es, dE0s)
    plt.xlabel('Energy (eV)')
    plt.ylabel('$d(E_0)$')
    plt.grid(color='#CCCCCC', linestyle=':')
    plt.show()



##############################################################

# q1a()

# q1b()

# q1cf()

# q2a()

q2b()

# q2extra()