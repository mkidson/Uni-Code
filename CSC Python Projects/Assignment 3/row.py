# User inputs a number and the program prints out 7 numbers starting from that number
# KDSMIL001
# 6 March 2019

start = eval(input("Enter the start number: "))
end = start + 7

if start > -6 and start < 93:
    for i in range(start, end):
        print("{:>2}".format(i), end='')
        if i < end-1:
            print(end=' ')
else:
    print("Number not between -6 and 93")