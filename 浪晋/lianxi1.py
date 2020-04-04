"""
练习1：
通过print打印，模拟一个红绿灯的功能，注意：红灯30次，绿灯35次，黄灯3次。
练习2：
使用代码，实现一个注册的功能。
用户输入账号和密码，要求账号长度是5-8位，密码6-12位，并且账号必须小写开头。
储到到字典中，{username:password}
"""

# a = range(30)
# print(a)
# for b in a:
#     print(b)
# # for b in a:
# #     print("红灯还有"+b+"秒")

# a = 30
# while a >= 0:
#     print("红灯还剩",a,"秒")
#     a = a-1
# print()
# b = 35
# while b >= 0:
#     print('绿灯还剩',b,"秒")
#     b = b-1
# print()
# c = 3
# while c >= 0:
#     print("黄灯还剩",c,"秒")
#     c = c-1



# a = int(input("请设置红灯："))
# # print(a)
# b = int(input('请设置绿灯：'))
# # print(b)
# c = int(input('请设置黄灯：'))
# # print(c)
# table = {'red':a,'green':b,'yellow':c}
# print(table)
# for i in table:
#     if  
#     print(i)

# a = {'red':"input":""}
# print(a)


'''
练习2：
使用代码，实现一个注册的功能。
用户输入账号和密码，要求账号长度是5-8位，密码6-12位，并且账号必须小写开头。
储到到字典中，{username:password}
'''

# a = input('请输入账号：')
# if len(a) < 5 or len(a) > 8:
#     print("账号长度要求5-8位")
#     a = input('请输入账号：')
# else:
#     b = input('请输入密码：')
#     if len(b) < 6 or len(b) > 12:
#         print("密码长度要求6-12位")
#         b = input('请输入密码：')
#     else:
#         print("设置成功")
# print({"username":a,"password":b})

# a = input('请输入账号：')
#  len(a) < 5 or len(a) > 8:
#     print("账号长度要求5-8位")
#     a = 
# else:
#     b = input('请输入密码：')
#     if len(b) < 6 or len(b) > 12:
#         print("密码长度要求6-12位")
#         b = input('请输入密码：')
#     else:
#         print("设置成功")
# print({"username":a,"password":b})

import pymysql

# db = pymysql.connect(host='192.144.148.91',user='ljtest',password='123456',db='ljtestdb')
# cursor = db.cursor()
# cursor.execute("show tables;")
# res = cursor.fetchall()
# print(res)
# print( )
# for i in res:
#     print(i)

def chaxun(sql):
    db = pymysql.connect(host='192.144.148.91',user='ljtest',password='123456',db='ljtestdb')
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        res = cursor.fetchall()
        return res
    except Exception as e:
        return"SQL语句错误！",e
   
def xiugai(sql):
    db = pymysql.connect(host='192.144.148.91',user='ljtest',password='123456',db='ljtestdb')
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        db.commit()
        return True
    except Exception as e:
        return"SQL语句错误！",e
