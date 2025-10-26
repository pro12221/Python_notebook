from functools import wraps
from idlelib.debugobj import myrepr


def file(engine):
    def auth(func):
        def wapper(*args,**kwargs):
            username=input("input username").strip()
            password=input("input pw").strip()
            if engine=="mysql":
                if username=="wsa" and password=="123":
                    res=func()
                    return res
                else:
                    print("error")
            else:
                print("error")

        return wapper
    return auth


@file('mysql') # index=auth的内存地址(index)
def index():
    print("from index")

print(index)