import requests
import json
import time

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

URL = "https://pravatey:f975494768@api.github.com"
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

Base.metadata.create_all(engine)

def add_user(user):
	keys = ["login", "avatar_url", "gravatar_id", "url", "html_url", "followers_url", "following_url", "gists_url", "starred_url", "subscriptions_url", "organizations_url", "repos_url", "events_url", "received_events_url", "type", "name", "company", "blog", "location", "email", "bio", "public_repos", "public_gists", "followers", "following", "created_at", "updated_at"]
	for k in keys:
		if k not in user:
			user[k] = None

	session = Session()
	if session.query(User).filter_by(name=user["login"]).first():
		print "user %s already in database!" % user["login"]
		pass
	else:
		new_user = User(
				login=user["login"], 
				avatar_url=user["avatar_url"], 
				gravatar_id=user["gravatar_id"], 
				url=user["url"], 
				html_url=user["html_url"], 
				followers_url=user["followers_url"], 
				following_url=user["following_url"], 
				gists_url=user["gists_url"], 
				starred_url=user["starred_url"], 
				subscriptions_url=user["subscriptions_url"], 
				organizations_url=user["organizations_url"], 
				repos_url=user["repos_url"], 
				events_url=user["events_url"], 
				received_events_url=user["received_events_url"], 
				type=user["type"], 
				name=user["name"], 
				company=user["company"], 
				blog=user["blog"], 
				location=user["location"], 
				email=user["email"], 
				bio=user["bio"], 
				public_repos=user["public_repos"], 
				public_gists=user["public_gists"], 
				followers=user["followers"], 
				following=user["following"], 
				created_at=user["created_at"], 
				updated_at=user["updated_at"], )
		session.add(new_user)
		session.commit()

#repos_fullname = "fanux/lhttp"
def get_user_info():
	headers = {"Accept":"application/vnd.github.v3+json"}
	for p in range(2000):
		response = re_session.get(URL + "/users" + "?page=%d&per_page=100" % p, headers=headers)
		users = json.loads(response.text)

		for u in users:
			user_str = re_session.get(URL + "/users/" + u["login"], headers=headers)
			user = json.loads(user_str.text)
			if user["email"] != "null" and user["email"] != None:
				try:
					add_user(user)
					time.sleep(0.73)
				except Exception, e:
					print "error ------"
					pass
	
get_user_info()
