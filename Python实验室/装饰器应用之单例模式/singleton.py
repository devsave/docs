class Manager:
    def __init__(self):
        print("One manager is instantiated.")

    def who_am_i(self):
        print("My address is %s." % id(self))

manager1 = Manager()
manager2 = Manager()
manager1.who_am_i()
manager2.who_am_i()
print(manager1 == manager2)

# # 定义装饰器
# def singleton(obj_class):
#     instances = {}
#     def wrapper():
#         if obj_class in instances:
#             return instances.get(obj_class)
#         else:
#             obj = obj_class()
#             instances[obj_class] = obj
#         return obj
#     return wrapper

# # 使用装饰器
# @singleton
# class Manager:
#     def __init__(self):
#         print("One manager is instantiated.")

#     def who_am_i(self):
#         print("My address is %s." % id(self))

# manager1 = Manager()
# manager2 = Manager()
# manager1.who_am_i()
# manager2.who_am_i()
# print(manager1 == manager2)
