import os
a = os.path.join('a', 'b', 'c')
print(a)
# a\b\c 返回文件路径字符串
b = os.getcwd()
print(b)
# C:\Users\yuhaifeng\PycharmProjects\mat 打印当前工作目录
os.chdir(r'C:\Users\yuhaifeng\PycharmProjects')
print(os.getcwd())
# C:\Users\yuhaifeng\PycharmProjects
# os.makedirs(r'C:\Users\yuhaifeng\PycharmProjects\a') #创建文件目录
os.chdir(r'C:\Users\yuhaifeng\PycharmProjects\a')
print(os.getcwd())
# C:\Users\yuhaifeng\PycharmProjects\a
path = 'C:\\Users\\yuhaifeng\\PycharmProjects\\a '
print(os.path.dirname(path))
# C:\Users\yuhaifeng\PycharmProjects 获取文件路径
print(os.path.getsize('C:\\Users\\yuhaifeng\\PycharmProjects\\mat\\map.py'))
# 435 获取文件大小
print(os.listdir('C:\\Users\\yuhaifeng\\PycharmProjects'))
# ['a', 'alien_invasion', 'liaoxuefeng', 'mat', 'matplotlib', 'pythonproject', 'pythonrmsj', 'scrapy', 'soup', 'test']
# 获取文件列表
print(os.path.exists('C:\\Users\\yuhaifeng\\PycharmProjects'))
# 判断路径是否存在 True
print(os.path.isdir('C:\\Users\\yuhaifeng\\PycharmProjects'))
# 判断是否是目录 True
print(os.path.isfile('C:\\Users\\yuhaifeng\\PycharmProjects'))
# 判断是否为文件 False