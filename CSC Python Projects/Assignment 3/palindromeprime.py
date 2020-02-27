# Computes all the palindromic primes between two integers supplied as input
# Miles Kidson
# 8 February 2019

start = int(input("Enter the start point N:\n")) # collects a start and end point for the loop
end = int(input("Enter the end point M:\n"))

print("The palindromic primes are:")

for num1 in range(start+1, end):            # iterates through the range given by the user, excluding the start and end points
    for num2 in range(2, num1):             # divides the current value for num1 by every integer before it
        if num1 % num2 == 0:                # if it is evenly divisible by anything apart from 1 and itself, break and move on to the next number in the range
            break
    else:                                   # if the number isn't divisible by anything before it, do this loop
        pal1 = str(num1)                    # creates a string out of the current num1, which will be prime
        pal2 = pal1[::-1]                   # creates another string which is pal1 in reverse
        if pal2 == pal1:                    # if the reverse of the first number is the same as the first number, print it out
            print(pal1)
            