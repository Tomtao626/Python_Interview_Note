#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author:tom_tao626 
@license: Apache Licence 
@file: 8_四种python列表反转显示方法.py 
@time: 2020/12/12
@contact: tp320670258@gmail.com
@site: xxxx.suizhu.net
@software: PyCharm 
"""

listNode = [1, 2, 3, 4, 5]

# 1 使用reversed函数 返回结果是一个反转的迭代器 还需使用list转换
newList_reversed = reversed(listNode)
print(newList_reversed)  # <list_reverseiterator object at 0x7ff38b2857d0>
print(list(newList_reversed))  # [5, 4, 3, 2, 1]

# 2 使用sorted函数 sorted是排序函数 它是对一个列表进行排序后生成一个新的list列表，而sort是在原有list列表基础上进行排序
newList_sorted = sorted(listNode, reverse=True)  # reverse是排序规则 True表示按降序排列，False则相反
print(newList_sorted)  # [5, 4, 3, 2, 1]

# 3 使用切片技术
li = listNode[::-1]  # [5, 4, 3, 2, 1]
print(li)
"""
    切片的格式是[0:3:1]，其中下标0指的是序列的第一个元素（左边界），下标3指的是切片的数量（右边界），参数1表示切片的步长为1，
    如果是-1则表示从右边开始进行切片且步长为1，切片不包括右边边界下标
    [:]表示获取序列所有的元素，省略步长则会默认步长为1 
"""

# 4 使用循环，递归
# 循环
new = list()
head = listNode
while head != None:
    new.append(head.val)
    head = head.next
new.reverse()
print(new)


# 递归
def getLists(self, listNode):
    if listNode is None:
        return []
    l = self.getLists(listNode.next)
    return l + [listNode.val]


lists = [1, 2, 3, 4, 5]
getLists(lists)

# + 连接多个小的列表，最后组成一个新的大列表，相当于使用多个值或列表新建一个列表

