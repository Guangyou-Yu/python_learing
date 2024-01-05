#!/usr/bin/python
# encoding: utf-8

"""
@author:ygy
contact:1033207632@qq.com
@file:demo_2.py
@project:pycharm
@time:2023/12/8  8:47
"""

x1 = 10
y1 = 20

x2,y2 = 14,40

dist = ((x1-x2) ** 2 + (y1-y2) ** 2) ** 0.5

print(dist)
print(dist > 3)