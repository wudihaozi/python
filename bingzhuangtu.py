import matplotlib.pyplot as plt
import numpy as np

'''
data是一组包含7个数据的随机数值
图中的标签通过labels来指定
autopct指定了数值的精度格式
plt.axis('equal')设置了坐标轴大小一致
plt.legend()指明要绘制图例（见下图的右上角）
'''
labels = ['Mon', 'Tue', 'web', 'Thu', 'Fri', 'Sat', 'Sun']
data = np.random.rand(7) * 100
plt.pie(data, labels=labels, autopct='%1.1f%%')
plt.axis('off')
plt.legend()

plt.show()