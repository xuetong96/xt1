''' 异常捕获 : try:    expect:  '''
''' 代码报错就是异常 '''

# try:
#     print(a+1)
# except:
#     print("错误")

''' 
异常类（python自带）: exception
主要可以用作处理用户输入的错误数据（用户输入错误的格式导致代码报错）
'''

# try:
#     print(a+1)
# except Exception as a:
#     print("错误",a)


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