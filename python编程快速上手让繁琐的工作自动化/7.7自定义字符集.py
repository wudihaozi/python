import re

vowelRegex = re.compile(r'[aeiouAEIOU]')
vowelRegexStr = re.compile(r'[A-F]')
vowelRegexStr2 = re.compile(r'[^A-F]')
vowelRegexStr3 = re.compile(r'[^aeiouAEIOU]')
vowelRegexNum = re.compile(r'[1-5]')
mo = vowelRegex.findall('ToboCop eats baby food. BABY FOOD.')
mostr = vowelRegexStr.findall('ToboCop eats baby food. BABY FOOD. 3.14159265')
mostr2 = vowelRegexStr2.findall('ToboCop eats baby food. BABY FOOD. 3.14159265')
mostr3 = vowelRegexStr3.findall('ToboCop eats baby food. BABY FOOD. 3.14159265')
moNum = vowelRegexNum.findall('3.14159265')
print(mo)
# ['o', 'o', 'o', 'e', 'a', 'a', 'o', 'o', 'A', 'O', 'O']
print(mostr)
# ['C', 'B', 'A', 'B', 'F', 'D']
print(mostr2)
# ['T', 'o', 'b', 'o', 'o', 'p', ' ', 'e', 'a', 't', 's', ' ', 'b', 'a', 'b', 'y', ' ', 'f', 'o', 'o', 'd', '.', ' ', 'Y', ' ', 'O', 'O', '.', ' ', '3', '.', '1', '4', '1', '5', '9', '2', '6', '5']
print(mostr3)
# ['T', 'b', 'C', 'p', ' ', 't', 's', ' ', 'b', 'b', 'y', ' ', 'f', 'd', '.', ' ', 'B', 'B', 'Y', ' ', 'F', 'D', '.', ' ', '3', '.', '1', '4', '1', '5', '9', '2', '6', '5']
print(moNum)
# ['3', '1', '4', '1', '5', '2', '5']
#
