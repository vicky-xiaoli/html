
# 1.写出下列表达式的结果：
# 1)已知x =3, 那么执行x+=6之后，x的值为？  9
# 9
# 2)[3] in [1,2,3,4]
# false

# 3)任意长度的列表、元组、字符串的最后 一个元素下标为？ -1
# -1

# 4)list(range(1,10,5))值？
# 1,6

# 5)d = {'a': 1, 'b': 2}, d.setdefault('x','yes') yes
# d = {'a': 1, 'b': 2}
# print(d.setdefault('x','yes'))

# 6)求li = [3,6,9,11,15] 的长度  # print(len(li))
# li = [3,6,9,11,15]

# 7)字典对象中返回字典中“键”列表的方法是？  # dcit.keys()


# 8)1<2<3结果   true
# print(1<2<3)

# 9)li = [3,5,7], li.append([1,2])  #[3,5,7,[1,2]]
# li = [3,5,7]
#

# 10)无穷循环while True:的循环体中可用什么语句退出循环？ # break


# 2.写出下列代码的运行结果  #543
# def fun(number):
#     number = number//100
#     if number == 0:
#         return
#     print(number)
# fun(54321)


# prime_number=[]         2357
# for i in range(2,11):
#     counter = 0
#     for j in range(1,i):
#         if i % j == 0:
#             counter += 1
#     if counter == 1:
#         prime_number.append(i)
# print(prime_number)


# 3.字符串操作
# strinfo=" hello,where are you from? Are you American? do you from china? no,I am from Australian "
# 1) 统计出其"re"和空格各出现的次数
# print(strinfo.count(" "))
# print(strinfo.count("re"))

# 2) 将字符串中所有"om"替换成"en"
# print(strinfo.replace("om","en"))

# 3) 将字符串以"？"号进行分割，并保存为列表
# print(strinfo.split("?"))

# 4）去掉前后空格
# print(strinfo.strip())

# 5) 组成笑脸Y(^_^)Y  # print("Y(^ _ ^)Y")




# li=['h', 'e', 'l', 'l', 'o'] #写出每一步单独操作的结果或者方法。
#print(li [1:])

# 2) li [:-4]
# print(li [:-4])

# 3) 在两个“l”元素之间插入一个"x"
# (li.insert(3,"x"))
# print(li)

# 4) 得出['o', 'l', 'l', 'e', 'h']
# li.reverse()
# print(li)

# 5) 获取"e"元素的下标
# print(li.index("e"))

# 5. 有一个文本文件“person.txt”，内容为:
# 编写代码读取文件中的内容，打印出如下结果，
# 张三的年龄为30
# 李四的年龄为20
# 并将该结果写入一个新的文件“detail.txt”。




# 6.谈谈你理解的类、对象、属性、方法、继承？


# 7.写一个Person类和一个Student类，要求能体现类继承的所有要素。


# 8.实现对列表li=[18,56,24,21,33]的冒泡排序。
# li=[18,56,24,21,33]
# for i in range(len(li) -1):
#     for j in range(len(li) -1-i):
#         if li[i] > li[i + 1]:
#             li[i],li[i+1] = li[i+1],li[i]
# print(li)

# 9.元组和列表的区别



# 10.常用的 Python 标准库都有哪些?


# 11.Python面向对象中的继承有什么特点？


# 12.什么是异常?


