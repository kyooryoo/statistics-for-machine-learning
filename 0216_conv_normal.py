import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(2, 2)
mean = np.array([0, 0])

conv_1 = np.array([[1, 0], [0, 1]]) # 二元标准正态分布
conv_2 = np.array([[1, 0.3], [0.3, 1]]) # 协方差 0.3
conv_3 = np.array([[1, 0.85], [0.85, 1]]) # 协方差 0.85
conv_4 = np.array([[1, -0.85], [-0.85, 1]]) # 协方差 -0.85

x_1, y_1 = np.random.multivariate_normal(mean, conv_1, 3000).T
x_2, y_2 = np.random.multivariate_normal(mean, conv_2, 3000).T
x_3, y_3 = np.random.multivariate_normal(mean, conv_3, 3000).T
x_4, y_4 = np.random.multivariate_normal(mean, conv_4, 3000).T

ax[0][0].plot(x_1, y_1, 'bo', alpha=0.2)
ax[0][1].plot(x_2, y_2, 'ro', alpha=0.2)
ax[1][0].plot(x_3, y_3, 'go', alpha=0.2)
ax[1][1].plot(x_4, y_4, 'yo', alpha=0.2)

ax[0][0].grid(ls='--')
ax[0][1].grid(ls='--')
ax[1][0].grid(ls='--')
ax[1][1].grid(ls='--')
plt.show()