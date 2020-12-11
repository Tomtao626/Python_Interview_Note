#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author:tom_tao626 
@license: Apache Licence 
@file: 3-建造者模式.py 
@time: 2020/12/07
@contact: tp320670258@gmail.com
@site: xxxx.suizhu.net
@software: PyCharm 
"""


# 建造者，顾名思义是修建建筑的工人，按照基本的施工方式：打桩-浇筑框架-砌墙-装修，同样的施工流程却能造就千差万别的建筑，因为不同的材料、不同设计，可以表现出千差万别，这就是建造者模式的简要理解。

# 示例代码：

# -*- coding:utf-8 -*-


class Builder():
    """建造流程：原料—施工"""

    def __init__(self):
        self.materiel = None
        self.design = None

    def run(self):
        print('修建完工！设计建筑: %s | 购买原料: %s' % (self.design, self.materiel))


class A(Builder):
    """方案A，修建毛坯房"""

    def get_materiel(self):
        self.materiel = "砖瓦"

    def get_design(self):
        self.design = "毛坯房"


class B(Builder):
    """方案B，修建写字楼"""

    def get_materiel(self):
        self.materiel = "玻璃"

    def get_design(self):
        self.design = "写字楼"


class Director:
    """调度：买原料-组织施工"""

    def __init__(self):
        self.programme = None

    def build(self):
        self.programme.get_materiel()
        print("购买原料:{}".format(self.programme.materiel))
        self.programme.get_design()
        print("设计方案:{}".format(self.programme.design))
        self.programme.run()


if __name__ == '__main__':
    # 修建毛坯房
    test = Director()
    test.programme = A()
    test.build()

    # 修建写字楼
    test = Director()
    test.programme = B()
    test.build()
"""
----------------------------
购买原料:砖瓦
设计方案:毛坯房
修建完工！设计建筑: 毛坯房 | 购买原料: 砖瓦
购买原料:玻璃
设计方案:写字楼
修建完工！设计建筑: 写字楼 | 购买原料: 玻璃
"""

# 上面是一个很简单直白的例子，建造者模式应该有几个关键要素：相同的流程、不同的表示、修建者。
# 也就是同一个对象（建筑）在同一修建者组织下，以相同的实例化流程（施工流程）来达到不同的表示效果（毛坯、写字楼）
# 这样的好处使得构建与它的表示分离，使得同样的构建过程可以创建不同的表示。
