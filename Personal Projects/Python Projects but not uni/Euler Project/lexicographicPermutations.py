# finds the millionth  number in the lexicographic permutation of 0 - 9
# Miles Kidson
# 22-10-19

str = '0123456789'
strList = list(str)
arr = []
temp = ''

for x in range(10):

    for i in range(10):
    
        for c in range(9):
            arr.append("".join(strList))
            temp = strList[c]
            strList[c] = strList[c+1]
            strList[c+1] = temp
    
    

print(len(arr))