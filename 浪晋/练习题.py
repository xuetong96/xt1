"""
练习：
现在有10个学生的成绩，需要录入到系统中。
这是个人分别是，张三、李四、王麻子、浪晋、流云、希希、小梁、二狗、陈平安、朱珠、亚索
并且名字和成绩需要对应上。
而且大于60的和小于60的需要分开存放。
"""
highchengji = {}  # 定义了一个空字典，用来存储大于60的信息
lowchengji = {}  # 定义了一个空字典，用来存储小于60的信息
studentlist = ["张三","李四","王麻子","浪晋","流云","希希","小梁","二狗","陈平安","朱珠","亚索"]
a = 0  # 定义了一个变量，用来控制数组的下标的变化
while a < len(studentlist):  # 因为所有的人的信息的录入，都是要用input，所有写了循环，len判断了数组的长度，总长度-1就是最大的下标
    chengji = int(input("请输入"+studentlist[a]+"的成绩："))  # 录入信息，为了方便判断，所以转换了格式
    if chengji >= 60:  # 判断分数
        highchengji[studentlist[a]] = chengji  # 存到字典中
    else:
        lowchengji[studentlist[a]] = chengji
    a = a + 1  # 控制下标变化，每一次循环，都+1
print("大于60的：",highchengji)
print("小于60的：",lowchengji)


"""
练习：
获取用户输入的个人信息，并且存储到字典中。
个人信息包括了，name,age,sex。
"""
name = input("请输入你的姓名：")
age = input("请输入你的年龄：")
sex = input("请输入你的性别：")
userinfo.update(name=name,sex=sex,age=age)
# userinfo = {"name":name,"sex":sex,"age":age}
# userinfo["name"] = name
# userinfo["age"] = age
# userinfo["sex"] = sex
print(userinfo)


"""
练习：通过代码获取两段内容，并且计算他们的长度的和。
"""
a = input("请输入：")
b = input("请输入：")
print("两段字符串的长度是：",len(a)+len(b))


"""
练习：
现在有10个学生的成绩，需要录入到系统中。
这是个人分别是，张三、李四、王麻子、浪晋、流云、希希、小梁、二狗、陈平安、朱珠、亚索
并且名字和成绩需要对应上。
而且大于60的和小于60的需要分开存放。
"""
highchengji = {}  # 定义了一个空字典，用来存储大于60的信息
lowchengji = {}  # 定义了一个空字典，用来存储小于60的信息
studentlist = ["张三","李四","王麻子","浪晋","流云","希希","小梁","二狗","陈平安","朱珠","亚索"]
for i in studentlist:  # 因为所有的人的信息的录入，都是要用input，所有写了循环，len判断了数组的长度，总长度-1就是最大的下标
    chengji = int(input("请输入"+i+"的成绩："))  # 录入信息，为了方便判断，所以转换了格式
    if chengji >= 60:  # 判断分数
        highchengji[i] = chengji  # 存到字典中
    else:
        lowchengji[i] = chengji
print("大于60的：",highchengji)
print("小于60的：",lowchengji)



"""
练习：
打印九九乘法表
"""
for i in range(1,10):
    for j in range(1,i+1):
        print(i,"X",j,"=",i*j,end="  ")
    print()

"""
练习1：
通过print打印，模拟一个红绿灯的功能，注意：红灯30次，绿灯35次，黄灯3次。
练习2：
使用代码，实现一个注册的功能。
用户输入账号和密码，要求账号长度是5-8位，密码6-12位，并且账号必须小写开头。
储到到字典中，{username:password}
"""


light = {"红灯":30,"绿灯":35,"黄灯":3}
for i in light:
    for j in range(light[i]):
        print(i,"倒计时还有",light[i]-j,"秒")


username = input("请输入账号：")
password = input("请输入密码：")
if len(username) >=5 and len(username) <=8:
    if username[0] in "qazwsxedcrfvtgbyhnujmikopl":
        if len(password) >= 8 and len(password) <= 12:
            print("注册成功！",{username:password})
        else:
            print("密码必须8-12位！")
    else:
        print("账号的首字母必须小写字母开头！")
else:
    print("账号的长度不符合规范，请输入5-8位的账号")



"""
练习：
定义一个方法，用来判断用户输入的账号密码是否符合规范。
"""

def checkname(username,password):
    """
    自动的判断账号长度是5-8位，并且账号必须小写开头
    """
    if len(username) >=5 and len(username) <=8:
        if username[0] in "qazwsxedcrfvtgbyhnujmikopl":
            if len(password) >= 8 and len(password) <= 16:
                return True
            else:
                return "密码不符合规范"
        else:
            return "账号的首字母必须小写字母开头！"
    else:
        return "账号的长度不符合规范，请输入5-8位的账号"