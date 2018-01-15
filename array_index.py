 # array index

import numpy as np
# 访问Numpy数组中的数据

base_data = np.arange(100, 200)
print("base_data \n{}\n".format(base_data))

print("basd_data[10] = {}\n".format(base_data[10]))                               # 通过指定下标来访问数组元素

every_five = np.arange(0, 100, 5)                                                 # every_five是包含要获取数组的下标的数组
# print("every_five \n{}\n".format(every_five))
print("base_data[every_five] = \n{}\n".format(base_data[every_five]))

a = np.array([(1, 2), (10, 20)])                                                  # 下标数组是多维的
print("a = \n{}\n".format(a))
print("base_data[a] = \n{}\n".format(base_data[a]))

base_data2 = base_data.reshape(10, -1)                                            # 将数组转换成一个10X10的二维数组
print("base_data2 = base_data.reshape(10, -1) = \n{}\n".format(base_data2))

print("base_data2[2] = \n{}\n".format(base_data2[2]))                             # 对于二维数组，只指定一个下标，则访问结果仍然是一个一维数组
print("base_data2[2, 3] = \n{}\n".format(base_data2[2, 3]))                       # 指定两个下标，则访问结果是其中的元素
print("base_data2[-1, -1] = \n{}\n".format(base_data2[-1, -1]))                   # 通过“-1”来指定“最后一个”的元素

print("base_data2[2, :]] = \n{}\n".format(base_data2[2, :]))                      # 通过“：”的形式来指定范围，如“2：5”，只写“：”表示全部范围
print("base_data2[:, 3]] = \n{}\n".format(base_data2[:, 3]))
print("base_data2[2:5, 2:4]] = \n{}\n".format(base_data2[2:5, 2:4]))

