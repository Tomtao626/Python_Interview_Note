#!/usr/bin/env python  
# -*- coding:utf-8 _*-
"""
@author:tom_tao626
@license: Apache Licence
@file: 23.展开列表清单.py
@time: 2020/12/10
@contact: tp320670258@gmail.com
@site: xxxx.suizhu.net
@software: PyCharm
"""
# 有时不知道列表的嵌套深度，并且只想把所有元素放在一个普通列表中。可以通下面的方法得到数据：

from iteration_utilities import deepflatten
# 如果嵌套列表的深度只有1层
def flatten(l):
  return [item for sublist in l for item in sublist]
l=[[1,2,3],[3]]
print(flatten(l))
# [1,2,3,3]

# 如果不知道列表嵌套深度
l=[[1,2,3], [4, [5], {6, 7}], [8, [9, [10]]]]
print(list(deepflatten(l,depth=3)))
# [1,2,3,4,5,6,7,8,9,10]