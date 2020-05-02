
def Third_Upper(a):
    count=0
    for i in a:
        count+=1
        if count%3==0:
            i=i.upper()
        print(i, end='')

Third_Upper("hellothere")


