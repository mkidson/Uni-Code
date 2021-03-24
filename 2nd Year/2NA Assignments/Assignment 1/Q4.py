from math import sqrt
def g1(x):
    return x**2-2
def g2(x):
    return sqrt(x+2)
def g3(x):
    return 2/(x-1)
def g4(x):
    return (2/x)+1
def FPI(g, startX):
    diff = abs(g(startX)-startX)
    xNew = g(startX)
    count = 0
    while diff > 1e-12 and count < 100:
        xNew = g(xNew)
        diff = abs(g(xNew)-xNew)
        count += 1
    if count == 100:
        return "Could not converge"
    else:
        return xNew, count
print(FPI(g1, 1.5))
print(FPI(g2, 1.5))
print(FPI(g3, 1.5))
print(FPI(g4, 1.5))