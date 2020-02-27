primes = []


num = 3

while num < 600851475143:
    for i in range(2,num):
        if (num % i) == 0:
            break
        else:
            primes.append(num)

print(primes)
