pascal=[[1],[1,1]]
even=0
odd=0
tot=0
for i in range(2,2001):
    print(i)
    x=[1]
    for j in range(1,i):
        x.append(pascal[i-1][j-1]+pascal[i-1][j])
    x.append(1)
    pascal.append(x)
    if i%1000==0:
        for p in pascal:
            if p==[0]:
                pass
            else:
                tot+=len(p)
                for c in p:
                    if c%2==0:
                        even+=1
                    else:
                        odd+=1
        pascal[:i-2]=[0]*(i-2)
        

print(tot)
print(even)
print(odd)
print(odd/tot)
# print(pascal)