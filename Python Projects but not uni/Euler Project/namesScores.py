# calculates the alphabetical score of all the names in a list
# Miles Kidson
# 21-10-19

def calcScore1(string):
    tot = 0
    for c in string:
        tot += (ord(c) - 64)
    
    # print(tot)
    return tot

file = open("Python Projects but not uni\\Euler Project\\names.txt", "r")

for line in file:
    lines = line.split(',')

for i in lines:
    lines[lines.index(i)] = i.strip('"')
    # print(i)

lines.sort()
# print(lines)
print(lines.index("COLIN"))
print(calcScore1(lines[937]))

linesScores = []
for i in lines:
    # print(i)
    linesScores.append(calcScore1(i) * (lines.index(i) + 1))
    # print(linesDict.index(i))

# print(linesDict.keys()[937])


sum = 0
count = 0

for i in linesScores:
    count += 1
    if i == 49714:
        print(count)
    sum += i

print(sum)

file.close()