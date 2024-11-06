# 创建一个字典，模拟学生分数表
scores = {
    "脱缰凯": 32,
    "赵德柱": 16,
    "司马一": 99,
}

# 添加新元素
scores["鹰眼"] = 6

# 修改已有元素
scores["赵德柱"] = 10

# 删除元素
del scores["司马一"]

# 输出学生分数
print("学生分数：")
for student, score in scores.items():
    print(f"{student}: {score}")

# 输出修改后的字典
print("\n学生分数（修改版）")
print(scores)
