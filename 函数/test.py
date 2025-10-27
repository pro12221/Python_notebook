def func(start,stop,step):
    while start < stop:
        yield start
        start += step

start = func(1, 5, 3)
for i in start:
    print(i)

print(type(start))
print(type(func))