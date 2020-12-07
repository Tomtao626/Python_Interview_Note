#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author:tom_tao626 
@license: Apache Licence 
@file: 6.避免不必要的函数调用.py
@time: 2020/12/07
@contact: tp320670258@gmail.com
@site: xxxx.suizhu.net
@software: PyCharm 
"""


def square(number):
    return number * 2


squares = [square(i) for i in range(1000)]


# -----------------
def compute_squares():
    return [i ** 2 for i in range(1000)]
