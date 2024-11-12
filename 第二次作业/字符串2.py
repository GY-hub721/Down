def introduction(name, age, job):
    # 使用f-string格式化字符串，将传入的name, age, job值嵌入到模板中
    return f"姓名: {name}, 年龄: {age}, 职业: {job}"

# 定义变量
name = "迪迦"  # 姓名
age = "3000万"  # 年龄
job = "奥特曼"  # 职业

x = introduction(name, age, job)

print(x)
