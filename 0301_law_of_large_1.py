from random import sample
import numpy as np
from scipy.stats import binom
import matplotlib.pyplot as plt

n = 10
p = 0.4
expected_value = n*p
sample_size = 15000
# 准备一系列从1到15000的数列，以10递增
N_samples = range(1, sample_size, 10)

# 计算累积二元随机变量的平均值并并绘图三次
for k in range(3):
    # 定义二元随机变量对象并生成样本空间
    binom_rv = binom(n, p)
    X = binom_rv.rvs(size=sample_size)
    # 计算累积二元随机变量的均值，即前10，前20，前30等等
    sample_average = [X[:i].mean() for i in N_samples]
    # 从绘图结果可以看到，随着均值的样本空间变大，均值收敛于n*p
    plt.plot(N_samples, sample_average, label=F"average of sample {k}")

# 绘出期待的均值，作为观察样本空间变大后均值变化的参考
plt.plot(N_samples, expected_value * np.ones_like(sample_average), ls='--', label=F"true expected value:n*p={n*p}", c='k')
plt.legend()
plt.grid(ls='--')
# 结论是，随着样本空间的增大，均值收敛于期望值
plt.show()