# Displays a conversion table for measurements in feet to metres in a range
# KDSMIL001
# 13 March 2019

minf = eval(input("Enter the minimum number of feet (not less than 0):\n"))
maxf = eval(input("Enter the maximum number of feet (not more than 99):\n"))

if minf >= 0 and maxf <= 99:
    for i in range(minf, maxf+1):
        print("{:>4}' |{:>7.2f}m".format(i, i/3.28, 2))
else:
    print("Not in range")