#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author:tom_tao626 
@license: Apache Licence 
@file: 20.通过枚举获取索引值对.py
@time: 2020/12/10
@contact: tp320670258@gmail.com
@site: xxxx.suizhu.net
@software: PyCharm 
"""

ls = {'a', 'b', 'c', 'd', 'e'}
for k, v in enumerate(ls):
    print(f"{k}:{v}")

"""
    0:c
    1:a
    2:b
    3:e
    4:d
"""