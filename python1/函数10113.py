

# 有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？

# num = input("请输入一个三位数：")
# bw = num[0]
# sw = num[1]
# gw = num[2]

lit = []
for i in [1,2,3,4]:
    for j in [1,2,3,4]:
        for k in [1, 2, 3, 4]:
            if i!= j and j != k:
                print(str(i) + str(j) + str(k))

