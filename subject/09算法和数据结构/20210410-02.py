"""
    2. 数组中的第 K 个最大元素
    在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的
    元素，而不是第 k 个不同的元素。
    示例 1:
    输入: [3,2,1,5,6,4] 和 k = 2
    输出: 5
    示例 2:
    输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
    输出: 4
    说明:
    你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。
"""
from typing import List


#
# def ArrayMaxNum(nums: List[int], k: int) -> int:
#     length = len(nums)
#     if length <= 1:
#         return 1
#     nums = sorted(nums, reverse=True)
#     return nums[k - 1]
def quickSort(nums: List[int]) -> List[int]:
    if len(nums) <= 1:
        return nums
    else:
        top = nums[0]
        left = [lg for lg in nums[1:] if lg < top]
        right = [lg for lg in nums[1:] if lg >= top]
        nums = quickSort(right) + [top] + quickSort(left)
        return nums


def ArrayMaxNum(nums: List[int], k: int) -> int:
    """:cvar
    数组中的第 K 个最大元素
    """
    length = len(nums)
    if length <= 1:
        return 1
    return quickSort(nums)[k - 1]


print(ArrayMaxNum([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))  # 4

"""
class Solution:
    def quickSort(self, nums: list) -> list[int]:
        if len(nums) <= 1:
            return nums
        else:
            top = nums[0] # 主元
            left = [lg for lg in nums[1:] if lg<top] # 主元左侧的元素
            right = [lg for lg in nums[1:] if lg>=top] # # 主元左侧的元素
            nums = self.quickSort(right) + [top] + self.quickSort(left)
            return nums

    def findKthLargest(self, nums: List[int], k: int) -> int:
        length = len(nums)
        if length <= 1:
            return 1
        return self.quickSort(nums)[k-1]
"""
