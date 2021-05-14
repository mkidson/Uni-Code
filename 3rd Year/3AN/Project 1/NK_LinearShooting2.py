from matplotlib import pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp
from numpy import cos, pi, sin, sqrt, exp, random
import matplotlib
matplotlib.rcParams.update({
    'pgf.texsystem': 'pdflatex',
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
})

n=1
a=0.001
b=10
alpha=0
beta=1
p=(beta-alpha)/(b-a)

N=200
h=(b-a)/N
print('h',h)

r_span=np.array([a,b])
rs=np.linspace(a,b,N)
h=rs[1]-rs[0]
guess=p*rs # Initial guess
particularICs=[0,0]
homogICs=[0,1]

print(np.where(rs==rs[0])[0][0])

def UPrime(arr):
    out=[]
    out.append((arr[1]-arr[0])/h)
    for ind, elem in enumerate(arr[1:-1]):
        out.append((arr[ind+1]-arr[ind-1])/(2*h))
    out.append((arr[-2]-arr[-1])/h)
    return np.array(out)

def f(r, guess):
    uPr=UPrime(guess)
    ind=np.where(rs==r)[0][0]
    return -((1/r)*uPr[ind] + (guess[ind]/(1-(guess[ind])**2))*(uPr[ind]**2 - (n**2)/(r**2)) + (guess[ind])*(1-(guess[ind])**2))

def Q(r, guess):
    uPr=UPrime(guess)
    ind=np.where(rs==r)[0][0]
    return -((1+(guess[ind])**2)/((1-(guess[ind])**2)**2)*(uPr[ind]**2 - (n**2)/(r**2)) + (1-3*(guess[ind])**2))

def P(r, guess):
    uPr=UPrime(guess)
    ind=np.where(rs==r)[0][0]
    return -((1/r) + (guess[ind])/(1-(guess[ind])**2)*(2*uPr[ind]))

def N(r, guess):
    uPr=UPrime(guess)
    uPrPr=UPrime(uPr)
    ind=np.where(rs==r)[0][0]
    return -uPrPr[ind]+f(r, guess)

# def f(r, guess):
#     out=[]
#     uPr=UPrime(guess)
#     for ind, elem in enumerate(r):
#         out.append(-((1/elem)*uPr[ind] + (guess[ind]/(1-(guess[ind])**2))*(uPr[ind]**2 - (n**2)/(elem**2)) + (guess[ind])*(1-(guess[ind])**2)))
#     return out

# def Q(r, guess):
#     out=[]
#     uPr=UPrime(guess)
#     for ind, elem in enumerate(r):
#         out.append(-((1+(guess[ind])**2)/((1-(guess[ind])**2)**2)*(uPr[ind]**2 - (n**2)/(elem**2)) + (1-3*(guess[ind])**2)))
#     return out

# def P(r, guess):
#     out=[]
#     uPr=UPrime(guess)
#     for ind, elem in enumerate(r):
#         out.append(-((1/elem) + (guess[ind])/(1-(guess[ind])**2)*(2*uPr[ind])))
#     return out

# def N(r, guess):
#     out=[]
#     uPr=UPrime(guess)
#     uPrPr=UPrime(uPr)
#     for ind, elem in enumerate(r):
#         out.append(-uPrPr[ind]+f(r, guess))
#     return out

def particular(r,u):
    y=u[0]
    y1=u[1]
    return np.array([y1, P(r, guess)*y1 + Q(r, guess)*y + N(r, guess)])

def homog(r,u):
    w=u[0]
    w1=u[1]
    return np.array([w1, P(r, guess)*w1 + Q(r, guess)*w])


tol=1e-5 # The program never seems to reach this level of accuracy but i'm leaving it in for the sake of completeness
maxIter=2 # If this is too low then the higher vorticities don't reach a stable solution
k=1 # Counter variable

while k < maxIter:
    ySoln = solve_ivp(particular, r_span, particularICs, t_eval=rs, method='RK45')
    wSoln = solve_ivp(homog, r_span, homogICs, t_eval=rs, method='RK45')
    t=ySoln.t

    C=(-ySoln.y[0][-1])/wSoln.y[0][-1]
    # print(C)
    z=ySoln.y[0]+C*wSoln.y[0]
    guess+=z

    particularICs[0]=u[0]


    k+=1


# plt.plot(t, z, label='z')
# plt.plot(t, ySoln.y[0], label='y')
# plt.plot(t, wSoln.y[0], label='w')
plt.plot(t, guess, label='u(linear shooting)')
plt.plot(t, p*t, label='u0')
# plt.plot(rs[2:-1], Q(rs[2:-1]), label='Q')
plt.legend()
plt.show()