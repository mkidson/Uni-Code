# a module of functions I use a lot

def is_prime(a):
    num = a
    num2 = num//2
    if num % 2 == 0:
        return False
    for i in range(3, num2, 2):
        if num % i == 0:
            return False
        else:
            continue
    else:
        
        return True