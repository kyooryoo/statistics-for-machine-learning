import matplotlib.pyplot as plt
from sklearn.mixture import GaussianMixture
from sklearn.datasets import make_blobs

# 产生和绘制实验数据
X, y_true = make_blobs(n_samples=1000, centers=4)
fig, ax = plt.subplots(1,2,sharey='row')
ax[0].scatter(X[:,0],X[:,1],s=5,alpha=.5)
ax[0].grid(ls='--')

# 高斯混合模型拟合样本
gmm = GaussianMixture(n_components=4)
gmm.fit(X)
print(F"各分布的权重：\n{gmm.weights_}")
print(F"各分布的均值：\n{gmm.means_}")
print(F"各分布的协方差矩阵：\n{gmm.covariances_}")
print(F"样本点属于每个分布的概率（取前十个）：\n{gmm.predict_proba(X)[:10].round(5)}")

# 通过 GMM 模型推测每个样本所属的类别
labels = gmm.predict(X)
print(F"每个样本点所属的类别：\n{labels}")
# 不同类别标记为不同颜色
ax[1].scatter(X[:,0],X[:,1],s=5,alpha=.5,c=labels,cmap='viridis')
ax[1].grid(ls='--')
plt.show()

