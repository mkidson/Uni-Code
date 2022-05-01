# KDSMIL001
# 27-04-2022

from matplotlib import pyplot as plt
import numpy as np
import scipy as sp
import matplotlib
from scipy.special import factorial
import time, random

# Functions written generally for later use. lagrangePolynomial should probably be in lagrangeInterpolation but i'm not sure
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
    """Returns the value of the Lagrange interpolating polynomial for data pairs `(xs[i], ys[i])` at point `x`
    
        Args
        ----
            x (float):
        Position at which to evaluate the Lagrange interpolating polynomial. Must be within the interval `[min(xs), max(xs)]`
    
            xs (array, float):
        Array of data points x_i over which to interpolate
    
            ys (array, float):
        Array of data points y_i corresponding to x_i. Must be the same length as `xs`
    
    
    
        Returns
        -------
            y (float):
        Value of the Lagrange interpolating polynomial at position `x`
    """
    y = 0

    for i in range(len(xs)):
        y += ys[i]*lagrangePolynomial(x, i, xs)

    return y
    
def regulaFalsiInterp(x1, x2, func, xs, ys, tol=0.01, printIntermediate=True):
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

            printIntermediate (bool):
        Tells the function whether it should print out the step number, x-value, and y-value at each step

        Returns
        -------
            x0 (float):
        The x-value for the root of the function `func`
    """
    y1 = func(x1, xs, ys)
    y2 = func(x2, xs, ys)
    
    x0 = x1 - y1 * ((x2 - x1) / (y2 - y1))      # Using the formula for linear interpolation with y(x) = 0 to find x
    y0 = func(x0, xs, ys)
    
    i = 0
    while np.abs(y0) >= tol:
        i += 1
        if y0 * y1 < 0:     # Checking if y0 and y1 are on opposite sides of the root, and if so setting y2 to y0
            y2 = y0
            x2 = x0
        elif y0 * y2 < 0:   # Same here
            y1 = y0
            x1 = x0
            
        x0 = x1 - y1 * ((x2 - x1) / (y2 - y1))      # Sets new x0 value as above
        y0 = func(x0, xs, ys)
        
        if printIntermediate:
            print(f'step {i}')
            print(f'x: {x0:.5}')
            print(f'y: {y0:.5}')
            print('---')
    
    return x0

def smoothParticleInterpolation(x, xs, ys, h, kernel):
    """Returns the value at `x` of the interpolated function, using Smooth Particle Interpolation, over the data pairs `(xs[i], ys[i])`. A range of evaluation can be specified, but defaults to `[min(xs), max(xs)]`. If x is an array of values, it returns an array of y values, and if it's a float it returns a float.
    
        Args
        ----
            x (float) or (array, float):
        Position at which to evaluate the interpolated function. Should be within `xEvalRange`. Could also be array of floats within `xEvalRange`
    
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
            y (float) or (array, float):
        Value of the the interpolated function at `x`. Note that for `x = xs[i]`, this may not necessarily return `ys[i]`. Could return array of interpolated values if `x` is an array.
    """
    # Making them numpy arrays because they're just better to work with
    xs = np.array(xs)
    ys = np.array(ys)

    xSpacing = []
    for i in range(len(xs)):
        # Finds the spacing between "particles" by finding the distance between the midpoint of x[i] and x[i+1] and the midpoint of x[i-1] and x[i]. For the first and last points it just takes the distance between it and the point above or below it.
        if i == 0:
            xSpacing.append((xs[i+1] - xs[i]))

        elif i == len(xs)-1:
            xSpacing.append((xs[i] - xs[i-1]))

        else:
            xSpacing.append((xs[i+1] - xs[i]) / 2 + (xs[i] - xs[i-1]) / 2)

    # My fix for being able to accept both arrays and floats to interpolate for. Could use some work/nifty numpy methods
    if (type(x) == np.ndarray) or (type(x) == list):
        y = []
        for i in x:
            y.append(np.sum(xSpacing*ys*kernel(i, xs, h)))
        y = np.array(y)
    elif (type(x) == float) or (type(x) == int):
        y = np.sum(xSpacing*ys*kernel(x, xs, h))

    return y

def gaussLaguerreIntegration(numRoots, func, *funcArgs):
    """Blindingly simple implementation of Gauss-Laguerre quadrature integration. 
    
        Args
        ----
            numRoots (int):
        Number of roots of the Laguerre polynomials to use in the integration
    
            func (function):
        Name of the function q(t) in the integrand of the integral, where the entire integrand is q(t) e^-t

            *funcArgs (optional):
        Arguments of `func` if any are needed. Obviously need to be fed in the order that they appear in `func`
    
        Returns
        -------
            int (float):
        Value of the integral that has been esimated using Gauss-Laguerre quadrature
    """
    points, weights = np.polynomial.laguerre.laggauss(numRoots)     # Finds the roots of the Laguerre polynomials to use in the method

    int = np.sum(func(points, *funcArgs) * weights)

    return int

# A collection of equations needed for specific questions, vaguely labelled in a logical way
def q1eqn(x):
    return np.exp(x) * np.log(x) - x**2

def q2eqn(x):
    return 3 * x**4 - 3 * x**2

def q2eqnPrime(x):
    return 12 * x**3 - 6 * x

def q2eqnPrimePrime(x):
    return 36 * x**2 - 6

def gaussianKernel(x, xPrime, h):
    return (1 / (h * np.sqrt(np.pi))) * np.exp(-((xPrime - x) / h)**2)

def gaussianKernelPrime(x, xPrime, h):
    return -((2 * (xPrime - x)) / (h**3 * np.sqrt(np.pi))) * np.exp(-((xPrime - x) / h)**2)

def gaussianKernelPrimePrime(x, xPrime, h):
    return -((2) / (h**3 * np.sqrt(np.pi))) * np.exp(-((xPrime - x) / h)**2) + ((4 * (xPrime - x)**2) / (h**5 * np.sqrt(np.pi))) * np.exp(-((xPrime - x) / h)**2)

def q3eqn(u, mu, T):
    return ((u**2) / (1 - np.exp(mu / T) * np.exp(-u)))

# Code used for specific questions
def q1():
    # Generating the data to be used in the interpolation
    xData = np.arange(1, 2.1, 0.1)
    yData = q1eqn(xData)

    xEval = np.linspace(1, 2, 100)      # The points at which we interpolate the function in order to plot it
    
    x0 = regulaFalsiInterp(xData[0], xData[-1], lagrangeInterpolation, xData, yData, 1e-5)      # Finds the root using regula falsi to a tolerance of 1e-5

    yInterp = lagrangeInterpolation(xEval, xData, yData)

    plt.plot(xData, yData, 'rs', ms=4, label='Data')
    plt.plot(xEval, yInterp, label='Interpolated Function')
    plt.axvline(x0, color='green', lw=1, label=f'$x_0={x0:.5}$')
    plt.grid(color='#CCCCCC', linestyle=':')
    plt.title('$e^x \ln x-x^2$ Interpolated')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    # plt.savefig('.\Plots\q1.pdf')
    plt.show()

def q2a():
    # Defining bounds
    xMin = -10
    xMax = 10
    xEvalMin = -5
    xEvalMax = 5

    # Chose these by trial and error, informed by the results of the next part
    numParticles = 50
    h = 0.5

    # Generating the data from the function
    xData = np.linspace(xMin, xMax, numParticles)
    yData = q2eqn(xData)

    xEval = np.linspace(xEvalMin, xEvalMax, 1000)       # Making the array of points on which to evaluate the interpolation
    yExact = q2eqn(xEval)       # Finding the exact value of the function for the points we're going to interpolate for

    # Not strictly necessary, but just getting those data points that lie within the range we're interpolating over
    xDataPlot = xData[np.logical_and(xData >= xEvalMin, xData <= xEvalMax)]
    yDataPlot = yData[np.logical_and(xData >= xEvalMin, xData <= xEvalMax)]

    # Feeding the functions arrays so they return arrays. Note the first deriv has a negative out front
    yInterp = smoothParticleInterpolation(xEval, xData, yData, h, gaussianKernel)
    yInterpPrime = -smoothParticleInterpolation(xEval, xData, yData, h, gaussianKernelPrime)
    yInterpPrimePrime = smoothParticleInterpolation(xEval, xData, yData, h, gaussianKernelPrimePrime)

    # # Plotting the errors
    plt.figure()
    plt.plot(xEval, yInterp-yExact, lw=2, label=f'error')
    plt.plot(xDataPlot, [0]*24, 's', ms=3, label='Data')
    plt.title('Function Error')
    plt.xlabel('x')
    plt.legend()
    # plt.savefig('.\Plots\q2a1.pdf')

    plt.figure()
    plt.plot(xEval, yInterpPrime-q2eqnPrime(xEval), lw=2, label=f'error')
    plt.plot(xDataPlot, [0]*24, 's', ms=3, label='Data')
    plt.title('First Derivative Error')
    plt.xlabel('x')
    plt.legend()
    # plt.savefig('.\Plots\q2a2.pdf')

    plt.figure()
    plt.plot(xEval, yInterpPrimePrime-q2eqnPrimePrime(xEval), lw=2, label=f'error')
    plt.plot(xDataPlot, [0]*24, 's', ms=3, label='Data')
    plt.title('Second Derivative Error')
    plt.xlabel('x')
    plt.legend()
    # plt.savefig('.\Plots\q2a3.pdf')

    # Plotting the functions 
    # plt.figure()
    # plt.plot(xEval, yInterp, lw=2, label='f(x)')
    # plt.plot(xEval, yInterpPrime, lw=2, label='f\'(x)')
    # plt.plot(xEval, yInterpPrimePrime, lw=2, label='f\'\'(x)')
    # plt.plot(xDataPlot, [0]*24, 's', ms=3, label='Data')
    # plt.xlabel('x')
    # plt.ylabel('y')
    # plt.title('Interpolated')
    # plt.legend()
    # # plt.savefig('.\Plots\q2afunc.pdf')

    # plt.figure()
    # plt.plot(xEval, yExact, lw=1, ls='--', label='f(x)')
    # plt.plot(xEval, q2eqnPrime(xEval), lw=1, ls='--', label='f\'(x)')
    # plt.plot(xEval, q2eqnPrimePrime(xEval), lw=1, ls='--', label='f\'\'(x)')
    # plt.xlabel('x')
    # plt.ylabel('y')
    # plt.title('Exact')
    # plt.legend()
    # # plt.savefig('.\Plots\q2aexact.pdf')


    plt.show()

def q2b():
    # Defining bounts
    xMin = -10
    xMax = 10
    xEvalMin = -5
    xEvalMax = 5

    # Chosen mostly because they showed interesting features in the contour plot
    numParticles = np.arange(15, 45)
    hs = np.linspace(0.3, 1.5, 25)
    
    xEval = np.linspace(xEvalMin, xEvalMax, 1000)       # Making the array of points on which to evaluate the interpolation
    yExact = q2eqn(xEval)       # Finding the exact value of the function for the points we're going to interpolate for

    # Initialising the arrays to be populated by arrays god why are there so many arrays
    yInterp = []
    absErrors = []

    for i, n in enumerate(numParticles):
        # Making the data from the given eqn
        xData = np.linspace(xMin, xMax, n)
        yData = q2eqn(xData)

        absErrorsNew = []       # Array to be appended to absErrors so it's 2D

        for h in hs:    # Just using temp here because it's easier for the error analysis later
            yInterpTemp = smoothParticleInterpolation(xEval, xData, yData, h, gaussianKernel)
            yInterp.append(yInterpTemp)

            absError = np.sum(np.abs(yInterpTemp - yExact))     # Chose this again because it gave reasonable plots. Chi square and error squared all were odd
            absErrorsNew.append(absError)

        absErrors.append(absErrorsNew)

    plt.figure()
    plt.contourf(hs, numParticles, absErrors, levels=40)
    plt.colorbar(label='error')
    plt.xlabel('h')
    plt.ylabel('N')
    plt.title('Absolute Error of Interpolated vs Exact')
    plt.show()
    # plt.savefig('.\Plots\q2b.pdf')

def q3(r, mu, T):
    reV = (r * 1e-15) / (1.97327e-7)
    V = np.pi * reV**3 * 4 / 3
    T = T * 1e9
    ints = []
    Ts = np.linspace(0.06, 0.18, 50) * 1e9
    mus = np.linspace(-0.2, 0.2, 50) * 1e9

    for t, ts in enumerate(Ts):
        ints.append([])
        for m in mus:
            const = (V / (2 * np.pi**2)) * ((np.exp(m / ts)) * ts**3)
            ints[t].append(const * gaussLaguerreIntegration(5, q3eqn, m, ts))

    # print(lagGaussInt)

    plt.contourf(mus, Ts, ints)
    # plt.plot(mus, ints[0])
    plt.xlabel('mu (GeV)')
    plt.ylabel('T (GeV)')
    # plt.ylabel('N')
    # plt.title('')
    plt.show()



if __name__ == "__main__":
    # q1()

    # q2a()

    # q2b()

    # q3(6, 1, 0.16)

    pass