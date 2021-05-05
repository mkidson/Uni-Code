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

N=100
h=(b-a)/N
print('h',h)

rs=np.linspace(a,b,N)
u_0=p*rs # Initial guess
u_1=p # Initial guess first derivative

def f(r):
    return -((1/r)*u_1 + ((p*r)/(1-(p*r)**2))*(u_1**2 - (n**2)/(r**2)) + (p*r)*(1-(p*r)**2))

def Q(r):
    return -((1+(p*r)**2)/((1-(p*r)**2)**2)*(u_1**2 - (n**2)/(r**2)) + (1-3*(p*r)**2))

def P(r):
    return -((1/r) + (p*r)/(1-(p*r)**2)*(2*u_1))

def N(r):
    return f(r)

# Trying to implement finite difference method instead of linear shooting
ps=P(rs[1:-1])
qs=Q(rs[1:-1])
ns=N(rs[1:-1])

A=np.diag((-2-(h**2)*qs), k=0)+np.diag((1+(h*ps[1:])/2),k=-1)+np.diag((1-(h*ps[:-1])/2),k=1)
B=(h**2)*ns
B[-1]+=(1-(h*ps[-1])/2)

c1=np.matmul(np.linalg.inv(A),B)
c=np.insert(c1,0,[0])
c=np.append(c,[0])
final=u_0+c

plt.plot(rs, final, label='u(finite difference)')
plt.plot(rs, u_0, label='u0')
# plt.plot(rs, c, label='c')
plt.legend()
plt.show()