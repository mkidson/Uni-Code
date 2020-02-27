# Displays a conversion table between inches and metres in a range of values
# KDSMIL001
# 13 March 2019

mini = eval(input("Enter the minimum number of inches (not less than 0):\n"))
maxi = eval(input("Enter the maximum number of inches (not greater than 11):\n"))

if mini >= 0 and maxi <= 11:
    print("Inches:", end='')
    for i in range(mini, maxi+1):
        print("{:>5}".format(i), end='')
    print("\nMetres:", end='')
    for c in range(mini, maxi+1):
        print("{:>5.2f}".format(c/39.3701, 2), end='')