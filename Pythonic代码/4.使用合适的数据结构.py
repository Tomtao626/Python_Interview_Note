#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author:tom_tao626 
@license: Apache Licence 
@file: 4.使用合适的数据结构.py 
@time: 2020/12/07
@contact: tp320670258@gmail.com
@site: xxxx.suizhu.net
@software: PyCharm 
"""

# 使用set()做成员测试和去重
million_numbers = list()


def check_number(number):
    for item in million_numbers:
        if item == number:
            return True
    return False


print(check_number(50000))

# in

print(50000 in million_numbers)

# -------------------
unique = list()
for element in million_numbers:
    if element not in unique:
        unique.append(element)

# 等价于
set(million_numbers)
