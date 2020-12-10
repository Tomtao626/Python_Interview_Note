#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author:tom_tao626 
@license: Apache Licence 
@file: 19.使用 try-except-else 块.py 
@time: 2020/12/10
@contact: tp320670258@gmail.com
@site: xxxx.suizhu.net
@software: PyCharm 
"""

a,b = 1,0
try:
    print(a/b)
except ZeroDivisionError:
    print("除数为0")
else:
    print("不存在异常")
finally:
    print("此段总是会运行")