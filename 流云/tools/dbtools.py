'''
代码的单位：
包 > 模块 > 类 > 方法 > 变量
但可以并列使用
'''
 
''' 
导入包 ： import 包名
1、python 有很多自带的包 ： import 包名 ；即可
2、第三方的包需要 下载：pip install 包名； 
                 卸载：pip uninstall 包名；
                 查看安装了哪些包： pip list;
3、常见的第三方的包：
     pymesql : 用于操作mysql数据库
     selenium：用于网站的自动化测试
     appium：  用于APP自动化测试
     requests：用于接口自动化测试
     xlrd :    用于操作Excel表的
     xlwt :    写入Excel表


注意：一般导入的包写在文件的最上方
'''
# import time      ''' 控制时间 '''
# import random    ''' 随机数 '''

# for i in range(10):
#     time.sleep(1)
#     print(i)

# a = random.randint(1,10)
# print(a)

'''
pymysql
'''
import pymysql

# db = pymysql.connect(host="192.144.148.91",user='ljtest',password='123456',db='ljtestdb') # 连接本地测谈网数据库
# cursor = db.cursor() # 获取游标
# cursor.execute('show tables;') # 使用游标来执行SQL语句
# res = cursor.fetchall() # 获取所有结果
# for i in res:
#     print(i)

''' 将以上代码封装成一个方法'''
''' 需要变化的作为参数 '''
# def cetanwangchaxun(sql):
#     '''连接测谈网并使用SQL语句查询'''
#     db = pymysql.connect(host="192.144.148.91",user='ljtest',password='123456',db='ljtestdb') # 连接本地测谈网数据库
#     cursor = db.cursor() # 获取游标
#     cursor.execute(sql) # 使用游标来执行SQL语句
#     return cursor.fetchall() # 获取所有结果,并返回
#     # return res

# # a = cetanwangchaxun("show tables;")
# # print(a)

# # a = cetanwangchaxun('select * from t_user limit 3')
# # for i in a:
# #     # print(i)
# #     print(i[1],i[2])


'''防止因为sql语句写错，使用异常捕获'''
def cetanwangchaxun(sql):
    '''连接测谈网并使用SQL语句查询'''
    db = pymysql.connect(host="192.144.148.91",user='ljtest',password='123456',db='ljtestdb') # 连接本地测谈网数据库
    cursor = db.cursor() # 获取游标
    try:
        cursor.execute(sql) # 使用游标来执行SQL语句
        return cursor.fetchall() # 获取所有结果,并返回
        db.close()
    except Exception as e:
        db.close()
        return "sql语句输入错误！",e
    
# a = cetanwangchaxun('select * from t_use limit 3')
# print(a)


''' DML语句'''
def cetanwangxiugai(sql):
    '''连接测谈网并使用SQL语句新增、修改、查询'''
    db = pymysql.connect(host="192.144.148.91",user='ljtest',password='123456',db='ljtestdb') # 连接本地测谈网数据库
    cursor = db.cursor() # 获取游标
    try:
        cursor.execute(sql) # 使用游标来执行SQL语句
        db.commit() # 提交，应用
        return Ture
        db.close()
    except Exception as e:
        db.close()
        return "sql语句输入错误！",e
    
# a = cetanwangchaxun('')
# print(a)


''' 
做一个类，把定义的两个方法包含进去
实现，可以控制其他的数据库
'''
class shujuku:

    def __init__(self,host,user,password,dbname,port='3306'):
        self.host = host
        self.user = user
        self.password = password
        self.db = dbname
        self.port = port

    def chaxun(self,sql):
        db = pymysql.connect(host=self.host,user=self.user,password=self.password,db=self.db) 
        cursor = db.cursor() # 获取游标
        try:
            cursor.execute(sql) # 使用游标来执行SQL语句
            return cursor.fetchall() # 获取所有结果,并返回
            db.close()
        except Exception as e:
            db.close()
            return "sql语句输入错误！",e

    def xiugai(self,sql):
        db = pymysql.connect(host=self.host,user=self.user,password=self.password,db=self.dbname) 
        cursor = db.cursor() # 获取游标
        try:
            cursor.execute(sql) # 使用游标来执行SQL语句
            db.commit() # 提交，应用
            return Ture
            db.close()
        except Exception as e:
            db.close()
            return "sql语句输入错误！",e

# hh = shujuku("192.144.148.91",'ljtest','123456','ljtestdb')
# a = hh.chaxun('show tables;')
# for i in a:
#     print(i)