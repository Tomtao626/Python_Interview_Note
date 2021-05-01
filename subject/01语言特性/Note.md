# Python 的解释器有哪些？
    CPython：采用 C 语言开发的的一种解释器，目前最通用也是使用最多的解释器。
    IPython：是基于 CPython 之上的一个交互式解释器器，交互方式增强功能和 CPython 一样。
    PyPy：目标是执行效率，采用 JIT 技术。对 Python 代码进行动态编译，提高执行的速度。
    JPython：基于 Java 语言的解释器，可以直接将 Python 代码编译成 Java 字节码执行。
    IronPython：运行在微软 .NET 平台上的解释器，把 Python 编译成 .NET 的字节码，然后执行。

# Python 3 和 Python 2 的区别？
## print
   ```python
    print "hello"
    在py2中，print是语句
    python2.6+ 可以使用 from __future__ import print_function 来实现相同功能，将print当作函数使用

    print("hello")
    在py3中，print是函数
   ```
## 编码
   ```python
    py2默认编码是ascii，一般在文件顶部需要加 coding:utf-8
    >>> import sys
    >>> sys.version
    '2.7.16 (default, Feb 28 2021, 12:34:25) \n[GCC Apple LLVM 12.0.5 (clang-1205.0.19.59.6) [+internal-os, ptrauth-isa=deploy'
    >>> sys.getdefaultencoding()
    'ascii'

    py3默认是utf-8
    >>> import sys
    >>> sys.version
    '3.8.2 (default, Apr  8 2021, 23:19:18) \n[Clang 12.0.5 (clang-1205.0.22.9)]'
    >>> sys.getdefaultencoding()
    'utf-8'
   
   ```

## 字符串
   ```python
    py2中字符串有两种类型，unicode文本字符串和str字节序列
    字符串格式化方法 % 
    age = 18
    print("%s" % age)

    py3中字符串是str，字节序列是byte
    字符串格式化方法 format
    age = 18
    print("{0}".format(age))
    py3新的格式化输出方式 f-string
    print(f"{age}")

   ```

## True和False
   ```python
    py2:
        True和False是两个全局变量，分别对应1和0，既然是变量，那么他们就可以指向其它对象，可以被重新赋值
    
    py3:
        修复了这个缺陷，True和False变成了两个关键字，永远指向两个固定的对象
   ```

## 迭代器
   ```python
    py2:很多内置函数和方法都是返回列表对象
    py3:全都更改成了返回迭代器对象，因为迭代器的惰性加载特性使得操作大数据更有效率
    py2的range和xrange函数合并成了range，如果想同时兼容py2和py3，可以这样写：
    try:
        range = xrange
    except:
        pass
    另外字典对象的dict.keys()和dict.values()方法不再返回一个列表，而是以一个迭代器的'view'的对象返回，
    高阶函数map，filter，zip返回的也不是列表对象了，
    py2的迭代器必须实现next方法
    py3则是__next__方法
   ```

## nonlocal 
   ```python
    py2:
        在函数里面，可以用关键字global声明某个变量为全局变量，但是在嵌套函数中是没法实现的
        name_x = "tomtao"
        def hello_x():
            def update_name_x():
                global name_x
                name_x = "9527"
            update_name_x()
            print(name_x) # name依旧是"tomtao"
        
    py3:
        可以使用关键字nonlocal实现，使得在嵌套函数中非局部变量成为可能。
        name_y = "tomtao"
        def hello_y():
            def update_name_y():
                nonlocal name_y
                name_y = "9527"
            update_name_y()
            print(name_y) # name="9527"
   ```

## 除法符号 /
   ```python
    py2:
        除法/的返回的结果是整型，
    py3:
        返回的结果是浮点类型。
   ```

## 声明元类
   ```python
    py2:
    class newclass:
        _metaclass_ = MetaClass
    py3:
    class newclass(metaclass=MetaClass):
        pass
   ```
    
## 异常
   ```python
    py2:
    except Exception, var：
        pass
    py3:
    except Exception as var:
        pass
   ```

## 不等运算符
   ```python
    py2:
        != <>
    py3:
        != 去掉了<>
   ```

## 经典(旧式)类和新式类
   ```python
    py2:
        默认都是经典(旧式)类，只有继承了object才是新式类，有以下三种写法：
        #新式类写法
        class Test(object):
            pass
        #经典(旧式)类
        class Test:
            pass
        
        class Test():
            pass
        py2中新式类和经典(旧式)类的区别:
            经典(旧式)类采用的是深度优先算法，当子类继承多个父类时，如果继承的多个父类有属性相同的，根据深度优先，会以继承的第一个父类的属性为主；
            新式类采用的是广度优先算法，当子类继承多个父类时，如果继承的多个父类有属性相同的，根据广度优先，后面继承的属性会覆盖前面已经继承的属性。
    py3:
        默认都是新式类，并且不必显式的继承object，有以下三种写法:
        class Test(object):
            pass
        
        class Test:
            pass
        
        class Test():
            pass
   ```

## Python3 和 Python2 中 int 和 long 区别
   ```python
    py2:
        有int和long类型。int类型最大值不能超过 sys.maxint，而且这个最大值是平台相关的。可以通过在数字的末尾附上一个Ｌ来定义长整型，它比int类型表示的数字范围更大。
    py3:
        只有一种整数类型int，大多数情况下，和Python２中的长整型类似。
   ```

## xrange 和 range 的区别
   ```python
    py2:
        xrange 是在 Python2 中的用法，
    py3:
        只有range,xrange用法与range完全相同，所不同的是生成的不是一个list对象，而是一个生成器。
   ```
