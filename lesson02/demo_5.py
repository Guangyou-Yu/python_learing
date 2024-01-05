#!/usr/bin/python
# encoding: utf-8

"""
@author:ygy
contact:1033207632@qq.com
@file:demo_5.py
@project:pycharm
@time:2023/12/28  8:52
"""
import time

t1 = time.time()
x = range(1,10000000000)
t2 = time.time()
y = range(1,10000000000)
t3 = time.time()
print(t2-t1,t3-t2)