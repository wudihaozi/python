? 匹配零次或一次前边的分组
* 匹配零次或多次前边的分组
+ 匹配一次或多次前边的分组
{n}匹配n次前边的分组
{n,}匹配n次或者更多次前边的分组
{,m}匹配零次到m次前边的分组
{n,m}匹配至少n次、至多m次前边的分组
{n,m}?或*或+ 对前边的分组进行非贪心算法匹配
^spam 意味着字符串必须以spam开始
spam$ 意味着字符串必须以spam结尾
.匹配所有字符,换行符除外
\d \w \s 分别匹配数字 单词 空格
\D \W \S 分别匹配数字 单词 空格 之外的字符
[abc0-9]匹配方括号里的任意字符
[^abcA-Z]匹配方括号之外的任意字符