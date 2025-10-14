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


print("-------------------------------------------------------数据类型常用方法-------------------------------------------------")
# 字符串类型方法
str1="hello world"
## 正向和反向取值
print(str1[1],str1[-1])
## 切片(顾头不顾尾)
print(str1[0:2])
print(str1[0:3:2])# 取0-3，步长为2
print(str1[::-1])# 反向取出字符串

## strip移除字符串首尾指定的字符
str2=" **hel lo** "
print(str2.strip()) ## strip括号内无字符指定移除空格
str2="**hel lo**"
print(str2.strip("*")) # 指定括号内指定字符

## 切分split
str3="hello world"
print(str3.split())#括号内不指定字符，默认已空格作为切分符号
str4="127.0.0.1"
print(str4.split("."))#括号内指定字符,已.作为分割

## lower,upper
str5="Hello,World!"
print(str5.lower(),str5.upper())# 全部转换为大写或者小写

## startswith，endswith
str3 = 'tony jam'
# startswith()判断字符串是否以括号内指定的字符开头，结果为布尔值True或False
print(str3.startswith('t'))
# endswith()判断字符串是否以括号内指定的字符结尾，结果为布尔值True或False
print(str3.endswith('jam'))

## join操作
# 从可迭代对象中取出多个字符串，然后按照指定的分隔符进行拼接，拼接的结果为字符串
print('%'.join('hello')) # 从字符串'hello'中取出多个字符串，然后按照%作为分隔符号进行拼接
print('|'.join(['tony','18','read']) ) # 从列表中取出多个字符串，然后按照*作为分隔符号进行拼接

## replace
# 用新的字符替换字符串中旧的字符
str7 = 'my name is tony, my age is 18!'  # 将tony的年龄由18岁改成73岁
str7 = str7.replace('18', '73')  # 语法:replace('旧内容', '新内容')

# 可以指定修改的个数
str7 = 'my name is tony, my age is 18!'
str7 = str7.replace('my', 'MY', 1)  # 只把一个my改为MY


# 列表类型操作
## 按照索引修改指定位置的值
list1=["tony","18","read"]
list1[0]="mkie"
print(list1)
## 切片（同字符串）

## append
list1.append(1) # 在列表尾部追加元素
print(list1)

## extend
list1.extend([1,2,3]) # 一次性在列表尾部添加多个元素
print(list1)

## insert
list1.insert(1,'jack') # 在列表一号索引插入元素
print(list1)

## del
del list1[0] #删除0号索引对应元素
print(list1)

## pop默认删除最后一个元素并返回,括号内可以加索引来指定删除元素
test=list1.pop()
print(test)

## remove 括号内指定要删除的元素，没有返回值
list1.remove(1) # 重复的都删除
print(list1)

## reverse 颠倒列表内元素顺序
list1.reverse()
print(list1)

## sort 给列表排序，列表之间元素必须是相同数据类型
