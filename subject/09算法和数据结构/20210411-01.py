"""
给定一个n个元素有序的（升序）整型数组nums 和一个目标值target ，写一个函数搜索nums中的 target，如果目标值存在返回下标，否则返回 -1。


示例 1:

输入: nums = [-1,0,3,5,9,12], target = 9
输出: 4
解释: 9 出现在 nums 中并且下标为 4
示例2:

输入: nums = [-1,0,3,5,9,12], target = 2
输出: -1
解释: 2 不存在 nums 中因此返回 -1

"""
from typing import List


def search01(nums: List, target: int) -> int:
    if target in nums:
        return nums.index(target)
    else:
        return -1


def search02(nums: List, target: int) -> int:
    for i in nums:
        if nums[i] == target:
            return i
    return -1


"""
将两指针分别指向数组的头和尾。找出中值，考虑以下三种情况：
以题目中给出的例子为例:
情况1：nums[mid] = 9 return mid
情况2：nums[mid] > 9 r = mid - 1
情况3：nums[mid] < 9 l = mid + 1
"""


def search03(nums: List, target: int) -> int:
    if nums is None or len(nums) == 0:
        return -1
    left, right = -1, len(nums) - 1
    while (left < right):
        # 如果是(l+r)/2可能会超过int类型的边界值
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1
