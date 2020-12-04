#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author:tom_tao626 
@license: Apache Licence 
@file: 2-单例模式.py 
@time: 2020/12/04
@contact: tp320670258@gmail.com
@site: xxxx.suizhu.net
@software: PyCharm 
"""

'''
单例模式
什么是单例模式？单例模式（Singleton Pattern）是一种常用的软件设计模式，该模式的主要目的是确保某一个类只有一个实例存在。当你希望在整个系统中，某个类只能出现一个实例时，单例对象就能派上用场。

在 Python 中，我们可以用多种方法来实现单例模式：

使用模块
使用 __new __
使用装饰器（decorator）
使用元类（metaclass）
我们主要介绍前面三种。

1-使用模块
其实，Python 的模块就是天然的单例模式，因为模块在第一次导入时，会生成 .pyc 文件，当第二次导入时，就会直接加载 .pyc 文件，而不会再次执行模块代码。因此，我们只需把相关的函数和数据定义在一个模块中，就可以获得一个单例对象了。我们来看一个例子，首先写一个py文件，比如说：

'''


class My_Singleton(object):
    def func(self):
        print("hello world!")


my_singleton = My_Singleton()

# 然后再创建一个py文件去调用它，比如我创建了一个333.py文件，然后导入该模块进行调用：
# from mysingleton import my_singleton
#
# my_singleton.func()

# 输出 hello world
# 在该项目文件夹下，看到.pyc的缓存文件

'''
2-使用__new__方法
__ new__() 是一个静态方法，该方法将实例被请求的类作为第一个参数，将类调用时传递的参数作为剩下的参数。
__ new__() 的返回值应该是新的对象实例。(通常是类cls的实例)。
而它与__ init__()方法不同之处在于__init__()方法在__new__()方法创建实例后，实例被返回给调用者之前调用。
它的参数是传递给构造表达式的那些参数。
也就是说__new__()用于创建实例，而__init__()则负责初始化实例。所以new方法可以用来构造单例。
'''


class Singleton(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:  # 反反为真
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


class MyClass(Singleton):
    a = 1


one = MyClass()
two = MyClass()

print(one == two)  # 做一个Boolean判断
print(id(one), id(two))  # 返回对象的唯一标识，在Cpython中可以认为是对象引用的内存地址
print(one, two)
"""
True
2029424727656 2029424727656
<__main__.MyClass object at 0x000001D88323D668> <__main__.MyClass object at 0x000001D88323D668>

上面这段代码我觉得是最为能概括单例特点的一段，
首先来看Singleton类，我们将类的实例和一个类变量 _instance 关联起来，
如果 cls._instance 为 None 则创建实例，否则直接返回 cls._instance。
这体现了单例的一个特点，即全局赋予一个实例，而后面的MyClass类则是继承了Singleton，
从打印结果可以看出，one和two对象同样的内存地址也能说明他们共享了属性。下面让我们再来看另一个例子：
"""
"""
选自：http://code.activestate.com/recipes/66531/  
"""


class Singleton(object):
    _state = {}

    def __new__(cls, *args, **kw):
        ob = super(Singleton, cls).__new__(cls, *args, **kw)
        ob.__dict__ = cls._state
        return ob


class MyClass2(Singleton):
    a = 1


one = MyClass2()
two = MyClass2()

# one和two是两个不同的对象,id, ==, is对比结果可看出
two.a = 3
print(one.a)
# 3
print(id(one))
# 2981458138784
print(id(two))
# 2981458138000
print(one == two)
# False
print(one is two)
# False
# 但是one和two具有相同的（同一个__dict__属性）,见:
print(id(one.__dict__))
# 2981458090240
print(id(two.__dict__))
# 2981458090240

'''
我们可以看到上面这个例子，one和two这里虽然是两个不同的对象，但他们引用了同一个类的实例，
即在该单例模式下，他们都共享了相同的属性__dict__，将所有实例的__dict__指向同一个字典，
这样实例就共享相同的方法和属性。对任何实例的名字属性的设置，无论是在__init__中修改还是直接修改，
所有的实例都会受到影响。不过实例的id是不同的。要保证类实例能共享属性，但不和子类共享，注意使用cls._state,而不是Singleton._state
'''

'''
3-使用装饰器
什么是装饰器？从概念来讲，就是在不改变原有代码的同时，动态地修改一个类或函数的功能。
装饰器也可以看做是一种模式，并且和六大原则中的开放封闭原则有很大关系，这个我们以后再讲，
顺便考虑另开一篇讲装饰器的博文，这里我们可以先从闭包讲起：

闭包(closure)是函数式编程的重要的语法结构。它需要具有如下几个特点：

必须有一个内嵌函数
内嵌函数必须引用外部函数中的变量
外部函数的返回值必须是内嵌函数
然后我们可以根据如上提示，大概写出闭包的一个通用式：
def outer(func):
	def inner(*arg,**kwargs):
		ret = func(*arg,**kwargs)
	return ret
return inner	# 返回的 inner，inner代表的是函数，非执行函数
'''

# 然后我们就可以写出闭包结构下的单例模式：
from functools import wraps


def singleton(cls):
    instances = {}

    @wraps(cls)  # 这是一个python内置的装饰器工具，装饰器修复技术，目的是让被装饰的函数的属性不会被改变
    def getinstance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return getinstance


@singleton
class MyClass3(object):
    a = 1


one = MyClass3()
two = MyClass3()
three = MyClass3()
print(id(one), id(two), id(three))
"""
2710090207976 2710090207976 2710090207976
"""
