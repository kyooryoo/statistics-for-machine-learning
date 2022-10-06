import random
from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

# 目标采样分布
def pi(x):
    return (.3*np.exp(-(x-.3)**2)+.7*np.exp(-(x-2.)**2/.3))/1.2113

m = 10_000 # 燃烧期样本数
N = 100_000 # 稳定期样本数 - 实际保留的有效样本数
sample = [0 for _ in range(m+N)] # 初始化采样数组

sample[0] = 2 # 任选一个起点，值无所谓
for t in range(1, m+N):
    x = sample[t-1]
    # 生成下一个随机游走的点
    x_star = norm.rvs(loc=x, scale=1, size=1)[0]
    # 指定接受概率
    alpha = min(1, (pi(x_star)/pi(x)))
    # 生成满足0～1之间均匀分布的随机数
    u = random.uniform(0,1)
    # 接受～拒绝的过程
    sample[t] = x_star if u < alpha else x

x = np.arange(-2, 4, .01)
# 绘制实际的目标分布
plt.plot(x, pi(x), color='r', lw=3)
# 绘制实际分布的近似采样
plt.hist(sample[m:], bins=100, density=True, edgecolor='k', alpha=.6)
plt.grid(ls='--')
plt.show()