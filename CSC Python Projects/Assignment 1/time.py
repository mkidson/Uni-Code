# Checks the validity of a time entered by a user
# Miles Kidson KDSMIL001
# 25 February 2019

# User inputs their numbers for hours, minutes, seconds and eval converts them into floats or integers
hours = eval(input("Enter the hours: "))
minutes = eval(input("Enter the minutes: "))
seconds = eval(input("Enter the seconds: "))


if hours > 24 or hours < 0:
    print("Your time is invalid.")       # Checks that hours is between 0 and 24 (inclusive) and prints "Your time is invalid" if it isn't, if hours is valid, it continues.
elif minutes > 60 or minutes < 0:
    print("Your time is invalid.")       # Does the same for minutes and seconds
elif seconds > 60 or seconds < 0:
    print("Your time is invalid.")
else:
    print("Your time is valid.")         # If all 3 are true, it prints "Your time is valid"