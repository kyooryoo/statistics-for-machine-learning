from scipy.special import comb
import math

# # 从20个样本中取出13个样本的不同组合数量
# print(comb(20,13))

# # 每次概率为2/5采样13次得到的累积概率，即2/5的13次方
# print(math.pow(2/5, 13))

def get_possibility(n, head, p_head):
    return comb(n,head)*math.pow(p_head,head)*math.pow((1-p_head),(n-head))

print(get_possibility(20, 13, 2/5))
print(get_possibility(20, 13, 1/2))
# 可以看到如下概率值最大，最有可能是概率为3/5的这枚硬币
print(get_possibility(20, 13, 3/5))