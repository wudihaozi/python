import re
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())
# Batman
mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())
# Batwoman
