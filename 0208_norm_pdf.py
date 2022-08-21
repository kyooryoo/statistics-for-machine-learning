from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(1, 1)
# 准备两个参数不同的正太分布实例
norm_0 = norm(loc=0, scale=1)
norm_1 = norm(loc=1, scale=2)

x = np.linspace(-10, 10, 1000)
# 直接调用正太分布实例的pdf方法绘制其概率密度函数
ax.plot(x, norm_0.pdf(x), color='red', lw=3, 
        alpha=0.6, label='loc=0, scale=1')
ax.plot(x, norm_1.pdf(x), color='blue', lw=3, 
        alpha=0.6, label='loc=1, scale=2', linestyle='--')
ax.legend(loc='best', frameon=True)
plt.grid(ls='--')
plt.show()