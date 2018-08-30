#!python3
#emailer.py is a simple script for sending emails using smtplib

import smtplib

from credentials import password

from_addr = 'jdbarks@gmail.com'
to_addr = 'jdbarks@gmail.com'

body = """New Releases and Sales on Steam
    
Click the links below to check them out!
   
"""

smtp_server = smtplib.SMTP('smtp.gmail.com', 587)

smtp_server.ehlo()

smtp_server.starttls()

smtp_server.login(' jdbarks@gmail.com ', password)

smtp_server.sendmail(from_addr, to_addr, body)

smtp_server.quit()

print('Email sent successfully')
