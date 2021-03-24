from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from scipy.integrate import odeint
from numpy import cos, pi, sin, sqrt, exp, random
import matplotlib as mpl
import random
#matplotlib.use('pgf')
mpl.rcParams.update({
    'pgf.texsystem': 'pdflatex',
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
    'legend.fontsize': 10
})
# Constants
a=0.1
# bs=np
bs=np.linspace(0.01,4,200)
# bs=[4,6,8.5,9,12,18]
# bs=[0.01]
tmodel=np.linspace(0,30,1000)
# Generating random ICs, each with x,y,z between 0 and 1
ICs=[]
eigReal1=[]
eigImag1=[]
eigReal2=[]
eigImag2=[]
for p in range(5):
    ICs.append([random.random(),random.random(),random.random()])
for b in bs:
    # Fixed Points
    FP1=[(b+np.lib.scimath.sqrt(b**2-4*a**2))/(2),-(b+np.lib.scimath.sqrt(b**2-4*a**2))/(2*a),(b+np.lib.scimath.sqrt(b**2-4*a**2))/(2*a)]
    FP2=[(b-np.lib.scimath.sqrt(b**2-4*a**2))/(2),-(b-np.lib.scimath.sqrt(b**2-4*a**2))/(2*a),(b-np.lib.scimath.sqrt(b**2-4*a**2))/(2*a)]
    # Eigenvalue calculations
    jacobian1=np.array([[0,-1,-1],[1,a,0],[FP1[2],0,FP1[0]-b]])
    jacobian2=np.array([[0,-1,-1],[1,a,0],[FP2[2],0,FP2[0]-b]])
    eigenvalues1, eigenvector1=np.linalg.eig(jacobian1)
    eigenvalues2, eigenvector2=np.linalg.eig(jacobian2)
    eigReal1.append(np.real(eigenvalues1))
    eigImag1.append(np.imag(eigenvalues1))
    eigReal2.append(np.real(eigenvalues2))
    eigImag2.append(np.imag(eigenvalues2))

# Setting up the 3d axes
fig = plt.figure()
ax = fig.gca(projection='3d')

# Plotting each soln
ax.plot(eigReal1, eigImag1, bs, linewidth=1,label='FP1')
# ax.plot(eigReal2, eigImag2, bs, linewidth=1,label='FP2')
# Just some more plotting things
# ax.scatter([],[],[],c='black',label='Initial Conditions')
ax.set_xlabel('Real')
ax.set_ylabel('Imaginary')
ax.set_zlabel('b')
ax.legend()
plt.show()