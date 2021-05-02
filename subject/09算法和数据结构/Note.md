# 快速排序
> 快速排序使用分治法（Divide and conquer）策略来把一个序列（list）分为较小和较大的2个子序列，然后递归地排序两个子序列。
  步骤为：
> + 挑选基准值：从数列中挑出一个元素，称为"基准"（pivot）;
> + 分割：重新排序数列，所有比基准值小的元素摆放在基准前面，所有比基准值大的元素摆在基准后面（与基准值相等的数可以到任何一边）。在这个分割结束之后，对基准值的排序就已经完成;
> + 递归排序子序列：递归地将小于基准值元素的子序列和大于基准值元素的子序列排序。
> + 递归到最底部的判断条件是数列的大小是零或一，此时该数列显然已经有序。
> + ![https://pic.leetcode-cn.com/d13bd82917a8eba049efa261bebd3beb74b9e7c1adf39ce51bf1c9dd60d49f57-Quicksort-example.gif](https://pic.leetcode-cn.com/d13bd82917a8eba049efa261bebd3beb74b9e7c1adf39ce51bf1c9dd60d49f57-Quicksort-example.gif)
> + ![https://pic.leetcode-cn.com/e9ca22f1693e33a2fef64f55c10096ec93b9466459937f69eb409b0dad3f55bd-849589-20171015230936371-1413523412.gif](https://pic.leetcode-cn.com/e9ca22f1693e33a2fef64f55c10096ec93b9466459937f69eb409b0dad3f55bd-849589-20171015230936371-1413523412.gif)
```python
l = [3,1,5,2,8,5,9,4,7,3]
def quick_sort(nums: list) -> list:
    if len(nums) < 2:
        return nums
    else:
        top = nums[0] # 主元
        left = [lg for lg in nums[1:] if lg<top] # 主元左侧的元素
        right = [lg for lg in nums[1:] if lg>=top] # # 主元左侧的元素
        nums = quick_sort(left) + [top] + quick_sort(right)
        return nums

print(quick_sort(l))
```

# 选择排序
> + 首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，
> + 然后，再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。以此类推，直到所有元素均排序完毕。
> + ![https://pic.leetcode-cn.com/3b5a9383650b7ba01211846defeda8917d78827f02132113c57fcbd09715bf4b-849589-20171015224719590-1433219824.gif](https://pic.leetcode-cn.com/3b5a9383650b7ba01211846defeda8917d78827f02132113c57fcbd09715bf4b-849589-20171015224719590-1433219824.gif)
```python
l = [3,1,5,2,8,5,9,4,7,3]
def select_sort(nums: list) -> list:
    if len(nums) < 2:
        return nums
    else:
        n = len(nums)
        for i in range(n):
            for j in range(i, n):
                if nums[j] > nums[i]:
                    nums[j], nums[i] = nums[i], nums[j]
        return nums

print(select_sort(l))
```

# 冒泡排序（Bubble Sort）
> 冒泡排序时针对相邻元素之间的比较，可以将大的数慢慢“沉底”(数组尾部)
> + 所谓冒泡，就是将元素两两之间进行比较，谁大就往后移动，直到将最大的元素排到最后面，
> + 接着再循环一趟，从头开始进行两两比较，而上一趟已经排好的那个元素就不用进行比较了。
> + ![https://pic.leetcode-cn.com/faa1a3c1b3f1ae8a406e9c8e86bd28a9a1fb621ed6cc8eead1fe6e14ee0ec1c4-v2-d4c88b8cc620af6af67c33910899fcf7_b.gif](https://pic.leetcode-cn.com/faa1a3c1b3f1ae8a406e9c8e86bd28a9a1fb621ed6cc8eead1fe6e14ee0ec1c4-v2-d4c88b8cc620af6af67c33910899fcf7_b.gif)
> + ![https://pic.leetcode-cn.com/7d9af5dcad63d4097876f2614f38484f49b4e34f75c296a75001b19cf8134bb4-849589-20171015223238449-2146169197.gif](https://pic.leetcode-cn.com/7d9af5dcad63d4097876f2614f38484f49b4e34f75c296a75001b19cf8134bb4-849589-20171015223238449-2146169197.gif)
```python
def bubble_sort(nums: list) -> list:
    if len(nums) < 2:
        return nums
    else:
        n = len(nums)
        for i in range(n):
            if nums[i] > nums[i+1]:
                nums[j], nums[i] = nums[i], nums[j]
        return nums
```

# LRUCache算法
> Least-Recently-Used 替换掉最近最少使用的对象
> + 缓存剔除策略,当缓存空间不够用的时候需要一种方式剔除key
> + 常见的有LRU, LFU等
> + LRU通过使用一个循环双端队列不断把最新访问的key放到表头实现
> + 字典用来缓存，循环双端链表用来记录访问顺序

> 利用python内置的dict + collections.OrderedDict实现
> + dict 用来当作k/v键值对的缓存
> + OrderedDict用来实现更新最近访问的key
```python
from collections import OrderedDict
class LRUCache:
    def __init__(self, capacity=128):
        self.od = OrderedDict()
        self.capacity = capacity

    def get(self, key):  # 每次访问更新最新使用的key
        # 由于用OrderedDict来存取最近访问的key
        if key not in self.od:
            return -1
        if key in self.od:
            val = self.od[key]
            self.od.move_to_end[key]
            return val

    def put(self, key, value):  # 更新k/v
        if key not in self.od:  # insert
            self.od[key] = value
            # 判断容量是否已满
            if len(self.od) > self.capacity:
                self.od.popitem(last=False)
        del self.od[key]
        self.od[key] = value  # 更新key到表头
```
