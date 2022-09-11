import numpy as np
import matplotlib.pyplot as plt

X = [-2,-1,-1,0,0,1,1,2]
Y = [0,1,-1,2,-2,1,-1,0]

# 协方差为 0 所以看似 X 和 Y 是不相关
S = np.vstack([X, Y])
print(np.cov(S))

# 但从图形来看 Y=0 的概率为 1/4
# 但增加随机变量 X=2 后概率为 1/8
# 所以 X 影响了 Y 的概率，二者不独立
plt.plot(X, Y, 'ro', alpha=1)
plt.grid(ls='--')
plt.show()