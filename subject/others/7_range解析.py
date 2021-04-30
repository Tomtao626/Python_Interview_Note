
#!/usr/bin/env python
# -*- coding:utf-8 _*-
""" 
@author:tom_tao626 
@license: Apache Licence 
@file: 7_range解析.py 
@time: 2020/10/26
@contact: tp320670258@gmail.com
@site:  
@software: PyCharm 
"""


"""
range()方法是python的内置方法，但在python2和python3使用方法不同
range()方法详解
range(start,stop[,step])
作用：可创建一个整数列表，一般用在for循环中

参数说明：
start：起点，一般和stop搭配使用，即生成从start开始到stop结束（不包含stop）范围内的整数，例如range(1,10)，会生成[1,2,3,4,5,6,7,8,9]
stop：终点，可以和start搭配使用，也可以单独使用，即当start=0时，如range(0,5)=range(5)
step：步长，即下一次生成的数和这一次生成的数的差，例如range(1, 10, 2) 生成[1,3,5,7,9]，再如range(1,10,3) 生成[1, 4, 7]

使用区别：
在python2中，range方法得到的就是一个确定的列表对象，列表对象所拥有的方法，range方法生成的结果对象都可以直接使用；
而在python3中，range方法得到的对象是一个迭代器而不是一个确定的列表，如果想要转化为列表对象则需要再使用list方法进行转化。
for i in range(start, stop)在python2和python3中都可使用
Python2直接生成列表，Python3需要配合list方法使用
"""

# python3
'''
Python 3.8.5 (default, Jul 21 2020, 10:48:26) 
[Clang 11.0.3 (clang-1103.0.32.62)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> py3_ls = range(1,10)
>>> type(py3_ls)
<class 'range'>
>>> list(py3_ls)
[1, 2, 3, 4, 5, 6, 7, 8, 9]
'''

# python2
'''
Python 2.7.16 (default, Nov  1 2020, 09:27:23) 
[GCC Apple LLVM 12.0.0 (clang-1200.0.30.4) [+internal-os, ptrauth-isa=sign+stri on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> py2_ls = range(1,10)
>>> type(py2_ls)
<type 'list'>
>>> py2_ls
[1, 2, 3, 4, 5, 6, 7, 8, 9]
'''

# Python3中range()方法生成的已经不是一个列表， 而是一个range的迭代器





