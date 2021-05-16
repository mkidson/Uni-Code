from matplotlib import pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp
from numpy import cos, pi, sin, sqrt, exp, random
import matplotlib, time
# matplotlib.use('pgf')
matplotlib.rcParams.update({
    'pgf.texsystem': 'pdflatex',
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
})

ns=[1,2,3] # Vorticity
a=0.1 # Start of r, should be 0 but the program freaks out if we go smaller
b=10 # End of r, should be infty but again we get issues
alpha=0 # Left BC
beta=1 # Right BC
p=(beta-alpha)/(b-a) # Slope for initial guess, not used
N=4000 # Number of iterations. Too small and our approximations to the derivative get innacurate. Make nice and big and you're gucci gang

rs=np.linspace(a,b,N) # Array of rs. linspace not arange in order to keep spacing consistent with h and the last point in the array being b
h=rs[1]-rs[0] # Getting an h to use later
print(f'h: {h}')

# region Functions used, not too important, just done like this to save space
def UPrime(arr):
    out=[]
    out.append((-3*arr[0]+4*arr[1]-arr[2])/(2*h))
    for ind, elem in enumerate(arr[1:-1]):
        if ind==0:
            pass
        else:
            out.append((arr[ind+1]-arr[ind-1])/(2*h))
    out.append((3*arr[-1]-4*arr[-2]+arr[-3])/(2*h))
    return np.array(out)

def f(r, guess, ind):
    uPr=UPrime(guess)
    return -((1/r)*uPr[ind] + (guess[ind]/(1-(guess[ind])**2))*(uPr[ind]**2 - (n**2)/(r**2)) + (guess[ind])*(1-(guess[ind])**2))

def Q(r, guess):
    out=[]
    uPr=UPrime(guess)
    for ind, elem in enumerate(r):
        out.append(-((1+(guess[ind])**2)/((1-(guess[ind])**2)**2)*(uPr[ind]**2 - (n**2)/(elem**2)) + (1-3*(guess[ind])**2)))
    return np.array(out)

def P(r, guess):
    out=[]
    uPr=UPrime(guess)
    for ind, elem in enumerate(r):
        out.append(-((1/elem) + (guess[ind])/(1-(guess[ind])**2)*(2*uPr[ind])))
    return np.array(out)

def N(r, guess):
    out=[]
    uPr=UPrime(guess)
    uPrPr=UPrime(uPr)
    for ind, elem in enumerate(r):
        out.append(-uPrPr[ind]+f(elem, guess, ind))
    return np.array(out)
# endregion

"""
tol is actually the norm of the rhs vector in our vector equation. idk why it's that but that's just what we use. I also calculate the norm of the correction z as i feel that's more useful but i don't use it as a condition
"""

for n in ns:
    u=-exp(-rs)+1 # Initial guess. Not arbitrary as a straight line messes up
    tol=1 # Initial tolerance so the loop doesn't break. 
    maxIter=100 # Just to put an upper limit so the program can reach the tolerance. doesn't always manage it but idc
    k=1 # Counter variable
    t0=time.time()
    while k < maxIter and tol > 1e-5:
        print('-------------------------------------------------------------------------')
        print(f'Iteration: {k}')
        # Gets arrays of p, q, and n excluding the endpoints, as i don't need the endpoints for the matrix eqn
        ps=P(rs[1:-1], u)
        qs=Q(rs[1:-1], u)
        ns=N(rs[1:-1], u)
        # creates the tridiagonal matrix, note the slicing for p
        A=np.diag((-2-(h**2)*qs), k=0)+np.diag((1+(h*ps[1:])/2),k=-1)+np.diag((1-(h*ps[:-1])/2),k=1)
        B=(h**2)*ns # The RHS vector. not complete yet, needs some additions which happens in the next few lines
        # Calculates the endpoints for the correction z as per the NK equations and uses them for those extra naughty bits on the front and end of the RHS vector
        newAlpha=-u[0]+alpha
        print(f'left BC correction: {newAlpha}')
        B[0]-=newAlpha*(1+(h*ps[0])/2)
        newBeta=-u[-1]+beta
        print(f'right BC correction: {newBeta}')
        B[-1]-=newBeta*(1-(h*ps[-1])/2)
        
        tol=np.linalg.norm(B) # Updates tolerance
        print('tol:',tol)
        z1=np.linalg.solve(A,B) # Solves the matrix eqn
        z=np.insert(z1,0,[newAlpha]) # These two lines just add the endpoints for z onto the front and end of it
        z=np.append(z,[newBeta])
        print('correction:',np.linalg.norm(z))
        u+=z # Updates our guess
        k+=1

    # Plots things
    # plt.figure()
    print('--------------------------------------')
    print(f'Iterations: {k}')
    t1=time.time()
    print(f'Time taken: {t1-t0}')
    plt.plot(rs, u, label=f'n={n}')

plt.legend()
plt.xlabel('r')
plt.ylabel('u')
plt.title('Newton-Kantorovich method using Finite Differences')
plt.show()
# plt.savefig(r'3rd Year\3AN\Project 1\Plots\NK_FD.pgf')