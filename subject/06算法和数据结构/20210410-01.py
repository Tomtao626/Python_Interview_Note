"""
    1. 移动零(LeetCode)
    给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
    示例:
    输入：[0,1,0,3,12]
    输出：[1,3,12,0,0]
    说明:
    必须在原数组上操作，不能拷贝额外的数组。
    尽量减少操作次数。
"""
from typing import List
def moveZeroes(nums: List[int]) -> List[int]:
    """:cvar
    移动零
    """
    length = len(nums)
    if length <= 1:
        return nums
    else:
        m = -1
        for n in range(len(nums)):
            if nums[n] != 0:
                m += 1
                nums[m], nums[n] = nums[n], nums[m]
        return nums


print(moveZeroes([0, 1, 0, 3, 12]))  # [1, 3, 12, 0, 0]
