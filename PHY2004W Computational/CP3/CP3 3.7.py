from matplotlib import pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import matplotlib
matplotlib.use('pgf')
matplotlib.rcParams.update({
    'pgf.texsystem': 'pdflatex',
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
})
# Defines a few starting conditions, constants, and arrays we will need later on
deltat = 0.01
omega0 = 5
TotalT = 10
N = int(TotalT/deltat+1.5)
NL = 100
L = np.linspace(1, 100, NL)
p = np.zeros((NL, N))
q = np.zeros((NL, N))
E = np.zeros((NL, N))
T = np.zeros(NL)
TSmallAngles = np.zeros(NL)
yfit = np.zeros((NL, N))
omega = np.zeros(NL)
q[:, 0] = 90*np.pi/180 # Our initial condition of theta at 90 degrees to the vertical
p[:, 0] = 0            # Another initial condition that says we start from rest
p0 = [1, 0, 1, 1]
def f(t, A, gamma, omega, alpha):   # The function that curve_fit will use later on
    return A*np.exp(-1*gamma*t/2)*np.cos(omega*t-alpha)
# The Loop. Does all the calculations of theta and omega for each time step and then does it again for different omegas
for j in range(NL):
    time = np.zeros(N)
    omega[j] = np.sqrt(9.8/L[j])
    for i in range(N-1):
        time[i+1] = (i+1)*deltat
        p[j, i+1] = p[j, i] - (omega[j]**2)*np.sin(q[j, i])*deltat
        q[j, i+1] = q[j, i] + p[j, i+1]*deltat
    popt, pcov = curve_fit(f, time, q[j], p0, maxfev=5000)
    T[j] = abs(2*np.pi/popt[2])
    TSmallAngles[j] = 2*np.pi/omega[j]
# Plots the two calculated periods per length
plt.plot(L, T, 'b-', label='Observed Period')
plt.plot(L, TSmallAngles, 'r-', label='Small Angle Approximation Prediction')
plt.xlabel('Length (m)')
plt.ylabel('Period T (s)')
plt.legend()
# Saves the plots to a pgf for inclusion in the report
plt.savefig('PHY2004W Computational\CP3\CP3c 90.pgf')