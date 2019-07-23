# from functools import wraps

# def decorate(dec_param1):
#     def wrapper(func):
#         @wraps(func)
#         def inner(func_param):
#             print("%s Before func." % dec_param1)
#             result = func(func_param)
#             print("%s After func." % dec_param1)
#             return result
#         return inner
#     return wrapper

# @decorate("I am a decorator:")
# def func(func_param):
#     print("This is func. %s" % func_param)

# func('hello')
# print(func.__name__)


def decorate1(dec_param1):
    def wrapper(func):
        def inner(func_param):
            print("Decorate 1 start: %s" % dec_param1)
            result = func(func_param)
            print("Decorate 1 end: %s" % dec_param1)
            return result
        return inner
    return wrapper

def decorate2(dec_param2):
    def wrapper(func):
        def inner(func_param):
            print("Decorate 2 start: %s" % dec_param2)
            result = func(func_param)
            print("Decorate 2 end: %s" % dec_param2)
            return result
        return inner
    return wrapper

# @decorate2('hello')
# @decorate1("world")
def func(func_param):
    print("Func executed:%s" % func_param)

decorate2('hello')(decorate1('world')(func))('test')
# func('test')