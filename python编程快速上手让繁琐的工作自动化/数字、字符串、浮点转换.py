str()   转换成字符串
int()   转换成整数
float() 转换成浮点型 

int() 的值不能是字符串,浮点数转换成整型直接舍弃小数部分，不进行四舍五入。

>>>int('99.99')
Traceback (most recent call last):
  File "<input>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '99.99'


>>>str(0)
'0'
>>>str(-3.14)
'-3.14'
>>>int('42')
42
>>>int('99')
99
>>>int(1.25)
1
>>>int(1.999)
1
>>>float('3.14')
3.14
>>>float(10)
10.0