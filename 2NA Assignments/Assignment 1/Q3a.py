initialGuess = 2
def f(xn, xn2, count):
    count += 1
    xn2 = xn-(((xn**4)-(10*xn))/((2*xn**3)+(10)))
    if (abs(xn - xn2)) < 1e-12:
        return xn2, count
    else:
        return f(xn2, xn, count)

print(f(initialGuess, initialGuess, 0))