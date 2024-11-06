tuble = (721, "Passoion", 1024, "向左")

# 访问元组中的元素
print(tuble[0])  # 输出: 721
print(tuble[1])  # 输出: Passoion
print(tuble[2])  # 输出: 1024
print(tuble[3])  # 输出: 向左

# 尝试修改元组中的元素
try:
    tuble[0] = 2006  # 会抛出TypeError
except TypeError as e:
    print(f"错误: {e}")  # 输出: 错误: 'tuple' object does not support item assignment
