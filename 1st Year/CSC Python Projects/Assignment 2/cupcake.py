# Goes through a flow chart to determine whether you should eat the food you just dropped
# KDSMIL001
# 28-02-19


print('Welcome to the 30 Second Rule Expert')
print('------------------------------------')
print('Answer the following questions by selecting from among the options.')

r = input('Did anyone see you? (yes/no)\n')

if r == 'no':
    r = input('Was it sticky? (yes/no)\n')
    if r == 'no':
        r = input('Is it an Emausaurus? (yes/no)\n')
        if r == 'no':
            r = input('Did the cat lick it? (yes/no)\n')
            if r == 'no':
                decision = 'Eat it.'
            else:
                r = input('Is your cat healthy? (yes/no)\n')
                if r == 'no':
                    decision = 'Your call.'
                else:
                    decision = 'Eat it.'
        else:
            r = input('Are you a Megalosaurus? (yes/no)\n')
            if r == 'no':
                decision = "Don't eat it."
            else:
                decision = 'Eat it.'
    else:
        r = input('Is it a raw steak? (yes/no)\n')
        if r == 'no':
            r = input('Did the cat lick it? (yes/no)\n')
            if r == 'no':
                decision = 'Eat it.'
            else:
                r = input('Is your cat healthy? (yes/no)\n')
                if r == 'no':
                    decision = 'Your call.'
                else:
                    decision = 'Eat it.'
        else:
            r = input('Are you a puma? (yes/no)\n')
            if r == 'no':
                decision = "Don't eat it."
            else:
                decision = 'Eat it.'
else:
    r = input('Was it a boss/lover/parent? (yes/no)\n')
    if r == 'no':
        decision = 'Eat it.'
    else:
        r = input('Was it expensive? (yes/no)\n')
        if r == 'no':
            r = input('Is it chocolate? (yes/no)\n')
            if r == 'no':
                decision="Don't eat it."
            else:
                decision = 'Eat it.'
        else:
            r = input('Can you cut off the part that touched the floor? (yes/no)\n')
            if r == 'no':
                decision = 'Your call.'
            else:
                decision = 'Eat it.'

print('Decision:', decision)