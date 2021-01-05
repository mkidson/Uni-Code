

file=open(r'Personal Projects\Python Projects but not uni\Euler Project\pokerHands.txt','r')
lines=file.readlines()

player1=[]
player2=[]

for line in lines:
    lineArr=line.split()
    player1.append(lineArr[0:5])
    player2.append(lineArr[5:10])

player1Hand=[]
player2Hand=[]
temp=''

for i in player1:
    temp=''
    for c in i:
        c.split('')
    # 