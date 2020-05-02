# Finds sum of all even fibonacci numbers between 0 and 4000000


# Sets fib_tot to 0
fib_tot = 0
fib = 1
fib2 = 2
# While fib and fib2 are smaller than 4000000
while fib < 4000000 and fib2 < 4000000:
    # If fib and fib2 are even numbers
    if fib % 2 == 0:
        print(fib)
        fib_tot += fib
    if fib2 % 2 == 0:
        print(fib2)
        fib_tot += fib2
         # Print both fib and fib2 and add them to fib_tot
    fib += fib2
    fib2 += fib
    # Sets fib and fib2 to next two fibonacci numbers

print(fib_tot)
# Prints fib_tot


# really nicely creates an array of fibonacci numbers
fib = []
fib1 = 1
fib2 = 1
while fib1 < 365435296162:
    fib1 += fib2
    fib2 += fib1
    fib.append(fib1)
    fib.append(fib2)