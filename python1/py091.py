#从键盘接收一个输入，输入成绩，当输入的成绩在60以下时，打印不及格，60-79打印及格，80及以上打印优秀
degree = int(input("请输入成绩：")) #必须转换成整型，字符型是一个一个比较，不合适此处。→数字比较都要转换成数字
# if degree >= 80:      #if语句的运用
#     print("优秀")
# elif degree >= 60:
#     print("及格")
# else:
#     print("不及格")

##2根据上题循环输入成绩
# while True:     #判断真假，死循环的运用
#     degree = int(input("请输入成绩："))
#     if degree >= 80:
#         print("优秀")
#     elif degree >= 60:
#         print("及格")
#     else:
#         print("不及格")