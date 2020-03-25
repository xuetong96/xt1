# print("你好")
# print(1)
# print(1.1)  # 小数
# print(True)
# """
# 这个是注释
# """
# 
# a=len(input('你好吗？      '))
# b=len(input('我也好。      '))
# print(a+b)
# a = (1,3,4,True,"haha",'hh','hh','hh')
# # print(a[-2])
# # print(a.index("hh"))
# # print(a.count("hh"))
# # b = (a,"jj","kk")
# # print (b[0][-1])
# a = [1,3,4,True,"haha",'hh','hh','hh']
# a.append("append")
# print(a)
# a.insert(1,"heihei")
# print(a)
# b = a.pop(0)
# c = a.pop(0)
# print(a)
# print(b)
# print(c)
# # a.clear()
# print(a)
# xx = ['添加的','tianjiande ']
# a.extend(xx)
# print(a)
# print(a+xx)
# a.remove(3)
# print(a)
a = {'name':"薛彤","age":24,"身高":"160cm"}
print(a['age'])
a['身高']='162cm'
print(a)
a.update(name=1111)
print(a)
b=a.get('name')
print(b)
print(a)
c=a.pop('name')
print(c)
print(a)
print(c)
print(a)
