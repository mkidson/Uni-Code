# Displays a conversion table for feet and inches to metres in a range
# KDSMIL001
# 13 March 2019

minf = eval(input("Enter the minimum number of feet (not less than 0):\n"))
maxf = eval(input("Enter the maximum number of feet (not more than 30):\n"))


if minf >= 0 and maxf <=30:
    print("\n      |   0\"   1\"   2\"   3\"   4\"   5\"   6\"   7\"   8\"   9\"  10\"  11\"")
    for i in range(minf, maxf+1):
        print("{:>4}' |".format(i), end='')
        for c in range(0, 12):
            print("{:5.2f}".format(round(i/3.2808,4)+round(c/39.370,4)), end='')
        print()