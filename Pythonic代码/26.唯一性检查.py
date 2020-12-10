#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author:tom_tao626 
@license: Apache Licence 
@file: 26.唯一性检查.py 
@time: 2020/12/10
@contact: tp320670258@gmail.com
@site: xxxx.suizhu.net
@software: PyCharm 
"""


# 下面的函数检查列表中的元素是否唯一。
def unique(l):
    if len(l) == len(set(l)):
        print("所有元素是唯一的")
    else:
        print("存在重复")


unique([1, 2, 3, 4])
# 所有元素是唯一的
unique([1, 1, 3, 4])
# 存在重复
