import smtplib
import requests
import json

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

URL = "https://fanux:f******@api.github.com"
re_session = requests.session()

engine = create_engine('postgresql://postgres:111111@localhost/orm_test')
Session = sessionmaker(bind=engine)
Base = declarative_base()

class User(Base):
	__tablename__ = 'users'

	id = Column(Integer, primary_key=True)
	name = Column(String)
	email = Column(String)

Base.metadata.create_all(engine)

def add_user(user):
	session = Session()
	if session.query(User).filter_by(name=user["login"]).first():
		print "user %s already in database!" % user["login"]
		pass
	else:
		new_user = User(name=user["login"], email=user["email"])
		session.add(new_user)
		session.commit()

#repos_fullname = "fanux/lhttp"
def get_user_info_from_repos_stargazers(repos_fullname):
	u_list = []
	users = []
	headers = {"Accept":"application/vnd.github.v3+json"}
	for p in range(20):
		response = re_session.get(URL + "/repos/" + repos_fullname + "/stargazers?page=%d&per_page=100" % p, headers=headers)
		users = users + json.loads(response.text)

	for u in users:
		user_str = re_session.get(URL + "/users/" + u["login"], headers=headers)
		user = json.loads(user_str.text)
		if "email" in user and user["email"] != "null" and user["email"] != None:
			u_dict = {"login":user["login"], "email":user["email"]}
			u_list.append(u_dict)
	
	return u_list

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

def send_email(to_email):
	fromaddr = 'lamelegdog@gmail.com'
	msg = MIMEText(MSG, 'plain', 'utf-8')
	msg['From'] = Header('fanux', 'utf-8')
	msg['To'] = Header('Dear friend', 'utf-8')
	msg['Subject'] = Header('A good websocket framework', 'utf-8')
	username = 'lamelegdog@gmail.com'
	password = 'f*******'
	server = smtplib.SMTP('smtp.gmail.com:587')
	server.ehlo()
	server.starttls()
	server.login(username,password)
	server.sendmail(fromaddr, to_email, msg.as_string())
	server.quit()


#send_email('474785153@qq.com')
repos = ['gorilla/websocket']
#repos = ['fanux/user']

for repo in repos:
	u_list = get_user_info_from_repos_stargazers(repo)
	for u in u_list:
		add_user(u)
		send_email(u['email'])

#add_user({"login":"fanux", "email":"fhtjob@hotmail.com"})

"""
def printJson(s):
	b = json.loads(s)
	print json.dumps(b, indent=4)

def test_getUser(self):
	headers = {"Accept":"application/vnd.github.v3+json"}
	response = re_session.get(URL + "/users/fanux", headers=headers)

	self.printJson(response.text)

	response = re_session.get(URL + "/users/fanux/followers", headers=headers)

	self.printJson(response.text)
	self.printJson(response.text)
"""
