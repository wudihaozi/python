
# 匹配结果分组
import  re

phoneNumTegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
mo = phoneNumTegex.search('My number is 415-555-4242.')
print('Phone number found: ' + mo.group())

print(mo.group(0))
# 415-555-4242
print(mo.group(1))
# 415
print(mo.group(2))
#  555
print(mo.group(3))
# 4242
print(mo.group())
# 415-555-4242
print(mo.groups())
# ('415', '555', '4242')




import  re

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print(mo.group(1))
# 415
print(mo.group(2))
# 555-4242
print(mo.group())
# 415-555-4242
print(mo.groups())
# ('415', '555-4242')

