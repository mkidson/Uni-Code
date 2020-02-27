# Prints out 3 different triangles depending on user input
# Miles Kidson
# 27-02-19



height = int(input("How high: "))
t_type = input("What type of tringle would you like? (l, c, or r): ")

if t_type == "l":
    for row in range(height):
        for stars in range(row+1):
            print("*", end="")
        print()