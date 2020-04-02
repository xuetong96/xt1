'''判断 '''

# age = int(input("请输入你的年龄："))
# if age > 60:
#     print("你应该退休了")
# elif age > 30:
#     print("家庭的责任很重吧")
# elif age > 20:
#     print("一定要好好规划你的未来！")
# else:
#     print("读书的时候，要认真！")

# if age > 20 and age <=30:
#     print("22222222")
# elif age > 30:
#     print("333333333")
# elif age > 60:
#     print("66666666")
# else:
#     print("xxxxxxxxxx") 

''' 判断条件： ==(判断是否相等）， !=， >， <， in（在元组、数组、字典中）， is(判断类型）， not in，not is '''
''' exit()  ： 退出！'''
# a = input("请输入：")
# if a == "":
#     print("不能为空！")
#     exit()
# if a in "0123456789":
#     a = int(a)
# else:
#     print("请输入正确的年龄！")
#     exit()

# if a > 5:
#     print("大")
# else:
#     print("小")

# a = "dkjfedj"
# if type(a) is int:
#     print("是数字！")
# elif type(a) is str:
#     print("是字符串")
# else:
#     print("其他")


''' 循环 '''
''' while '''
''' 死循环的话 按 Ctrl+c 终止'''
# a = 1
# while a < 10:
#     print("哈哈哈啊哈",a)
#     a = a + 2

''' 练习：学生成绩表，需要名字与成绩一一对应，并且把大于60小于60的分开存放 '''



''' for  : 遍历 '''
# a = "你好，今天你吃了吗？"
# a = ["张三","李四","王麻子","浪晋","流云","希希","小梁","二狗","陈平安","朱珠","亚索"]
# for i in a:
#     print(i)

''' range() : 数列生成器 '''
''' end ： 不换行？？ '''
# for i in range(1,10):
#     for j in range(1,i+1):
#         if i == 3:
#             continue
#         print(i,"X",j,"=",i*j,end="  ")
#     print()


''' 步径 '''
# for i in range(1,10,2):
#     print(i)


''' 练习： 打印99乘法表'''
''' 练习： 红绿黄灯的打印'''
''' 练习： 使用代码，实现注册的功能，用户输入账号和密码，要求账号长度是5-8位，密码6-12位，账号必须小写开头
    储存到字典中  '''



''' continue : 循环过程中，如果满足这个条件，跳过本次循环，进行下一循环 '''
# for i in range(10):
#     if i == 3:
#         continue
#     print(i)

''' break : 跳出循环，终止整个循环；嵌套循环的话只针对本层循环 '''
# for i in range(10):
#     if i == 3:
#         break
#     print(i,'hh')




# def 方法的声明
# checkname 方法的名字
# username 方法的参数
# """方法的说明"""
# 方法的逻辑代码





"""
返回值，返回后我们可以对这个值做其他的操作
而，print不能
"""




# username = input("请输入你的账号：")
# password = input("请输入你的密码：")
# if checkname(username) == True:
#     if len(password) >= 8 and len(password) <= 12:
#         print("注册成功！",{username:password})
#     else:
#         print("密码必须8-12位！")
# else:
#     print(checkname(username))


# def jiafa(a,b):
#     """
#     这个方法的作用是实现两个数字相加
#     """
#     if type(a) is int and type(b) is int:
#         print(a+b)
#     else:
#         return "输入的数据类型不正确"
