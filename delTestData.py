import requests


class DelTestData:
    def __init__(self):
        self.ip = 'http://api.pre.mars-tech.com.cn'
        self.headers = {'os': '1', "Content-Type": "application/json; charset=UTF-8"}
        path = '/api/v2/pwdLogin'
        data = {"username": "18217484395", "password": "123456"}
        r = requests.post(url=self.ip + path, headers=self.headers, json=data)
        self.token = r.json()['data']['token']

    def del_test_data(self):
        pass
