from matplotlib import pyplot as plt
import numpy as np

x = [1.21, 2.04, 3.57]
xUn = [0.16, 0.10, 0.13]
y = [10.2, 15.3, 19.8]
yUn = [2.1, 3.2, 2.6]

plt.errorbar(x, y, yUn, xUn, 'rs', 'black', 0.5, capsize=3, label="PHY2004W Data", \
    markersize=5, capthick=0.5)

xDiff = np.arange(0.4, 5, 0.1)

plt.plot(xDiff, (0.5*xDiff)+14)

plt.show()