# -*- coding: utf-8 -*
import random

list_1 = []   # 待输入的数组
n_start = 0   # 匹配成功的起始位置
flag = 0    # 是否找到231 的开头

#  50000 个    1 < 随机数 < 51
for i in range(50000):
    list_1.append(random.randint(1, 51))

length = len(list_1)  # 计算数组长度
new_list = list(reversed(list_1))  # 翻转 生成新的数组

for i, num in enumerate(new_list):
    if flag == 0:  # 找头
        if i > length - 231:
            # 这里还没找到头 那就没了
            break
        if num < 50:
            # 找到头了
            flag = 1
            n_start = i
    elif flag == 1:  # 已有头
        if i - n_start == 231:
            # 数量够了
            break
        if num >= 50:
            if i - n_start < 231:
                # 说明不足231个就完了
                # 重新找头
                flag = 0
                n_start = 0
                continue

if n_start == 0:
    print("没找到231个连续的")
    exit(0)

# 结果数组
out_list = []

for i in range(231):
    out_list.append(new_list[n_start + i])
# print(n_start)
print(list(reversed(out_list)))

