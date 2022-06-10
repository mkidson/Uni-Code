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
