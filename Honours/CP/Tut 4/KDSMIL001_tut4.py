# KDSMIL001
# 26-05-2022

import numpy as np
import random
import matplotlib.pyplot as plt

def q1b():

    xMin = 0        # left BC x value
    xMax = 1        # Right BC x value
    u0 = 2          # Left BC u value
    uNp1 = 1        # Right BC u value
    deltaX = 0.001      # grid spacing
    eps = 0.0001       # Constant in diff eq
    numPoints = int((xMax - xMin) / deltaX)     # Number of points in the grid

    xs = np.linspace(xMin, xMax, numPoints)     # Array of x values 
    # Constants derived for this scheme
    alpha = np.full(numPoints, (eps + deltaX / 2))
    beta = np.full(numPoints, (eps - deltaX / 2))
    gamma = np.full(numPoints, (-2 * eps))

    # Tridiagonal matrix. Weird indexing going on here but it works
    A = np.diag(alpha[2:-1], -1) + np.diag(gamma[1:-1], 0) + np.diag(beta[1:-2], 1)
    w = np.zeros(numPoints - 2)     # RHS of the matrix eqn
    w[0] = -alpha[0] * u0       # Adding in the ends of w, from derivation
    w[-1] = -beta[-1] * uNp1

    u = np.linalg.solve(A, w)       # Solving the matrix eqn
    u = np.insert(u, 0, u0)         # Adding in the BCs
    u = np.append(u, uNp1)

    # Plotting the solution
    plt.plot(xs, u, label='Finite Difference solution')
    plt.xlabel('$x$')
    plt.ylabel('$u(x)$')
    plt.legend()
    plt.title('Solution to one-dimensional advection-diffusion equation, $\epsilon=0.1$')
    plt.grid(color='#CCCCCC', linestyle=':')
    plt.show()

def q1c():
    # Now with upwinding

    xMin = 0        # left BC x value
    xMax = 1        # Right BC x value
    u0 = 2          # Left BC u value
    uNp1 = 1        # Right BC u value
    deltaX = 0.001      # grid spacing
    eps = 0.0001       # Constant in diff eq
    numPoints = int((xMax - xMin) / deltaX)     # Number of points in the grid

    xs = np.linspace(xMin, xMax, numPoints)     # Array of x values 
    # Constants derived for this scheme
    alpha = np.full(numPoints, (eps + deltaX))
    beta = np.full(numPoints, (eps))
    gamma = np.full(numPoints, (-2 * eps - deltaX))

    # Tridiagonal matrix. Weird indexing going on here but it works
    A = np.diag(alpha[2:-1], -1) + np.diag(gamma[1:-1], 0) + np.diag(beta[1:-2], 1)
    w = np.zeros(numPoints - 2)     # RHS of the matrix eqn
    w[0] = -alpha[0] * u0       # Adding in the ends of w, from derivation
    w[-1] = -beta[-1] * uNp1

    u = np.linalg.solve(A, w)       # Solving the matrix eqn
    u = np.insert(u, 0, u0)         # Adding in the BCs
    u = np.append(u, uNp1)

    # Plotting the solution
    plt.plot(xs, u, label='Finite Difference solution')
    plt.xlabel('$x$')
    plt.ylabel('$u(x)$')
    plt.legend()
    plt.title('Solution to one-dimensional advection-diffusion equation, $\epsilon=0.0001$')
    plt.grid(color='#CCCCCC', linestyle=':')
    plt.show()

def q1d():
    xMin = 0        # left BC x value
    xMax = 1        # Right BC x value
    u0 = 2          # Left BC u value
    uNp1 = 1        # Right BC u value
    deltaX = 0.01      # grid spacing for x
    deltaT = 0.00001       # grid spacing for t
    eps = 0.1       # Constant in diff eq
    numPoints = int((xMax - xMin) / deltaX)     # Number of points in the grid

    xs = np.linspace(xMin, xMax, numPoints)     # Array of x values 
    alpha = np.full(numPoints, (( eps / deltaX**2 ) + ( 1 / ( 2 * deltaX ) )) * deltaT)
    beta = np.full(numPoints, (( eps / deltaX**2 ) - ( 1 / ( 2 * deltaX ) )) * deltaT)
    gamma = np.full(numPoints, (( -2 * eps / deltaX**2 ) * deltaT ) + 1)

    IC = - xs + 2

    A = np.diag(alpha[2:-1], -1) + np.diag(gamma[1:-1], 0) + np.diag(beta[1:-2], 1)

    spatialSolns = []
    dudts = []
    oldSoln = IC
    plt.plot(xs, oldSoln, label='Initial Condition')

    dudt = 1

    numSteps = 0
    while dudt > 0.001:
        newSoln = np.matmul(A, oldSoln[1:-1])
        newSoln[0] += alpha[0] * u0
        newSoln[-1] += beta[-1] * uNp1
        newSoln = np.insert(newSoln, 0, u0)
        newSoln = np.append(newSoln, uNp1)

        dudt = np.sum((newSoln - oldSoln) / deltaT)
        dudts.append(dudt)

        oldSoln = newSoln
        numSteps += 1

    plt.plot(xs, newSoln, label=f'Soln after {numSteps} steps')

    plt.xlabel('$x$')
    plt.ylabel('$u(x)$')
    plt.legend()
    plt.title('Solution to one-dimensional advection-diffusion equation, $\epsilon=0.1$')
    plt.grid(color='#CCCCCC', linestyle=':')
    plt.show()



if __name__ == "__main__":

    # q1b()

    # q1c()

    q1d()






    pass