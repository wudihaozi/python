import matplotlib.pyplot as plt
import numpy as np

'''
data��һ�����7�����ݵ������ֵ
ͼ�еı�ǩͨ��labels��ָ��
autopctָ������ֵ�ľ��ȸ�ʽ
plt.axis('equal')�������������Сһ��
plt.legend()ָ��Ҫ����ͼ��������ͼ�����Ͻǣ�
'''
labels = ['Mon', 'Tue', 'web', 'Thu', 'Fri', 'Sat', 'Sun']
data = np.random.rand(7) * 100
plt.pie(data, labels=labels, autopct='%1.1f%%')
plt.axis('off')
plt.legend()

plt.show()