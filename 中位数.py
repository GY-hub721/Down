def findMedian(nums1, nums2):
    # 确保 nums1 是较短的数组
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    a, b = len(nums1), len(nums2)
    left, right = 0, a

    while left <= right:
        i = (left + right) // 2  # nums1 的切分位置
        j = (a + b) // 2 - i      # nums2 的切分位置

        # 边界值处理
        left1 = nums1[i - 1] if i > 0 else float('-inf')
        right1 = nums1[i] if i < a else float('inf')
        left2 = nums2[j - 1] if j > 0 else float('-inf')
        right2 = nums2[j] if j < b else float('inf')

        # 检查切分是否有效
        if left1 <= right2 and left2 <= right1:
            # 总长度为偶数
            if (a + b) % 2 == 0:
                return (max(left1, left2) + min(right1, right2)) / 2
            # 总长度为奇数
            else:
                return max(left1, left2)
        elif left1 > right2:
            right = i - 1  # 向左移动右边界
        else:
            left = i + 1   # 向右移动左边界

nums1 = [1, 3]
nums2 = [2]

# 将数组从大到小排序
nums1_sorted = sorted(nums1, reverse=True)
nums2_sorted = sorted(nums2, reverse=True)

print(findMedian(nums1_sorted, nums2_sorted))  # 输出: 2.0
