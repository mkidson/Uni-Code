# finds the largest prime factor of a given number
# Miles Kidson
# 02-03-19

# step 1. define an array of prime numbers smaller than 600851475143
# step 2. iterate through the array, dividing by each number until it is no longer perfectly divisible by it
# step 3. each time one divides evenly, append it to a new array called prime_factors and then check if all the values in that array multiply to 600851475143
# step 4. if they do, break and print the final value of the set

import numpy

num = eval(input("Enter the number: "))
numcpy = num
primes = []
prime_factors = []



for num1 in range(2,num+2):
    for num2 in range(2,num1):
        if num1 % num2 == 0:
            break
    else:
        while numcpy % num1 == 0:
            prime_factors.append(num1)
            numcpy /= num1
            print(num1)
            print(numcpy)
            print(prime_factors)
            if numcpy == 1:
                print("The largest prime factor of", int(num), "is:", prime_factors[len(prime_factors)-1])
                