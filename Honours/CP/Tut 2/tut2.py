# KDSMIL001
# 27-04-2022

from matplotlib import pyplot as plt
import numpy as np
import scipy as sp
import matplotlib
from scipy.special import factorial
import time, random

def lagrangePolynomial(x, i, xs, N=None):
    """Returns the value of the `N`-th degree, `i`-th Lagrange polynomial evaluated at `x` with respect to data points `xs`.
    
        Args
        ----
            x (float):
        Position at which to evaluate the Lagrange polynomial. Needs to be within the interval `[min(xs), max(xs)]`
    
            i (int):
        Index of the value in `xs` to skip when taking the product
    
            xs (array, float):
        Array of x-values to use when generating the Lagrange polynomial
    
            N (int, optional): Degree of the Lagrange polynomial to evaluate, i.e. the number of j-values to iterate over. Defaults to `len(xs)`
    
        Returns
        -------
            y (float):
        Value of the Lagrange polynomial at point `x`
    """
    if N == None:       # Setting a default value for N
        N = len(xs)

    p = 1       # Can't be 0, lol

    for j in range(N):
        if j == i:      # Skips j=i term
            continue
        p *= (x - xs[j]) / (xs[i] - xs[j])

    return p

def lagrangeInterpolation(x, xs, ys):
    """
    Returns the value of the Lagrange interpolating polynomial for data pairs `(xs[i], ys[i])` at point `x`

    Parameters
    ----------
    x : (float) Position at which to evaluate the Lagrange interpolating polynomial. Must be within the interval `[min(xs), max(xs)]`

    xs : (array)(float) Array of data points x_i over which to interpolate

    ys : (array)(float) Array of data points y_i corresponding to x_i. Must be the same length as `xs`

    Returns
    -------
    y : (float) Value of the Lagrange interpolating polynomial at position `x`
    """
    y = 0

    for i in range(len(xs)):
        y += ys[i]*lagrangePolynomial(x, i, xs)

    return y
    
def regulaFalsiInterp(x1, x2, func, xs, ys, tol=0.01):
    """Returns the root of the function `func`, which is interpolated from the points `xs` and `ys`. `x1` and `x2` are the bracketing first guesses.
    
        Args
        ----
            x1 (float):
        Leftmost inital guess
    
            x2 (float):
        Rightmost inital guess
    
            func (function):
        The function which calls the method to interpolate the data in `xs` and `ys`, at some point `x`. Needs to be of the form `func(x, xs, ys)`
    
            xs (array, float):
        Array of data points x_i over which to interpolate
    
            ys (array, float):
        Array of data points y_i corresponding to x_i. Must be the same length as `xs`
    
            tol (float):
        The tolerance to which the root-finding method must reach before exiting and outputting the x-value at the root. Should be less than 1

        Returns
        -------
            x0 (float):
        The x-value for the root of the function `func`
    """
    y1 = func(x1, xs, ys)
    y2 = func(x2, xs, ys)
    
    x0 = x1 - y1 * ((x2 - x1) / (y2 - y1))      # Using the formula for linear interpolation with y(x) = 0 to find x
    y0 = func(x0, xs, ys)
    
    while np.abs(y0) >= tol:
        if y0 * y1 < 0:     # Checking if y0 and y1 are on opposite sides of the root, and if so setting y2 to y0
            y2 = y0
            x2 = x0
        elif y0 * y2 < 0:   # Same here
            y1 = y0
            x1 = x0
            
        x0 = x1 - y1 * ((x2 - x1) / (y2 - y1))      # Sets new x0 value as above
        y0 = func(x0, xs, ys)
        
        print(y0)       # Debugging
    
    return x0

def bisectionInterp(x1, x2, func, xs, ys, tol=0.01):
    # I don't care enough about this method to comment it.
    y1 = func(x1, xs, ys)
    y2 = func(x2, xs, ys)
    
    x0 = x1 + (x2 - x1) / 2
    y0 = func(x0, xs, ys)
    
    while np.abs(y0) >= tol:
        if y0 * y1 < 0:
            y2 = y0
            x2 = x0
        elif y0 * y2 < 0:
            y1 = y0
            x1 = x0

        x0 = x1 + (x2 - x1) / 2
        y0 = func(x0, xs, ys)
        
        print(y0)
    
    return x0

def q1eqn(x):
    return np.exp(x) * np.log(x) - x**2

def q1():
    xData = np.arange(1, 2.1, 0.1)
    yData = q1eqn(xData)

    xEval = np.linspace(1, 2, 100)
    
    x0 = regulaFalsiInterp(xData[0], xData[-1], lagrangeInterpolation, xData, yData, 1e-5)
    print(x0)

    # yInterp = lagrangeInterpolation(xEval, xData, yData)

    # plt.plot(xData, yData, 'o')
    # plt.plot(xEval, yInterp, 's')
    # plt.grid(color='#CCCCCC', linestyle=':')
    plt.show()

def gaussianKernel(x, xPrime, h):
    return (1 / (h * np.sqrt(np.pi))) * np.exp(-((x - xPrime) / h)**2)

def gaussianKernelPrime(x, xPrime, h):
    return -((2 * (x - xPrime)) / (h**3 * np.sqrt(np.pi))) * np.exp(-((x - xPrime) / h)**2)

def gaussianKernelPrimePrime(x, xPrime, h):
    return -((2) / (h**3 * np.sqrt(np.pi))) * np.exp(-((x - xPrime) / h)**2) + ((4 * (x - xPrime)**2) / (h**5 * np.sqrt(np.pi))) * np.exp(-((x - xPrime) / h)**2)

