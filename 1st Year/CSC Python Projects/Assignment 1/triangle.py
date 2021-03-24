# Calculates the area of a triangle, the sides of which are given by the user 
# Miles Kidson KDSMIL001
# 25 February 2019

from math import sqrt

a = eval(input("Enter the length of the first side: "))     # Requests inputs for the 3 sides
b = eval(input("Enter the length of the second side: "))
c = eval(input("Enter the length of the third side: "))

s = (a+b+c)/2                                               # Calculates s

# Prints the area as long as the sides are all valid length, ie. not negative
if a < 0:
    print("a has an invalid length. Must be positive.")
elif b < 0:
    print("b has an invalid length. Must be positive.")
elif c < 0:
    print("c has an invalid length. Must be positive.")
else:
    print("The area of the triangle with sides of length ", a, " and ", b, " and ", c, " is ", sqrt(s*(s-a)*(s-b)*(s-c)), ".", sep=(""))