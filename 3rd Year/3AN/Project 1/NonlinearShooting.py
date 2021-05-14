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

"""
In order to make this work for vorticity of 3, N needs to be greater than 50 and maxIter needs to be greater than 200. Not sure why this is but it seems to be fine. 
"""

n=2 # Vorticity
a=0.001 # Start of r, should be 0 but that leads to problems
b=10 # End of r, meant to be infinity

N=100 # Number of integration points
h=(b-a)/N
# print('h',h)

r_span=np.array([a,b]) # Array containing start and end of r, used for solve_ivp
rs=np.linspace(a,b,N) # Array of rs, needs to be defined for solve_ivp or else it will make its own array, which could be bad

alpha=0 # Left BC
beta=1 # Right BC
p=(beta-alpha)/(b-a) # Initial guess for the shooting parameter (gradient at r=0)
print('Initial p:', p)
ICs=np.array([alpha,p,0,1]) # Initial conditions [u(0)=alpha, v(0)=p, z(0)=0, w(0)=1]

# These are just for convenience, could just be done explicitly in the du_dr function
def f(r,u,v):
    return -((1/r)*v + (u/(1-u**2))*(v**2 - (n**2)/(r**2)) + u*(1-u**2))

def df_du(r,u,v):
    return -((1+u**2)/((1-u**2)**2)*(v**2 - (n**2)/(r**2)) + (1-3*u**2))

def df_dv(r,u,v):
    return -((1/r) + u/(1-u**2)*(2*v))

# The function solve_ivp will use to solve the 2 IVPs
def du_dr(R,y):
    U=y[0]
    V=y[1]
    Z=y[2]
    W=y[3]
    return np.array([V, f(R,U,V), W, df_du(R,U,V)*Z + df_dv(R,U,V)*W])
u_1=0 # Just used so the while doesn't break the first loop around
tol=1e-5 # The program never seems to reach this level of accuracy but i'm leaving it in for the sake of completeness
maxIter=400 # If this is too low then the higher vorticities don't reach a stable solution
k=1 # Counter variable

# The actual loop that implements the shooting method
while k <= maxIter and (abs(u_1-b)>tol):
    # Integrator. I could use RK45 but it seems to struggle with the higher vorticities, so this higher order RK method is better
    soln=solve_ivp(du_dr, r_span, ICs, t_eval=rs, method='DOP853')

    # Saves a copy of the initial guess but at higher vorticities the initial guess is pretty much unintegrable, so plotting it leads to unusable plots
    if k==1:
        u_0=soln.y[0]
        u_0_t=soln.t
    
    # This handles getting the last element of the solution for u and z in order to update p
    u=soln.y[0]
    u_1=u[-1]
    z=soln.y[2]
    z_1=z[-1]

    # And then updates p and updates the ICs
    p=p-(u_1-beta)/(z_1)
    ICs[1]=p
    
    # print(k)
    k+=1

print("Final p:",p)
# print('z_1', z_1)

# r values for plotting. They should all be the same across u, v, z, w. I called it t because that's what the integrator calls it
t=soln.t

# Plotting details
plt.plot(t, u, label='u')
# plt.plot(t,0.1*t)
# plt.plot(u_0_t, u_0, label='u0')

plt.legend()
plt.show()
