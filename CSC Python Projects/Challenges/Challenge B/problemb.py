S = ''
final = []

while S != '#':
    S = input()
    if S == 'HELLO':
        final.append('ENGLISH')
    elif S == 'HALLO':
        final.append('AFRIKAANS')
    elif S == 'BONJOUR':
        final.append('FRENCH')
    elif S == 'MOLO':
        final.append('ISIXHOSA')
    elif S == 'SAWUBONA':
        final.append('ISIZULU')
    elif S == 'MARHABA':
        final.append('ARABIC')
    else:
        final.append('UNKNOWN')

for i in range(len(final)-1):
    print(final[i])
