#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author:tom_tao626 
@license: Apache Licence 
@file: 1.内置函数.py
@time: 2020/12/07
@contact: tp320670258@gmail.com
@site: xxxx.suizhu.net
@software: PyCharm 
"""

# 1.多使用内置函数
# 计算列表长度
# 新手写法
how_many = 0
one_million_elements = [1, 2, 3, 4, 5, 6, 7]
for element in one_million_elements:
    how_many += 1
print(how_many)

# pythonic len()
# len()一把梭
print(len(one_million_elements))
