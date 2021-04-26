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
a=0.001 #might need to be 0.001
b=10
alpha=0
beta=1
p=(beta-alpha)/(b-a)

N=50
h=(b-a)/N
print('h',h)

r_span=np.array([a,b])
rs=np.linspace(a,b,N)
u_0=p*rs # Initial guess
u_1=p # Initial guess first derivative
yICs=[0,0]
wICs=[0,1]


def f(r):
    return -((1/r)*u_1 + ((p*r)/(1-(p*r)**2))*(u_1**2 - (n**2)/(r**2)) + (p*r)*(1-(p*r)**2))

def Q(r):
    return -((1+(p*r)**2)/((1-(p*r)**2)**2)*(u_1**2 - (n**2)/(r**2)) + (1-3*(p*r)**2))

def P(r):
    return -((1/r) + (p*r)/(1-(p*r)**2)*(2*u_1))

def N(r):
    return -u_1+f(r)

def particular(r,u):
    y=u[0]
    y1=u[1]
    return np.array([y1, P(r)*y1 + Q(r)*y + N(r)])

def homog(r,u):
    w=u[0]
    w1=u[1]
    return np.array([w1, P(r)*w1 + Q(r)*w])


ySoln = solve_ivp(particular, r_span, yICs, t_eval=rs)
wSoln = solve_ivp(homog, r_span, wICs, t_eval=rs)
t=ySoln.t

C=(beta-ySoln.y[0][-1])/wSoln.y[0][-1]
z=ySoln.y[0]+C*wSoln.y[0]
final=u_0+z

plt.plot(t, z, label='z')
plt.plot(t, final, label='u')
plt.plot(t, u_0, label='u0')
plt.legend()
plt.show()

