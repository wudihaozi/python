import re
batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batman')
mo2 = batRegex.search('The Adventures of Batwoman')
mo3 = batRegex.search('The Adventures of Batwowowowoman')
print((mo1 == None))
# True
print(mo2.group())
# Batwoman
print(mo3.group())
# Batwowowowoman