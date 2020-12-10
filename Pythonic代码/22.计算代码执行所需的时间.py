#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author:tom_tao626 
@license: Apache Licence 
@file: 22.计算代码执行所需的时间.py 
@time: 2020/12/10
@contact: tp320670258@gmail.com
@site: xxxx.suizhu.net
@software: PyCharm 
"""
import time

start_time = time.time()
a, b = 1, 2
c = a + b
end_time = time.time()
time_taken_in = (end_time-start_time)*(10**6)
print(time_taken_in)