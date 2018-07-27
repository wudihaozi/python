import re

robocop = re.compile(r'robocop', re.I)
mo1 = robocop.search('RoboCop is part man, part machine, all cop.').group()
mo2 = robocop.search('ROBOCOP procects the innocent.').group()
print(mo1)
print(mo2)