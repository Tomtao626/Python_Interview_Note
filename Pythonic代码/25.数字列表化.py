#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author:tom_tao626 
@license: Apache Licence 
@file: 25.数字列表化.py 
@time: 2020/12/10
@contact: tp320670258@gmail.com
@site: xxxx.suizhu.net
@software: PyCharm 
"""

# 下面代码将整数转换为数字列表。
nums = 123456
# 使用map
digit_list = list(map(int, str(nums)))
print(digit_list)
# [1,2,3,4,5,6]
# 使用列表表达式
digit_list = [int(x) for x in str(nums)]
print(digit_list)
# [1,2,3,4,5,6]
