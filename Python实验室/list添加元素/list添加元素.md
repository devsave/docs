# Python实验室「a += [3] 和 a = a + [3]真的等同吗？」

## 前言
上一文我们在介绍Python[可变变量与不可变变量](https://www.toutiao.com/i6717525334629024263/)时，遗留了一个问题：

```python
def append_element1(var):
    var += [3]

def append_element2(var):
    var = var + [3]

a = [1, 2]
b = [1, 2]
append_element1(a)
append_element2(b)
print('a = %s' % str(a))
print('b = %s' % str(b))
```
运行结果：  
a = [1, 2, 3]  
b = [1, 2] 

熟悉其他语言的读者碰到这样的结果一定会有些困惑。我们在介绍'+='运算符时通常解释'+='是'='和'+'运算符组合的简写，其含义一样，结果也应该一样。但是，它们在Python中表现出了一定的差异性，本文即对此问题进行探究。

## 探索
为什么会出现这样的差异性？要理解这个问题，我们首先必须理解Python究竟是如何处理'+='和'+'运算符的。

Python处理运算符时都是将运算符映射为对象对应的函数进行处理。其中'+'运算符将被映射为'\_\_add\_\_'方法，'+='运算符被映射为'\_\_iadd\_\_'方法。理解这两个方法实现的差异，我们就能解释上述问题的原因了，下面我们研究下这两个方法。

参考Python帮助文档，\_\_iadd\_\_属于原地(in-place)方法，顾名思义，**计算结果将直接更新到对象自身**，并将自身返回；于此相反，\_\_add\_\_属于非原地方法，修改不会更新自身，而是创建一个新的对象并返回。

是不是真的是这样呢，我们写个简单的例子试验一下：
```python
a = [1, 2]
b = [1, 2]

print('The id of a: %d' % id(a) )
a += [3]
print('The id of a: %d' % id(a) )
print('a = %s' % str(a))

print('The id of b: %d' % id(b) )
b = b + [3]
print('The id of b: %d' % id(b) )
print('b = %s' % str(b))
```
运行结果：  
The id of a: 2121104837832  
The id of a: 2121104837832  
a = [1, 2, 3]  
The id of b: 2121105443784  
The id of b: 2121104837704  
b = [1, 2, 3]  

从结果看出，列表a在计算前后其id没变，增加了新元素'3'，所以列表a实际上是在它自身中插入了新元素；而列表b在计算前后，它的id发生了变化，说明b已经指向了新创建的列表，且指向的新列表中包含了新元素'3'。

让我们更进一步，看看b计算前所指列表是不是被修改了：

```python
b = [1, 2]
c = b

print('Before calculation')
print('The id of b: %d' % id(b))
print('The id of c: %d' % id(c))
b = b + [3]
print('After calculation')
print('The id of b: %d' % id(b) )
print('The id of c: %d' % id(c))
print('b = %s' % str(b))
print('c = %s' % str(c))
```
运行结果：  
Before calculation 
The id of b: 2373282385096  
The id of c: 2373282385096   
After calculation  
The id of b: 2373281327368  
The id of c: 2373282385096  
b = [1, 2, 3]  
c = [1, 2]   

为了能找到b原来所指列表，在运算前，我们定义`c = b`，观察b和c的id可知它们指向同一个列表。
运算后，b和c的id不再相同，b指向了新的列表并包含了新插入的元素，而c保持不变，可见原列经过'='和'+'运算后并未被修改。

回到开始我们提出的问题，由于`var = var + [3]`实际上创建并修改了新的列表，由参数传入的列表不会发生修改，也即函数外所引用的列表不会发生修改。因此，在函数内使用'='和'+'的组合时，我们需要明白这里将会发生什么。

如果我们把列表换成元组会怎么样呢？
```python
b = (1, 2)
c = b

print('Before calculation')
print('The id of b: %d' % id(b))
print('The id of c: %d' % id(c))
b += (3, )
print('After calculation')
print('The id of b: %d' % id(b) )
print('The id of c: %d' % id(c))
print('b = %s' % str(b))
print('c = %s' % str(c))
```
运行结果：  
Before calculation  
The id of b: 1723124645128  
The id of c: 1723124645128  
After calculation  
The id of b: 1723123982624  
The id of c: 1723124645128  
b = (1, 2, 3)  
c = (1, 2)  

观察元组，尽管我们使用的是'+='运算符，但是，计算前后，b所指向的元组id仍发生了变化，似乎与我们上面分析列表的结果不符。我们查看元组实现的方法：  
\>>> dir(tuple)  
\['\_\_add_\_', '\__class__', '\_\_contains\_\_', ...]  
从原组包含的方法可以看出，元组并没有实现\_\_iadd\_\_方法，实际上，对于不可变变量（包括int，bool，str等)都不会实现\_\_iadd\_\_，避免修改变量本身。Python解析器在碰到'+='时，如果对象没有实现\_\_iadd\_\_，就会默认调用\_\_add\_\_方法，也即返回一个计算后的新对象。

## 总结
- '+='运算符映射为'\_\_iadd\_\_'方法（i为in-place的缩写），计算后会以结果更新对象自身；
- '+'运算符组合映射为'\_\_add\_\_'方法，计算后返回一个新对象包含计算结果，对象自身不会被更新；
- 不可变对象不会实现'\_\_iadd\_\_'方法，Python解析器在遇到'+='运算符是将会默认调用\_\_add\_\_方法。