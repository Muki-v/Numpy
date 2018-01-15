# create a array

import numpy as np

a = np.array([1, 2, 3])
b = np.array([(1, 2, 3), (4, 5, 6)])

print('a=')
print(a)

print("a's ndim {}".format(a.ndim))             # 数组的维数。称之为rank
print("a's shape {}".format(a.shape))           # 数组的维度。
# 长度维n的一维数组的shape是（n）.一个n行m列的矩阵的shape是（n,m）
print("a's size {}".format(a.size))             # 数组中所有元素的数量
print("a's dtype {}".format(a.dtype))           # 数组中元素的类型，例如numpy.int32, numpy.int16 或者 numpy.float64
print("a's itemsize {}".format(a.itemsize))     # 数组中每个元素的大小，单位为字节
# array.data 存储数组元素的缓冲。通常我们只需要通过下标来访问元素，而不需要访问缓冲

print('')

print("b's ndim {}".format(b.ndim))
print("b's shape {}".format(b.shape))
print("b's size {}".format(b.size))
print("b's dtype {}".format(b.dtype))
print("b's itemsize {}".format(b.itemsize))