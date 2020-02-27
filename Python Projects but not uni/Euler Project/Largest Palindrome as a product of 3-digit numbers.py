# Computes the largest palindrome which is a product of two 3-digit numbers
# Miles Kidson
# 06-03-19

num1 = range(999,99,-1)                 # creates a list of numbers starting from 999, ending at 100, in descending order
finals = []                             # creates an empty list which is populated in line 15 by all the palindromes we find
number1 = []                            # creates two more empty lists which are populated in line 16 and 17 which hold the two factors of the palindrome
number2 = []

for i in range(0,len(num1)):            # loops through the range of num1
    for c in range(0,len(num1)):        # loops through the range of num2
        pal1 = str(num1[i]*num1[c])     # creates a string which is the two numbers multiplied together
        pal2 = pal1[::-1]               # creates another string which is the pal1 in reverse
        if pal2 == pal1:                # if the reverse of the first number is the same as the first number, continue, else start again
            finals.append(int(pal1))    # saves the palindrome created to a list of all the palindromes created
            number1.append(num1[i])     # saves the two numbers used to create the palindrome to 2 lists, where their position will be the same as the palindrome
            number2.append(num1[c])

                                                             # largest # in list of all palindromes                # the factors of that palindrome
print("The largest palindrome as a product of two 3-digit numbers is", max(finals), "and the 3-digit numbers are", number1[finals.index(max(finals))], "and", number2[finals.index(max(finals))])