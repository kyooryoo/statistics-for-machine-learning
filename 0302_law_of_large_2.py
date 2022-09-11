import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# 原始的正态分布的样本分布图像，分布形态最为扁平
norm_rvs = norm(loc=0, scale=20).rvs(size=1_000_000)
plt.hist(norm_rvs, density=True, alpha=.3, color='b', bins=100, label='original')

# 准备一个空的数组用于保存均值数列
mean_array = []

# 从原始正态分布样本中每次随机选取5个数，计算均值，重复10000次
for i in range(10_000):
    sample = np.random.choice(norm_rvs, size=5, replace=False)
    mean_array.append(np.mean(sample))
# 可以看到分布形态开始向中央收敛，较原始形态略为高耸
plt.hist(mean_array, density=True, alpha=.3, color='r', bins=100, label='sample size=5')

# 从原始正态分布样本中每次随机选取50个数，计算均值，重复10000次
for i in range(10_000):
    sample = np.random.choice(norm_rvs, size=50, replace=False)
    mean_array.append(np.mean(sample))
# 可以看到分布形态向中央显著收敛，分布图像形态十分高耸
plt.hist(mean_array, density=True, alpha=.3, color='g', bins=100, label='sample size=50')

# 结论是，随每次选取的样本数量增多，均值分布越发向期望值集中
plt.gca().axes.set_xlim(-60, 60)
plt.legend(loc='best')
plt.grid(ls='--')
plt.show()