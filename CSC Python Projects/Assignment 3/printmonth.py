# User inputs a month and start day and the program prints out a grid 7 wide, 6 tall, for that month's days
# KDSMIL001
# 11 March 2019

month = input("Enter the month ('January', ..., 'December'): ")
start = input("Enter the start day ('Monday', ..., 'Sunday'): ")

if month == "January":
    days = 31
elif month == "February":
    days = 28
elif month == "March":
    days = 31
elif month == "April":
    days = 30
elif month == "May":
    days = 31
elif month == "June":
    days = 30
elif month == "July":
    days = 31
elif month == "August":
    days = 31
elif month == "September":
    days = 30
elif month == "October":
    days = 31
elif month == "November":
    days = 30
elif month == "December":
    days = 31
    
if start == "Monday":
    n = 1
elif start == "Tuesday":
    n = 0
elif start == "Wednesday":
    n = -1
elif start == "Thursday":
    n = -2
elif start == "Friday":
    n = -3
elif start == "Saturday":
    n = -4
elif start == "Sunday":
    n = -5

print(month)
print("Mo Tu We Th Fr Sa Su")

for i in range(6):
    for c in range(n, n+7):
        if c < 1:
            print("{:>2}".format(' '), end='')
        else:
            print("{:>2}".format(c), end='')
        if (c - n + 1) % 7 != 0:
            print(end=' ')
        if c == days:
            break        
    n += 7
    print()
    if c == days:
        break