# print("hello world!")  # 字符串
# print(2333)  # 整数
# print(2.333)  # 小数
# print(True)  # 布尔值 True False
# print(())  # 元组
# print([])  # 数组
# print({})  # 字典
# 锄禾日当午
# 汗滴禾下土
# print("哈哈",2333,2.333)
# print("哈哈"+"嘻嘻")  # 字符串的拼接
# print("哈哈哈"*100)
# print(((1+2)*100-9.9)/2)
# print(2<3)
# # 变量
# # 赋值
# name = "张三"  # 把张三这个值赋值给了名字叫a的这个变量
# print(name)



# 数据格式的转换
# print(type("哈哈"))
# print(type(2333))
# print(type(2.333))
# print(type(True))
# print(type(()))
# print(type([]))
# print(type({}))


# a = float(input("请输入："))
# b = float(input("请输入："))
# print("input获取的内容：",a+b)


'''字符串长度'''
# a = "3456"
# print(len(a))


''' 元组 '''

'''下标，从0开始编号'''
# a = (1,2,3,4,"哈哈","哈哈","哈哈","哈哈","哈哈","嘻嘻",True,False,1) 
# print(a[-2])

''' 查找某个值的下标 , 如有多个重复值，则显示第一个的下标值'''
# print(a.index("哈哈"))

''' 统计某个重复值的数量 '''
# print(a.count("哈哈"))
''' 以上两个仅对一维元组有效  '''


''' 二维元组'''
# a = (1,2,3,4,"哈哈","哈哈","哈哈","哈哈","哈哈","嘻嘻",True,False,1) 
# b = (a,"哈哈","嘻嘻")
# print(b[1])

''' 取出b元组中a元组的某个值 '''
# print(b[0][3]) 

'''
切片（批量取值）
左闭右开
不写的话是从首位开始，或者是到末尾结束
'''
# a = (1,2,3,4,"哈哈","哈哈","哈哈","哈哈","哈哈","嘻嘻",True,False,1) 
# print(a[:4])   
# print(a[4:9])
# print(a[9:])

""" 数组（列表）"""

""" 同样适用下标 """
""" 元组一定写好过后不可以修改，而数组是可以修改的(用代码修改) """
# a = [1,2,3,4,"哈哈","嘻嘻",True,False]

""" index count 同样适用数组 """

""" 追加数据 ： 添加的数据永远在数组的尾巴  """
# a.append("append1")
# a.append("append2")
# print(a)

""" 在指定位置插入一个值 """
# a.insert(4,"薛彤")
# print(a)

""" 剪切数据 ： pop(下标) """
# a = [1,2,3,4,"哈哈","哈哈","哈哈","哈哈","哈哈","嘻嘻",True,False,1]
# b = a.pop(0) 
# c = a.pop(0) 
# print(b+c)
# print(a)
# print(b)

""" 清空数组 ： clear() """
# a.clear()

""" 插入数组 : extend(要加入的数组名) """
# xx = ["你好","不好"]
# a = [1,2,3,4,"哈哈","哈哈","哈哈","哈哈","哈哈","嘻嘻",True,False,1]
# print(a+xx)
# a.extend(xx)
# print(a)

''' 删除某个值 ： remove(数组里的某个值) '''
# a = [1,2,3,4,"哈哈","哈哈","哈哈","哈哈","哈哈","嘻嘻",True,False,1]
# print(a)
# b = a.remove(1)
# print(b)
# print(a)

''' Ture = 1 ; Flase = 0 '''

''' 下标不要超出范围 = 越界 '''
# xx = [a,0,1,2,3]

''' 二维数组，类似二维元组 '''

"""
python的语法
所有的方法都是小括号结尾。比如，print(),input(),len()
元组、数组、字典的取值，都是用中括号,比如 a[0]
元组、数组、字典的定义，分别是(),[],{}
"""



"""
字典   的特点
1、字典中的值没有顺序。(无下标)
2、字典的结构必须是 键值对的结构。 key:value  
3、字典的取值，是通过key去取这个value
"""

# a = {"name":"张三",0:"哈哈","age":25}

''' 取值 : 通过key取值，相当于把下标自定义了'''
# print(a["name"])

''' 新增 '''
# a["high"] = "183cm"
# print(a)

''' 修改 '''
# a["name"] = "李四"
# print(a)

''' get : 取值 '''
''' get 和  通过key取值的区别 ：如果去空值，get返回空值，key显示报错 '''
# b = a.get("name")
# print(b)
# print(a.get("name11"))
# print(a["name11"])

''' pop : 剪切 '''
# b = a.pop("name")
# print(b)
# print(a)

''' update : 新增或修改 '''
''' 所有的字符串都要加引号，update 认为是赋值，故可以不加引号'''
# a.update(name="哈哈")
# print(a)


''' 数组和字典的删除 : del '''
# del a["name"]
# print(a)
# del a[0]




'''
练习：
获取用户输入的个人信息，并且存储到字典中，
个人信息包括：name age sex
'''