import requests

# url = "http://192.144.148.91:2333/login"
# data = {"username":"liuyun1", "password":"a12345678"}
# method = 'post'
# headers = {"Content-Type":"application/json"}
# res = requests.request(method, url=url, json=data, headers=headers)
# print(res.text)

# url = "http://192.144.148.91:2333/get_title_img"
# res = requests.request('get', url=url)
# print(res.text)
# print(res.status_code)

from tools.requeststools import request1
from tools.dbtools import shujuku

url = "http://192.144.148.91:2333/get_title_img"
r = request1('get', url, {}, {}, 200, 200)
print(r)

r = request1('get',url)
print(r)