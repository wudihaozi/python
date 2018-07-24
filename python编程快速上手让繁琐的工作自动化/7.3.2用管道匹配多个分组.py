import re

heroRegex = re.compile(r'Batman|Tina')
mo1 = heroRegex.search('Batman and Tina')
# search 只匹配一次
mo2 = heroRegex.search('Tina and Batman')
print(mo1.group())
# Batman
print(mo2.group())
# Tina

#匹配多个模式中的一个
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo3 = batRegex.search('Batmobile lost a wheel')
print(mo3.group())
# Batmobile
print(mo3.group(1))
# mobile
