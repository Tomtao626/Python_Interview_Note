#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author:tom_tao626 
@license: Apache Licence 
@file: 17.列表中的元素统计.py 
@time: 2020/12/09
@contact: tp320670258@gmail.com
@site: xxxx.suizhu.net
@software: PyCharm 
"""

# collections.Counter()

from collections import Counter
list1 = ['a', 'b', 'b', 'c', 'd', 'e', 'a', 'b', 'e']
count = Counter(list1)
print(count)
# Counter({'a': 2, 'b': 2, 'e': 2, 'c': 1, 'd': 1})
print(count['b'])
# 3
print(count.most_common(1))
# [('b', 3)]
print(count.items())
# dict_items([('a', 2), ('b', 3), ('c', 1), ('d', 1), ('e', 2)])
