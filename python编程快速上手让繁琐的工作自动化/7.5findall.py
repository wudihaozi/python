import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
phoneNumRegex1 = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
mo1 = phoneNumRegex.search('Cell: 415-555-9999 work:212-555-0000')
mo2 = phoneNumRegex.findall('Cell: 415-555-9999 work: 212-555-0000')
mo3 = phoneNumRegex1.findall('Cell: 415-555-9999 work: 212-555-0000')
print(mo1.group())
# 415-555-9999 search 返回的是一个match对象
print(mo2)
# ['415-555-9999', '212-555-0000'] findall 返回的是一个字符串列表
print(mo3)
# [('415', '555', '9999'), ('212', '555', '0000')] 如果匹配模式是一个表达式 则返回字符串元组的列表
print(mo3[1][2])
# 0000 