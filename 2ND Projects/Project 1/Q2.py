from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from scipy.integrate import odeint
from numpy import cos, pi, sin, sqrt, exp, random
import matplotlib as mpl
mpl.use('pgf')
mpl.rcParams.update({
    'pgf.texsystem': 'pdflatex',
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
    'legend.fontsize': 10
})
# Constants etc
a=0.1
bs=[0.01, 0.1, 1, 10]
tmodel=np.linspace(0,20,1000)
# Generating random ICs, each with x,y,z between 0 and 1
ICs=[]
for p in range(5):
    ICs.append([random.uniform(-1,1),random.uniform(-1,1),random.uniform(-1,1)])

for b in bs:
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    def system(f, t, b):
        x,y,z=f
        dfdt=[-y,x+a*y,a-b*z]
        return dfdt
    for c in ICs:
        soln=odeint(system, c, tmodel, args=(b,))

        ax.scatter(c[0],c[1],c[2])
        x=[]
        y=[]
        z=[]
        for i in soln:
            x.append(i[0])
            y.append(i[1])
            z.append(i[2])
        ax.plot(x, y, z,linewidth=1)
    ax.scatter([],[],[],c='black',label='Initial Conditions')
    ax.legend()
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    # ax.set_title('b='+str(b))
    plt.savefig(r'2ND Projects\Project 1\Report\Plots\Q2_'+str(b)+'.pgf')
# plt.show()