# 列表如何去除重复的元素

# 不改变原有顺序
# set集合和sorted
ls_one = [1, 2, 5, 3, 8, 5, 2, 10, 9]
print(list(set(ls_one)))

def sortList(nums: list):
    pass

ls_a = list()
for i in ls_one:
    if i not in ls_a:
        ls_a.append(i)

print(ls_a)