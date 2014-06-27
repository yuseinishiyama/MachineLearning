# -*- coding:utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import math

# nCr
def comb(n, r):
    return math.factorial(n) / (math.factorial(n - r) * math.factorial(r))

# ベルヌーイ試行の一方の確率を入力として、２項分布を生成する関数を出力する。
def binominal(p):
    def f(n, x):
        prob = comb(n, x) * p ** x * (1 - p) ** (n - x)
        return prob
    return f

p = 0.5
L = []
trial_count = (10, 20, 30, 40, 50)
colors = ["r", "g", "b", "c", "y"]
f = binominal(p)

for n in trial_count:
    L.append([f(n, x) for x in range(n)])

for prob, color in zip(L, colors):
    plt.plot(prob, color)

ax = plt.axes()
ax.set_xlim(0, 50)
ax.set_ylim(-0.05, 0.3)

plt.title(r'$\mathrm{Binominal Distribution}\ P=%f$' % (p))
plt.xlabel('Trial')
plt.ylabel('Probability')
plt.legend([str(n) for n in trial_count])
plt.show()
