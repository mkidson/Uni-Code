# calculates the number of letters used when counting from 1 to 1000
# Miles Kidson
# 28 June 2019


numberNames = {0:"", 1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine", 10:"ten", 11:"eleven", 12:"twelve", 13:"thirteen", 14:"fourteen", 15:"fifteen", 16:"sixteen", 17:"seventeen", 18:"eighteen", 19:"nineteen"}
tensNames = {0:"", 1:"ten", 2:"twenty", 3:"thirty", 4:"forty", 5:"fifty", 6:"sixty", 7:"seventy", 8:"eighty", 9:"ninety"}


print(numberNames[2])

total = 0

for i in range(1001):
    stringI = str(i)

    if len(stringI) == 1:
        numberName = numberNames[i]
        print(numberName)
        total += len(numberName)
        print(total)
    
    elif len(stringI) == 2:
        if stringI[0] == "1":
            numberName = numberNames[int(stringI)]
            print(numberName)
            total += len(numberName)

        else:
            numberName = tensNames[int(stringI[0])] + numberNames[int(stringI[1])]
            print(numberName)
            total += len(numberName)

    elif len(stringI) == 3:
        if stringI[1:] == "00":
            numberName = numberNames[int(stringI[0])] + "hundred"
            print(numberName)
            total += len(numberName)

        elif stringI[1] == "1":
            numberName = numberNames[int(stringI[0])] + "hundredand" + numberNames[int(stringI[1:])]
            print(numberName)
            total += len(numberName)

        else:
            numberName2 = numberNames[int(stringI[0])] + "hundredand" + tensNames[int(stringI[1])] + numberNames[int(stringI[2])]
            print(numberName2)
            total += len(numberName2)
    
    elif len(stringI) == 4:
        numberName3 = "onethousand"
        print(numberName3)
        total += len(numberName3)
    

print(total)
