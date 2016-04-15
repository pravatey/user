import requests
import json
import time

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

URL = "https://pravatey:*********8@api.github.com"
re_session = requests.session()

engine = create_engine('postgresql://postgres:111111@localhost/orm_test')
Session = sessionmaker(bind=engine)
Base = declarative_base()

class User(Base):
	__tablename__ = 'user_info'

	id = Column(Integer, primary_key=True)
	login = Column(String)
	avatar_url = Column(String)
	gravatar_id = Column(String)
	url = Column(String)
	html_url = Column(String)
	followers_url = Column(String)
	following_url = Column(String)
	gists_url = Column(String)
	starred_url = Column(String)
	subscriptions_url = Column(String)
	organizations_url = Column(String)
	repos_url = Column(String)
	events_url = Column(String)
	received_events_url = Column(String)
	type = Column(String)
	name = Column(String)
	company = Column(String)
	blog = Column(String)
	location = Column(String)
	email = Column(String)
	bio = Column(String)
	public_repos = Integer()
	public_gists = Integer()
	followers = Integer()
	following = Integer()
	created_at = Column(String)
	updated_at = Column(String)

MSG = """Dear friend,
	I am steven, a coder in China, I am honoured to introduce a websocket framwork for you. 
https://github.com/fanux/lhttp , you can build a IM application very quickly with lhttp. 
Lhttp is fast, support cluster, easy to customize etc,. 
It not only websocket framework but also a btter way to create long live application.
	Hope you like it, sorry about to disturb you.

Regards,
Steven.
"""
from email.mime.text import MIMEText
from email.header import Header
import smtplib

def send_email():
	fromaddr = 'lamelegdog@gmail.com'
	msg = MIMEText(MSG, 'plain', 'utf-8')
	msg['From'] = Header('fanux', 'utf-8')
	msg['To'] = Header('Dear friend', 'utf-8')
	msg['Subject'] = Header('A good websocket framework', 'utf-8')
	username = 'lamelegdog@gmail.com'
	password = 'f975494768'
	server = smtplib.SMTP('smtp.gmail.com:587')
	server.ehlo()
	server.starttls()
	server.login(username,password)
	page = 0

	count = 0

	log = open('log', 'w')

	session = Session()
	for page in range(2000):
		emails = session.query(User.email)[page * 100:page * 100 + 100]
		for to_email in emails:
			try:
				count = count + 1
				log.write("to_email:%s %d \r\n" % (to_email[0],count))
				server.sendmail(fromaddr, to_email[0], msg.as_string())
			except Exception, e:
				print "error"
				pass

	server.quit()

send_email()


