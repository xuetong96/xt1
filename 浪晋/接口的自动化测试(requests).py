'''
requests 的使用
'''

import requests  # 导入requests的包

'''
使用postman 里面的 code 复制代码啊啊啊啊
'''
# url = "http://192.144.148.91:2333/login" 

# payload = "{\r\n\"username\":\"langjin\",\r\n\"password\":\"lj123456\" \r\n}\r\n"
# headers = {
#     'Content-Type': "application/json",
#     'cache-control': "no-cache",
#     'Postman-Token': "8ba99fdf-180f-4964-88b3-c585c321143f"
#     }

# response = requests.request("POST", url, data=payload, headers=headers)

# print(response.text)

'''post 类型接口操作'''

# url = "http://192.144.148.91:2333/login"  # 接口地址
# headers = {"Content-Type":"application/json"} # 请求头
# data = {"username":'langjin',"password":"lj123456"} # 接口参数

# res = requests.post(url=url,headers=headers,json=data) # 返回值包含postman下方所有的内容
# print(res.text)

'''get 类型接口操作 '''
'''headers 可以省略不写 '''

# url = "http://192.144.148.91:2333/get_title_img"  # 接口地址
# headers = {"Content-Type":"application/json"} # 请求头

# res = requests.get(url=url,headers=headers) # 返回值包含postman下方所有的内容
# print(res.text)

''' 
text : 以文本或字符串的格式显示返回结果 
json() : 转换成字典格式
'''

# url = "http://192.144.148.91:2333/login"  # 接口地址
# headers = {"Content-Type":"application/json"} # 请求头
# data = {"username":'langjin',"password":"lj123456"} # 接口参数

# res = requests.post(url=url,headers=headers,json=data) # 返回值包含postman下方所有的内容
# # print(res.text)
# # print(type(res.text)) # text : 以文本或字符串的格式显示返回结果
# # print(res.json())
# # print(type(res.json())) # json() ： 转换成字典格式
'''
确认接口是否OK
'''
# res1 = res.json()
# # print(res1['msg'])
# msg = res1.get('msg') 
# print(msg)
# if msg == '登录成功！':
#     print('登录成功！测试通过！')
# else:
#     print('登录失败！')

'''
与数据库数据进行对比
'''
# from dbtools import shujuku # 导入之前封装的数据库的类
# hh = shujuku("192.144.148.91",'ljtest','123456','ljtestdb') # 首先把类实例化，才能使用

# url = 'http://192.144.148.91:2333/get_title_img'
# res = requests.get(url) # 返回值
# print(res.text)
# res1 = res.json() # 转换成字典格式
# data = res1.get('data') # 取出字典中data对应的值
# print(data) # 可以看出data是一个数组
# len = len(data) # 数组是有长度的，可以数
# print(len)
# ku = hh.chaxun('select count(*) from t_title_img where status = 0')
# print(ku)
# if ku[0][0] == len:
#     print('与数据库信息对比成功，测试成功！')
# else:
#     print('与数据库信息对比失败，测试异常！')

'''
token 的传递,想办法吧token放在一个固定的地方：文件、数据库啥的
'''
# url = "http://192.144.148.91:2333/login"  # 接口地址
# headers = {"Content-Type":"application/json"} # 请求头
# data = {"username":'langjin',"password":"lj123456"} # 接口参数
# res = requests.post(url=url,headers=headers,json=data) # 返回值包含postman下方所有的内容
# res1 = res.json()
# # token = res1.get('data').get('token')
# # print(token)
# token = res1['data']['token']
# print(token)
# with open('token.txt','w') as f:  # 创建一个文件“token.txt”
#     f.write(token)  # 将获取的token值写入文件

with open('token.txt','r') as f:
    token = f.readline() 
url = "http://192.144.148.91:2333/logout"
headers = {"Content-Type":"application/json",'token':token} 
res = requests.get(url=url,headers=headers)
print(res.text)