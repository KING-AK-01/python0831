# a = 1
# while a <101:
#     print(a)
#     a = a + 1

# b = 0
# a = 1
# while a < 101:
#     # print(b+a)
#     b = a+b
#     a = a + 1
# 乘积计算
# print(b)
# b = 1
# a = 1
# while a < 11:
#     b = a * b
#     a = a + 1
#     print(b)

# a = 0
# b = 0
# while a < 101:
#     b = a + b
#     a = a + 2
#     print(b)
#
# a = 1
# b = 0
# while a < 101:
#     if a%2==0:
#        b = b - a
#     else:
#         b = b + a
#     a = a + 1
# print(b)
# a = 0
# while a < 10:
#     a = a+1
#     if a ==6 or a==7:
#         continue
#     print(a)
# else:
#     print('while循环正常结束执行else下的代码')
#

# print('欢迎登陆毒奶粉充值平台')
# a = 0
# while  a < 5:
#     mm = '123'1
#     x = input('请输入密码\n')
#     if x == '123':
#         print('登陆成功')
#         break
#     else:
#         a+=1
#         print('密码错误请重新输入')
# else:
#     print('一小时后再试')


# mima = '123456'
# zhanghao = '00'
# a = 0
# while a < 5:
#     username = input('请输入账号：')
#     password = input('请输入密码：')
#     # 登录成功处理
#     if mima == password and zhanghao==username:
#         print('密码输入正确，登陆成功\n正在跳转界面，请等待.....')
#         break
#     else:
#         print('密码输入错误，请重新输入')
#         print('数入次数剩余',4-a,"次")
#         a = a + 1
#
# else:
#     print('账户被锁死，请到柜台办理相关业务')

"""
练习：买票进火车站需求:
(1)定义一个 has_ticket 车票，表示是否有车票，定义一个 knife_length 刀的长度，
(2)检查火车票，是否满足，否则不让上火车
(3)检查行李箱，是否有违法品，如果刀子长度超过 20cm 不让上火车
"""
# print('欢迎来到火车站\n您是否有车票')
# has_ticket =input('有车票请按:y,无车票请按:n,\n')
# if has_ticket == 'y':
#     print('请收好车票进行安检')
# else:('请购票后进站')
# knife = input('是否携带刀具：\n有:yes\n:无:no')
# if knife == 'no':
#     print('行李没有违禁品请进站')
# else:
#     print('您的行李有刀具请打开检查')
# length=int(input('请输入刀具长度'))
# if length > 20:
#     print('刀具超过规定长度未通过安检')
# else:
#     print('请进站上车')



"""
100-200之间  那些数字可以同时被7和9整除
这些数字总共有多少个
"""
# a=100
# while a <200:
#     # print(a)
#     a=a+1
#
#     if a % 7 ==0 and a%9==0:
#         print(a)
'''
a=int(input("请输入一个三位数：")) 
# 获得个位数
b=a%10
# 获得十位数
c=a//10%10 
# 获得百位数
d=a//100%10
 f=b*100+c*10+d print(f)
'''
'水仙花数 三位数 个位**3+十位**3+百位**3 = 本身'#每个数的立方
# print(1**3 + 5**3 + 3**3)

#100-999所有的水仙花数
# a = 100
# while a <999:
#     #print(a)
#     a = a + 1     #拆分后得到的
#     b = a % 10    #个位数
#     c=a//10%10    #十位数
#     d=a//100%10   #百位数
#     if a  == b**3+c**3+d**3:
#       print(a)
























