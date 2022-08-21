from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

# 绘制正态分布的概率密度函数曲线
norm_rv = norm(loc=2, scale=2)
x = np.linspace(-10, 10, 1000)
plt.plot(x, norm_rv.pdf(x), 'r', lw=3, alpha=0.6, label="$\\mu=2,\\sigma=2$")
# 取样并绘制正态分布样本的直方图
norm_rvs = norm_rv.rvs(size=100000)
plt.hist(norm_rvs, density=True, bins=50, alpha=0.6, edgecolor='k')
# 显示注释，定义曲线线形，并显示图形
plt.legend()
plt.grid(ls='--')
plt.show()