initialGuess = 2
def f(xn, xn2, count):
    count += 1
    xn2 = xn-((xn**3-10)/(3*xn**2))
    if (abs(xn - xn2)) < 0.00001:
        return xn2, count
    else:
        return f(xn2, xn, count)

print(f(initialGuess, initialGuess, 0))