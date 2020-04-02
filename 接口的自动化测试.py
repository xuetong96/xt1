'''
使用postman 里面的 code 复制代码啊啊啊啊
'''

import requests

url = "http://192.144.148.91:2333/login"

payload = "{\r\n\"username\":\"langjin\",\r\n\"password\":\"lj123456\" \r\n}\r\n"
headers = {
    'Content-Type': "application/json",
    'cache-control': "no-cache",
    'Postman-Token': "8ba99fdf-180f-4964-88b3-c585c321143f"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)