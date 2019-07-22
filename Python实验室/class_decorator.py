# class Add:
#     def __init__(self, value1):
#         self.value1 = value1
    
#     def __call__(self, value2):
#         return self.value1 + value2

# add = Add(1)
# result = add(3)
# print(result)

# # 无参类装饰器修饰无参函数
# class Decorate:
#     def __init__(self):
#         pass

#     def __call__(self, func):
#         def wrapper():
#             print("Pre func call.")
#             result = func()
#             print("Post func call.")
#             return result
#         return wrapper

# decorate = Decorate()

# # 修饰
# @decorate
# def func():
#     print('Func is called.')

# # 使用
# func()

# 定义装饰器
# class Decorate:
#     def __init__(self):
#         pass

#     def __call__(self, func):
#         def wrapper():
#             print("Pre func call.")
#             result = func()
#             print("Post func call.")
#             return result
#         return wrapper


# # 修饰函数
# @Decorate()
# def func():
#     print('Func is called.')

# # 使用函数
# func()

# # 定义装饰器
# class Decorate:
#     def __init__(self, func):
#         self.func = func

#     def __call__(self):
#         print("Pre func call.")
#         result = self.func()
#         print("Post func call.")
#         return result


# # 修饰函数
# @Decorate
# def func():
#     print('Func is called.')

# # 使用函数
# func()

# class decorate:
#     def __init__(self, func):
#         self.func = func

#     def __call__(self, func_param):
#         print("Pre func call.")
#         result = self.func(func_param)
#         print("Post func call.")
#         return result

# # 修饰
# @decorate
# def func(func_param):
#     print('Func is called. %s' % func_param)

# # 使用
# func('hello')

# 无参类装饰器修饰带参函数
# # 定义装饰器
# class Decorate:
#     def __init__(self):
#         pass

#     def __call__(self, func):
#         def wrapper(func_param):
#             print("Pre func call.")
#             result = func(func_param)
#             print("Post func call.")
#             return result
#         return wrapper


# # 修饰函数
# @Decorate()
# def func(func_param):
#     print('Func is called. %s' % func_param)

# # 使用函数
# func('hello')

# # 定义
# class Decorate:
#     def __init__(self, func):
#         self.func = func

#     def __call__(self, func_param):
#         print("Pre func call.")
#         result = self.func(func_param)
#         print("Post func call.")
#         return result

# # 修饰
# @Decorate
# def func(func_param):
#     print('Func is called. %s' % func_param)

# # 使用
# func('hello')


# # 带参类装饰器修饰带参函数
# class decorate:
#     def __init__(self, des_param):
#         self.des_param = des_param

#     def __call__(self, func):
#         def wrapper(func_param):
#             print("Pre func call. %s" % self.des_param)
#             result = func(func_param)
#             print("Post func call. %s" % self.des_param)
#             return result
#         return wrapper

# # 修饰
# @decorate("Decorator")
# def func(func_param):
#     print('Func is called. %s' % func_param)

# # 使用
# func('hello')


# class Decorate:
#     def __init__(self):
#         pass

#     def __call__(self, func):
#         def wrapper(func_param):
#             print("Pre func call.")
#             result = func(func_param)
#             print("Post func call.")
#             return result
#         return wrapper

# # 实例化一个对象
# decorate = Decorate()

# # 修饰函数
# @decorate
# def func(func_param):
#     print('Func is called. %s' % func_param)

# # 使用函数
# func('hello')

# # 定义装饰器
# class Decorate:
#     def __init__(self, dec_param):
#         self.dec_param = dec_param

#     def __call__(self, func):
#         def wrapper():
#             print("Pre func call. %s" % self.dec_param)
#             result = func()
#             print("Post func call. %s" % self.dec_param)
#             return result
#         return wrapper


# # 修饰函数
# @Decorate("Decorator")
# def func():
#     print('Func is called.')

# # 使用函数
# func()

# # 使用函数
# func('hello')

# 定义装饰器
# class Decorate:
#     def __init__(self, dec_param):
#         self.dec_param = dec_param

#     def __call__(self, func):
#         def wrapper(func_param):
#             print("Pre func call. %s" % self.dec_param)
#             result = func(func_param)
#             print("Post func call. %s" % self.dec_param)
#             return result
#         return wrapper


# # 修饰函数
# @Decorate("Decorator")
# def func(func_param):
#     print('Func is called. %s' % func_param)

# # 使用函数
# func('hello')

# # 定义装饰器
# class Decorate:
#     def __init__(self, dec_param):
#         self.dec_param = dec_param

#     def __call__(self, func):
#         def wrapper(*args, **kwargs):
#             print("Pre func call. %s" % self.dec_param)
#             result = func(*args, **kwargs)
#             print("Post func call. %s" % self.dec_param)
#             return result
#         return wrapper


# class Hello:
#     def __init__(self):
#         self.hello = 'hello'

#     @Decorate("Decorator")
#     def func(self, param):
#         print(self.hello + param)

# # 使用函数
# hello = Hello()
# hello.func("world")

class Decorate:
    def __init__(self):
        pass

    def __call__(self, func):
        def wrapper(func_param):
            print("Pre func call.")
            result = func(func_param)
            print("Post func call.")
            return result
        return wrapper

# 实例化一个对象
decorate = Decorate()

# 修饰函数
@decorate
def func(func_param):
    print('Func is called. %s' % func_param)

# 使用函数
func('hello')