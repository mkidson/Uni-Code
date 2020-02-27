# calculates the number of possible paths from top left to bottom right on a 20x20 grid
# Miles Kidson
# 27 June 2019

import numpy


grid = numpy.zeros((20, 20))

grid[0,0] = 1
grid[19,19] = 1

print(grid)

case = True

while case:
    pass