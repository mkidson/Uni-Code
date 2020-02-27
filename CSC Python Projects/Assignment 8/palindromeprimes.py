import sys
sys.setrecursionlimit (30000)

def isprime2 (n, a):
    if a == 1 or a == 0:
        return True
    elif n % a == 0:
        return False
    else:
        return isprime2 (n, a-1)

def isprime (n):
    return isprime2 (n, n//2)

def palin2 (n, m):
    if n == 0:
        return m
    else:
        return palin2 (n // 10, (m * 10) + n % 10)

def palin (n):
    return palin2 (n, 0)

def print_palinprimes (n, m):
    if n <= m:
        if palin(n) == n and isprime (n):
            print (n)
        print_palinprimes (n+1, m)    

n = int (input ("Enter the starting point N:\n"))
m = int (input ("Enter the ending point M:\n"))
print ("The palindromic primes are:")
print_palinprimes (n, m)