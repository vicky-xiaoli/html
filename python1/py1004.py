
# 一些四位数,百位数字都是3,十位数字都是6,并且它们既能被2整除,
# 又能被 3整除,求这样的四位数中最大的和最小的两数各是

# lis = []
# for i in range(1,10):   #循环千位，千位只能取1-10
#     for j in range(10):  #循环个位，取0-10
#         num = int(str(i) + "36" + str(j))   num数字，需要转换类型，字符串拼接
#         if num  % 2 == 0 and int((str(i) + "36" + str(j))) % 3 == 0:
#             lis.append(num)
# print(lis[0])
# print(lis[-1])



