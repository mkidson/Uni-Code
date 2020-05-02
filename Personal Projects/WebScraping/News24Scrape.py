from urllib.request import urlopen, Request
from bs4 import BeautifulSoup as soup
import json
from io import StringIO
import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Retrieves the webpage, needs to be a request instead of a string because some websites don't like being scraped
req = Request("https://www.news24.com/", headers={'User-Agent': 'Mozilla/5.0'})
uClient = urlopen(req)
pageHTML = uClient.read()
uClient.close()
pageSoup = soup(pageHTML, "html.parser")

mainWrap = pageSoup.find('div', 'main_wrap')
mainPanel = mainWrap.find('div', 'grid_8')
panel4s = mainPanel.findAll('div', 'grid_4')


print(len(panel4s))
print(panel4s[1].prettify())