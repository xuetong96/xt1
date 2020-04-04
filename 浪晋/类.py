''' 类 '''
"""
类的写法：
1、class 类的名字，类的名字首字母必须大写
2、指定默认值 : def __init__(self，。。。。)
3、指定其他方法 ： def 方法名(self,...)

注意：类里面所有的方法，都必须要传一个参数，叫self，且self必须是首个参数
"""

# class GirlFriend():
#     """
#     女朋友
#     """
#     def __init__(self):
#         self.sex = '女'
#         self.high = '170'
#         self.weight = '50kg'
#         self.hair = '大波浪'
#         self.age = '18'
    
#     def caiyi(self,num):  # 才艺
#         if num == 1:
#             print('跳舞')
#         elif num == 2:
#             print("唱歌")
#         else:
#             print('画画')
    
#     def work(self):  # 工作
#         print('企业高管')

''' 类的实例化 '''
# szj = GirlFriend()

# ''' 操作类 '''
# szj.caiyi(1)
# szj.work()
# print(szj.high)

" 参数 进阶 使用"
class GirlFriend():
    """
    女朋友
    """
    def __init__(self,sex,high,weight,hair,age):
        self.sex = sex
        self.high = high
        self.weight = weight
        self.hair = hair
        self.age = age
    
    def caiyi(self,num):
        """
        才艺表演
        """
        print("你性别为"+self.sex+"身高"+self.high+"体重"+self.weight+"发型"+self.hair+"年龄"+self.age+"的女朋友开始了自己的才艺表演之：")
        if num == 1:
            print("胸口碎大石！")
        elif num == 2:
            print("唱跳RAP篮球")
        else:
            print("单手开瓶盖！")
    
    def chuyi(self):
        """
        厨艺持家
        """
        print("你性别为"+self.sex+"身高"+self.high+"体重"+self.weight+"发型"+self.hair+"年龄"+self.age+"的女朋友开始了自己的厨艺表演之：")
        print("精通八大菜系！中外融合！啥都会做！")

# szj = GirlFriend("女",'170','60kg','短发','20')
# szj.caiyi(5)
# szj.chuyi()
# print(szj.weight)

'''
类的特点：
1、继承
2、重写/多态
'''
''' Girlfrieng: 父类； nvshen: 子类 '''
# class nvshen(GirlFriend): 
#     pass

# szj = nvshen('nv','jj','hh','de','hu')
# szj.chuyi()
# szj.caiyi(9)

" 对 work 进行重写 "
# class nvshen(GirlFriend): 
#     def work(self):
#         print("弹琴")

# szj = nvshen('1','2','3','4','5')
# szj.work()

''' 
object ： 祖宗类 
def __int__(self) 就是对object这个类的重写
'''