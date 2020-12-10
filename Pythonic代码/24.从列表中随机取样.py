#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author:tom_tao626 
@license: Apache Licence 
@file: 24.从列表中随机取样.py
@time: 2020/12/10
@contact: tp320670258@gmail.com
@site: xxxx.suizhu.net
@software: PyCharm 
"""

# 下面代码从给定列表中生成了 n 个随机样本。
import random
import secrets

list1 = ['a', 'b', 'c', 'd', 'e']
ns = 2
samples = random.sample(list1, ns)
print(samples)
# ['a','c']

# 或者使用secrets库生成随机样本进行， 下面代码仅适用于 Python 3.x。


s_rand = secrets.SystemRandom()

list1 = {'a', 'b', 'c', 'd', 'e'}
ns = 2
samples = s_rand.sample(list1, ns)
print(samples)
# ['c','d']
