#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author:tom_tao626 
@license: Apache Licence 
@file: 18.判断两个字符串是否为异序词.py 
@time: 2020/12/10
@contact: tp320670258@gmail.com
@site: xxxx.suizhu.net
@software: PyCharm 
"""

# 异序词是通过重新排列不同单词或短语的字母而形成的单词或短语。如果两个字符串的 Counter 对象相等，那么它们就是相同字母异序词对。

from collections import Counter

s1, s2, s3 = "abcde", "abdec", "abcdb"
c1, c2, c3 = Counter(s1), Counter(s2), Counter(s3)
if c1 == c2:
    print(f"{c1}和{c2}是异序词")
if c1 == c3:
    print(f"{c1}和{c3}是异序词")
