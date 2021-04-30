#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author:tom_tao626 
@license: Apache Licence 
@file: 6_func参数解析.py 
@time: 2020/10/25
@contact: tom@007vin.com
@site:  
@software: PyCharm 

# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""

'''
    函数参数传递方式  值传递  引用传递
    参数传递机制具有值传递（int、float等值数据类型）和引用传递（以字典、列表等非值对象数据类型为代表）两种基本机制。
    
'''
#  值传递，应用的参数不发生更改。（传了个副本进去） 见下
a = 5


def test(a):
    a += 1
    print("函数内：", a)


test(a)  # 函数内： 6
print("函数外：", a)  # 函数外： 5

#  引用传递，引用的参数发生更改（传的是真实的地址）见下
a = [1, 2, 3]
print(a)  # [1,2,3]


def test(a):
    a.append(4)
    print(a)


test(a)  # [1,2,3,4]
print(a)  # [1,2,3,4]

# python中还允许包裹方式的参数传递，这为不确定参数个数和参数类型的函数调用提供了基础：


'''
    *args和**kwargs主要用于函数定义，你可以将不定数量的参数传递一个函数，
    这里的不定的意思是：预先并不知道，函数使用者会传递多少个参数给你，所以在这个场景下，使用这两个关键字。
        *args用来发送一个非键值对的可变数量饿参数列表给一个函数，这里有个例子帮你梳理清楚：
        # 在函数调用时，*会以单个元素的形式解包一个元祖，使其成为独立的参数。
'''


def f(a, *args):
    print("a=", a)
    print("args=", args)


f(1, 2, 3, 4)  # 输出 a = 1, args = (2, 3, 4)


#  虽然传入1，2，3，4，但是解包为(1) (2,3,4)

def f1(a, b, *args):
    print("a=", a)
    print("b=", b)
    print("args=", args)


f1(1, 3, [1, 2, 3, 4, 5])
# 输出为 a=1,b=3,args= ([1, 2, 3, 4, 5],)  # 变成元组了

# 在python中，当*和**符号出现在函数定义的参数中时，表示任意数目参数。
# *arg表示任意多个无名参数，类型为tuple;**kwargs表示关键字参数，为dict，
# 使用时需将*arg放在**kwargs之前，否则会有“SyntaxError: non-keyword arg after keyword arg”的语法错误

'''
    **kwargs允许你将不定长度键值对，作为参数传递给一个函数。如果你想要在一个函数里面处理带名字的参数，
        你应该使用**kwargs，这里有个例子帮你梳理清楚：
        # 在函数调用时，**会以键/值对的形式解包一个字典，使其成为独立的关键字参数。
'''


def f2(**kwargs):
    print("kwargs=", kwargs)


f2(a=1, b=2)  # 实际上传入参数是两个，但是给包裹在一起


# 输出为：kwargs= {'a': 1, 'b': 2}

def person(name, age, **kwargs):
    print("name:", name, "age:", age, "other:", kwargs)


# 传入4个参数，自动将后两位  拼接到成字典
person('jack', 18, gender='M', job='engineer')


# 输出为：name: jack age: 18 other: {'gender': 'M', 'job': 'engineer'}

# 再看看*args和**kwargs混合的例子
def test_demo(a, *args, **kwargs):
    print(a, args, kwargs)


test_demo(1, 2, 3, x='4', y='5')
# 输出为： 1 (2, 3) {'x': '4', 'y': '5'}
# 丢进去不确定参数的包裹：1,2,3,x='4',y='5'
# 解包： 1 --> a
# 解包： (2,3) --> args
# 解包： {'x': '4', 'y': '5'} --> kwargs
