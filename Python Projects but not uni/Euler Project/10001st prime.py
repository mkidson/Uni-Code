# Finds the 10 001st prime number
# Miles Kidson
# 6 April 2019

def is_prime(a):

    num = a
    for i in range(2, num):
        if num % i == 0:
            return False
        else:
            continue
    else:
        return True


def main():

    i = 2
    primes = []

    while len(primes) <= 10000:
        if is_prime(i):
            primes.append(i)
        i += 1

    print(primes)
    print(primes[-1])


if __name__ == '__main__':
    main()