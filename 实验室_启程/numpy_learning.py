import numpy as np
# arr1 = np.array([1, 2, 3, 4, 5])
# # print(arr1)
# # arr2 = np.array([[1, 2, 3], [4, 5, 6]])
# # print(arr2)
# # print(arr1.shape)
# # print(arr2.shape)
# # arr1[0] = 10.00
# # print(arr1)
# # arr1 = arr1.astype(float)
# # print(arr1)
# arr2 = np.array([1.3, 5.2, 1.4])
# # print(arr2)
# arr3 = np.array([2.1, 3.2, 4.3])
# # print(arr3 + arr2)
# # print(arr3 + 1)
# # arr = (arr2 + 1) * 2
# # print(arr)
# # arr4 = np.array([[1, 2, 3], [4, 5, 6]])
# # print(arr4.shape,arr1.shape)
# # arr5 = np.arange(10).reshape(2, 5)
# # print(arr5)
# # arr6 = arr5.reshape(-1)
# # print(arr6)
# arr4 = np.zeros((2, 3))
# print(arr4)
# arr5 = np.ones((2, 3))
# print(arr5)
# arr1 =90*np.random.rand(2, 3)+60
# arr1 = arr1.astype(int)
# print(arr1)
# arr2 = np.random.randint(1, 10, (2, 30))
# print(arr2)
# arr1 = np.arange(1, 17).reshape(4, 4)
# print(arr1)
# print(arr1[0,1])
# print(arr1[0][1])

# arr1[[0,1], [1,0]] = 100
# print(arr1[[0,1], [1,0]])
# print(arr1[:, 0])
# print(arr1[1:3:1,1:3:1])
# import numpy as np

# arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print("原始数组：")
# print(arr)

# view = arr[1:3, 1:3]  # 切片，得到一个视图
# print("\n切片视图：")
# print(view)
# view[0, 0] = 99  # 修改视图中的数据
# print("\n修改后的视图：")
# print(view)
# print("\n修改后的原始数组：")
# print(arr)
# import numpy as np

# arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print("原始数组：")
# print(arr)

# # # 视图：共享内存
# # view = arr[1:3, 1:3]
# # view[0, 0] = 99
# # print("\n修改视图后，原始数组也被改：")
# # print(arr)

# # # 复制：独立内存
# # copy = arr[1:3, 1:3].copy()
# # copy[0, 0] = 88
# # print(copy)
# # print("\n修改复制后，原始数组不变：")
# # print(arr)
# # copy1 = copy.T
# # print(copy)
# # print(copy1)
# # arr_lr = np.fliplr(arr)
# # print(arr_lr)
# # arr_up = np.flipud(arr)
# # print(arr_up)
# arr2 = np.array([[1, 2], [3, 4], [5, 6]])
# print(arr2)
# arr3 = np.hstack((arr, arr2))
# print(arr3)
# arr4 = np.concatenate((arr, arr2.T))
# print(arr4)
# import numpy as np

# arr1 = np.array([[1, 2], [3, 4]])
# arr2 = np.array([[5, 6], [7, 8]])

# print("原始数组1：")
# print(arr1)
# print("\n原始数组2：")
# print(arr2)

# print("\naxis=0（垂直拼接）：")
# print(np.concatenate((arr1, arr2)))

# print("\naxis=1（水平拼接）：")
# print(np.concatenate((arr1, arr2), axis=1))
# import numpy as np

# arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
# # print("原始数组：")
# # print(arr)

# # print("\n按行平均分成 2 份：")
# # result1 = np.split(arr, 2, axis=0)
# # for i, sub_arr in enumerate(result1):
# #     print(f"第 {i+1} 份：\n{sub_arr}")

# # print("\n按列平均分成 2 份：")
# # result2 = np.split(arr, 2, axis=1)
# # for i, sub_arr in enumerate(result2):
# #     print(f"第 {i+1} 份：\n{sub_arr}")

# # print("\n按行在索引 [1, 3] 处分割：")
# # result3 = np.split(arr, [1, 3], axis=0)
# # for i, sub_arr in enumerate(result3):
# #     print(f"第 {i+1} 份：\n{sub_arr}")
# arr1,arr2,arr3 = np.split(arr, [0, 1], axis=0)
# print(arr1) 
# print(arr2) 
# print(arr3) 
# import numpy as np

# # 标量广播
# arr1 = np.array([[1, 2, 3], [4, 5, 6]])
# print("标量广播：")
# print(arr1 * 2)

# # 一维到二维广播
# vec = np.array([10, 20, 30])
# print("\n一维到二维广播：")
# print(arr1 + vec)

# # 两数组广播
# col = np.array([[1], [2], [3]])  # 形状 (3, 1)
# row = np.array([10, 20])          # 形状 (2,)
# print("\n两数组广播：")
# print(col + row.reshape(1, 2))    # 调整 row 为 (1, 2)
# import numpy as np

