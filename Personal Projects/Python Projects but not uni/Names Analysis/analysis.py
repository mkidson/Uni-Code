import json

names=json.load(open(r'Personal Projects\Python Projects but not uni\Names Analysis\names.JSON','r'))

namesTally={}
surnamesTally={}

for name in names:
    if name['name'][0] in namesTally:
        namesTally[name['name'][0]]+=1
    else:
        namesTally[name['name'][0]]=1
    
    if name['surname'] in surnamesTally:
        surnamesTally[name['surname']]+=1
    else:
        surnamesTally[name['surname']]=1

namesRanked={}
surnamesRanked={}

for n in sorted(namesTally.items(),key=lambda x: x[1],reverse=True):
    namesRanked[n[0]]=n[1]
    
for s in sorted(surnamesTally.items(),key=lambda x: x[1],reverse=True):
    surnamesRanked[s[0]]=s[1]

with open(r'Personal Projects\Python Projects but not uni\Names Analysis\namesRanked.JSON', 'w') as writeFile:
    json.dump(namesRanked, writeFile, indent=4)

with open(r'Personal Projects\Python Projects but not uni\Names Analysis\surnamesRanked.JSON', 'w') as writeFile:
    json.dump(surnamesRanked, writeFile, indent=4)

# dic={'name': 4,'matt': 5}

# print(dic)