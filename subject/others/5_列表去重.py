# python实现列表去重

# 先通过集合去重，再转列表

lis = [11, 12, 13, 12, 15, 16, 13]

a = set(lis)
print(a)

x = [i for i in a]
print(x)
