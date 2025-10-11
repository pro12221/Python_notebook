# 输入
## 在python3中input功能会等待用户的输入，用户输入任何内容，都存成字符串类型，然后赋值给等号左边的变量名
username = input('请输入您的用户名：')
password = input('请输入您的密码：')

# 输出
## 格式化输出
# %s占位符：可以接收任意类型的值
# %d占位符：只能接收数字
print('亲爱的%s你好！你%s月的话费是%d，余额是%d' % ('tony', 12, 103, 11))


# 练习1：接收用户输入，打印成指定格式
name = input('your name: ')
age = input('your age: ')  # 用户输入18,会存成字符串18,无法传给%d
print('My name is %s,my age is %s' % (name, age))

