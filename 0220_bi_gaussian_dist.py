import numpy as np
import matplotlib.pyplot as plt

# 分布以(0,0)为中心
mean_1 = np.array([0, 0])
# 方差 XX 和 YY 都为 1 表示纵横方向分布相同 
# 协方差为 0 表示不相关，即分布图像没有任何偏转
conv_1 = np.array([[1, 0], [0, 1]])

# 分布以(0,-7)为中心
mean_2 = np.array([0, -7])
# 方差 XX 为 4 方差 YY 为 0.25 即分布呈横向拉成纵向压扁的形态
# 协方差为 0 表示不相关，即分布图像没有任何偏转
conv_2 = np.array([[4, 0], [0, 0.25]])

# 分布以(4,4)为中心
mean_3 = np.array([4, 4])
# 方差 XX 为 4 方差 YY 为 0.25 即分布呈横向拉成纵向压扁的形态
# 协方差为 -3 表示负相关，即分布图像向左上方或逆时针偏转
conv_3 = np.array([[4, -3], [-3, 0.25]])

x_1, y_1 = np.random.multivariate_normal(mean_1, conv_1, 2000).T
x_2, y_2 = np.random.multivariate_normal(mean_2, conv_2, 2000).T
x_3, y_3 = np.random.multivariate_normal(mean_3, conv_3, 2000).T

plt.plot(x_1, y_1, 'ro', alpha=0.05)
plt.plot(x_2, y_2, 'bo', alpha=0.05)
plt.plot(x_3, y_3, 'go', alpha=0.05)

plt.gca().axes.set_xlim(-10, 10)
plt.gca().axes.set_ylim(-10, 10)
plt.grid(ls='--')
plt.show()