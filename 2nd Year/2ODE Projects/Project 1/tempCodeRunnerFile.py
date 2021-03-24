maxY = []
for i in Vs:
    maxY.append(max(abs(Y(i, t))))

maxMaxY = max(maxY)
print(maxMaxY, Vs[maxY.index(maxMaxY)])

plt.plot(Vs, maxY)