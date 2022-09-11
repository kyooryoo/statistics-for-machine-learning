# 这里保持协方差为 0 不变，调整方差观察图形的分布变化
import numpy as np
import matplotlib.pyplot as plt

mean = np.array([0, 0])
conv_1 = np.array([[1, 0], [0, 1]])
# 注意以下协方差依然为 0 表示随机变量之间没有相关性
# X2 方差为 4 且 Y2 方差为 0.25 的分布更为扁平
conv_2 = np.array([[4, 0], [0, 0.25]])

x_1, y_1 = np.random.multivariate_normal(mean, conv_1, 3000).T
x_2, y_2 = np.random.multivariate_normal(mean, conv_2, 3000).T
plt.figure(figsize=(6, 6))
plt.plot(x_1, y_1, 'ro', alpha=0.2)
plt.plot(x_2, y_2, 'bo', alpha=0.2)
plt.gca().axes.set_xlim(-6, 6)
plt.gca().axes.set_ylim(-6, 6)
plt.grid(ls='--')
plt.show()