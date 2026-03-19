# 📅 学习笔记：Numpy 初探与环境配置填坑

> **日期**：2026-03-17
> **状态**：✅ 已解决
> **关键词**：`PowerShell策略`、`Conda激活`、`Numpy类型截断`、`同质性`

---

## 🛠️ 一、 环境配置：PowerShell 的“拦路虎”

### 1. 问题描述
在 VS Code 的 PowerShell 终端中使用 `conda activate` 切换环境时，报错：
> `无法加载文件 ...\profile.ps1，因为在此系统上禁止运行脚本。`
> `CategoryInfo : SecurityError`

### 2. 原因分析
- **机制**：PowerShell 默认的执行策略（Execution Policy）是 `Restricted`（受限模式），出于安全考虑，禁止运行任何脚本（包括 Conda 的初始化脚本）。
- **对比**：CMD（命令提示符）没有此限制，所以之前在 CMD 中可以成功。

### 3. 解决方案
通过修改执行策略为 `RemoteSigned`（允许本地脚本，远程脚本需签名）。

**操作步骤**：
1.  **管理员身份**运行 PowerShell。
2.  执行命令：`Set-ExecutionPolicy RemoteSigned`
3.  输入 `A` 确认。
4.  重启终端，`conda activate` 成功，出现 `(env_name)` 标识。

---

## 🐍 二、 Numpy 基础与“隐形陷阱”

### 1. 代码实战
```python
import numpy as np

# 1. 创建一维数组
arr1 = np.array([1, 2, 3, 4, 5])
print(arr1)

# 2. 创建二维数组
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2)

# 3. 查看形状
print(arr1.shape)  # 输出 (5,)
print(arr2.shape)  # 输出 (2, 3) -> 2行3列

# 4. ⚠️ 挖坑测试：类型修改
arr1[0] = 10.00
print(arr1)
```

### 2. 🚨 重点陷阱：类型截断（Type Truncation）

**现象**：
执行 `arr1[0] = 10.00` 后，打印结果为 `[10, 2, 3, 4, 5]`，而不是 `[10.0, ...]`。小数部分被“悄悄”丢弃了。

**原理分析**：
- **同质性（Homogeneity）**：与 Python 原生列表（List）不同，**Numpy 数组要求所有元素的数据类型必须完全一致**。
- **初始化定性**：
  - 在创建 `arr1 = np.array([1, 2, 3, 4, 5])` 时，Numpy 扫描所有元素都是整数，于是将数组类型锁定为 **`int32` (或 `int64`)**。
- **强制转换**：
  - 当试图将浮点数 `10.00` 塞入这个“整数数组”时，Numpy 为了保持类型一致且不报错，会**自动执行向下取整**（截断），将 `float` 强转为 `int`。

### 3. 💡 思考与总结
- **Python List**：`[1, "a", 3.0]` -> 灵活，但内存开销大，速度慢。
- **Numpy Array**：`[1, 2, 3]` (必须全是int) -> 内存紧凑，计算速度极快（C语言级别）。
- **教训**：如果需要存储小数，初始化时就应该让它变成浮点型，例如：
  ```python
  # 方法A：带上小数点
  arr = np.array([1.0, 2, 3]) 
  # 方法B：指定dtype
  arr = np.array([1, 2, 3], dtype=np.float64)
  ```