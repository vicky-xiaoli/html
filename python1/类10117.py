
# 2. 定义一个列表的操作类：Listinfo
# 包括的方法:
# 1 列表元素添加: add_key(keyname) [keyname:字符串或者整数类型]
# 2 列表元素取值：get_key(num) [num:整数类型]
# 3 列表合并：update_list(list) [list:列表类型]
# 4 删除并且返回最后一个元素：del_key()

# class Listinfo():
#     def __init__(self,list):   #表有表名，先设定表名
#         self.list = list     #赋值self.list给list
#     # def add_key(self,keyname): #设定添加方法中输入元素的变量
#     #     if isinstance(keyname,(str,int)): #判断keyname是str,int,是的话返回True  ****
#     #         self.list.append(keyname)   #添加新的元素
#     #         return self.list    #返回添加后的列表
#     # def get_key(self,num):   ##设定取值方法中输入元素的变量
#     #     if isinstance(num,int) and num >= -len(self.list) and num < len(self.list):  #判断输入的num是# 整数型，且长度不超过列表长度
#     #         return self.list[num]   #返回索引对应的元素
#     # def update_list(self,lit):#设定添加方法中输入元素的变量
#     #     if isinstance(lit,list):  #判断新增的lit是一个列表
#     #         self.list.extend(lit)   #列表合并
#     #         return self.list   #返回新列表
#     def del_key(self):   #设定删除方法中输入元素的变量
#         return self.list.pop() #返回删除最后一个元素
#
#
# li = [23,12,34,"huk",2,78,9,3.8]
# lit1 =[1,45,3,6]
# lis =Listinfo(li)
#
# print(lis.list)
# # print(lis.add_key(4))
# # print(lis.get_key(7))
# # print(lis.update_list(lit1))
# print(lis.del_key())

