# def say_hello():
#     hello = 'hello'
#     def inner():
#         print(hello)
#     return inner

# f = say_hello()
# f()

# def show_content():
#     content = [1, 2, 3]

#     def inner():
#         nonlocal content
#         content.append(5)
#         print(content)
#     return inner

# f1 = show_content()
# f1()
# f2 = show_content()
# f2()



def get_content():
    content = [1, 2]
    def show_content():
        nonlocal content

        def inner():
            nonlocal content
            print(content)
            content.append(5)
            print(content)
        return inner
    return show_content

f = get_content()
f1 = f()
f1()
f2 = f()
f2()