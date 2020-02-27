

cases = int(input())
inputs = []

if cases < 100:
    for i in range(cases):
        inputs.append(int(input()),int(input()),int(input()))
        #L = int(input())
        #W = int(input())
        #H = int(input())
        #inputs.append(L)
        #inputs.append(W)
        #inputs.append(H)
    
for c in range(0, cases):
    if inputs[c*3] > 50 or inputs[(c*3)+1] > 50 or inputs[(c*3)+2] > 50:
        print("Case {}: bad".format(c+1), sep='')
    else:
        print("Case {}: good".format(c+1), sep='')


#else:
    #print("Too many cases")