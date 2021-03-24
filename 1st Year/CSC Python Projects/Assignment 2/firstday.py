# Calculates the day that January 1st falls on for a range of years specified by the user
# KDSMIL001
# 28-02-19


a = int(input("Enter the first year:\n"))       # receives start and end years
b = int(input("Enter the second year:\n"))


day = 0

for i in range(a,b+1):                          # iterates through a range starting at the first year and ending at the last, assigning i to the year currently being checked
    day = 5*((i-1) % 4)                         # computes the day, outputted as a number from 0 to 6
    day = day + (4*((i-1) % 100))
    day = day + (6*((i-1) % 400))
    day = (day + 1) % 7
    if day == 0:
        print("The 1st of January", i, "falls on a Sunday.")    # if day is found to be 0, it prints out that it was a sunday. similarly for 1, 2, 3.
    elif day == 1:
        print("The 1st of January", i, "falls on a Monday.")
    elif day == 2:
        print("The 1st of January", i, "falls on a Tuesday.")
    elif day == 3:
        print("The 1st of January", i, "falls on a Wednesday.")
    elif day == 4:
        print("The 1st of January", i, "falls on a Thursday.")
    elif day == 5:
        print("The 1st of January", i, "falls on a Friday.")
    elif day == 6:
        print("The 1st of January", i, "falls on a Saturday.")
 