def smoothParticleInterpolation(x, xs, ys, h, kernel):
    """Returns the value at `x` of the interpolated function, using Smooth Particle Interpolation, over the data pairs `(xs[i], ys[i])`. A range of evaluation can be specified, but defaults to `[min(xs), max(xs)]`.
    
        Args
        ----
            x (float):
        Position at which to evaluate the interpolated function. Should be within `xEvalRange`
    
            xs (array, float):
        Array of data points x_i over which to interpolate
    
            ys (array, float):
        Array of data points y_i corresponding to x_i. Must be the same length as `xs`
    
            h (float):
        The so-called "smoothing length" for the kernel function
    
            kernel (function):
        The kernel with which to perform the smoothing approximation. Needs to be a function of the place to evaluate, `x`, the values to iterate over, `xPrime`, and smoothing parameter `h`
    
        Returns
        -------
            y (float):
        Value of the the interpolated function at `x`. Note that for `x = xs[i]`, this may not necessarily return `ys[i]
    """
    # Making them numpy arrays because they're just better to work with
    xs = np.array(xs)
    ys = np.array(ys)

    y = 0

    xSpacing = []
    for i in range(len(xs)):
        # Finds the spacing between "particles" by finding the distance between the midpoint of x[i] and x[i+1] and the midpoint of x[i-1] and x[i]. For the first and last points it just takes the distance between it and the point above or below it.
        if i == 0:
            xSpacing.append((xs[i+1] - xs[i]))

        elif i == len(xs)-1:
            xSpacing.append((xs[i] - xs[i-1]))

        else:
            xSpacing.append((xs[i+1] - xs[i]) / 2 + (xs[i] - xs[i-1]) / 2)

    y = np.sum(xSpacing*ys*kernel(x, xs, h))

    return y

def q2eqn(x):
    return 3 * x**4 - 3 * x**2

def q2eqnPrime(x):
    return 12 * x**3 - 6 * x

def q2eqnPrimePrime(x):
    return 36 * x**2 - 6

def q2(xMin, xMax, xEvalMin, xEvalMax, nParticle, avgParticleSpacing=None, hs=None):

    if avgParticleSpacing == None:
        avgParticleSpacing = (xMax - xMin) / nParticle
    elif avgParticleSpacing != None:
        nParticle = int((xMax - xMin) / avgParticleSpacing)

    if hs == None:
        hs = np.linspace(0.5, 4) * avgParticleSpacing

    # Making the data from the given eqn
    xData = np.linspace(xMin, xMax, nParticle)
    yData = q2eqn(xData)


    xDataPlot = xData[np.logical_and(xData >= xEvalMin, xData <= xEvalMax)]
    yDataPlot = yData[np.logical_and(xData >= xEvalMin, xData <= xEvalMax)]
    
    xEval = np.linspace(xEvalMin, xEvalMax, 1000)       # Making the array of points on which to evaluate the interpolation
    yExact = q2eqn(xEval)       # Finding the exact value of the function for the points we're going to interpolate for

    yInterp = []
    yInterpPrime = []
    yInterpPrimePrime = []
    chiSqaures = []

    for i, h in enumerate(hs):      # Trying out a range of h values 
        yInterp.append([])
        yInterpPrime.append([])
        yInterpPrimePrime.append([])
        for x in xEval:
            yInterp[i].append(smoothParticleInterpolation(x, xData, yData, h, gaussianKernel))
            yInterpPrime[i].append(-smoothParticleInterpolation(x, xData, yData, h, gaussianKernelPrime))
            yInterpPrimePrime[i].append(smoothParticleInterpolation(x, xData, yData, h, gaussianKernelPrimePrime))

        yInterpArr = np.array(yInterp[i])
        print(np.sum((yInterpArr - yExact)**2 / yExact))
        chiSqaures.append(np.sum((yInterpArr - yExact)**2 / yExact))
        # plt.plot(xEval, np.abs(yInterp-yExact), lw=2, label=f'h = {i}')
        # plt.figure()
        # # plt.plot(xDataPlot, yDataPlot, 's', ms=3, label='Data')
        # plt.plot(xEval, yInterp[i], lw=2, label='Interpolated')
        # plt.plot(xEval, yInterpPrime[i], lw=2, label='First Deriv')
        # plt.plot(xEval, yInterpPrimePrime[i], lw=2, label='Second Deriv')
        # plt.legend()

        # plt.figure()
        # plt.plot(xEval, yExact, lw=2, ls='--', label='Exact')
        # plt.plot(xEval, q2eqnPrime(xEval), lw=2, ls='--', label='First Deriv')
        # plt.plot(xEval, q2eqnPrimePrime(xEval), lw=2, ls='--', label='Second Deriv')
        # plt.legend()
        # plt.title(f'h = {h}')


    # plt.plot(xData, yData, 'o')
    # plt.plot(xData, yInterp, 's')

    plt.plot(hs, chiSqaures)


    plt.show()

def q3eqn(u, mu, T):
    return ((u**2) / (1 - np.exp(mu / T) * np.exp(-u)))

def gaussLaguerreIntegration(numPoints, func, *funcArgs):

    points, weights = np.polynomial.laguerre.laggauss(numPoints)

    int = np.sum(func(points, *funcArgs) * weights)

    return int

def q3(r, mu, T):
    V = np.pi * r**2 * 4 / 3

    const = (V / (2 * np.pi**2)) * ((np.exp(mu / T)) * T**3)

    lagGaussInt = const * gaussLaguerreIntegration(3, q3eqn, mu, T)

    print(lagGaussInt)



if __name__ == "__main__":
    # q1()

    # q2(-10, 10, -5, 5, 40, 0.1)

    q3(6, 1, 0.16)

    pass