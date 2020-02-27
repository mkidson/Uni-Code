import smtplib, ssl
import json
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

port = 465
senderEmail = "miles.dev.email@gmail.com"
receiverEmail = "miles.kidson@gmail.com"

with open('data.JSON', 'r') as fileRead:
    data = json.load(fileRead)

msg = MIMEMultipart('alternative')

message = '<html><body>'

for i in data:
    print(i['name'])
    
    message += """<img class='image' size src={}>\n<h1>{}</h1>\n<h2>{}</h2>\n<h3>{}</h3>\n<h3>{}</h3>\n""".format(i['image link'], i['name'], i['price'], i['description'], i['link'])
    # print(message)

message += '</body></html>'

part1 = MIMEText(message, 'html')
msg.attach(part1)

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(senderEmail, 'KnEffKMI63Uu')
    server.sendmail(senderEmail, receiverEmail, msg.as_string())
