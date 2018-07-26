import re

beginWithHello = re.compile(r'^Hello')
endWithNumber = re.compile(r'\d$')
x = beginWithHello.search('Hello world')
y = endWithNumber.search(r' My number is 43')
z = endWithNumber.search(r'My number is three')
print(x.group())
# Hello
print(y.group())
# 3
print(z == None)
# True