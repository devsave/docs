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
我们的探索是不是就到此结束了呢，没有，知识的复杂性并不仅仅在于原理，还在于其复杂的应用场景，后面我们会一步步揭秘装饰器在各种场景下的应用。