import re

heroRegex = re.compile(r'Batman|Tina')
mo1 = heroRegex.search('Batman and Tina')
mo2 = heroRegex.search('Tina and Batman')
print(mo1.group())
print(mo2.group())