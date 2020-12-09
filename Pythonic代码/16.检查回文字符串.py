#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author:tom_tao626 
@license: Apache Licence 
@file: 16.检查回文字符串.py 
@time: 2020/12/09
@contact: tp320670258@gmail.com
@site: xxxx.suizhu.net
@software: PyCharm 
"""


str1 = "aabbaa"
if str1 == str1[::-1]:
    print(True)
else:
    print(False)