import numpy as np
from scipy.stats import geom
import matplotlib.pyplot as plt

fig, ax = plt.subplots(2, 2)

# 绘制p=.3的几何分布的原始图形
geom_rv = geom(p=.3)
geom_rvs = geom_rv.rvs(size=1_000_000)
mean, var, skew, kurt = geom_rv.stats(moments='mvsk')
ax[0, 0].hist(geom_rvs, bins=100, density=True)
ax[0, 0].set_title('geom distribution:p=0.3')
ax[0, 0].grid(ls='--')

n_array = [0, 2, 5, 50]
for i in range(1, 4):
    Z_array = []
    n = n_array[i]
    for j in range(100_000):
        # 从样本空间中随机采样 n 个样本
        sample = np.random.choice(geom_rvs, n)
        # 根据Zn即中央极限定理的定义，计算每次采样得到的随机变量Zn的值
        Z_array.append((sum(sample) - n * mean) / np.sqrt(n * var))
    # 注意这里用i动态定义绘图位置坐标的方法
    ax[i // 2, i % 2].hist(Z_array, bins=100, density=True)
    ax[i // 2, i % 2].set_title(F"n={n}")
    ax[i // 2, i % 2].set_xlim(-3, 3)
    ax[i // 2, i % 2].grid(ls='--')

# 观察和对比四个图形，随着每次采样样本个数的增多，随机变量Zn收敛于正态分布
fig.set_tight_layout(True)
plt.show()