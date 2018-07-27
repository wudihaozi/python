缩写字母分类			表示
\d						0-9的任何数字
\D						除0-9以外的任何数字
\w                      任何字母、数字或下划线
\W						除字母、数字或下划线以外的字符
\s   					空格、制表符、换行符（匹配空白）
\S  					除空格、制表符、换行符以外的任何字符

import re

xmasRegexN = re.compile(r'[0-5]+\s\w+')
xmasRegexS = re.compile(r'\d+\s\w+')
x1 = xmasRegexS.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rigns, 4 birds, 3hens, 2 doves, 1 partridge')
x2 = xmasRegexN.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rigns, 4 birds, 3hens, 2 doves, 1 partridge')
print(x1)
# ['12 drummers', '11 pipers', '10 lords', '9 ladies', '8 maids', '7 swans', '6 geese', '5 rigns', '4 birds', '2 doves', '1 partridge']
print(x2)
# ['12 drummers', '11 pipers', '10 lords', '5 rigns', '4 birds', '2 doves', '1 partridge']

