#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author:tom_tao626 
@license: Apache Licence 
@file: 7.避免不必要的bool测试.py 
@time: 2020/12/07
@contact: tp320670258@gmail.com
@site: xxxx.suizhu.net
@software: PyCharm 
"""

# checking for true
variable = 0

if variable == True:
    pass

# 等价于
if variable is True:
    pass

# 等价于
if variable:
    pass


# checking for false
variable = 0

if variable == False:
    pass

# 等价于
if variable is False:
    pass

# 等价于
if not variable:
    pass