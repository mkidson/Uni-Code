# Does basic vector calculations in 3 dimensions
# KDSMIL001
# 5 April 2019

import math

def vector_add(a, b):
    c = []
    c.append(a[0] + b[0])
    c.append(a[1] + b[1])
    c.append(a[2] + b[2])
    
    return c

def vector_dot(a, b):
    c = a[0]*b[0]+a[1]*b[1]+a[2]*b[2]
    
    return c

def vector_norm(a):
    c = math.sqrt(a[0]**2+a[1]**2+a[2]**2)

    return c

def main():
    a = []
    b = []

    a = input("Enter vector A:\n").split()
    b = input("Enter vector B:\n").split()

    for i in range(3):
        a[i] = eval(a[i])
        b[i] = eval(b[i])

    
    print("A+B = {}".format(vector_add(a, b)))
    print("A.B = {}".format(vector_dot(a, b)))
    print("|A| = {:.2f}".format(vector_norm(a)))
    print("|B| = {:.2f}".format(vector_norm(b)))


if __name__ == '__main__':
    main()