# User inputs a number and the program prints out every 7th number in the range n+41
# KDSMIL001
# 11 March 2019

n = eval(input("Enter a number: "))

if n > -6 and n < 2:
    for i in range(n, n+41, 7):
        print("{:>2}".format(i))
else:
    print("Number not in range")