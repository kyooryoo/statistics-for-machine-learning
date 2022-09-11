import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from scipy.stats import uniform

n = 100_000
r = 1.0
o_x, o_y = (0., 0.)

# 在xy两个维度准备后退一个半径为中心，尺度两个半径的均匀分布，并采样10万个
uniform_x = uniform(o_x-r, 2*r).rvs(n)
uniform_y = uniform(o_y-r, 2*r).rvs(n)

# 计算随机点到圆心的距离
d_array = np.sqrt((uniform_x - o_x) ** 2 + (uniform_y - o_y) ** 2)
# 小于圆半径即可认为落在圆内，计算这样的点的总数
res = sum(np.where(d_array < r, 1, 0))
# 根据正方形与圆形的面积之比近似等于相应区域内随机点数量之比，计算近似的pi值
pi = (res / n) / (r**2) * (2*r)**2

fig, ax = plt.subplots(1, 1)
# 直接绘制以均匀分布值为长宽的正方形，用于演示
ax.plot(uniform_x, uniform_y, 'ro', alpha=0.2, markersize=0.3)
plt.axis('equal')
# 直接调用绘制圆形的函数来绘制圆形，用于演示
circle = Circle(xy=(o_x, o_y), radius=r, alpha=0.5)
ax.add_patch(circle)

print(F"pi={pi}")
plt.grid(ls='--')
plt.show()