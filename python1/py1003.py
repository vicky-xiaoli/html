
# 实现登录，账号名为admin，密码123，则提示“登录成功”，如果账号或者密码错误，
# 则提示“账号名或密码错误”并允许重新输入用户名和密码，如果3次登录失败，则提示“登录失败”并退出程序。

# count = 0
# while True:
#     nu = input("请输入用户名：")
#     pswd = input("请输入密码：")
#     if nu == "admin" and pswd == "123":
#         print("登陆成功")
#         break
#     else:
#         count = count + 1
#         if count == 3:
#             print("退出程序")
#             break
#         print("用户名密码错误")

# #方法二 因为已知循环次数，所以推荐用for
# for i in range(3):
#     nu = input("请输入用户名：")
#     pswd = input("请输入密码：")
#     if nu == "admin" and pswd == "123":   #循环的时候，如果账号密码正确，直接提示登陆成功，结束循环
#         print("登陆成功")
#         break
#     else:
#         if i < 2:
#             print("用户名密码错误")  否则，当循环次数小于第三次时，输出用户名喵喵错误
#         else:
#             print("退出程序")  循环第三次是，输出退出程序










