# calculates a pythagorean triplet such that a+b+c = 1000 and then finds the product abc
# Miles Kidson
# 05-05-19

from math import sqrt

a = 1
b = 1

for i in range(1000):
    for c in range(1000):
        c = sqrt(a**2 + b**2)
        if a + b + c == 1000:
            print(a*b*c)
        else:
            b += 1
    else:
        b = 1
        a += 1