from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

# 建立一个均值为 0 标准差为 1 标准正态分布
norm_rv = norm(loc=0, scale=1)
x = np.linspace(-1, 1, 1000)
# 定义每次去样的样本数量
sample_n = 100
# 预留一个保存所有均值结果的空数组
x_array = []
# 从正态分布中每次取样 100 并计算均值，取样 1000 万次
for i in range(1_000_000):
    norm_rvs = norm_rv.rvs(size=sample_n)
    x_bar = sum(norm_rvs) / float(sample_n)
    x_array.append(x_bar)

# 这里得到的所有均值结果的均值接近实际值 0 表示估计量接近真值
print(np.mean(x_array))
plt.hist(x_array, bins=100, density=True, alpha=0.3, edgecolor='k')
plt.axvline(0, ymax=0.8, color='r')
plt.gca().axes.set_xlim(-0.4, 0.4)
plt.grid(ls='--')
plt.show()
