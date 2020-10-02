from bs4 import BeautifulSoup as soup
import json
import codecs

file=codecs.open(r'Personal Projects\Python Projects but not uni\Names Analysis\studentNames.html','r',encoding='utf-8')
pageHTML=file.read()
pageSoup = soup(pageHTML, "html.parser")

tbody=pageSoup.find(id='roster_form:rosterTable:tbody_element')
objects=tbody.findAll('tr',recursive=False)

names=[]

for o in objects:
    i=o.find('a')
    name=i.text
    try:
        nameStripped=name.split(', ')
        names.append({
            'name': nameStripped[1].lower().split(),
            'surname': nameStripped[0].lower()
        })
    except IndexError as identifier:
        pass

with open(r'Personal Projects\Python Projects but not uni\Names Analysis\names.JSON', 'w') as writeFile:
    json.dump(names, writeFile, indent=4)

print(len(names))
