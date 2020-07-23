# Finds the fib no with 1000 digits

fib1 = 1
fib2 = 1
count = 0

while len(str(fib1)) < 1000:
    count += 2
    fib1 += fib2
    fib2 += fib1

print(count)