
import zhuche_
import denglu_
#学号字典
user_Stu_id={}
#管理员密钥
admin =(12138)
#课程列表
course =['Python',
        'java',
        'web',
        'unity',
        'UI']
#学生选课集合
course_1=set()
def run():
    while True:
        print("""
    ^^^^^^*************^^^^^^
    欢迎来到中公选课系统
    1注册
    2登录
    3退出
    ^^^^^^*************^^^^^^""")
    #用户注册
        options=int(input("请输入要选择的选项\n"))
        if options == 1:
            zhuche_.zhuche()
        elif options == 2:
            denglu_.dengluhanshu()
        elif options == 3:
            print("欢迎再次登陆，再见！")
            break
        else:
            break
run()