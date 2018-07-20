import matplotlib.pyplot as plt
import numpy as np
'''
多个figure
可以简单的理解为一个figure就是一个图形窗口。matplotlib.pyplot会有一个默认的figure，我们也可以通过plt.figure()创建更多个
'''
data = np.arange(100, 201)
plt.plot(data)

data2 = np.arange(200, 301)
plt.figure()
plt.plot(data2)
plt.show()