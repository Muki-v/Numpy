# create a specific array

import numpy as np

a = np.zeros((2, 3))                                               # 创建元素全部是0的数组
print('np.zeros((2, 3))= \n{}\n'.format(a))

b = np.ones((2, 3))                                                # 创建元素全部是1的数组
print('np.ones((2, 3))= \n{}\n'.format(b))

c = np.empty((2, 3))                                               # 创建未初始化的数据，因此内容是不确定的
print('np.empty((2, 3))= \n{}\n'.format(c))

d = np.arange(1, 2, 0.3)                                           # 通过指定范围和步长来创建数组
print('np.arange(1, 2, 0.3)= \n{}\n'.format(d))

e = np.linspace(1, 2, 7)                                           # 通过制定范围和元素数量来创建数组
print('np.linspace(1, 2, 7)= \n{}\n'.format(e))

f = np.random.random((2, 3))                                       # 生成随机数
print('np.random.random((2, 3))= \n{}\n'.format(f))