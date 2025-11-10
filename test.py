# 1. 执行简单代码
code = """
x = 10
y = 20
result = x + y
print(f"结果是: {result}")
"""
exec(code)

# 2. 使用全局和局部命名空间
global_namespace = {'a': 100}
local_namespace = {'b': 200}

code = """
c = a + b + 50
print(f"c = {c}")
"""

exec(code, global_namespace, local_namespace)
print("局部命名空间:", local_namespace)