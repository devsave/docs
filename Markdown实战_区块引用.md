区块引用以符号 __'>'__ 标识于段落开始处，会在引用段落周边生成一个引用框，注意段内换行不会结束引用，因此，对一个段落只需要在开始处加上标签即可。

<table>
    <tr>
        <th>Markdown写法</th>
        <th>HTML</th>
        <th>渲染效果</th>
    </tr>
    <tr>
        <td>
            <p>这是第一个段落</p>
            <p>这是第二个段落</p>
            <p><strong>&gt;<strong> 这是一个引用段落</p> 
            <p>这是第三个段落</p>
        </td>
        <td>
            &lt;p&gt;这是第一个段落&lt;/p&gt;<br>
            &lt;p&gt;这是第二个段落&lt;/p&gt;<br>
            &lt;blockquote&gt;&lt;p&gt;这是一个引用段落&lt;/p&gt;&lt;/blockquote&gt;<br>
            &lt;p&gt;这是第三个段落&lt;/p&gt;<br>
        </td>
        <td>
            <p>这是第一个段落</p>
            <p>这是第二个段落</p>
            <blockquote><p>这是一个引用段落</p></blockquote>
            <p>这是第三个段落</p>
        </td>
    </tr>
</table>
