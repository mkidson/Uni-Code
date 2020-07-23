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

def print_factors(x):
   # This function takes a number and prints the factors

   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)