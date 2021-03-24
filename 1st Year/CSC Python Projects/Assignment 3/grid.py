# User inputs a number and the program outputs a grid of rows 7 numbers across from n to n+41
# KDSMIL001
# 11 March 2019

n = eval(input("Enter the start number: "))

      
if n > -6 and n < 2:
    for i in range(6):
        for c in range(n, n+7):
            print("{:>2}".format(c), end='')
            if (c - n + 1) % 7 != 0:
                print(end=' ')
        n += 7
        print()
else:
    print("Number not in range")