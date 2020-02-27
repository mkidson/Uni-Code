# Module containing some functions
# KDSMIL001
# 25 March 2019

def is_leap_year(year):
    if (( year%400 == 0) or (( year%4 == 0 ) and ( year%100 != 0))):
        return True
    else:
        return False

def month_name(n):
    if n == 1:
        return "January"
    elif n == 2:
        return "February"
    elif n == 3:
        return "March"
    elif n == 4:
        return "April"
    elif n == 5:
        return "May"
    elif n == 6:
        return "June"
    elif n == 7:
        return "July"
    elif n == 8:
        return "August"
    elif n == 9:
        return "September"
    elif n == 10:
        return "October"
    elif n == 11:
        return "November"
    elif n == 12:
        return "December"

def days_in_month(month_number, year):
    if month_number == 1 or month_number == 3 or month_number == 5 or month_number == 7 or month_number == 8 or month_number == 10 or month_number == 12:
        return 31
    elif month_number == 4 or month_number == 6 or month_number == 9 or month_number == 11:
        return 30
    elif month_number == 2:
        if is_leap_year(year) == True:
            return 29
        else:
            return 28
      
def first_day_of_year(year):
    day = 5*((year-1) % 4)
    day = day + (4*((year-1) % 100))
    day = day + (6*((year-1) % 400))
    day = (day + 1) % 7
    if day == 0:
        return 0
    elif day == 1:
        return 1
    elif day == 2:
        return 2
    elif day == 3:
        return 3
    elif day == 4:
        return 4
    elif day == 5:
        return 5
    elif day == 6:
        return 6

def first_day_of_month(month, year):
    day = 0
    if month == 1:
        days = 0
    elif month == 2:
        days = 31
    elif month == 3:
        days = 31+28
    elif month == 4:
        days = 31+28+31
    elif month == 5:
        days = 31+28+31+30
    elif month == 6:
        days = 31+28+31+30+31
    elif month == 7:
        days = 31+28+31+30+31+30
    elif month == 8:
        days = 31+28+31+30+31+30+31
    elif month == 9:
        days = 31+28+31+30+31+30+31+31
    elif month == 10:
        days = 31+28+31+30+31+30+31+31+30
    elif month == 11:
        days = 31+28+31+30+31+30+31+31+30+31
    elif month == 12:
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
        return 0
    elif (day+days) % 7 == 1:
        return 1
    elif (day+days) % 7 == 2:
        return 2
    elif (day+days) % 7 == 3:
        return 3
    elif (day+days) % 7 == 4:
        return 4
    elif (day+days) % 7 == 5:
        return 5
    elif (day+days) % 7 == 6:
        return 6

