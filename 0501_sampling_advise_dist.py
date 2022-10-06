import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def p(z):
    return (0.3*np.exp(-(z-0.3)**2)+0.7*np.exp(-(z-2.0)**2/0.3))/1.2113

q_norm_rv = norm(loc=1.4, scale=1.2)
M = 2.5

z = np.arange(-4.0, 5.0, 0.01)
plt.plot(z,p(z),color='r',lw=3,alpha=0.6,label='p(z)',linestyle='--')
plt.plot(z,M*q_norm_rv.pdf(z),color='b',lw=3,alpha=0.6,label='Mq(z)')
plt.legend()
plt.grid(ls='--')
plt.show()