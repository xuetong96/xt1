''' 文件的读写 '''

'''
W是写入，总是会写成新的文件
a 是在该文件内追加
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
