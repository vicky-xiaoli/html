

#输入两个整数，放入到a与b变量中去，如果a>=b就将a与b中的值进行交换，否则就不交换。目的就是要让a中放的值总是小于或等于b中的数，输出
# a= int(input("输入整数："))
# b= int(input("输入整数："))
# if a >= b:
#     a,b =b,a    #/
# # print(a,b)      #结束始终都会执行此操作，故不用跟else，直接结束语句：print顶格
#                #else不是必须跟if一起的

# 方法二
# a= int(input("输入整数："))
# b= int(input("输入整数："))
# if a >= b:
#     # c =a        用第三个变量互换：c = a a = b b = c
#     a =b
#     b = c
# print(a,b)