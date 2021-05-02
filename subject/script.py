

l = [3,1,5,2,8,5,9,4,7,3]
def bubble_sort(nums: list) -> list:
    if len(nums) < 2:
        return nums
    else:
        n = len(nums)
        for i in range(1, n-i):
            if nums[i] > nums[i+1]:
                nums[i-1], nums[i] = nums[i], nums[i-1]
        return nums

print(bubble_sort(l))
