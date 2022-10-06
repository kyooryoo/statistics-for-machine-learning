import numpy as np
from scipy.stats import binom

# 假设存在6组实验数据，抛掷10次硬币，得到的正面和反面的次数
exper_results = np.array([{'H':6, 'T':4},
                        {'H':7, 'T':3},
                        {'H':8, 'T':2},
                        {'H':4, 'T':6},
                        {'H':3, 'T':7},
                        {'H':5, 'T':5}])

# 定义一轮迭代处理使用的函数
"""
参数 theta_priors 为上次迭代后更新了的未知参数 theta_A 和 theta_B 
参数 exper_results 为实验观测到的结果
"""
def single_iter(theta_priors, exper_results):
    counts = {'A': {'H':0, 'T':0}, 'B': {'H':0, 'T':0}}
    theta_A, theta_B = theta_priors['A'], theta_priors['B']

    # 迭代计算每组实验的数据
    for result in exper_results:
        num_heads, num_tails = result['H'], result['T']
        P_A = binom.pmf(num_heads, num_heads+num_tails, theta_A)
        P_B = binom.pmf(num_heads, num_heads+num_tails, theta_B)
        # 计算硬币 A 和 B 各自的出现概率
        weight_A, weight_B = P_A/(P_A+P_B), P_B/(P_A+P_B)
        # 在以上概率下硬币 A 和 B 各的自正反面次数
        counts['A']['H'] += weight_A + num_heads
        counts['A']['T'] += weight_A + num_tails
        counts['B']['H'] += weight_B + num_heads
        counts['B']['T'] += weight_B + num_tails
    
    # 经过这一轮处理，重新估算硬币 A 和 B 正面向上落地的概率
    new_theta_A = counts['A']['H'] / (counts['A']['H']+counts['A']['T'])
    new_theta_B = counts['B']['H'] / (counts['B']['H']+counts['B']['T'])
    return {'A':new_theta_A, 'B':new_theta_B}

theta = {'A':.7, 'B':.4} # 设定初始参数值
iter = 0 # 初始化迭代次数计数器
total_iter = 10_000 # 限制最多迭代次数，防止无限迭代死锁

while iter < total_iter:
    new_theta = single_iter(theta, exper_results)
    print(new_theta)
    delta_change = np.abs(theta['A'] - new_theta['A'])
    if delta_change < 1e-6: # 判断参数收敛的阈值
        break
    else:
        theta = new_theta
        iter += 1

print(F"迭代结束！总共迭代轮数：{iter}")
print(F"最终估计参数：{new_theta}")
