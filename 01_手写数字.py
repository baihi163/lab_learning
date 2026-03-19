import os
# 给系统发通行证：允许两个库同时使用 OpenMP
os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'

import torch
from torchvision import datasets, transforms
import matplotlib.pyplot as plt

print("正在加载 MNIST 手写数字数据集...")

# 1. 准备数据集 (因为刚才已经下载过了，这次它会直接从你本地的 data 文件夹读取，瞬间完成！)
train_dataset = datasets.MNIST(
    root='./data',               
    train=True,                  
    transform=transforms.ToTensor(), 
    download=True                
)

print(f"加载完成！我们一共拿到了 {len(train_dataset)} 张手写数字图片！")

# 2. 抽出第 1 张来看看
image, label = train_dataset[0]  

print(f"👉 这张图片的标准答案（标签）是: {label}")
print(f"👉 这张图片在电脑里的形状是: {image.shape}") 

# 3. 画出图片
plt.imshow(image.squeeze(), cmap='gray') 
plt.title(f"AI needs to recognize this as: {label}")
plt.show()
