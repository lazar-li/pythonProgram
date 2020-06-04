#装饰器的总结     装饰器就是对函数 或者 类进行扩充  扩充之后在返回或者函数类  因此在调用函数的时候  就是一个新的函数 或者类


#1  装饰器自身为函数


# 装饰器为函数  不带参数


# from time import sleep as sleeping
# from time import time as nowTime
#
# from functools import wraps
#
# #装饰器为函数
# def timeit(func):
#     @wraps(func)
#     def wrap(*args,**kwargs):
#         start = nowTime()
#         ret = func(*args,**kwargs)
#         print(nowTime()-start)
#         return ret
#     return wrap

# #装饰的对象为函数
#
# @timeit
# def sleep(n):
#     sleeping(n)
#     print("我睡了{}".format(n))
#     return n
#
# #调用装饰后的sleep函数
#
#
# sleep(5)
# print(sleep.__name__)
#

# _______________________________________________________________
# print_msg是外围函数
# def print_msg1():
#     msg = "梁子欧把111"
#
#     # printer是嵌套函数
#     def printer():
#         # msg = "lazar"
#         print(msg)
#
#     return printer
#
#
# # 这里获得的就是一个闭包
# closure = print_msg1()
# # 输出 I'm closure
# closure()
#


#--------------------------------------------------------------
# python 程序题
# import functools
#
#
# def log(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         print('call %s():' % func.__name__)
#         print('args = {}'.format(*args))
#         return func(*args, **kwargs)
#
#     return wrapper
#
#
# @log
# def test(p):
#     print(test.__name__ + " param: " + p)
# @log
# def lazar(s):
#     print("lazar"+s)
#
# # test("I'm a param")
# lazar("李ianzibba")


#带有参数的装饰器
import functools
def log_with_param(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kwargs):
            print("cass %s" % func.__name)
            print("args = {}".format(*args))
            print("log_param = {}".format(text))
            return func(*args,**kwargs)
        return wrapper()
    return decorator

@log_with_param("lazar")
def lazar(p):
    print(lazar.__name__)
    
