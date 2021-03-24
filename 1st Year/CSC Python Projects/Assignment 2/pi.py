# Computes pi and then displays the area of a circle with radius entered by the user
# KDSMIL001
# 28-02-19

from math import sqrt

pi = 1
i = 2
j = sqrt(2)

while i != 1:
    pi *= i
    i = 2/j
    j = sqrt(2+j)
    
print("Approximation of pi:", round(pi, 3))

r = eval(input("Enter the radius:\n"))

area = pi*(r**2)

print("Area:", round(area, 3))