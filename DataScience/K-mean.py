import numpy as np
import matplotlib.pyplot as plt

# 本例展示二维数据点K近邻可视化，详情见Python Data Science Handbook: P79
K = 3

# 随机生成二维数据点
X = np.random.randn(20, 2).round(2)
print(X)

# 计算距离的平方
dist_sq = np.sum((X[:, np.newaxis, :] - X[np.newaxis, :, :]) ** 2, axis=-1)

# # 利用argsort方法对距离排序
# nearest_index = np.argsort(dist_sq, axis=1)
# # print(nearest_index)

# 或利用argpartition方法直接找出K最近邻
K_partition = np.argpartition(dist_sq, K + 1, axis=1)
# print(K_partition)


# K近邻可视化
## 作散点图
plt.scatter(X[:,0], X[:,1], s=200)
## 将K近邻的点连接起来
for i in range(X.shape[0]):
    for j in K_partition[i, :K+1]:
        plt.plot(*zip(X[i], X[j]), color='black')

plt.show()