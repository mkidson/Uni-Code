import multiprocessing as mp
import numpy as np
import time

def randomSquare(seed):
    np.random.seed(seed)
    randNum=np.random.randint(0,10)
    return randNum**2

t0=time.time()
numCpu=mp.cpu_count()

pool=mp.Pool(processes=numCpu)
results=list(map(randomSquare, range(10000000)))
print(results)
t1=time.time()
print(f'This took {t1-t0}s')