import re

# 通配符
atRegex = re.compile(r'.at')
mo1 = atRegex.findall('THe cat in the hat set on the flat mat.')
print(mo1)
# ['cat', 'hat', 'lat', 'mat']

# 匹配所有字符
nameRegex = re.compile(r'First Name:(.*) Last Name:(.*)')
mo2 = nameRegex.search('First Name: Ai Last Name: Sweigart')
print(mo2.group(1))
# Ai
print(mo2.group(2))
# Sweigart

# 贪心模式（默认）和非贪心模式
nogreedyRegex = re.compile(r'<.*?>')
greedyRegex = re.compile(r'<.*>')
mo3 = nogreedyRegex.search('< To save man> for dinner.')
mo4 = greedyRegex.search('< To save man> for dinner.>')
print(mo3.group())
# < To save man>
print(mo4.group())
# < To save man> for dinner.>

#匹配换行

noNewLineRegex = re.compile('.*')
# .* 匹配换行以外的所有字符
mo5 = noNewLineRegex.search('Serve the public trust.\nProtect the innocent.')
print(mo5.group())
#  Serve the public trust.
NewLineRegex = re.compile('.*', re.DOTALL)
mo6 = NewLineRegex.search('Serve the public trust.\nProtect the innocent.')
print(mo6.group())
# Serve the public trust.
# Protect the innocent.