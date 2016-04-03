import unittest

import requests
import json

URL = "http://localhost:8080"
session = requests.session()

class UserTest(unittest.TestCase):
	def printJson(self, s):
		b = json.loads(s)
		print json.dumps(b, indent=4)

	def setUp(self):
		pass

	def tearDown(self):
		session.close()

	def test_createUser(self):
		data = {
				"account":"fanux",
				"passwd":"123456",
				"email":"fhtjob@hotmail.com",
				"phone":"15805691422",
				"portrait":"https://avatars3.githubusercontent.com/u/8912557?v=3&u=c1d9c4e6eb1ba6c52732b377269903818f665cff&s=140"
		}
		headers = {"content-type":"application/json"}
		response = session.post(URL + "/users", headers=headers, data=json.dumps(data))
		self.printJson(response.text)

if __name__ == '__main__':
	unittest.main()
