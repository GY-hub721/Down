list1 = [1, 2, 3, 4, 5]
list2 = [5, 6, 7, 8, 9]

# 将列表转换为集合
set1 = set(list1)
set2 = set(list2)

# 计算交集
intersection = set1 & set2

# 计算并集
union = set1 | set2

# 输出结果
print("交集:", intersection)
print("并集:", union)
