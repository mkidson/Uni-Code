# User enters a month and a year and the program prints out the first day
# KDSMIL001
# 13 March 2019

month = input("Enter the month: ")
year = eval(input("Enter the year: "))
day = 0

if month == "January":
    days = 0
elif month == "February":
    days = 31
elif month == "March":
    days = 31+28
elif month == "April":
    days = 31+28+31
elif month == "May":
    days = 31+28+31+30
elif month == "June":
    days = 31+28+31+30+31
elif month == "July":
    days = 31+28+31+30+31+30
elif month == "August":
    days = 31+28+31+30+31+30+31
elif month == "September":
    days = 31+28+31+30+31+30+31+31
elif month == "October":
    days = 31+28+31+30+31+30+31+31+30
elif month == "November":
    days = 31+28+31+30+31+30+31+31+30+31
elif month == "December":
    days = 31+28+31+30+31+30+31+31+30+31+30


if year % 4 == 0 and days > 32:
    if year % 100 == 0:
        if year % 400 == 0:
            days += 1



day = 5*((year-1) % 4)
day = day + (4*((year-1) % 100))
day = day + (6*((year-1) % 400))
day = (day + 1) % 7
if (day+days) % 7 == 0:
    print("The 1st of {} {} is a Sunday.".format(month, year))
elif (day+days) % 7 == 1:
    print("The 1st of {} {} is a Monday.".format(month, year))
elif (day+days) % 7 == 2:
    print("The 1st of {} {} is a Tuesday.".format(month, year))
elif (day+days) % 7 == 3:
    print("The 1st of {} {} is a Wednesday.".format(month, year))
elif (day+days) % 7 == 4:
    print("The 1st of {} {} is a Thursday.".format(month, year))
elif (day+days) % 7 == 5:
    print("The 1st of {} {} is a Friday.".format(month, year))
elif (day+days) % 7 == 6:
    print("The 1st of {} {} is a Saturday.".format(month, year))
