
# 有这样一个矩阵，设计一个函数，根据我输入的参数，返回其所在的位置是几行几列
# lit=[[3,8 ,9],[6,11,2],[7,18,5]]  #---本题考点：双层for 循环
# def fu(num):
#     lit = [[3,8 ,9],[6,11,2],[7,18,5]]
#     for i in range(3):   #循环行
#         for j in range(3):  #循环列
#             if num == lit[i][j]: #if循环语句，按索引找出输入数字所在位置
#                 h = i + 1       #索引加1就是所在位置
#                 k = j + 1
#     print("%d在第%d行,第%d列" %(num,h,k))  #输出数字所在行列
# fu(8)
# # #
#
#   #---本题考点：双层for 循环
# num=int(input("请输入一个数字："))
# lit = [[3,8 ,9],[6,11,2],[7,18,5]]
# for i in range(3):   #循环行
#     for j in range(3):  #循环列
#         if num == lit[i][j]: #if循环语句，按索引找出输入数字所在位置
#             h = i + 1       #索引加1就是所在位置
#             k = j + 1
# print("%d在第%d行,第%d列" %(num,h,k))  #输出数字所在行列
#
