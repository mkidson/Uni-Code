def f(x):
    return x**3-10
x1 = 2
x2 = 4
x4 = abs(x1-x2)
count = 0
found = False
while x4 > 0.00001:
    count += 1
    x3 = (x2+x1)/2
    if f(x3) < 0:
        x1 = x3
    elif f(x3) > 0:
        x2 = x3
    elif f(x3) == 0:
        print(x3, count)
        found = True
        break
    x4 = abs(x1-x2)
if found == False:
    print(x3, count)