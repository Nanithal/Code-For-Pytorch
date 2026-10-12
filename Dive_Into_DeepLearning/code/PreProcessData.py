# 预处理数据的代码
import os

# 创建一个人工数据表
# 这里创建的是csv文件---逗号分隔值文件（用逗号分隔同一行里的不同单元格，换行代表一行）
os.makedirs(os.path.join('..', 'data', ), exist_ok=True)
data_file = os.path.join('..', 'data', 'data2.csv')
with open(data_file, 'w') as f:
    f.write('NumRooms,Alley,Price\n')  # 列名
    f.write('NA,Pave,127500\n')  # 每行表示一个数据样本
    f.write('2,NA,106000\n')
    f.write('4,NA,178100\n')
    f.write('NA,NA,140000\n')

# 从创建的csv文件中加载数据
import pandas as pd
data = pd.read_csv(data_file)
print(data)

# 上述创建的文件中NaN代表缺失值
# 可以用插值法或者删除法处理缺失值
inputs, outputs = data.iloc[:, 0:2], data.iloc[:, 2]
# 选出数值列，均值填充
numeric_cols = inputs.select_dtypes(include="number").columns
inputs[numeric_cols] = inputs[numeric_cols].fillna(inputs[numeric_cols].mean())

# 选出类别（字符串）列，众数填充
cat_cols = inputs.select_dtypes(include=["object", "string"]).columns
for col in cat_cols:
    inputs[col] = inputs[col].fillna(inputs[col].mode()[0])
print(inputs)

# Alley列只接受两种类型的值“Pave”和“NaN”
# pandas可以自动将此列转换为两列“Alley_Pave”和“Alley_nan”
inputs = pd.get_dummies(inputs, dummy_na=True)
print(inputs)

# inputs和outputs中的所有条目都是数值类型，可以转换为张量格式
import torch
x = torch.tensor(inputs.to_numpy(dtype=float))
y = torch.tensor(outputs.to_numpy(dtype=float))
print(x)
print(y)