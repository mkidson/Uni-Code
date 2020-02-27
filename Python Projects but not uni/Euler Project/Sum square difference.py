# Finds the difference between the sum of the squares of the first 100 natural numbers and the square of the sum
# Miles Kidson
# 6 April 2019

def make_100():

    a = []

    for i in range(1, 101):
        a.append(i)

    return a

def sum_squares():
    
    a = make_100()
    b = 0

    for i in a:
        b += i**2
    
    return b

def square_sum():

    a = make_100()
    b = 0

    for i in a:
        b += i
    
    b = b**2

    return b

def find_dif(a, b):

    c = a - b

    return c

def main():

    print(find_dif(square_sum(), sum_squares()))


if __name__ == '__main__':
    main()