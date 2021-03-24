# generates a personal spam message
# Miles Kidson KDSMIL001
# 25 February 2019


# Requests values for name, amount of money, country.
first_name = input("Enter first name:\n")
last_name = input("Enter last name:\n")
money = eval(input("Enter sum of money in USD:\n"))
country = input("Enter country name:\n")
money30 = money * (30/100)      # Calculates 30% of the total money

# Prints it al out. sep=("") is used to make sure there is no separator, making formatting easier.
print("\nDearest ", first_name, sep=(""))
print("It is with a heavy heart that I inform you of the death of my father,", sep=(""))
print("General Fayk ", last_name, ", your long lost relative from Mapsfostol.", sep=(""))
print("My father left the sum of ", money, "USD for us, your distant cousins.", sep=(""))
print("Unfortunately, we cannot access the money as it is in a bank in ", country, ".", sep=(""))
print("I desperately need your assistance to access this money.", sep=(""))
print("I will even pay you generously, 30% of the amount - ", money30, "USD,", sep=(""))
print("for your help.  Please get in touch with me at this email address asap.", sep=(""))
print("Yours sincerely", sep=(""))
print("Frank ", last_name, sep=(""))