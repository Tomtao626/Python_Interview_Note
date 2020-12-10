#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author:tom_tao626 
@license: Apache Licence 
@file: 21.合并两个字典.py 
@time: 2020/12/10
@contact: tp320670258@gmail.com
@site: xxxx.suizhu.net
@software: PyCharm 
"""

# 在 Python 2 中，使用 update（）合并两个字典，Python 3 变得更加简单。
# 下面脚本中，两个字典被合并。在相交的情况下，使用第二个字典中的值。

dict1 = dict(a=1, b=2, c=3)
dict2 = dict(test1=111, test2=222)
combine_dict = {**dict1, **dict2}
print(combine_dict)
# {'a': 1, 'b': 2, 'c': 3, 'test1': 111, 'test2': 222}
