## 字符串

#1、需要考虑引号嵌套的配对问题
msg = "My name is Tony , I'm 18 years old!" #内层有单引号，外层就需要用双引号
#2、多引号可以写多行字符串
msg1 = '''
        天下只有两种人。比如一串葡萄到手，一种人挑最好的先吃，另一种人把最好的留到最后吃。
        照例第一种人应该乐观，因为他每吃一颗都是吃剩的葡萄里最好的；第二种人应该悲观，因为他每吃一颗都是吃剩的葡萄里最坏的。
        不过事实却适得其反，缘故是第二种人还有希望，第一种人只有回忆。
      '''
print(msg)
print(msg1)
# 数字可以进行加减乘除等运算，字符串呢？也可以，但只能进行"相加"和"相乘"运算。
name = 'tony'
age = '18'
t1=name + age #相加其实就是简单的字符串拼接

t2 = name * 5 #相乘就相当于将字符串相加了5次
print(t1 + '\n' + t2)


## 列表

# 1、列表类型是用索引来对应值，索引代表的是数据的位置，从0开始计数
stu_names=['张三','李四','王五']
print(stu_names[0],stu_names[1],stu_names[2])

# 2、列表可以嵌套，嵌套取值如下
students_info=[['tony',18,['jack',]],['jason',18,['play','sleep']]]
print(students_info[0][2][0])


## 字典
# 1、字典类型是用key来对应值，key可以对值有描述性的功能，通常为字符串类型
person_info={'name':'tony','age':18,'height':185.3}
print(person_info["name"])
print(person_info["age"])
print(person_info["height"])
# 2、字典可以嵌套，嵌套取值如下
students=[
{'name':'tony','age':38,'hobbies':['play','sleep']},
{'name':'jack','age':18,'hobbies':['read','sleep']},
{'name':'rose','age':58,'hobbies':['music','read','sleep']},
]
print(students[1]["hobbies"][1])
