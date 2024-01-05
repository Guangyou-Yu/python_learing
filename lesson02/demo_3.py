#!/usr/bin/python
# encoding: utf-8

"""
@author:ygy
contact:1033207632@qq.com
@file:demo_3.py
@project:pycharm
@time:2023/12/12  8:46
"""

p1 = [10,20]
p2 = [14,34]

dist = ( (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2) ** 0.5
print(dist)


p1 = {'x':10,'y':20}
p2 = {'y':34,'x':14}
dist = ( (p1['x'] - p2['x'])**2 + (p1['y'] - p2['y'])**2) ** 0.5
print(dist)