import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

mail_content = 'Default message'
#The mail addresses and password
sender_address = os.getenv('email_mail') #Email environment variable

sender_pass = os.getenv('email_password') #Sender email environment password
receiver_address = 'lmc00@alumnos.unican.es'
#Setup the MIME
message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = 'Just testing the cool email sending script'   #The subject line
#The body and the attachments for the mail
message.attach(MIMEText(mail_content, 'plain'))
#Create SMTP session for sending the mail

session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port You need to reduct security on gmail. Just create a new mail for this task or host your own SMTP Server
session.starttls() #enable security
session.login(sender_address, sender_pass) #login with mail_id and password
text = message.as_string()
session.sendmail(sender_address, receiver_address, text)
session.quit()
print('Mail Sent')