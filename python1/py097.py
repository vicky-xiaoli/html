

#6输入一个三位整数，判断其是不是降序数如:531是降序数 百位>十位>个位   -----字符串索引取值判断排序
nu = input("请输入一个整数 ")
while len(nu) == 3 and nu.isdigit():
    a = nu[0]
    b = nu[1]
    c = nu[2]
    if a > b > c:
        print("这个数是降序")
        break
    else:
        print("这个数不是降序")
        break
else:
    print("错误，请输入三位整数")



# num = input("输入三位整数：")
# if len(num) == 3 and num.isdigit():   #num.isdigit判断输入的是数字
#     a = num[0]
#     b = num[1]
#     c = num[2]
#     if a > b > c:    #while也可以，用while时，条件成立后面需要加break结束语句
#         print("这个数是降序")
#     else:
#         print("这个数不是降序")
# else:
#     print("输入错误，请输入三位整数")