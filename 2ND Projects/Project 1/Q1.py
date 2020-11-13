from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from scipy.integrate import odeint
from numpy import cos, pi, sin, sqrt, exp, random
import matplotlib as mpl
# mpl.use('pgf')
mpl.rcParams.update({
    'pgf.texsystem': 'pdflatex',
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
    'legend.fontsize': 10
})

a=8
ICs=[0.3,0.3]
tmodel=np.linspace(0,20,1000)

def system(f, t):
    x,y=f
    dfdt=[-y,x+a*y]
    return dfdt
soln=odeint(system, ICs, tmodel)

fig = plt.figure()
x=[]
y=[]
for i in soln:
    x.append(i[0])
    y.append(i[1])

plt.scatter(ICs[0],ICs[1],c='b')
dot = plt.scatter([],[],c='b',label='Initial Condition')
plt.grid(color='#CCCCCC', linestyle=':')
plt.plot(x,y,c='b',linewidth='1')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.show()
# plt.savefig(r'2ND Projects\Project 1\Q1.pgf')