在代码前留出一个TAB或四个空格的缩进，会自动形成一个代码块，如果代码块在列表中，则需要提供两个TAB或八个空格的缩进。

    def func():
        print("hello world")

也可以使用 __\`\`\`(可指定语言)__ 包裹一段代码：

MarkDown写法：  
<pre>
```python
    def func():
        print("hello world")
```
</pre>

渲染效果：
```python
    def func():
        print("hello world")
```

如果在一个段落中插入函数，可以用反引号 __\`__  将其包裹：

Markdown写法：    
段落中的函数\`print('hello world');\`写法对不对?

渲染效果：  
段落中的函数`print('hello world');`写法对不对?