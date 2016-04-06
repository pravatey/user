import unittest

import requests
import json

URL = "https://api.github.com"
session = requests.session()

class UserTest(unittest.TestCase):
	def printJson(self, s):
		b = json.loads(s)
		print json.dumps(b, indent=4)

	def setUp(self):
		pass

	def tearDown(self):
		session.close()

	def test_getUser(self):
		headers = {"Accept":"application/vnd.github.v3+json"}
		response = session.get(URL + "/users/limengwei", headers=headers)

		self.printJson(response.text)

if __name__ == '__main__':
	unittest.main()
