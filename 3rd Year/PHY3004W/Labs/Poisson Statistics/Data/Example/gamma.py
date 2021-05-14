from matplotlib import pyplot as plt
import numpy as np
from scipy.special import gamma
from numpy import cos, pi, sin, sqrt, exp, random
import matplotlib
# matplotlib.use('pgf')
matplotlib.rcParams.update({
    'pgf.texsystem': 'pdflatex',
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
})

xs=np.linspace(0,10,1000)

def poisson(x, mu):
    return ((mu**x)/(gamma(x+1)))*exp(-mu)

plt.plot(xs, poisson(xs, 1.5))
plt.xlabel('x')
plt.ylabel('Probability')
plt.show()