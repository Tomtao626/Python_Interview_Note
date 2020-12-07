#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author:tom_tao626 
@license: Apache Licence 
@file: 9.交换赋值.py 
@time: 2020/12/07
@contact: tp320670258@gmail.com
@site: xxxx.suizhu.net
@software: PyCharm 
"""

#  不推荐
a = 1
b = 2
temp = a
a = b
b = a

#  推荐
a, b = b, a  # 先生成一个元组(tuple)对象，然后unpack
