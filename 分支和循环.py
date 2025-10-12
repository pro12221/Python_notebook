# 几个例子
## 用户认证案例
# 用户认证程序的基本逻辑就是接收用户输入的用户名密码然后与程序中存放的用户名密码进行判断，判断成功则登陆成功，判断失败则输出账号或密码错误
username = "jason"
password = "123"
inp_name = input("请输入用户名：")
inp_pwd = input("请输入密码：")
if inp_name == username and inp_pwd == password:
    print("登陆成功")
else:
    print("输入的用户名或密码错误！")
# 通常认证失败的情况下，会要求用户重新输入用户名和密码进行验证，如果我们想给用户三次试错机会，本质就是将上述代码重复运行三遍，你总不会想着把代码复制3次吧。。。。
username = "jason"
password = "123"
# 第一次验证
inp_name = input("请输入用户名：")
inp_pwd = input("请输入密码：")
if inp_name == username and inp_pwd == password:
    print("登陆成功")
else:
    print("输入的用户名或密码错误！")
# 第二次验证
inp_name = input("请输入用户名：")
inp_pwd = input("请输入密码：")
if inp_name == username and inp_pwd == password:
    print("登陆成功")
else:
    print("输入的用户名或密码错误！")
# 第三次验证
inp_name = input("请输入用户名：")
inp_pwd = input("请输入密码：")
if inp_name == username and inp_pwd == password:
    print("登陆成功")
else:
    print("输入的用户名或密码错误！")


# 使用while循环
username = "jason"
password = "123"
# 记录错误验证的次数
count = 0
while count < 3:
    inp_name = input("请输入用户名：")
    inp_pwd = input("请输入密码：")
    if inp_name == username and inp_pwd == password:
        print("登陆成功")
        break
    else:
        print("输入的用户名或密码错误！")
        count += 1