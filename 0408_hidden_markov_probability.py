import numpy as np
from hmmlearn import hmm

# 隐状态集合Q
states = ['box1','box2','box3']
# 观测集合V
observations = ['black','white']
# 初始概率pi
start_probability = np.array([.3,.5,.2])
# 状态转移矩阵A
transition_probability = np.array([
    [.4,.4,.2],
    [.3,.2,.5],
    [.2,.6,.2]
])
# 观测概率矩阵B
emission_probability = np.array([
    [.2,.8],
    [.6,.4],
    [.4,.6]
])
# 对离散观测状态建模
model = hmm.MultinomialHMM(n_components=len(states))
model.startprob_ = start_probability
model.transmat_ = transition_probability
model.emissionprob_ = emission_probability
# 观测序列
observation_list = np.array([0,1,0])
# 计算观测序列概率，结果为概率值的自然对数值
print(model.score(observation_list.reshape(-1,1)))