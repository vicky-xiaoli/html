
# 下面是一个3*3的矩阵
# 3，8，9
# 6，11，2
# 7，18，5
# 实际上是一个二维列表
# [[3，8，9], [6，11，2], [7，18，5]]
# 通过键盘输入需要构造的矩阵维度，比如3*3, 2*2，并根据维度接收对应数量的数，构成矩阵(二维列表)
# lit = []
# n = int(input("请输入维度："))
# for nu in range(n):
#     lis = []
#     for num in range(n):
#         mu = int(input("第%d行，第%d列："  %(nu+1,num+1)))
#         lis.append(mu)
#     lit.append(lis)
# print(lit)