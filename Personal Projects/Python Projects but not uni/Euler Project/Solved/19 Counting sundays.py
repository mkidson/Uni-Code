# Counts the number of sundays that land on the first day of the month from 1901 to 2000
# 13-07-2020

def isLeapYear(year): 
    # returns True if the given year is a leap year
    # only works between 1900 and 2000
    if year%4 == 0 and year != 1900:
        return True
    else: return False

def setSundays(start): 
    # returns an array of the days in the year that are sundays. i think
    final = []
    temp = 0-start
    for i in range(52):
        temp += 7
        final.append(temp)
    return final

# The first days of each month, depending on leap year-osity
leapYearFirstDays = [1,32,61,92,122,153,183,214,245,275,306,336]
notLeapYearFirstDays = [1,32,60,91,121,152,182,213,244,274,305,335]
leapYear = 366
year = 365
# Sunday is day 0
startDay = (1+365)%7
numSundays = 0

for i in range(1901, 2001):
    if isLeapYear(i):
        sunDays = setSundays(startDay)
        for c in sunDays:
            if c in leapYearFirstDays:
                numSundays += 1
        startDay = (startDay+leapYear)%7
    else:
        sunDays = setSundays(startDay)
        for p in sunDays:
            if p in notLeapYearFirstDays:
                numSundays += 1
        startDay = (startDay+year)%7

print(numSundays)