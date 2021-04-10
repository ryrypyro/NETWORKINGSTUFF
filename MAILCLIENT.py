import smtplib # protocol sending mail 

import smtplib
from email.message import EmailMessage

msg = EmailMessage()

body = "TEST TEST TEST."
subject = "YALLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL WASSUHHHHHHHHHH"

msg.set_content(body)
msg['Subject'] = 'Haji'
msg['From'] = 'test-m405tlqgj@srv1.mail-tester.com' # used https://www.mail-tester.com/
msg['To'] = 'mailclient'

server = smtplib.SMTP_SSL('smtp.gmail.com', 465) # default port ssl (?)
server.login('test@gmail.com', 'password')
server.send_message(msg)
server.close()
print("mail sent.")

# THINK OF YOUR OWN PW / EMAIL 


