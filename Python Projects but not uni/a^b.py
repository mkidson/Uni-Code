a = float(input("Enter the base: "))
b = int(input("Enter the exponent: "))

if b < 0:
    print("nuh, uh!")
else:    
    ans = 1
    for i in range (1, b+1):
        ans *= a
    print(a, "**", b, "=", ans)