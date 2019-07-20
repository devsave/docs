表格以 __|__ 来划分各列，以 __-__ 来分隔表头和其他行。  
- **:--** :左对齐
- **--:** :右对齐
- **:-:** :居中对齐

<table>
    <tr>
        <th>Markdown写法</th>
        <th>HTML</th>
        <th>渲染效果</th>
    </tr>
    <tr>
        <td>
        |表格表头一|表格表头二|表格表头三|<br>
        |:--|:-:|--:|<br>
        |左对齐|居中对齐|右对齐|<br>
        |内容一|内容二|内容三|
        </td>
        <td>
            &lt;table><br>
                &nbsp;&nbsp;&nbsp;&nbsp;&lt;tr&gt;<br>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;th align="left"&gt;表格表头一&lt;/th&gt;<br>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;th align="center"&gt;表格表头二&lt;/th&gt;<br>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;th align="right"&gt;表格表头三&lt;/th&gt;<br>
                &nbsp;&nbsp;&nbsp;&nbsp;&lt;tr&gt;<br>
                &nbsp;&nbsp;&nbsp;&nbsp;&lt;/tr&gt;<br>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;td align="left"&gt;左对齐&lt;/td&gt;<br>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;td align="center"&gt;居中对齐&lt;/td&gt;<br>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;td align="right">右对齐&lt;/td&gt;<br>
                &nbsp;&nbsp;&nbsp;&nbsp;&lt;/tr&gt;<br>
                &nbsp;&nbsp;&nbsp;&nbsp;&lt;tr&gt;<br>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;td align="left"&gt;内容一&lt;/td&gt;<br>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;td align="center"&gt;内容二&lt;/td&gt;<br>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;td align="right"&gt;内容三&lt;/td&gt;<br>
                &nbsp;&nbsp;&nbsp;&nbsp;&lt;/tr&gt;<br>
            &lt;/table>
        </td>
        <td>
            <table>
                <tr>
                    <th align="left">表格表头一<th>
                    <th align="center">表格表头二<th>
                    <th align="right">表格表头三<th>
                </tr>
                <tr>
                    <td align="left">左对齐<td>
                    <td align="center">居中对齐<td>
                    <td align="right">右对齐<td>
                </tr>
                <tr>
                    <td align="left">内容一<td>
                    <td align="center">内容二<td>
                    <td align="right">内容三<td>
                </tr>
            </table>
        </td>
    </tr>
</table>