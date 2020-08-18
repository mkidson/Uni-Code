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
# Defines a few starting conditions and constants we will need later on
deltat = 0.01       # The time step
omega0 = 5          # The angular frequency
T = 10
N = int(T/deltat+1.5)
time = np.zeros(N)
p = np.zeros(N)
q = np.zeros(N)
E = np.zeros(N)
q[0] = 10*np.pi/180 # Our initial condition of omega at 10 degrees to the vertical
p[0] = 0            # Another initial condition that says we start from rest
E[0] = 0.5*p[0]**2 + 9.8*(1-np.cos(q[0])) # The loop will start assigning from 1
# The Loop. Does all the calculations of theta and omega for each time step
for i in range(N-1):
    time[i+1] = (i+1)*deltat
    p[i+1] = p[i] - (omega0**2)*np.sin(q[i])*deltat
    q[i+1] = q[i] + p[i]*deltat
    E[i+1] = 0.5*p[i]**2 + 9.8*(1-np.cos(q[i]))
# Plots the value of theta, omega, the phase plot, and the energy respectively
plt.subplot(221)
plt.plot(time, q, 'b-')
plt.xlabel('time (s)')
plt.ylabel('angle (rad)')
plt.title('$\\theta$')
plt.subplot(222)
plt.plot(time, p, 'b-')
plt.xlabel('time (s)')
plt.ylabel('angle (rad)')
plt.title('$\omega$')
plt.subplot(223)
plt.plot(q, p, 'b-')
plt.xlabel('angle (rad)')
plt.ylabel('angular velocity ($\\frac{rad}{s}$)')
plt.title('phase plot')
plt.subplot(224)
plt.plot(time, E, 'b-')
plt.xlabel('time (s)')
plt.ylabel('energy (J)')
plt.title('energy')
plt.tight_layout(pad=0.8)
# Saves the plots to a pgf for inclusion in the report
plt.savefig('PHY2004W Computational\CP3\CP3 10.pgf')