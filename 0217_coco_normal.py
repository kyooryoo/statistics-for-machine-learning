# 相关系数叫做 Correlation Coefficient 这里简称 coco
import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 2)
mean = np.array([0, 0])
conv = np.array([[1, 0.85], [0.85, 1]])

x_1, y_1 = np.random.multivariate_normal(mean, conv, 3000).T
x_2, y_2 = x_1*100, y_1*100

ax[0].plot(x_1, y_1, 'bo', alpha=0.05)
ax[1].plot(x_2, y_2, 'ro', alpha=0.05)

# 可以看到没有标准化之前的协方差值差别是很大的
S_1 = np.vstack((x_1, y_1))
S_2 = np.vstack((x_2, y_2))
print(np.cov(S_1))
print(np.cov(S_2))
# 而标准化之后的相关系数其实是没有太大差别的
print('**********')
print(np.corrcoef(S_1))
print(np.corrcoef(S_2))

ax[0].grid(ls='--')
ax[1].grid(ls='--')
plt.show()