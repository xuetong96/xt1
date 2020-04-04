'''
1、自动化测试是什么？
    UI自动化测试：
    接口自动化测试：
'''
'''
def __init__  :成员变量
.text : 打印返回值
.json() : json格式的返回值，可以打印成字典
assert : 断言，与if else功能相似 # 如果断言通过，就那继续往下执行，反之报错。
'''
'''
headers 
请求头
响应头

如果用了参数是json格式，headers可以省略不写。有token的必须写。
'''


import requests

#1.登录
url = "http://192.144.148.91:2333/login"
data = {"username":"liuyun1", "password":"a12345678"}
res = requests.post(url=url, json=data)
print(res.text)
assert res.status_code == 200 # 判断http状态码是否正常  status == 200（http状态码）
assert res.json()["status"] == 200 # 判断返回值的状态 status == 200
token = res.json()["data"]["token"]
print("登录成功了")

#2.写文章
url = "http://192.144.148.91:2333/article/new"
data = {"title":"123", "content":"123埃里克的是解放拉萨的","tags":"测试", 
"brief":"三生三世", "ximg":"dsfsdf.jpg"}
headers = {"token":token}
res = requests.post(url=url, json=data, headers=headers)
assert res.status_code == 200 
assert res.json()["status"] == 200
aid = res.json()["data"]["articleid"] # 修改写入的文章，获取这个新些的文章的ID
print("写文章成功了！")

#3.修改文章
url = "http://192.144.148.91:2333/article/update"
data = {"title":"为什么要学习测试","content":"内容","tags":"测试",
"brief":"介绍","ximg":"dsfsdf.jpg","aid":aid}
headers = {"token":token}
res = requests.post(url=url, json=data, headers=headers)
assert res.status_code == 200
assert res.json()["status"] == 200
print("修改文章成功了")