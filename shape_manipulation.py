# shape and manipulation

import numpy as np

# reshape 根据已有数组和指定shape，生成一个新的数组
# vstack 将多个数组在垂直（v代表vertical）方向拼接（数组维度必须相同）
# hstack 将多个数组在水平（h代表horizontal）方向拼接（数维度必须相同）
# vsplit 将数组在垂直方向拆分
# hsplit 将数组在水平方向拆分

zero_line = np.zeros((1, 3))
one_column = np.ones((3, 1))
print("zero_line = \n{}\n".format(zero_line))
print("one_column = \n{}\n".format(one_column))

a = np.array([(1, 2, 3), (4, 5, 6)])
b = np.arange(11, 20)
print("a = \n{}\n".format(a))
print("b = \n{}\n".format(b))

b = b.reshape(3, -1)                                               # 将b调整成3行3列的矩阵
print("b.reshape(3, -1) = \n{}\n".format(b))

c = np.vstack((a, b, zero_line))                                   # 将3个数组在垂直方向上拼接
print("c = np.vstack((a, b, zero_line)) = \n{}\n".format(c))

a = a.reshape(3, 2)                                                # 先调整数组a的结构
print("a = a.reshape(3, 2) = \n{}\n".format(a))

d = np.hstack((a, b, one_column))                                  # 在水平方向拼接三个数组
print("d = np.hstack((a, b, one_column)) = \n{}\n".format(d))

e = np.hsplit(d, 3)    # split d into 3                            # 将数组d在水平方向拆分为3个数组，将中间一个数组（下标为1）打印出来
print("e = np.hsplit(d, 3) = \n{}\n".format(e))
print("e[1] = \n{}\n".format(e[1]))

f = np.hsplit(d, (1, 3))                                           # 将数组d从第1列和第3列两个地方进行拆分
print("f = np.hsplit(d, (1, 3)) = \n{}\n".format(f))

g = np.vsplit(d, 3)                                                # 将数组d在垂直方向上进行拆分
print("g = np.vsplit(d, 3) = \n{}\n".format(g))