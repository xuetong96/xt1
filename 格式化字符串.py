'''
格式化字符串： format

注意引号的内外包含
'''

a = input('名称：')
b = input('密码：')
c = "insert into t_user (a,b) values ('zhangsan','123456')"
print(c)
print('--------------------------------------------------------')
c = "insert into t_user (a,b) values ('{}','{}')" .format(a,b)
print(c)