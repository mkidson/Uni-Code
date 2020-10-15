pascal=[[1],[1,1]]
for i in range(2,128):
    print(i)
    x=[1]
    for j in range(1,i):
        x.append(pascal[i-1][j-1]+pascal[i-1][j])
    x.append(1)
    print(len(x))
    pascal.append(x)
    # print(pascal)

even=0
odd=0
tot=0
for p in pascal:
    tot+=len(p)
    for c in p:
        if c%2==0:
            even+=1
        else:
            odd+=1
print(tot)
print(even)
print(odd)
print(odd/tot)