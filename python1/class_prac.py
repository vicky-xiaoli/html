
# class Person():   #声明
#     def __init__(self,name,age):  #属性
#         self.name =name
#         self.age =age
#     def walk(self):   #方法
#         print("%s都已经%d岁了，因此要多走路多运动！" %(self.name,self.age))
#
# p= Person("zhansan",30)  ##实例化
# p.walk()
# print(p.name)
# print(p.age)

# 1. 类的属性和方法练习：
# 写一个学生类
# 写出学生应该有的属性和方法

# class Student():
#     '''
#     调用时可以直接添加属性，但是无法直接添加方法
#     '''
#     x = "年轻"      ###不可变属性
#     y = "没头发"
# def __init__(self,name,nianji):  #可变属性
#     self.name = name
#     self.nianji = nianji
# def study(self):
#     print("%s成绩很好" %(self.name))
# lili = Student("胡胡","六年级二班")
# lili.name = "xiaolili"   #对lili这个人重新定义名字
# lili.study()
# lili.hobby = "吃饭" #直接在调用时增加属性
# print(lili.name)
# print(lili.nianji)


class Father():
    x = "双手"
    def __init__(self,family_name,gold):
        self.family_name = family_name
        self.gold = gold
    def play(self):
        return "%s喜欢打篮球" %(self.family_name)
    def watch(self):
        return "%s喜欢看美剧" %(self.family_name)

class Son(Father):
    def __init__(self,family_name,gold,age):
        Father.__init__(self, family_name, gold)
        self.age = age
    def watch(self):
        return "%s喜欢看动漫" % (self.family_name)

li = Son("李",500000,18)
print(li.play())
print(li.watch())
print(li.x)
print(li.age)




# 继承
#     写一个人类类
#     再写一个学生类
#     学生类继承人类的属性和方法
#     学生类拥有自身的属性和方法

# class Person():
#     def __init__(self,name,age,sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#     def sleep(self):
#         return "%s睡觉8小时" %(self.name)
# class Studet(Person):
#     def __init__(self,name,age,sex,clas):
#         Person.__init__(self,name,age,sex)
#         self.clas = clas
#     def jicheng(self):
#         self.sleep()
#     def sleep(self):
#         return "%s睡觉4小时" %(self.name)
# lili = Studet("小丽",18,"女","三班")
# print(lili.name)
# print(lili.age)
# print(lili.sex)
# print(lili.clas)
# print(lili.jicheng())
# print(lili.sleep())
