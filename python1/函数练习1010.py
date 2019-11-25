# def add(a, b):
#     f = a + b
#     c = a * b
#     return f, c
#
#
# x, y = add(3, 6)
# a = add(3, 6)
# print(x, y)
# print(a)
#
#
# def fu(name, age, sex="女", *args, **kwargs):
#     print("name= ", name)
#     print("age= ", age)
#     print("sex= ", sex)
#     print("args= ", args)
#     print("kwargs= ", kwargs)
#
#
# fu("lili", 18, "男", 23, "man", game="xiaoxiao")
# lis = ["fcs", 12, 3]
#

# def func(*lis):
#     print("args", lis)
# func("12",1,3)

def func(name,age):
    print("%s的年龄是%d" %(name,age))
person={"name":"lili","age":22}
func(**person)