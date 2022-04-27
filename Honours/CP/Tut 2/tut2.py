# KDSMIL001
# 27-04-2022

from matplotlib import pyplot as plt
import numpy as np
import scipy as sp
import matplotlib
from scipy.special import factorial
import time, random

def lagrangePolynomial(x, i, xs, N=None):
    """
    Returns the value of the `N`-th degree, `i`-th Lagrange polynomial evaluated at `x` with respect to data points `xs`.

    Parameters
    ----------
    x : (float) Position at which to evaluate the Lagrange polynomial. Needs to be within the interval `[min(xs), max(xs)]`

    i : (int) Index of the value in `xs` to skip when taking the product. 

    xs : (array)(float) Array of x-values to use when generating the Lagrange polynomial. Needs to be of length `N`

    N : (int) Degree of the Lagrange polynomial to evaluate, i.e. the number of j-values to iterate over. Defaults to `len(xs)`

    Returns
    -------
    p : (float) Value of the Lagrange polynomial at point `x`
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
    
def q1eqn(x):
    return np.exp(x) * np.log(x) - x**2

def q1():
    xData = np.arange(1, 2.1, 0.1)
    yData = q1eqn(xData)

    xEval = np.linspace(1, 2, 100)
    yInterp = lagrangeInterpolation(xEval, xData, yData)

    plt.plot(xData, yData, 'o')
    plt.plot(xEval, yInterp, 's')
    plt.grid(color='#CCCCCC', linestyle=':')
    plt.show()

def gaussianKernel(x, xPrime, h):
    return (1/(h*np.sqrt(np.pi)))*np.exp(-((x-xPrime)/h)**2)

def smoothParticleInterpolation(x, xs, ys, h):
    """
    Returns the value at `x` of the interpolated function, using Smooth Particle Interpolation, over the data pairs `(xs[i], ys[i])`. A range of evaluation can be specified, but defaults to `[min(xs), max(xs)]`.

    Parameters
    ----------
    x : (float) Position at which to evaluate the interpolated function. Should be within `xEvalRange`

    xs : (array)(float) Array of data points x_i over which to interpolate

    ys : (array)(float) Array of data points y_i corresponding to x_i. Must be the same length as `xs`

    h : (float) So-called "smoothing length" for the kernel function

    Returns
    -------
    y : (float) Value of the the interpolated function at `x`. Note that for `x = xs[i]`, this may not necessarily return `ys[i]
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

    y = np.sum(xSpacing*ys*gaussianKernel(x, xs, h))

    return y

def q2eqn(x):
    return 3 * x**4 - 3 * x**2

def q2(xMin, xMax, hs):
    # Making the data from the given eqn
    xData = np.arange(-10, 10.1, 0.1)
    yData = q2eqn(xData)
    
    xEval = np.linspace(xMin, xMax, 1000)       # Making the array of points on which to evaluate the interpolation
    yExact = q2eqn(xEval)       # Finding the exact value of the function for the points we're going to interpolate for

    for i in hs:      # Trying out a range of h values 
        yInterp = []
        for x in xEval:
            yInterp.append(smoothParticleInterpolation(x, xData, yData, i))

        plt.plot(xEval, np.abs(yInterp-yExact), 's', ms=2, label=f'h = {i}')


    # plt.plot(xData, yData, 'o')
    # plt.plot(xData, yInterp, 's')

    plt.legend()
    # plt.show()

if __name__ == "__main__":
    q1()

    # q2(-8, 8, [0.05, 0.1, 0.2, 0.4, 1])

    pass