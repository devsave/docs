# Python实验室-装饰器-原理篇

### 前言
在Python代码库中我们经常能看到`@staticmethod`、`@classmethod`这样的标签写在函数或类的上方。这些标签都有一个共同的特征，有一个 **@** 在最前面，**@**就是我们今天的主要研究对象——装饰器(Decorator)[ [Python Wiki](https://wiki.python.org/moin/PythonDecorators#What_is_a_Decorator) ]. 在了解装饰器之前，符号'@' 显得神秘而强大，不了解这样一款python利器，略显可惜。
<!--more-->

### 简介
装饰器是Python在2.4版本引入的一个语法糖，采用了Decorator设计模式的思想，动态增强一个函数的功能而不需要改变被增强函数的实现，被增强函数的实现者可以专注于他的业务逻辑而无需关注增强的具体细节。常见的案例是给函数增加运行时间统计的功能，在业务函数运行前记录当前时间，在业务函数执行后计算运行时间。  

Java中也有个类似功能-注解(Annotation)，但是实现方式不一样。Python中的装饰器更多是增强一个函数的功能，被装饰的函数经过装饰后本身已经携带装饰器本身的实现；Java中的注解更多在于给类添加动态属性，需要额外的逻辑读取这些属性再进行相应地处理。

### 探索

让我们从一个最简单的例子开始：
```python
def decorate(func):
    def wrapper():
        print("Before func.")
        result = func()
        print("After func.")
        return result
    return wrapper
```
如上便定义了一个最简单的装饰器`decorate`, 它的功能仅仅是在被修饰函数调用前后分别打印两个字符串。我们先不要研究其实现，先实际操作试试。

在使用装饰器前，我们先定义一个简单的函数：
```python
def func():
    print("This is func.")

func()
```
这个函数的功能非常简单，调用时在控制台打印字符串"This is func."。
在函数上应用装饰器：
```python
**@decorate**
def func():
    print("This is func.")

func()
```

此时控制台输出结果如下：
Before func.
This is func.
After func.

结果表明，装饰器成功地在函数前后加入了新的功能，而函数func并没有什么显著的修改，用户并不会意识到被装饰函数在定义实现和使用上有什么差别。
我们分析一下为什么会有这样的结果，我们重新仔细看一下装饰器函数的实现细节：
```python
def decorate(func):
    def wrapper():
        print("Before func.")
        result = func()
        print("After func.")
        return result
    return wrapper
```
从装饰器的实现可以看出，在装饰器函数decorate内部定义了另外一个函数wrapper, 并且此函数作为装饰器函数decorate的结果被返回。注意：装饰器返回的结果是一个函数，因此可以被再次调用。
要理解装饰器，我们首先需要知道Python解析器是如何处理@符号的：
```python
@decorate
def func():
    print("This is func.")
```
在模块加载时，解析器会对@进行处理，额外增加一行代码，如下：
```python
def func():
    print("This is func.")

**func = decorate(func)**
```
函数func = decorate(func) 是在模块加载时执行，得到 func = wrapper, 因此，函数func的实际实现已被替换为wrapper的实现。
当我们调用func()，实际调用的是wrapper()，先打印"Before func."，再执行原来func，最后打印"After func."，至此我们得到如上结果。

装饰器可以一次定义多次使用：
```python
@decorate
def func1():
    print("This is func1.")

@decorate
def func2():
    print("This is func2.")

func1()
func2()
```
运行后输出结果：

Before func.
This is func1.
After func.
Before func.
This is func2.
After func.

至此，我们便已解开了装饰器的神秘面纱，装饰器借助一个'@'符号隐式实现了上述过程。
我们的探索是不是就到此结束了呢，没有，知识的复杂性并不仅仅在于原理，还在于其应用场景的复杂性。
后面我们会一步步揭秘装饰器在各种场景下的应用。

#### 被装饰函数无参数
```python
@decorator
target:
    pass
```
这里`@decorator`等价于`target = decorator(target)`, 从这个等式可以看出，实际上装饰器所做的工作就是将target所引用的函数替换为decorator的返回值。注意，这里的装饰器返回值应当（非必须）是一个可调用对象，且参数因尽量保持和被装饰函数一致（非必须），这样在用户使用时才不会引起困惑，用户也无需了解装饰器本身的实现细节。

调用target：
```python
target()
```
等价于：  
```python
decorator(target)()
```
这里`decoratror(target)`

#### 被装饰函数带参数
```python
@decorator
target(target_param1, target_param2):
    pass
```
调用target： 
```python
target(target_param1, target_param2)
```
等价于:  
```python
decorator(target)(target_param1, target_param2)
```
#### 装饰器带参数
```python
@decorator(decorator_param1, decorator_param2)
target(target_param1, target_param2):
    pass
```
调用target：
```python
target(target_param1, target_param2)
```
等价于:  
```python
decorator(decorator_param1, decorator_param2)(target)(target_param1, target_param2)
```
分析上面三个括号的调用时机：  
+ 函数：第一和第二个括号是在被装饰函数实例化的时候调用的，第三个括号是在用户代码中调用该函数时调用的。实际上，用户调用的都是装饰过的函数，只是函数名称一样，可以说是被偷梁换柱了。另外，第一和第二个括号只会被调用一次，第三个括号会被调用多次，取决于用户代码的使用;  第一个括号的调用实际上返回了真正的装饰器同时创建了一个闭包的环境，使得装饰器在运行时能够调用构建装饰器时传入的参数。
+ 类：第一和第二个括号在类实例化的时候调用(\__init__前)，第三个括号是类的实例被当做可调用对象调用的时候被调用(\__call__)的;  第一个括号的调用可以将装饰器的参数传入构造函数(\__init__),以便\__call__方法调用的时候使用。

### 函数装饰器
#### 无参数
```python
def func_decorator(func):
    def wrapper():
        print("Before decoration")
        response = func()
        print("After decoration")
        return response
    return wrapper


@func_decorator
def source_func():
    print("This is the source function.")


source_func()
```
运行结果：
```Shell
Before decoration
This is the source function.
After decoration
```
这里的`@func_decorator`等价于`source_func = func_decorator(source_func)`, 注意这里func_decorator返回的实际上是另一个函数wrapper, 所以最后一行实际调用的是`wrapper()`，打印结果证明了这一点。

#### 被装饰函数带参数
```python
def param_func_decorator(func):
    def wrapper(func_param1: int, func_param2: int):
        print("Before decoration")
        response = func(func_param1, func_param2)
        print("After decoration")
        return response
    return wrapper


@param_func_decorator
def source_param_func(func_param1: int, func_param2: int):
    print("This is the source function.")
    print("First parameter is: %d" % func_param1)
    print("Second parameter is: %d" % func_param2)


source_param_func(1, 2)
```
运行结果：  
```Shell
Before decoration
This is the source function.
First parameter is: 1
Second parameter is: 2
After decoration
```
这里的`@param_func_decorator`等价于`source_param_func=param_func_decorator(source_param_decorator)`, 返回函数wrapper；   
函数调用`source_param_func(1, 2)`等价于`wrapper(1, 2)`;

这里需要注意的是wrapper的参数列表通常包含被装饰函数所需要的所有参数，如果装饰器需要能应用在不同签名(参数类型、个数不一样)的函数上，可以使用可变参数列表。  
```python
def param_func_generic_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before decoration")
        response = func(*args, **kwargs)
        print("After decoration")
        return response
    return wrapper
```
可变参数可以将用户传入的参数透过装饰器完整地传入到业务函数中，使得装饰器可以应用于各种函数上。

#### 装饰器带参数
```python
def param_func_param_decorator(decorator_param1, decorator_param2):
    def wrapper(func):
        def inner(func_param1: int, func_param2: int):
            print("First decorator parameter: %d" % decorator_param1)
            print("Second decorator parameter: %d" % decorator_param2)
            print("Before decoration")
            response = func(func_param1, func_param2)
            print("After decoration")
            return response
        return inner
    return wrapper


@param_func_param_decorator(3, 4)
def source_param_func2(func_param1: int, func_param2: int):
    print("This is the source function.")
    print("First parameter is: %d" % func_param1)
    print("Second parameter is: %d" % func_param2)


source_param_func2(1, 2)
```
运行结果：
```shell
First decorator parameter: 3
Second decorator parameter: 4
Before decoration
This is the source function.
First parameter is: 1
Second parameter is: 2
After decoration
```
为了实现装饰器传参，装饰器的实现上会有两层嵌套，第一层用于接收传入的参数，第二层用于接收装饰的函数对象。在该例中，inner函数对象才是最终返回的对象。  
这里`@param_func_param_decorator(3,4)`等价于`source_param_func2=param_func_param_decorator(3, 4)(source_param_func2)`, 返回inner函数。`source_param_func2(1, 2)`等价于`inner(1, 2)`。

### 类装饰器
#### 无参数
```python
class ClsDecorator:
    def __init__(self):
        pass

    def __call__(self, func):
        def wrapper():
            print("Before decoration")
            response = func()
            print("After decoration")
            return response
        return wrapper


@ClsDecorator()
def source_func_cls():
    print("This is the source function.")


source_func_cls()
```
运行结果：
```shell
Before decoration
This is the source function.
After decoration
```
定义类装饰器时，通常要实现两个魔法方法\__init__和\__call__, 当需要装饰对象时类装饰器需要先被实例化，此时类装饰器的\__init__会被调用。类装饰器修饰被装饰对象时，它表现为一个可调用对象，\__call__方法会被调用，此函数需要返回一个包含装饰逻辑的可调用对象，此处即为wrapper，该可调用对象将在用户调用业务函数时被调用。类装饰器与函数装饰器本质上并没有什么区别，只是我们无法控制函数实例化过程， 我们拿到的都将是函数实例，而在类装饰器实例化时，我们可以传入参数。  

**注意：**如果类装饰器不带参数，也需要加上括号，因为需要构造一个类装饰器实例。@ClsDecorator**()**

#### 被装饰函数带参数
```python
class FuncParamClsDecorator:
    def __init__(self):
        pass

    def __call__(self, func):
        def wrapper(func_param1: int, func_param2: int):
            print("Before decoration")
            response = func(func_param1, func_param2)
            print("After decoration")
            return response
        return wrapper


@FuncParamClsDecorator()
def source_func_param_cls(func_param1: int, func_param2: int):
    print("This is the source function.")
    print("First parameter is: %d" % func_param1)
    print("Second parameter is: %d" % func_param2)


source_func_param_cls(1, 2)
```
运行结果：
```shell
Before decoration
This is the source function.
First parameter is: 1
Second parameter is: 2
After decoration
```
此处与函数装饰器行为类似，不再赘述。

#### 装饰器带参数
```python
class FuncParamClsParamDecorator:
    def __init__(self, decorator_param1, decorator_param2):
        self.decorator_param1 = decorator_param1
        self.decorator_param2 = decorator_param2

    def __call__(self, func):
        def wrapper(func_param1: int, func_param2: int):
            print("First decorator parameter: %d" % self.decorator_param1)
            print("Second decorator parameter: %d" % self.decorator_param2)
            print("Before decoration")
            response = func(func_param1, func_param2)
            print("After decoration")
            return response
        return wrapper


@FuncParamClsParamDecorator(3, 4)
def source_func_param_cls_param(func_param1: int, func_param2: int):
    print("This is the source function.")
    print("First parameter is: %d" % func_param1)
    print("Second parameter is: %d" % func_param2)
```
运行结果：
```shell
First decorator parameter: 3
Second decorator parameter: 4
Before decoration
This is the source function.
First parameter is: 1
Second parameter is: 2
After decoration
```
类装饰器带参数时实现区别于函数装饰器，装饰器参数可以借助于\__init__传入并存储于类实例中，在\__call__中可以使用，\__call__的实现也不需要包含两层嵌套。

### 装饰关系
| 装饰器 | 被装饰对象 |
| :---- :| :------: |
| 类装饰器 | 类 |
| 类装饰器|函数|
| 函数装饰器 | 类 |
|函数装饰器|函数|

实际上，从语义上来说，被装饰对象只需要是一个可调用对象应该都可以，但语法不一定都支持。

### 装饰函数
上述实例都是将装饰器应用于函数上，主要是在业务函数实例化时使用装饰器进行装饰，在用户代码中调用装饰后的函数，此处不再赘述。  
  
另外，装饰器还可以用于装饰类方法：  
```python
def param_func_generic_decorator(func):
    def wrapper(*args, **kwargs):
        print("args:")
        print(*args)
        print("kwargs:")
        print(**kwargs)
        print("Before decoration")
        response = func(*args, **kwargs)
        print("After decoration")
        return response
    return wrapper


class DecorateClassMethod:

    @param_func_generic_decorator
    def instance_method(self):
        print("Hi, I am a instance method.")


decorated_obj = DecorateClassMethod()
decorated_obj.instance_method()
```
运行结果：
```shell
args:
<__main__.DecorateClassMethod object at 0x000002668CE43AC8>
kwargs:

Before decoration
Hi, I am a instance method.
After decoration
```
与装饰函数没有本质的区别，只是被装饰的类的实例会作为第一个位置参数传入。

### 装饰类
除了将装饰器用于装饰函数，还可以用于装饰类(**注意：**此处是类，不是类的实例)
```python
def decorator_cls(cls):
    def wrapper(object_id: int):
        print("Before decoration.")
        obj = cls(object_id)
        print("After decoration.")
        return obj
    return wrapper


@decorator_cls
class SourceCls:
    def __init__(self, object_id: int):
        self.object_id = object_id
        print(self.object_id)


instance = SourceCls(10)
```
运行结果：
```shell
Before decoration.
10
After decoration.
```
当装饰器用于装饰类时，传入装饰器的参数将不是函数的实例，而是一个类对象，在装饰器中需要使用该类对象创建一个类的实例，并返回实例化后的对象。也就是说装饰器实际上装饰的是类的实例化过程。  

装饰类的装饰器也可以带参数：
```python
def decorator_param_cls(owner: str):
    def wrapper(cls):
        def inner(object_id: int):
            print("Before decoration.")
            obj = cls(object_id)
            obj.owner = owner
            print(obj.owner)
            print("After decoration.")
            return obj
        return inner
    return wrapper


@decorator_param_cls("Tony")
class SourceParamCls:
    def __init__(self, object_id: int):
        self.object_id = object_id
        print(self.object_id)

instance2 = SourceParamCls(10)
```
运行结果：
```shell
Before decoration.
10
Tony
After decoration.
```

### 多层嵌套装饰
装饰器返回的函数仍是可调用对象，因此可以进一步被装饰，多个装饰器叠加到一个函数上，不断赋予函数新的功能。
```python
def func_decorator1(func):
    def wrapper():
        print("Decorator 1")
        return func()
    return wrapper


def func_decorator2(func):
    def wrapper():
        print("Decorator 2")
        return func()
    return wrapper


@func_decorator2
@func_decorator1
def decorated_func():
    print("source function")


decorated_func()

```
运行结果：
```shell
Decorator 2
Decorator 1
source function
```
从上面的例子可以看出，当业务函数被调用时，会首先执行最后一个装饰器的逻辑，然后依次执行倒数第二个...至第一个装饰器。  

在装饰函数时是给业务函数不断包裹新的逻辑，由近至远，因此装饰完成后，暴露在最外层的是最后一个装饰器的逻辑，也将是最先执行的。  
  
叠加多个装饰器给了我们更多的想象空间，装饰器逻辑可以重复应用到不同的对象上面，同时不同的对象也可以根据需要通过叠加装饰器扩展各种功能。

### 偷梁换柱更彻底
```python
def func_decorator(func):
    def wrapper():
        response = func()
        return response
    return wrapper


@func_decorator
def source_func():
    pass


source_func()
print(source_func.__name__)
```
运行结果：
```shell
wrapper
```
注意最后一行，用户不仅调用了业务函数source_func(), 同时他查看了source_func函数对象的名字，这里漏出马脚了，显示了真正被执行函数的名字wrapper.  
  
有没有什么方法隐藏这些信息呢？ 有！借助于functools库：  
```python
from functools import wraps


def func_decorator(func):
    @wraps(func)
    def wrapper():
        response = func()
        return response
    return wrapper


@func_decorator
def source_func():
    pass


source_func()
print(source_func.__name__)
```
运行结果：
```shell
source_func
```
在传入的装饰函数上加上@wraps装饰器，该装饰器会把被装饰函数的元信息拷贝到装饰函数上，使得装饰函数看起来更像被装饰函数。 @wraps的实现目标还没有深究。

### 注意点
+ 装饰器中在调用被装饰函数时应当确保被装饰函数所需要的参数均存在，否则会调用失败；
+ 装饰器中是否一定需要调用被装饰的函数？不一定，可以根据需要调整调用逻辑，例如权限控制中，如果权限不满足，可以转而调用其他逻辑；
+ 装饰器是否一定返回一个新的函数？不一定，如果只是想在函数实例化时执行一次性操作，可以在装饰器中增加一段逻辑，同时返回原函数；