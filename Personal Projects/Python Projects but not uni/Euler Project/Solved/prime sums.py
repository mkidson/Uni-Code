# finds the sum of all primes from 2 to 2 million
# Miles Kidson
# 05-05-19

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

n = 3
sum = 2
while n < 2000000:
    if is_prime(n):
        print(n)
        sum += n
    
    if n % 20000 == 0:
        print("We are {}{} of the way there.".format((2000000/n)/100, '%'))
    
    n += 2

print(sum)