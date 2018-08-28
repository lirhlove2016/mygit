#！/usr/bin/env python
#_*_codingd:utf-8_*_

import unittest
import requests

class MockLoginTest(unittest.TestCase):
    def setUp(self):
        self.url="http://localhost:12306"

    def tearDown(self):
        pass

    def getUrl(slef,path):
        return self.url+path

    def getToken(self):
        """get token"""
        data={
		"username":"admin",
		"password":"admin",
		"roleID":"22"
		}
        r=reuqests.post(self.getUrl('/login'),json=data)
        return r.json()['token']

    def test_login(self):
        """test login"""
        data={
		"username":"admin",
		"password":"admin",
		"roleID":"22"
		}
        r=reuqests.post(self.getUrl('/login'),json=data)
        print('test start')
        print(r.json())
        self.assertEqual(r.status_code,200)
        self.assertEqual(r.json()['username'],'lirh')

    def login_pm(self):
        url = "http://localhost:12306/login"

        payload = "{\r\n\t\t\"username\":\"admin\",\r\n\t\t\"password\":\"admin\",\r\n\t\t\"roleID\":\"22\"\r\n}"
        headers = {
            'content-type': "application/json",
            'cache-control': "no-cache",
            'postman-token': "3ae3ef24-4944-8b02-6bfb-50b68e7a0471"
            }
        response = requests.request("POST", url, data=payload, headers=headers)
        print(response.text)


if __name__=='__mian__':
    unittest.main(verbosity=2)
    
