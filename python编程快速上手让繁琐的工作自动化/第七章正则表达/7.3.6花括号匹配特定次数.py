import re
haRegex = re.compile(r'(Ha){3,5}')
mo1 = haRegex.search('HaHaHa')
mo2 = haRegex.search('HaHaHaHaHa')
print(mo1.group())
# HaHaHa
print(mo2.group())
# HaHaHaHaHa