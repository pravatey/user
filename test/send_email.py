'''
import smtplib
from email.mime.text import MIMEText
from email.header import Header

mail_host="smtp.live.com"
mail_user="fhtjob@hotmail.com"
mail_pass="f*********"

sender = 'fhtjob@hotmail.com'
receivers = ['474785153@qq.com', 'fhtjob@hotmail.com', 'haitao.fang@zasystem.com'] 

message = MIMEText('Python ', 'plain', 'utf-8')
message['From'] = Header("test", 'utf-8')
message['To'] =  Header("test2", 'utf-8')

subject = 'Python SMTP email test'
message['Subject'] = Header(subject, 'utf-8')


try:
	smtpObj = smtplib.SMTP()
	smtpObj.connect(mail_host, 25)
	smtpObj.login(mail_user, mail_pass)
	smtpObj.sendmail(sender, receivers, message.as_string())
except smtplib.SMTPException, e:
    print "Error:%s" % e
'''

import smtplib
fromaddr = 'lamelegdog@gmail.com'
toaddrs  = 'fhtjob@hotmail.com'
msg = 'Why,Oh why!'
username = 'lamelegdog@gmail.com'
password = 'f*********'
server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()
