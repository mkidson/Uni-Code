# Plots a graph on a -10:10 graph
# KDSMIL001
# 2 April 2019
import math

line = input("Enter a function f(x):\n")

line_new = line.replace("x", "{}")


for i in range(10, -11, -1):
    for c in range(-10, 11):
        if round(eval(line_new.format("(c)"))) == i:
            print("*", end='')
        elif i == 0:
            if c != 0:
                print("-", end='')
            else:
                print("+", end='')
        elif c != 0:
            print(" ", end='')
        else:
            print("|", end='')
    print()
        