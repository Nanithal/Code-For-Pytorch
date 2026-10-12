# 使用pytorch实现操作数据的代码
import torch

# 一维张量等差数组的创建
x = torch.arange(12)
print(x)
# 访问张量的形状----沿每个轴的长度
print(x.shape)
# 访问张量中元素的个数
print(x.numel())
# 改变张量的形状
X = x.reshape(3, 4)
print(X)
X = x.reshape(3, -1)    # 通过-1自动计算剩下一个纬度

# 创建元素全部是0的张量
# 括号围起来代表这是第一个参数，即指定张量的形状
x1 = torch.zeros((2, 3, 4))
# print(x1)
x1 = torch.ones((2, 3, 4))  # 同理，创建元素全部是1的张量
# print(x1)

# 从某个概率分布中随机采样来创建张量
x2 = torch.randn(3, 4)  # 从均值为0,标准差为1的标准高斯分布中随机采样创建张量

# 也可以提供具体数值的python列表来创建张量
x3 = torch.tensor([[2, 1, 3, 4], [1, 2, 3, 4]])
print(x3)


# 张量的运算
x4 = torch.tensor([1.0, 2, 4, 8])
y4 = torch.tensor([2, 2, 2, 2])
x4 + y4
x4 - y4
x4 * y4
x4 / y4
torch.exp(y4)   # 调用数学函数进行运算

# 张良之间按照某一个维度进行连接
x = torch.arange(12, dtype=torch.float32).reshape((3, 4))
y = torch.tensor([[2.0, 1, 4, 3], [1, 2, 3, 4], [4, 3, 2, 1]])
print(torch.cat((x,y), dim=0))
print(torch.cat((x,y), dim=1))
print(x == y) # 也可以通过逻辑运算构建张量
x.sum() # 对张量中的所有元素求和

a = torch.arange(3).reshape((3, 1))
b = torch.arange(2).reshape((1, 2))
print(a + b)    # 将两个矩阵广播为一个3x2矩阵（a复制列，b复制行，再相加）

# 索引与切片机制
print(x[-1])    # 指定第一轴为最后一个的元素
print(x[1:3])  # 指定第一轴为第二个和第三个的元素(依旧从0开始，且左闭右开)
x[1, 2] = 9    # 第一轴和第二轴都指定了第几个元素进行修改
x[0:2, :] = 12  # 也可以大范围更改
print(x)

# 下面的不是原地操作写法
before = id(y)
y = y + x
print(id(y) == before)
# 用切片可以实现原地操作
z = torch.zeros_like(y)
print('id(z)', id(z))
z[:] = x + y
print('id(z)', id(z))
# 下面的也是原地操作写法
print(id(x))
x += y
print(id(x))

# tensor转换为其他python对象
a = x.numpy()   # 从Tensor转换为NumPy
b = torch.tensor(a) # 从NumPy转换为Tensor
print(type(a))
print(type(b))

# 将大小为1的张量转换为Python标量,采用item或者其他的内置函数
a = torch.tensor([3.5])
print(a)
print(a.item())
print(float(a))
print(int(a))

print(x)
print(y)
print(x > y)

