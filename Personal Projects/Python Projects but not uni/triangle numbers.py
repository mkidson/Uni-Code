# finds the first triangle number with over 500 divisors
# Miles Kidson
# 10-05-19
from math import sqrt
from multiprocessing import Process

def tr_div(n):
    case = True
    count = 1
    num = 1

    while case:
        final = []
        num += count
        count += 1
        num2 = round(sqrt(num))
        for i in range(1, num2):
            if num % i == 0:
                final.append(i)
                final.append(num/i)

        if count % 10000 == 0:
            print(num)
            print(final)
            print(len(final))
        

        if len(final) > n:
            case = False

    print("The number is:", num)


if __name__ == "__main__":
    p = Process(target=tr_div, args=(500,))
    p.start()
    p.join()