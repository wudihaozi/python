��д��ĸ����			��ʾ
\d						0-9���κ�����
\D						��0-9������κ�����
\w                      �κ���ĸ�����ֻ��»���
\W						����ĸ�����ֻ��»���������ַ�
\s   					�ո��Ʊ�������з���ƥ��հף�
\S  					���ո��Ʊ�������з�������κ��ַ�

import re

xmasRegexN = re.compile(r'[0-5]+\s\w+')
xmasRegexS = re.compile(r'\d+\s\w+')
x1 = xmasRegexS.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rigns, 4 birds, 3hens, 2 doves, 1 partridge')
x2 = xmasRegexN.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rigns, 4 birds, 3hens, 2 doves, 1 partridge')
print(x1)
# ['12 drummers', '11 pipers', '10 lords', '9 ladies', '8 maids', '7 swans', '6 geese', '5 rigns', '4 birds', '2 doves', '1 partridge']
print(x2)
# ['12 drummers', '11 pipers', '10 lords', '5 rigns', '4 birds', '2 doves', '1 partridge']

