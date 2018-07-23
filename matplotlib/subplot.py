import matplotlib.pyplot as plt
import numpy as np

# two pic
data = np.arange(100, 201)
plt.subplot(2, 1, 1)
plt.plot(data)

data2 = np.arange(200, 301)
plt.subplot(2, 1, 2)
plt.plot(data2)

plt.show()

# one pic
data3 = np.arange(100, 201)
plt.subplot(211)
plt.plot(data3)

data4 = np.arange(200, 301)
plt.plot(212)
plt.plot(data4)

plt.show()


# three pic
import matplotlib.pyplot as plt
plt.subplot(221)
plt.subplot(222)
plt.subplot(212)
plt.show()
