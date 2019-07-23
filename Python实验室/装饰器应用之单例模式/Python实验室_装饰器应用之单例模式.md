# Python实验室 - 装饰器应用之单例模式

## 前言
前面我们研究了Python中的装饰器'@'的运行机制(详见[Python实验室](https://www.toutiao.com/i6716714866570166797/)的装饰器部分)，下面我们来介绍一些装饰器的精彩应用案例。本文主要探究利用装饰器来实现设计模式之单例模式。

## 背景
具有一定开发经验的读者应该都或多或少听到过由'四人帮'（Erich Gamma、Richard Helm、Ralph Johnson 和 John Vlissides ）总结的23种设计模式。这些模式对于特定的场景提供了一些通用的解决方案，这些方案经过了实践的检验，因此广泛应用于实际的开发生产过程中。
单例模式是其中一种设计模式，它保证了一个类最终只会有一个实例，且提供了全局访问点，是全局变量的一个很好替换方案。

## 实践
首先我们准备一个类：
```python
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
```
运行结果：   
One manager is instantiated.  
One manager is instantiated.  
My address is 2821183211392.  
My address is 2821183211280.   
False   

从运行结果可以看出，我们Manager类的\_\_init\_\_方法两次被调用，也即实例化出了两个对象，同时两个对象也告诉我们它们具有不同的内存地址。

下面我们来看一下利用装饰器来实现单例模式：
```python
# 定义装饰器
def singleton(obj_class):
    instances = {}
    def wrapper():
        if obj_class in instances:
            return instances.get(obj_class)
        else:
            obj = obj_class()
            instances[obj_class] = obj
        return obj
    return wrapper

# 使用装饰器
@singleton
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
```
运行结果：  
One manager is instantiated.  
My address is 1596847748376.  
My address is 1596847748376.  
True  

从运行结果可以看出，虽然我们试图实例化两个Manager对象，但是\_\_init\_\_只被调用了一次，manager1与manager2拥有相同的内存地址，且它们告诉我们它们相同，其实，他们是同一个对象。

为什么会有这样的效果? 这就是singleton装饰器发挥的作用：
```python
def singleton(obj_class):
    instances = {}
    def wrapper():
        if obj_class in instances:
            return instances.get(obj_class)
        else:
            obj = obj_class()
            instances[obj_class] = obj
        return obj
    return wrapper
```
从装饰器的实现可以看出装饰器内部维护了一个字典，记录了类与对应实例的映射，当收到一个实例化请求时，装饰器会查看它拥有的字典，如果不存在请求类对应的实例，则创建一个新的实例并登记到字典中；如果这个类已经有一个实例登记在册，则直接返回登记的实例，如此保证了一个类只会有一个实例。同时，从用户的角度来看，如果用户想找到一个单例类的实例，也非常容易，和重新创建一个新实例一样。

```python
@singleton
class Manager:
    def __init__(self):
        print("One manager is instantiated.")

    def who_am_i(self):
        print("My address is %s." % id(self))
```
从装饰器的使用来看，单例类与普通类的区别仅仅是在最开始的位置插入了一个单例装饰器声明，类内部实现并没有任何修改，这正是装饰器带来好处-无侵入地增强了修饰对象的功能。