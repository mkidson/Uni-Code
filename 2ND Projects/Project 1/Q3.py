from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from scipy.integrate import odeint
from numpy import cos, pi, sin, sqrt, exp, random
import matplotlib as mpl
import random
# mpl.use('pgf')
mpl.rcParams.update({
    'pgf.texsystem': 'pdflatex',
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
    'legend.fontsize': 10
})
# Constants
a=0.1
# a=8
# bs=[0.01,0.02,0.1,0.2,1,2,10,20]
# bs=np.arange(0.001,0.01,0.001)
# bs=[4,6,8.5,9,12,18]
bs=[0.2]
tmodel=np.linspace(0,30,1000)
# Generating random ICs, each with x,y,z between 0 and 1
ICs=[]
for p in range(5):
    # ICs.append([random.uniform(-1,1),random.uniform(-1,1),random.uniform(-1,1)])
    ICs.append([random.random(),random.random(),random.random()])
for b in bs:
    # Fixed Points
    FP1=[(b+np.lib.scimath.sqrt(b**2-4*a**2))/(2),-(b+np.lib.scimath.sqrt(b**2-4*a**2))/(2*a),(b+np.lib.scimath.sqrt(b**2-4*a**2))/(2*a)]
    FP2=[(b-np.lib.scimath.sqrt(b**2-4*a**2))/(2),-(b-np.lib.scimath.sqrt(b**2-4*a**2))/(2*a),(b-np.lib.scimath.sqrt(b**2-4*a**2))/(2*a)]
    print(FP1, FP2)
    # ICs.append(FP1)
    # ICs.append(FP2)
    # Eigenvalue calculations
    jacobian1=np.array([[0,-1,-1],[1,a,0],[FP1[2],0,FP1[0]-b]])
    jacobian2=np.array([[0,-1,-1],[1,a,0],[FP2[2],0,FP2[0]-b]])
    eigenvalues1, eigenvector1=np.linalg.eig(jacobian1)
    eigenvalues2, eigenvector2=np.linalg.eig(jacobian2)
    det1=np.linalg.det(jacobian1)
    det2=np.linalg.det(jacobian2)
    trace1=np.trace(jacobian1)
    trace2=np.trace(jacobian2)
    print('b is:',b)
    print('The eigenvalues for the first FP are:', eigenvalues1)
    # print('Its trace has sign:',np.sign(trace1))
    # print('And its determinant has sign:',np.sign(det1))
    print('The eigenvalues for the second FP are:', eigenvalues2)
    # print('Its trace has sign:',np.sign(trace2))
    # print('And its determinant has sign:',np.sign(det2))
    print()

    # Setting up the 3d axes
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    # The function to give to odeint
    def system(f, t, b):
        x,y,z=f
        dfdt=[-y-z,x+a*y,a-b*z+x*z]
        return dfdt
    # Calculating for each IC
    for c in ICs:
        # Solving using odeint
        soln=odeint(system, c, tmodel, args=(b,))
        # Plotting the IC
        ax.scatter(c[0],c[1],c[2])
        # Getting the solution into a form we can plot, odeint doesn't spit the results out nicely
        x=[]
        y=[]
        z=[]
        for i in soln:
            x.append(i[0])
            y.append(i[1])
            z.append(i[2])
        # Plotting each soln
        ax.plot(x, y, z, linewidth=1)
    # Just some more plotting things
    ax.scatter([],[],[],c='black',label='Initial Conditions')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    # ax.set_title('b='+str(b))
    ax.legend()
    # plt.savefig(r'2ND Projects\Project 1\Report\Plots\Q3_'+str(b)+'.pgf')
plt.show()