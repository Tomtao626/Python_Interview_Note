#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author:tom_tao626 
@license: Apache Licence 
@file: 3.try-except替代if.py
@time: 2020/12/07
@contact: tp320670258@gmail.com
@site: xxxx.suizhu.net
@software: PyCharm 
"""

class Foo(object):
    hello = "hello world"
foo = Foo()

# if判断Foo类是否有hello属性
if hasattr(foo, 'hello'):
    foo.hello

# try-except判断
try:
    foo.hello
except AttributeError:
    pass


