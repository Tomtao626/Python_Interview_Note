#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author:tom_tao626 
@license: Apache Licence 
@file: 9_IP地址分割.py 
@time: 2020/12/31
@contact: tp320670258@gmail.com
@site: xxxx.suizhu.net
@software: PyCharm 
"""


# 从键盘输入一个ip地址，判断是否是合格的ip
def check_ip(ipAddr):
    # 切割IP地址为一个列表
    addr = ipAddr.strip().split('.')
    # 切割后列表必须有4个参数
    if len(addr) != 4:
        return False
    for i in range(4):
        # 每个参数必须为数字，否则校验失败
        addr[i] = int(addr[i])
        # 每个参数值必须在0-255之间
        if 255 >= addr[i] >= 0:
            pass
        else:
            return False
        i += 1
    else:
        return True
