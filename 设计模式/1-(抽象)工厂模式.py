#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author:tom_tao626 
@license: Apache Licence 
@file: 1-(抽象)工厂模式.py
@time: 2020/12/04
@contact: tp320670258@gmail.com
@site: xxxx.suizhu.net
@software: PyCharm 
"""

'''
一、什么是“抽象工厂模式”——Abstract Factory Pattern

其实所谓的抽象工厂模式，是在前面讲解过的“简单工厂模式”、“工厂方法模式”的基础之上进行扩充的。回忆前面的这两种模式，我们可以得出：
工厂模式：针对一个系列的类（比如Circle、Rectangle、Ellipse、Triangle）, 它们有很多的共同点，很多书籍或者是文章将他们称之为一个系列的产品，通俗的说就是一个系列的类。使用一个工厂，用一个工厂创建函数去创建某一个类。
一系列类—— > 一个工厂—— > 一个创建函数—— > 某一个具体的类
工厂方法模式：针对一系列的类（比如Circle、Rectangle、Ellipse、Triangle），使用一个抽象的工厂接口，然后然后为每一个具体的类都编写一个工厂类，然后再在每一个类中用创建函数创建。
一系列类—— > 一个抽象工厂接口—— > 多个与系列对应的工厂类—— > 每个类有一个创建函数—— > 某一个具体的类
总结：简单工厂模式是笼统的承包服务，不管有多少个类需要创建，全部都由一个工厂去完成；
工厂函数模式是定制化的一对一服务，每一个工厂只能创建某一种特定的类，但是这些工厂统一遵循总工厂指定的原则（即抽象工厂接口的创建方法）。
那什么又是抽象工厂模式？
抽象工厂模式是“分类之后的一对一服务”，我们有多个系列的类需要创建，让某一个工厂专门负责某一类对象的创建，另一个工厂负责另外一类的对象创建（看到这里的小伙伴懵逼了，这不就是简单工厂模式吗？不就是多了几个工厂吗？没什么区别啊， 好像是的），但是区别还是有的，后面会讲到。
总结：
简单工厂模式：集中式生产
工厂方法模式：分散式成产
抽象工厂模式：对于同一系列的集中式生产，对于不同系列的分散式生产（这不就是前二者的结合嘛）

二、抽象工厂模式的使用情景
当出现一系列的产品族的时候，即出现很多的类的时候，而且这些类可以进行很好的分组，这个时候使用抽象工厂模式最为适合。为什么？因为此时如果使用简单工厂模式，则会导致那一个工厂任务繁重(
    因为要生产很多的类)，而且各个类之间没有区分度；如果使用工厂函数模式，每一个类要使用一个新的工厂（一对一服务），那么则需要创建太多的类了，导致代码臃肿；最好的办法就是现根据类的信息对各个系列的类进行分组处理，比如分成A、B、C三组，然后每一组由一个工厂类去完成，这样既体现了一对一的定制服务（先分组）又体现了工厂的集中生产（每一个工厂生产一类）

三、抽象工厂模式的python代码实现
比如我有很多的类需要定义，包括形状（比如Circle、Rectangle、Ellipse、Triangle），颜色类（比如Red、Blue、Black等等）

下面我将从一个“四步走”策略完整实现抽象工厂模式
'''

# 1、第一步，先定义形状类这个系列

import math


# 定义一个“形状”的接口，里面定义一个面积的接口方法，只有方法的定义，并没有实现体
class IShape(object):
    def Area(self):
        pass


# 定义4个图形类，都是实现Ishape接口，并且每一个图形都有一个可以计算面积的方法，相当于重写接口方法
class Circle(IShape):
    def Area(self, radius):
        return math.pow(radius, 2) * math.pi


class Rectangle(IShape):
    def Area(self, longth, width):
        return 2 * longth * width


class Triangle(IShape):
    def Area(self, baselong, height):
        return baselong * height / 2


class Ellipse(IShape):
    def Area(self, long_a, short_b):
        return long_a * short_b * math.pi


# 2、第二步，再定义颜色类这个系列


# 定义一个“颜色”的接口，里面定义一个颜色名称的接口方法，只有方法的定义，并没有实现体
class IColor(object):
    def color(self):
        pass


# 定义3个颜色类，都是实现IColor接口，并且每一个图形都有一个可以获取颜色名称的方法，相当于重写接口方法
class Red(IColor):
    def color(self, name):
        print(f'我的颜色是：{name}')


class Blue(IColor):
    def color(self, name):
        print(f'我的颜色是：{name}')


class Black(IColor):
    def color(self, name):
        print(f'我的颜色是：{name}')


# 3、第三步，定义抽象工厂以及与每一个系列对应的工厂


class IFactory:  # 模拟接口
    def create_shape(self):  # 定义接口的方法，只提供方法的声明，不提供方法的具体实现
        pass

    def create_color(self):
        pass


# 创建形状这一个系列的工厂
class ShapeFactory(IFactory):  # 模拟类型实现某一个接口，实际上是类的继承
    def create_shape(self, name):  # 重写接口中的方法
        if name == 'Circle':
            return Circle()
        elif name == 'Rectangle':
            return Rectangle()
        elif name == 'Triangle':
            return Triangle()
        elif name == 'Ellipse':
            return Ellipse()
        else:
            return None


# 创建颜色这一个系列的工厂
class ColorFactory(IFactory):  # 模拟类型实现某一个接口，实际上是类的继承
    def create_color(self, name):  # 重写接口中的方法
        if name == 'Red':
            return Red()
        elif name == 'Blue':
            return Blue()
        elif name == 'Black':
            return Black()
        else:
            return None


'''
注意：这里的抽象工厂和“工厂方法模式里面的抽象工厂有点区别，因为这里有两个系列的类型需要产生，所以，抽象工厂里面需要有两个函数接口，一个产生”形状“，一个产生”颜色“，然后再在实现该接口的工厂中分别进行重写。
'''
# 4、第四步，定义产生工厂类的类——抽象工厂模式的核心所在


# 定义一个专门产生工厂的类
class FactoryProducer:
    def get_factory(self, name):
        if name == 'Shape':
            return ShapeFactory()
        elif name == 'Color':
            return ColorFactory()
        else:
            return None


'''
注意：这一步是抽象工厂模式最为与众不同的，如果按照 “简单工厂模式 ”，只需要进行到第三步即可，因为然后我分别使用
ShapeFactory工厂类和ColorFactory类去分别产生每一个系列的类的实例即可，但是我们没有这么做。而是再定义一个新的

“工厂产生类”去让我们决定到底是要产生哪个类的实例。

总结：

抽象工厂模式（Abstract
Factory
Pattern）是围绕一个超级工厂创建其他工厂。该超级工厂又称为其他工厂的工厂。这种类型的设计模式属于创建型模式，它提供了一种创建对象的最佳方式。（这里的FactoryProducer就是超级工厂）

在抽象工厂模式中，接口是负责创建一个相关对象的工厂，不需要显式指定它们的类。每个生成的工厂都能按照工厂模式提供对象。
'''

# 5、运行结果如下：

if __name__ == '__main__':
    factory_producer = FactoryProducer()
    shape_factory = factory_producer.get_factory('Shape')
    color_factory = factory_producer.get_factory('Color')
    # --------------------------------------------------------------

    circle = shape_factory.create_shape('Circle')
    circle_area = circle.Area(2)
    print(f'这是一个圆，它的面积是：{circle_area}')

    rectangle = shape_factory.create_shape('Rectangle')
    rectangle_area = rectangle.Area(2, 3)
    print(f'这是一个长方形，它的面积是：{rectangle_area}')

    triangle = shape_factory.create_shape('Triangle')
    triangle_area = triangle.Area(2, 3)
    print(f'这是一个三角形，它的面积是：{triangle_area}')

    ellipse = shape_factory.create_shape('Ellipse')
    ellipse_area = ellipse.Area(3, 2)
    print(f'这是一个椭圆，它的面积是：{ellipse_area}')

    # ---------------------------------------------------------------
    red = color_factory.create_color('Red')
    red.color('红色')

    blue = color_factory.create_color('Blue')
    blue.color('蓝色')

    black = color_factory.create_color('Black')
    black.color('黑色')
'''
运行结果如下：

这是一个圆，它的面积是：12.566370614359172
这是一个长方形，它的面积是：12
这是一个三角形，它的面积是：3.0
这是一个椭圆，它的面积是：18.84955592153876
我的颜色是：红色
我的颜色是：蓝色
我的颜色是：黑色
'''

# 四、抽象工厂模式总结
'''
1、对比

再来看看工厂方法模式与抽象工厂模式对比：

工厂方法模式

抽象工厂模式

针对的是一个产品等级结构
针对的是面向多个产品等级结构
一个抽象产品类
多个抽象产品类
可以派生出多个具体产品类
每个抽象产品类可以派生出多个具体产品类
一个抽象工厂类，可以派生出多个具体工厂类
一个抽象工厂类，可以派生出多个具体工厂类
每个具体工厂类只能创建一个具体产品类的实例
每个具体工厂类可以创建多个具体产品类的实例
'''

'''
2、优点：

对于出现多系列的类型，创建逻辑清楚，因为是分门别类进行创建的；结合了“简单工厂模式”和“工厂方法模式”的优点
'''

'''
3、缺点

一系列产品族扩展非常困难，要增加一个系列的某一产品，既要在抽象的
Creator
里加代码，又要在具体的里面加代码。

比如，我还要在增加一系列的材质类型（包括Stone、Wood、Plastic等）。

首先，我需要再定义一个抽象材质接口，然后定义很多的类去实现这个接口；

然后，我需要在抽象工厂接口中添加一个create_material()
方法，并且还需要实现一个MaterialFactory工厂类；

最后，我还需要更改超级工厂FactoryProducer类

由此可见，牵一发而动全身，很麻烦。
'''



# 终极总结：抽象工厂模式：对于同一系列的集中式生产，对于不同系列的分散式生产，但是类型的创建不是由工厂函数直接完成，而是围绕一个“超级工厂”去搭建的
