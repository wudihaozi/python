import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
phoneNumRegex1 = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
mo1 = phoneNumRegex.search('Cell: 415-555-9999 work:212-555-0000')
mo2 = phoneNumRegex.findall('Cell: 415-555-9999 work: 212-555-0000')
mo3 = phoneNumRegex1.findall('Cell: 415-555-9999 work: 212-555-0000')
print(mo1.group())
# 415-555-9999 search ���ص���һ��match����
print(mo2)
# ['415-555-9999', '212-555-0000'] findall ���ص���һ���ַ����б�
print(mo3)
# [('415', '555', '9999'), ('212', '555', '0000')] ���ƥ��ģʽ��һ�����ʽ �򷵻��ַ���Ԫ����б�
print(mo3[1][2])
# 0000 