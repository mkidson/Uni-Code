# finds all the palindromic primes between two bounds
# KDSMIL001
# 20 April 2019

import sys
sys.setrecursionlimit (300000)


def is_pal(sentence):
    sentence = str(sentence)
    
    if len(sentence) == 1 or len(sentence) == 0:
        return True

    if sentence[0] != sentence[-1]:
        return False

    elif is_pal(sentence[1:-1]):
        return True
    
    else:
        return False


def is_prime2(n):
    return is_prime(n, n//2)

def is_prime(number, n):
    
    if n == 1 or n == 0:
        return True

    if number % n != 0:
        if is_prime(number, n=n-1):
            return number

def set_range(start, end):

    if start == end+1:
        return True

    if is_prime2(start):
        if is_pal(start):
            print(start)
            set_range(start+1, end)
        else:
            set_range(start+1, end)
    else:
        set_range(start+1, end)



def main():

    
    x = eval(input("Enter the starting point N:\n"))
    y = eval(input("Enter the ending point M:\n"))

    print("The palindromic primes are:")
    set_range(x, y)


if __name__ == '__main__':
    main()