from urllib.request import urlopen, Request
from bs4 import BeautifulSoup as soup
import json
from io import StringIO
import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import requests
import string

# Retrieves the webpage, needs to be a request instead of a string because some websites don't like being scraped

def getText():

    latinText = ''
    engText = ''

    for r in range(1,9):
        req = requests.get(f'https://www.sacred-texts.com/cla/jcsr/dbg{r}.htm')
        pageSoup = soup(req.content, "html.parser")

        trs = pageSoup.findAll('tr')

        eng = []
        latin = []

        for i in trs:

            tds = i.findAll('td')

            eng.append(tds[0].text)
            latin.append(tds[1].text)



        for c in latin:
            latinStripped = c.translate(str.maketrans('', '', string.punctuation+' '+'\n'))
            latinText = latinText + latinStripped.lower()

        for c in eng:
            engStripped = c.translate(str.maketrans('', '', string.punctuation+' '+'\n'))
            engText = engText + engStripped.lower()

    latinFile = open('latinText.txt', 'w')
    latinFile.write(latinText)
    latinFile.close()

    engFile = open('engText.txt', 'w')
    engFile.write(engText)
    engFile.close()


def analyseText(filename):
    vowels = ['a', 'e', 'i', 'o', 'u']
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    textFile = open(filename, 'r')
    tex = textFile.readline()

    vowNum = 0
    consNum = 0
    for x in tex:
        if x in vowels:
            vowNum += 1
        elif x in consonants:
            consNum += 1
        elif x in num:
            pass
    
    return vowNum, consNum

# getText()

latVow, latCons = analyseText('latinText.txt')
engVow, engCons = analyseText('engText.txt')

print(latVow/latCons)
print(engVow/engCons)