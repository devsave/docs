def decorate(dec_param1):
    def wrapper(func):
        def inner(func_param):
            print("%s Before func." % dec_param1)
            result = func(func_param)
            print("%s After func." % dec_param1)
            return result
        return inner
    return wrapper

@decorate("I am a decorator:")
def func(func_param):
    print("This is func. %s" % func_param)

func('hello')

