# class myList(list):
#     # def __init__(self, *args, **kwargs):
#     #     super().__init__(*args, **kwargs)

#     def __add__(self, other):
#         print('__add__ is called')
#         return super().__add__(other)

#     def __iadd__(self, other):
#         print('__iadd__ is called')
#         return super().__iadd__(other)

# a = [1, 2]
# a += [3]
# a = a + [3]


# def append_element(var):
#     var += (3,)

# a = (1, 2)
# append_element(a)

# b = [1, 2]
# append_element(b)

# print("a = " + str(a))
# print("b = " + str(b))

# a = (1, 2, 3)
# a[0] = 2 # 错误，tuple不能修改元素

# b = [1, 2, 3]
# b[0] = 2 # 正确，list可以修改颜色

a = (1, 2)
b = (1, 2)

c = [1, 2]
d = [1, 2]

print(id(a))
print(id(b))
print(a == b)
print(id(c))
print(id(d))
print(c is d)

# However, for the sake of optimization (mostly) there are some exceptions 
# for small integers (between -5 and 256) and small strings (interned strings, 
# with a special length (usually less than 20 character)) 