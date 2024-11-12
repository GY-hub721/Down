def maxArea(height):
    # 初始化左右指针
    left, right = 0, len(height) - 1
    # 初始化最大水量
    MaxArea = 0

    # 当左右指针没有交叉时继续循环
    while left < right:
        # 计算当前水量
        current = (right - left) * min(height[left], height[right])
        # 更新最大水量
        MaxArea = max(current, MaxArea)

        # 移动较短的柱子指针，尝试找到更高的柱子
        if height[left] < height[right]:
            left += 1  # 向右移动左指针
        else:
            right -= 1  # 向左移动右指针

    return MaxArea  # 返回找到的最大水量


height = [ 3,2, 1]
print(maxArea(height))
