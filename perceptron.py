import numpy as np
import matplotlib.pyplot as plt
import random

# サンプルの数
N = 100

# 乱数のシードを設定。
# 毎回同じデータを生成するので引数を0としておく。
np.random.seed(0)

# 2次元空間のランダムな点N個。
# 正規乱数
X = np.random.randn(N, 2)

# 真の分離平面
def h(x, y):
    return 5 * x + 3 * y - 1

T = np.array([ 1 if h(x, y) > 0 else -1 for x, y in X])

# 特徴関数
def phi(x, y):
    return np.array([x, y, 1])

# パラメータの初期化。3次元の0ベクトル。
w = np.zeros(3)

np.random.seed()

while True:
    aList = np.array(range(N))
    random.shuffle(aList)

    misses = 0
    for n in aList:
        x_n, y_n = X[n, :]
        t_n = T[n]

predict = np.sign((w * phi(x_n, y_n)).sum())

        # 予測が不正解。パラメータの更新。
        if predict != t_n:
            w += t_n * phi(x_n, y_n)
            misses += 1

    if misses == 0:
        break

seq = np.arange(-3, 3, 0.02)
xlist, ylist = np.meshgrid(seq, seq)
zlist = np.array([np.sign((w * phi(x, y)).sum()) for x, y in zip(xlist, ylist)])

plt.pcolor(xlist, ylist, zlist, alpha=0.2, edgecolors='white')
plt.plot(X[T== 1,0], X[T== 1,1], 'o', color='red')
plt.plot(X[T==-1,0], X[T==-1,1], 'o', color='blue')
plt.show()
