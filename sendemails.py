import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

with open('password.txt', 'r') as f:
    password=f.read()

print(password)
server.login('exampleFrom@gmail.com', password)

msg=MIMEMultipart()
msg['From']='TestFromPython'
msg['To']='exampleTo@gmail.com'
msg['Subject']='Just A test'

with open('message.txt', 'r') as f:
    message=f.read()

msg.attach(MIMEText(message, 'plain'))

filename='picture.jpg'

with open(filename, 'rb') as z:
    attachment=z.read()

p=MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attachment; filename={filename}')
msg.attach(p)

text=msg.as_string()
server.sendmail('exampleFrom@gmail.com', 'exampleTo@gmail.com', text)
server.quit()
