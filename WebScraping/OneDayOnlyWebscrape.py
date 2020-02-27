from urllib.request import urlopen, Request
from bs4 import BeautifulSoup as soup
import json
from io import StringIO
import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Retrieves the webpage, needs to be a request instead of a string because some websites don't like being scraped
req = Request("https://www.onedayonly.co.za",
              headers={'User-Agent': 'Mozilla/5.0'})
uClient = urlopen(req)
pageHTML = uClient.read()
uClient.close()
pageSoup = soup(pageHTML, "html.parser")

home = pageSoup.find(id="home")

objects = home.findAll('div', recursive=False)

products = []

for i in objects:
    # Error handling for an out of bounds error for some reason
    try:
        # Some of the blocks are containers for many products, so I needed to go into those blocks to handle it
        if i.attrs['class'][1] == 'shop_block':

            temps = i.findAll('div', 'block_wrapper')
            for c in temps[1:]:
                products.append(c.find('a', 'new_product_block'))
        
        else:
            products.append(i.find('a', 'new_product_block'))

    except IndexError as e:
        pass

finalProducts = []

# Assigns the various details I want to a 4 item dictionary, which then gets put in a master array
for product in products:

    try:
        finalProducts.append({
            'name': product.find('h2', 'shortname').string,
            'description': product.find('p', 'name').string,
            'link': product.attrs['href'],
            'price': product.find('h3', 'selling').string,
            'image link': product.img.attrs['src']
        })
    except AttributeError as e:
        pass



# Writes the contents of the master array to a JSON file using the json.dump method
with open('data.JSON', 'w') as writeFile:
    json.dump(finalProducts, writeFile, indent=4)

port = 465
senderEmail = "miles.dev.email@gmail.com"
receiverEmail = "miles.kidson@gmail.com"

with open('data.JSON', 'r') as fileRead:
    data = json.load(fileRead)

msg = MIMEMultipart('alternative')
msg['From'] = 'Miles Dev'
msg['Subject'] = 'One Day Only Deals'

message = '<html><body>'

for i in data:    
    message += """<img class='image' size src={}>\n<h1>{}</h1>\n<h2>{}</h2>\n<h3>{}</h3>\n<h3>{}</h3>\n""".format(i['image link'], i['name'], i['price'], i['description'], i['link'])

message += '</body></html>'

# Formats the string into an html format that the smtp client can send the email as
part1 = MIMEText(message, 'html')
msg.attach(part1)

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(senderEmail, 'KnEffKMI63Uu')
    server.sendmail(senderEmail, receiverEmail, msg.as_string())
