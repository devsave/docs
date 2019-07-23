# class Bird:
#     def __new__(cls):
#         print("__new__ is called.")
#         return super().__new__(cls)

#     def __init__(self):
#         print('__init__ is called.')

# a = Bird()
def decorate(obj_class):
    def wrapper():
        print('Pre func is called.')
        obj = obj_class()
        print('Post func is called.')
        return obj
    return wrapper

@decorate
class Bird:
    def __new__(cls):
        print("__new__ is called.")
        return super().__new__(cls)

    def __init__(self):
        print('__init__ is called.')

a = Bird()

# a = decorate(Bird)()