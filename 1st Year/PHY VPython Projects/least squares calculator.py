from math import sqrt

count = eval(input("count:"))
print()

xs = []
ys = []
sumx = 0
sumy = 0
sumxy = 0
sumx2 = 0

ds = []
sumd2 = 0
d = 0


for i in range(count):
    x = eval(input("x:"))
    y = eval(input("y:"))
    xs.append(x)
    ys.append(y)

print()

for c in range(count):
    sumx += xs[c]
    sumy += ys[c]
    sumxy += xs[c]*ys[c]
    sumx2 += xs[c]**2


print(sumx, sumy, sumxy, sumx2)
print()

m = round(((count*sumxy) - (sumx*sumy)) / ((count*sumx2) - (sumx)**2), 3)
c = round(((sumx2*sumy) - (sumxy*sumx)) / ((count*sumx2) - (sumx)**2), 3)


for n in range(count):
    ds.append(ys[n] - ((m*xs[n]) + c))
    sumd2 += ds[n]**2
    print("for x =", n, ": mx + c =", round((m * xs[n]) + c, 3))
    print("for x =", n, ": d =", round((ds[n]), 3))
    print("for x =", n, ": d^2 =", round((ds[n]**2), 3))
    print()

print("\nsumd^2 =", round((sumd2), 4))
print()

um = round(sqrt((sumd2 / ((count * sumx2) - (sumx)**2) * (count / (count - 2)))), 4)
uc = round(sqrt((sumd2 * sumx2) / (count * ((count * sumx2) - (sumx)**2) * (count / (count - 2)))), 4)

print("m = {}\nc = {}\nu(m) = {}\nu(c) = {}".format(m, c, um, uc))
print()
print("y = {}x + {}".format(m, c))
print()