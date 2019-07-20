- 写法一：__\[链接名称]\(链接地址) 或 <链接地址>__ :

|Markdown写法|渲染效果|
|:--|:--|
|我是 __\[ Markdown实战系列 \](http://mp.toutiao.com/preview_article/?pgc_id=6715676812434735627)__|我是 [Markdown实战系列](http://mp.toutiao.com/preview_article/?pgc_id=6715676812434735627)|
|链接为：__\<http://mp.toutiao.com/preview_article/?pgc_id=6715676812434735627>__|链接为：<http://mp.toutiao.com/preview_article/?pgc_id=6715676812434735627>|
|Email是：__\<xxx@toutiao.com>__|Email是：<hello@toutiao.com>|

- 写法二：可以用变量标识网址: __\[链接名称]\[变量名称]__，在文档最后给出链接：  

|Markdown写法|渲染效果|
|:--|:--|
|Markdown实战系列 __\[Markdown实战系列]\[1]__|Markdown实战系列[Markdown实战系列][1]|
|Markdown实战系列 __\[Markdown实战系列]\[markdown]__|Markdown实战系列[Markdown实战系列][markdown]|

\[1]: http://mp.toutiao.com/preview_article/?pgc_id=6715676812434735627
\[markdown]: http://mp.toutiao.com/preview_article/?pgc_id=6715676812434735627

[1]: http://mp.toutiao.com/preview_article/?pgc_id=6715676812434735627  
[markdown]: http://mp.toutiao.com/preview_article/?pgc_id=6715676812434735627