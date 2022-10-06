import scipy
import matplotlib.pyplot as plt
from math import sqrt

s0 = 10.0 # 初始股价
T = 1.0 # 估算周期，一般取整数，代表年数
n = 244 * T # 估算周期内的步骤总数
mu = 0.15 # 股价收益率的期望值
sigma = 0.2 # 股票的波动率
n_simulation = 10_000 # 模拟次数

dt = T/n # 估算期内每步骤的粒度
s_array = [] # 保存模拟结果的数列

for i in range(n_simulation):
    s = s0
    for j in range(int(n)):
        # 每轮生成一个服从标准正态分布的随机变量
        e = scipy.random.normal()
        # 通过如下递推公式迭代出下个时间点的股价
        s = s+mu*s*dt+sigma*s*e*sqrt(dt)
    s_array.append(s)

plt.hist(s_array, alpha=0.6, bins=30, density=True, edgecolor='k')
plt.grid(ls='--')
plt.show()