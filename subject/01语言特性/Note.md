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

# python中的DocStrings（解释文档）有什么作用
   ```python
    # DocStrings 的主要作用就是解释代码的作用，让其他人读你的代码时候，能更快速理解代码的作用是什么。
    # 当定义一个函数后，我们可以在函数的第一行使用一对三个单引号 ''' 或者一对三个双引号 """ 来定义一个文档字符串，该文档字符串就是该函数的解释文档。
    # 使用 __doc__（注意双下划线）调用函数中的文档字符串属性（注意，文中出现的反斜杠是转义符，去除一些符号的特殊格式）
    def get_max(x,y):
        '''
        比较取出两个int类型中较大的那个数
        :param x: int类型数字
        :param y: int类型数字
        :return: 输出较大值
        '''
        if x > y:
            return x
        else:
            return y
    
    get_max(3, 5)
    print(get_max.__doc__) # 输出解释文档的具体内容
   ```

# Python 3 中的类型注解
    Python 是一种高级语言，在我们编写代码的时候，我们定义的变量和定义函数里面的参数的时候，是不用区分它们的类型。
    但是作为作者我们知道函数的参数应该传入什么类型的数据，但是作为读者并不能快速知道变量或者参数的类型是什么。
    针对上述问题，我们就可以使用类型注解，类型注解的好处就是让读者快速知道我们变量或者参数的类型是什么。
   ```python
    # 通用写法
    def add(x, y):
        return x + y
    
    # 函数注解写法,表明传入的两个数字是int类型
    def add(x int, y int) -> int:
        return x + y
   ```

# 命名规范
    基本原则：Python 语言的标识符必须以字母、下划线 _ 开头，数字不能作为开头，后面可以跟任意数目的字母、数字和下划线 _。此处的字母并不局限于 26 个英文字母，可以包含中文字符、日文字符等。
    禁忌：Python 包含一系列关键字和内置函数，不建议使用它们作为变量名，防止发生冲突。

    常用命名规则：
    项目名：首字母大写、其余单词小写，多单词组合则用下划线分割
    包名、模块名：全用小写字母
    类名：首字母大写、其他字母小写，多单词采用驼峰
    方法：小写单词
    函数：若函数的参数名与保留关键字冲突，则在参数后加一个下划线，比拼音好太多
    全局变量：采用全大写，多单词用下划线分割

    注意：
    不论是类成员变量还是全局变量，均不使用 m 或 g 前缀。
    私有类成员使用单一下划线前缀标识，多定义公开成员，少定义私有成员。
    变量名不应带有类型信息，因为 Python 是动态类型语言。如 iValue、names_list、dict_obj 等都是不好的命名。
    开头、结尾一般为 Python 的自有变量，不要以这种方式命名
    以 __ 开头（2 个下划线），是私有实例变量（外部不嫩直接访问），依照情况进行命名。

# 下划线
    一个前导下划线：表示非公有，也叫做保护变量，表示类对象和子类对象自己才能访问这些变量。采用 from somemodulename import * 的方法导入模块时，被保护的变量不会被导入。
    一个后缀下划线：为了避免关键字冲突，采用的一种命名方法。
    两个前导下划线：私有属性，当命名一个类属性可能引起名称冲突时使用。避免与子类中的属性命名冲突，无法在外部直接访问（名字已经被重整所以访问不到），类对象和子类可以访问（公有方法可以间接访问，使用重整后的名称访问）。
    两个前导和后缀下划线：内置的的魔法对象或者属性（有特殊用途），例如 __init__ 或者 __file__。我们不要自己创造类似的名称，只需要使用他们即可。

    补充：
    私有属性和私有方法使用双前置下划线，私有属性和方法类内部，类的对象和子类可以访问
    私有属性和私有方法外部不能直接访问
    单前置下划线是普通方法
    父类的私有属性和私有方法
    子类对象不能在自己的方法内部，直接访问父类的私有属性或私有方法
    子类对象可以通过父类的公有方法间接访问到私有属性或私有方法

    私有属性本质：
    类创建的时候，在 __init__ 方法中，采用双前置下划线创建的属性，该属性创建后，类内部实际上对该属性进行了名字重整（改名了，私有方法和属性在外部不可以直接用属性或方法名调用，内部将私有方法和属性在前面增加了 "_类名"）。
    因此实例化对象后，外界访问不到，但是使用重整后的名字可以访问。
