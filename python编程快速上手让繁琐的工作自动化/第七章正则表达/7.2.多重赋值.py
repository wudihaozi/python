
#多重赋值
import re

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My phone number is 415-555-4242')
areaCode, mainNumber = mo.groups()
print(areaCode)
print(mainNumber)

