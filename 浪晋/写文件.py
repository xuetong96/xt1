''' 文件的读写 '''

'''
W是写入，总是会写成新的文件（write）
a 是在该文件内追加（add)
r 是读取（read）
encoding : 指定打开的编码

'''
# text = input("请输入今天的心情：")
# with open("日记.txt","w",encoding="utf8") as f:  
#     f.write(text)

# text = input("请输入今天的心情：")
# with open("日记.txt","a",encoding="utf8") as f:  
#     f.write(text)

''' 
制表符
\n  :  换行
\t  :  空格
'''
# text = input("请输入今天的心情：")
# with open("日记.txt","a",encoding="utf8") as f:  
#     # f.write(text+"\t")
#     f.write(text+"\n")

'''
自动获取时间： time.strftime("%y-%m-%d %H:%M:%S")
'''
# import time

# now = time.strftime("%y-%m-%d %H:%M:%S")
# print(now)
# text = input("请输入今天的心情：")
# with open("日记.txt","a",encoding="utf8") as f:  
#     f.write(now+'\n')
#     f.write(text+"\n")
#     f.write('-------------------'+'\n')


''' 保存文件到指定路径 '''
import time

now = time.strftime("%y-%m-%d %H:%M:%S")
print(now)
text = input("请输入今天的心情：")
with open("D:\日记.txt","a",encoding="utf8") as f:  
    f.write(now+'\n')
    f.write(text+"\n")
    f.write('-------------------'+'\n')
