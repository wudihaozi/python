import matplotlib.pyplot as plt
import numpy as np

N = 20
# np.random.random(N) 生成N个[0-1)之间的浮点数
plt.scatter(
    np.random.random(N) * 100,
    np.random.random(N) * 100,
    c='r', s=100 , alpha=0.5
)
plt.scatter(
    np.random.random(N) * 100,
    np.random.random(N) * 100,
    c='b', s=200, alpha=0.5
)
plt.scatter(
    np.random.random(N) * 100,
    np.random.random(N) * 100,
    c='g', s=300, alpha=0.5
)
plt.show()