import os
a = os.path.join('a', 'b', 'c')
print(a)
# a\b\c �����ļ�·���ַ���
b = os.getcwd()
print(b)
# C:\Users\yuhaifeng\PycharmProjects\mat ��ӡ��ǰ����Ŀ¼
os.chdir(r'C:\Users\yuhaifeng\PycharmProjects')
print(os.getcwd())
# C:\Users\yuhaifeng\PycharmProjects
# os.makedirs(r'C:\Users\yuhaifeng\PycharmProjects\a') #�����ļ�Ŀ¼
os.chdir(r'C:\Users\yuhaifeng\PycharmProjects\a')
print(os.getcwd())
# C:\Users\yuhaifeng\PycharmProjects\a
path = 'C:\\Users\\yuhaifeng\\PycharmProjects\\a '
print(os.path.dirname(path))
# C:\Users\yuhaifeng\PycharmProjects ��ȡ�ļ�·��
print(os.path.getsize('C:\\Users\\yuhaifeng\\PycharmProjects\\mat\\map.py'))
# 435 ��ȡ�ļ���С
print(os.listdir('C:\\Users\\yuhaifeng\\PycharmProjects'))
# ['a', 'alien_invasion', 'liaoxuefeng', 'mat', 'matplotlib', 'pythonproject', 'pythonrmsj', 'scrapy', 'soup', 'test']
# ��ȡ�ļ��б�
print(os.path.exists('C:\\Users\\yuhaifeng\\PycharmProjects'))
# �ж�·���Ƿ���� True
print(os.path.isdir('C:\\Users\\yuhaifeng\\PycharmProjects'))
# �ж��Ƿ���Ŀ¼ True
print(os.path.isfile('C:\\Users\\yuhaifeng\\PycharmProjects'))
# �ж��Ƿ�Ϊ�ļ� False