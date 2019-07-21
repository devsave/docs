- 无序列表  
    无序列表可以以 **'-' , '+' 或 '\*'**  这三种符号任何一种作为列表标记，注意：**标签和文本之间必须保留一个空格**。

    |Markdown写法|HTML|渲染效果|
    |:--|:--|:--|
    |\* 列表项一<br>\* 列表项二<br>\* 列表项三|\<ul><br>\<li>列表项一\</li><br>\<li>列表项二\</li><br>\<li>列表项三\</li><br>\</ul>| <ul><li>列表项一</li><li>列表项二</li><li>列表项三</li></ul>|
 
- 有序列表  
    有序列表以数字加 __'.'__ 作为列表标记。

    |Markdown写法|HTML|渲染效果|
    |:--|:--|:--|
    |1\. 第一项<br>2\. 第二项<br>3\. 第三项|\<ol><br>\<li>第一项\</li><br>\<li>第二项\</li><br>\<li>第三项\</li><br>\</ol> | <ol><li>第一项</li><li>第二项</li><li>第三项</li></ol>|

- 嵌套列表  
    当一个列表中需要嵌套另一个列表时，子列表相对于父列表缩进一个TAB或者一个以上空格：

    |Markdown写法|HTML|渲染效果|
    |:--|:--|:--|
    |\* 列表项一<br>**\[TAB\]** 1\. 第一项<br>**\[TAB\]** 2\. 第二项<br>**\[TAB\]** 3\. 第三项<br>\* 列表项二<br>\* 列表项三|\<ul><br>\<li>列表项一<br>&nbsp;&nbsp;&nbsp;&nbsp;\<ol><br>&nbsp;&nbsp;&nbsp;&nbsp;\<li>第一项\</li><br>&nbsp;&nbsp;&nbsp;&nbsp;\<li>第二项\</li><br>&nbsp;&nbsp;&nbsp;&nbsp;\<li>第三项\</li><br>&nbsp;&nbsp;&nbsp;&nbsp;\</ol><br>\</li><br>\<li>列表项二\</li><br>\<li>列表项三\</li><br>\</ul>|<ul><li>列表项一<ol><li>第一项</li><li>第二项</li><li>第三项</li></ol></li><li>列表项二</li><li>列表项三</li></ul>|