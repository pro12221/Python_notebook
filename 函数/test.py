l = [1, [2, [3, [4]]]]

def f(lst):  # 添加参数
    for item in lst:
        if type(item) is list:
            f(item)  # 递归调用时传递参数
        else:
            print(item)

f(l)  # 调用时传递参数