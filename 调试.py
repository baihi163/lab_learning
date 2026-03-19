import torch
from torchvision import datasets, transforms
import matplotlib.pyplot as plt

print("正在下载/加载 MNIST 手写数字数据集...")

# 1. 准备数据集
# datasets.MNIST 会自动帮我们从网上下载经典的“手写数字图片库”
train_dataset = datasets.MNIST(
    root='./data',               # 把数据下载到当前目录的 data 文件夹里
    train=True,                  # 我们要的是“训练集”（用来教 AI 的教材）
    transform=transforms.ToTensor(), # 关键！把图片转换成 PyTorch 能看懂的“数字矩阵（张量 Tensor）”
    download=True                # 如果没下载过，就自动下载
)

print(f"下载完成！我们一共拿到了 {len(train_dataset)} 张手写数字图片！")

# 2. 从这 6 万张图片里，抽出第 1 张来看看
image, label = train_dataset[0]  # 索引 0 就是第一张图。image 是图片本身，label 是它的标准答案

print(f"👉 这张图片的标准答案（标签）是: {label}")
print(f"👉 这张图片在电脑里的形状是: {image.shape}") 
# 剧透：形状会是 [1, 28, 28]，意思是 1个颜色通道(黑白)，高28像素，宽28像素

# 3. 把这张由数字组成的矩阵，真正画成图片显示出来
plt.imshow(image.squeeze(), cmap='gray') # squeeze() 是把多余的 1 去掉，变成 28x28 才能画图
plt.title(f"AI needs to recognize this as: {label}")
plt.show()
