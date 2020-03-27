def f(x):
    return x**3-10
x1 = 2
x2 = 4
x4 = abs(x1-x2)*0.5
count = 0
found = False
while x4 > 1e-12:
    count += 1
    x3 = (x2+x1)/2
    x5 = f(x3)*f(x1)
    if x5 > 0:
        x1 = x3
    elif x5 < 0:
        x2 = x3
    elif x5 == 0:
        print(x3, count)
        found = True
        break
    x4 = abs(x1-x2)*0.5
if found == False:
    print(x3, count)