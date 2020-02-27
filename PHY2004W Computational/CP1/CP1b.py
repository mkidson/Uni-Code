from matplotlib import pyplot as plt
import matplotlib
matplotlib.use("pgf")
matplotlib.rcParams.update({
    "pgf.texsystem": "pdflatex",
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
})
import numpy

x = [1.21, 2.04, 3.57]
xUn = [0.16, 0.10, 0.13]
y = [10.2, 15.3, 19.8]
yUn = [2.1, 3.2, 2.6]

N = 3

plt.errorbar(x, y, yUn, xUn, 'rs', 'black', 0.5, capsize=3, label="PHY2004W Data", \
    markersize=5, capthick=0.5)

plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.title("Comparison of Experimental Data with Theoretical Prediction")

plt.xlim(0,5)
plt.ylim(0,30)

xy = []
for c in range(N):
    xy.append(round(x[c]*y[c], 3))

x2 = []
for t in range(N):
    x2.append(round(x[t]**2, 3))

m = ((N*sum(xy)) - sum(x)*sum(y))/((N*sum(x2))-(sum(x))**2)
c = ((sum(x2)*sum(y))-(sum(xy)*sum(x)))/((N*sum(x2))-(sum(x)**2))

xLine = numpy.arange(0.5, 4, 0.1)
yLine = []
for i in xLine:
    yLine.append((m*i)+c)

plt.plot(xLine, yLine, color='blue', label="Line of Best Fit")

plt.legend(numpoints=2)
plt.savefig('CP1b Plot.pgf')

