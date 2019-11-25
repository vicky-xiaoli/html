

#输入三个int型的数据，放入到a,b,c三个变量中去，使用条件结构与交换逻辑将这三个变量中的值从小到大排列
# a = (int(input("输入整数：")))
# b = (int(input("输入整数：")))
# c = (int(input("输入整数：")))
# l=[a,b,c]
# l.sort()         #反向排序方法
# print(l)

 # 方法二  --符合本题要求的交换逻辑
# a = (int(input("输入整数：")))
# b = (int(input("输入整数：")))
# c = (int(input("输入整数：")))
# if a >= b:
#     if a >= c:
#         if b >= c:
#             a,b,c = c,b,a   #在a>b>c的情况下
#             print(a,b,c)
#         else:    #第三个语句的第二种情况
#             a,b,c = b,c,a#a>c>b的情况
#             print(a,b,c)
#     else:
#         a,b,c = b,a,c #第二个if语句的第二种情况
#         print(a,b,c)
# else:          #第一个if语句的第二种情况
#     if c < b:
#         if a < c:
#             a,b,c = a,c,b
#             print(a,b,c)
#         else:
#             a,b,c = c,a,b
#             print(a,b,c)
#     else:
#         print(a,b,c)
#
