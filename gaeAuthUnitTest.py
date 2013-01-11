#!/usr/bin/python

import unittest
from rkAuth import authenticate

'''
author: J.A. Simmons V (simmonsj@jasimmonsv.com)
date: 10 Jan 2012

'''

'''
Validate Username for user accounts
'''
class verifyUsernameTestCase(unittest.TestCase):

    userList = [('jsimmons',True),
                    ('ja',False),(1234,False),('1234',True),('ja$imm0ns',False),('jasimm0ns',True)
                    ]
    #def setup(self):
    a = authenticate()    
        
    '''
    verify username is valid
    '''
    def usernameIsValid(self):
        for i in range(len(self.userList)):
            self.assertTrue(self.a.authUsername(self.userList[i][0]), "Username is not a string")
            print i

    '''
    Username > 3 characters AND username < 25 characters
    '''
    def usernameLengthFail(self):
        for i in range(len(self.userList)):
            #TODO: check for expected results upon fail
            self.assertEqual(1, 1, "broken")

    '''
    username does not contain special characters
    '''
    def usernameSpecChar(self):
        pass
    
    def runTest(self):
        self.usernameIsValid()
        self.usernameLengthFail()
        self.usernameSpecChar()

'''
Validate passwords for user accounts
'''
class verifyPasswordTestCase(unittest.TestCase):
    
    def setup(self):
        return True
    
    '''
    Test Case
    Password is valid
    '''
    
'''
Validate emails for user accounts
'''

'''
Test Case - DB read - write
ensure user is created properly
catch db write errors

'''

if __name__ == '__main__':
    unittest.main()