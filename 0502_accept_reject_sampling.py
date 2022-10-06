import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import uniform, norm

def p(z):
    return (0.3*np.exp(-(z-0.3)**2)+0.7*np.exp(-(z-2.0)**2/0.3))/1.2113

q_norm_rv = norm(loc=1.4, scale=1.2)
M = 2.5

uniform_rv = uniform(loc=0, scale=1)
z_samples = []

for i in range(100_000):
    z = q_norm_rv.rvs(1)[0]
    u = uniform_rv.rvs(1)[0]
    if p(z) >= u*M*q_norm_rv.pdf(z):
        z_samples.append(z)

x = np.arange(-3.0, 5.0, 0.01)
plt.gca().axes.set_xlim(-3, 5)
plt.plot(x,p(x),color='r',lw=3)
plt.hist(z_samples,alpha=0.6,bins=150,density=True,edgecolor='k')
plt.grid(ls='--')
plt.show()