# def func(input = []):
#     input.append(5)
#     return input

# print(func.__defaults__)
# func()
# print(func.__defaults__)
# func()
# print(func.__defaults__)

# print(id(func()))
# print(id(func.__defaults__[0]))
# print(type(func.__defaults__))


# def func( a = -89):
#     print(id(a))
#     pass

# func()
# print(id(func.__defaults__[0]))

# def func(input = None):
#     result = input if input is not None else []
#     result.append(5)
#     return result

# print(func())
# print(func())

class Default:
    def __init__(self, default = []):
        self.value = default
    
    def append(self):
        self.value.append(5)

    def print(self):
        print(self.value)

    def print_id(self):
        print(id(self.value))

def1 = Default()
def2 = Default()
def1.print()
def2.print()

def1.append()
def1.print()
def2.print()

def1.print_id()
def2.print_id()

print(id(Default.__init__.__defaults__[0]))