# 求1-2+3-4+5-6... 99的所有数的和
# 方法一：
# n = 0
# for i in range(1,100,2):  #循环1-100，每循环一次加2，也就是找出奇数
#     n = n + i #  将循环值加起来
# m = 0
# for j in range(0,100,2): #循环0-100，每循环一次加2，也就是找出奇数
#     m = m + j   #将循环值加起来
# print(n - m) #做减法
#
# # 方法二：
# n = 0
# m = 0
# for i in range(1,100):  #循环1-100
#     if i % 2 == 0:   #如果是偶数时
#        n = n + i   #求偶数和
#     else:
#         m = m + i  #求奇数和
# print(m-n)  #求差


# 元素分类
# 有如下值集合 [11,22,33,44,55,66,77,88,99,90]，将所有大于 66 的值保存至字典的第一个 key 中，将小于 66 的值保存至第二个 key 的值中。
# 即： {'k1': 大于 66 的所有值,'k2': 小于 66 的所有值}
# lit = [11,22,33,44,55,66,77,88,99,90]
# ke = []    #建一个表
# ke1 = []   #建一个表
# dic = {}   #建一个字典
# for i in lit:  #循环列表
#     if i >= 66:   #当大于等于66时
#         ke.append(i) #将大于66的值加入ke列表
#         dic["k1"] = ke #将ke给ki这个键
#     else:
#         ke1.append(i)
#         dic["k2"] = ke1 #将k2给k2这个键
# print(dic)  # 打印字典


# 自定义一个list，每暂停一秒输出一个元素(使用 time 模块的 sleep() 函数)
# from time import sleep         #调用time中的sleep
# lit = [11,22,33,44,55,66,77,88,99,90]  #建一个列表
# for i in lit:       #循环列表中的值
#     sleep(1)       #沉睡
#     print(i)


# # 自定义一个list,按相反的顺序输出列表的值 （不能使用reverse()方法）
# lit = [11,22,33,44,55,66]
# for i in lit[-1::-1]:
#     print(i)



