#!python3
#emailer.py is a simple script for sending emails using smtplib

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from credentials import password

from_addr = 'jdbarks@gmail.com'
to_addr = 'jdbarks@gmail.com'
bcc = ['jdbarks@gmail.com', 'streakerv102@hotmail.com']

msg = MIMEMultipart()
msg['From'] = from_addr
msg['To'] = to_addr
msg['Subject'] = 'New Releases and Sales on Steam'

body = """New Releases and Sales on Steam
    
Click the links below to check them out!
   
"""

msg.attach(MIMEText(body, 'plain'))

smtp_server = smtplib.SMTP('smtp.gmail.com', 587)

smtp_server.ehlo()

smtp_server.starttls()

smtp_server.login(' jdbarks@gmail.com ', password)

text = msg.as_string()

smtp_server.sendmail(from_addr, [to_addr] + bcc, text)

smtp_server.quit()

print('Email sent successfully')
