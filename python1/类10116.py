

# . 定义一个字典类：dictclass。完成下面的功能：
# dict = dictclass({你需要操作的字典对象})
# ①　删除某个key，并返回删除后的字典
# del_dict(key)
# ②　判断某个键是否在字典里，如果在,返回键对应的值，不存在则返回"not found"
# get_dict(key)
# ③　返回键组成的列表：返回类型;(list)
# get_key()
# ④　合并字典，并且返回合并后字典的values组成的列表。返回类型:(list)
# update_dict({要合并的字典})
#
# class Dictclass():
#     def __init__(self,dict):#设置字典的属性
#         self.dict = dict    #将dict赋予新的名字self.dict
#     def del_key(self,key): #方法：设定删除的键
#         self.dict.pop(key) #删除key键的值
#         return self.dict  # 返回删除后的字典
#     # def get_key(self,key1): #方法：设定某个键
#     #     return self.dict.get(key1,"not found") #判断指定键是否在字典里的值,在里面输出key1的值，不在时输出notfound
#     # def list_key(self): #
#     #     return self.dict.keys() #取出键值，且以列表方式返回
#     # def update_dic(self,dict2):
#     #     (self.dict.update(dict2)) #将self.dict加入dict2
#     #     return self.dict.values()  #返回字典的键值，以列表的方式
#
# d = {"d":3,"4":4,"5":6}
# di = { "liu":6,"4":6}
# d1 = Dictclass(d)
# # print(d1.dict)
# print(d1.del_key("d"))
# # print(d1.get_key("8"))
# # print(d1.get_key("5"))
# # print(d1.list_key())
# # print(d1.update_dic(di))
