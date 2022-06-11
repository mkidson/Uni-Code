def dumbRejectionMethod(N, probDist, yMin=0.0, yMax=1.0):
    # Realised my method above works for reasonably good rejection rates only, with a bad one it can't handle the entire arrays in memory
    yRange = np.linspace(yMin, yMax, 2000)
    zMax = np.max(probDist(yRange))

    n = 0
    accepted = []
    while n < N:
        zRand = random.uniform(0, zMax)
        yRand = random.uniform(yMin, yMax)

        if zRand < probDist(yRand):
            accepted.append(yRand)
            n += 1
    
    return np.array(accepted)


def regulaFalsi(x1, x2, func, rootVal=0.0, tol=0.01, printIntermediate=True):
    """Returns the root of the function `func` that lies between `x1` and `x2`
    
        Args
        ----
            x1 (float):
        Leftmost inital guess
    
            x2 (float):
        Rightmost inital guess
    
            func (function):
        The function which calls the method to interpolate the data in `xs` and `ys`, at some point `x`. Needs to be of the form `func(x, xs, ys)`

            rootVal (float, optional): 
        Value of the function f(x) for which to find the corresponding x. Defaults to 0.
    
            tol (float, optional):
        The tolerance to which the root-finding method must reach before exiting and outputting the x-value at the root. Should be less than 1. Defaults to `0.01`

            printIntermediate (bool, optional):
        Tells the function whether it should print out the step number, x-value, and y-value at each step. Defaults to `True`

        Returns
        -------
            x0 (float):
        The x-value for the root of the function `func` in the interval [`x1`, `x2`]
    """
    y1 = func(x1)
    y2 = func(x2)
    
    x0 = x1 + (rootVal - y1) * ((x2 - x1) / (y2 - y1))      # Using the formula for linear interpolation with y(x) = 0 to find x
    y0 = func(x0)
    
    i = 0
    while np.abs(y0) >= tol:
        i += 1
        if y0 * y1 < 0:     # Checking if y0 and y1 are on opposite sides of the root, and if so setting y2 to y0
            y2 = y0
            x2 = x0
        elif y0 * y2 < 0:   # Same here
            y1 = y0
            x1 = x0
            
        x0 = x1 + (rootVal - y1) * ((x2 - x1) / (y2 - y1))      # Sets new x0 value as above
        y0 = func(x0)
        
        if printIntermediate:
            print(f'step {i}')
            print(f'x: {x0:.5}')
            print(f'y: {y0:.5}')
            print('---')
    
    return x0
