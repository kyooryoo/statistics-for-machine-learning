from scipy.stats import expon
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 1000)

expon_rv_0 = expon()
plt.plot(x, expon_rv_0.pdf(x), color='r', 
         lw=3, alpha=0.6, label='$\\lambda=1$')

expon_rv_1 = expon(scale=2)
plt.plot(x, expon_rv_1.pdf(x), color='b', 
         lw=3, alpha=0.6, label='$\\lambda=0.5$', linestyle='--')

expon_rv_1 = expon(scale=.5)
plt.plot(x, expon_rv_1.pdf(x), color='g', 
         lw=3, alpha=0.6, label='$\\lambda=2$', linestyle=':')

plt.legend(loc='best', frameon=False)
plt.grid(ls='--')
plt.show()