# # 一维数组：向量内积
# vec1 = np.array([1, 2, 3])
# vec2 = np.array([4, 5, 6])
# print("向量内积：")
# print(np.dot(vec1, vec2))

# # 二维数组：矩阵乘法
# mat1 = np.array([[1, 2], [3, 4]])
# mat2 = np.array([[5, 6], [7, 8]])
# print("\n矩阵乘法：")
# print(np.dot(mat1, mat2))

# # 一维与二维：向量-矩阵乘法
# vec = np.array([1, 2])
# mat = np.array([[3, 4], [5, 6]])
# print("\n向量-矩阵乘法：")
# print(np.dot(vec, mat))
# import numpy as np

# # 创建测试数组
# x = np.array([1, 2, 3, 4])
# y = np.array([[1, 2], [3, 4]])

# # 基本算术
# print("平方：", np.power(x, 2))  # [1, 4, 9, 16]
# print("平方根：", np.sqrt(x))  # [1., 1.414..., 1.732..., 2.]

# # 三角函数
# angles = np.array([0, 30, 45, 90])
# radians = np.deg2rad(angles)
# print("\n正弦值：", np.sin(radians))

# # 统计函数
# print("\n总和：", np.sum(y))  # 10
# print("按列平均：", np.mean(y, axis=0))  # [2., 3.]

# # 舍入和绝对值
# z = np.array([-1.6, -0.4, 0.5, 1.7])
# print("\n四舍五入：", np.round(z))  # [-2., -0., 1., 2.]
# print("绝对值：", np.abs(z))  # [1.6, 0.4, 0.5, 1.7]
# import numpy as np

# # 测试 np.abs
# x1 = np.array([-3.5, -2, 0, 1.5, -0.7])
# print("绝对值：", np.abs(x1))

# # 测试复数
# z = np.array([3+4j, 1-1j])
# print("复数绝对值：", np.abs(z))

# # 测试 np.log
# x2 = np.array([1, 2, np.e, 10])
# print("\n自然对数：", np.log(x2))
# print("以10为底：", np.log10(x2))
# print("以2为底：", np.log2(x2))

# # 测试定义域外输入
# x3 = np.array([-1, 0, 1])
# print("\n定义域外输入：", np.log(x3))  # 会警告并返回 nan

# import numpy as np

# # 创建测试数组
# x = np.array([[1, 2, 3],
#               [4, 5, 6]])

# # 基本统计
# print("总和：", np.sum(x))
# print("按列求和：", np.sum(x, axis=0))
# print("按行求和：", np.sum(x, axis=1))
# print("平均值：", np.mean(x))
# print("标准差：", np.std(x))

# # 极值
# print("\n最小值：", np.min(x))
# print("最大值：", np.max(x))
# print("最小值索引：", np.argmin(x))
# print("最大值索引：", np.argmax(x))

# # 累积
# y = np.array([1, 2, 3, 4])
# print("\n累积和：", np.cumsum(y))
# print("累积乘积：", np.cumprod(y))

# # 计数和条件
# z = np.array([0, 1, 0, 2, 0])
# print("\n非零元素个数：", np.count_nonzero(z))
# print("是否存在非零：", np.any(z))
# print("是否全为非零：", np.all(z))
# import numpy as np

# # 创建包含 nan 的数组
# x = np.array([1, 2, np.nan, 4])

# # 检查 nan
# print("是否为 nan：", np.isnan(x))

# # 普通聚合 vs 忽略 nan
# print("\n普通求和：", np.sum(x))
# print("忽略 nan 求和：", np.nansum(x))
# print("普通平均：", np.mean(x))
# print("忽略 nan 平均：", np.nanmean(x))

# # 替换 nan
# print("\n替换 nan 为 0：", np.nan_to_num(x, nan=0))

# # 过滤 nan
# print("过滤掉 nan：", x[~np.isnan(x)])

# # nan 的传播性
# print("\nnan 运算：", x + 1)
# print("nan 比较：", x == np.nan)  # 无效比较
# print("nan 自比较：", np.nan == np.nan)  # False
import numpy as np

# 创建测试数组
x = np.array([10, 20, 30, 40, 50])

# 创建布尔型数组
greater_than_25 = x > 25
less_than_45 = x < 45
combined = np.logical_and(greater_than_25, less_than_45)

print("大于25：", greater_than_25)
print("小于45：", less_than_45)
print("大于25且小于45：", combined)

# 布尔索引筛选
filtered = x[combined]
print("\n筛选结果：", filtered)

# 修改值
x[greater_than_25] = 99
print("修改后数组：", x)

# 统计
count = np.sum(greater_than_25)
print("大于25的元素个数：", count)

# 条件判断
print("是否存在大于30的元素：", np.any(x > 30))
print("是否所有元素大于5：", np.all(x > 5))

# 处理 nan
y = np.array([1, np.nan, 3, 4])
mask = ~np.isnan(y)
print("\n非 nan 值：", y[mask])
