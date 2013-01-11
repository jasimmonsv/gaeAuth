#!/usr/bin/python
'''
author: J.A. Simmons V (simmonsj@jasimmonsv.com)
date: 10 Jan 2013
Utilize the packaged user class and validate that the user has
been setup properly. Checks and balances
'''
import re
#from User import User #import base userclass

class authenticate(): 
	#this function will do all the checks for user info

	#ensure username is a string and nothing else
	def userTypeStr(self, username):
		return isinstance(username,str)

	def usernameLength(self, username):
		if (username <3) or (username >25):return False
		else: return True

	def valid_user(self, username):
		USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
		if username and USER_RE.match(username):return True
		else: return False

	def valid_password(password):
		PASS_RE = re.compile(r"^.{3,20}$")
		if password and PASS_RE.match(password): return True
		else:return False

	def valid_email(email):
		EMAIL_RE  = re.compile(r'^[\S]+@[\S]+\.[\S]+$')	
		if EMAIL_RE.match(email):return True
		else: return False

	def authUsername(self, username):
	#ensure username has no special characters
		self.userTypeStr(username)
		self.usernameLength(username)
		self.valid_user(username)
		return True