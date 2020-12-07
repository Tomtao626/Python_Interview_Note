#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author:tom_tao626 
@license: Apache Licence 
@file: 2.使用列表解析式.py 
@time: 2020/12/07
@contact: tp320670258@gmail.com
@site: xxxx.suizhu.net
@software: PyCharm 
"""

# 使用列表解析式

# 计算列表内哪些数是否能被2整除

# 新手写法
output1 = list()
million_elements = [1,2,3,4,5,6,7,8,9]
for element in million_elements:
    if element % 2:
        output1.append(element)

# 中级写法
output2 = list(filter(lambda x:x%2, million_elements))

# 高手写法
output3 = [item for item in million_elements if item % 2]