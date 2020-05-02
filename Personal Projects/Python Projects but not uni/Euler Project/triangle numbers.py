# finds the first triangle number with over 500 divisors
# Miles Kidson
# 10-05-19
from math import sqrt
from multiprocessing import Process
import numpy as np 


def tr_div(n):
    case = True
    count = 1
    num = 0

    while case:
        final = []
        num += count
        count += 1
        if num < 2000:
            print(num)
            
        if count >= 1000:
            num2 = round(sqrt(num))
            for i in range(1, num2):
                if num % i == 0:
                    final.append(i)
                    final.append(num/i)
                    
            final.sort()
            
            if count % 5000 == 0:
                print(num)
                print(final)
                print(len(final))
            

            if len(final) > n:
                case = False
        
        else: 
            continue

    print("The number is:", num, "\nCount is:", count, "\nFinal is:", final, "\nFinal len is:", len(final))

    # a = [num, count, final, len(final)]
    # f = open("triangle_num.txt", "w+")
    # for i in range(len(a)):
    #     f.writelines(a[i])
    # f.close()

if __name__ == "__main__":
    p = Process(target=tr_div, args=(500,))
    p.start()
    p.join()


# 275274209056