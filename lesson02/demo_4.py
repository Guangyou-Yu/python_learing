#!/usr/bin/python
# encoding: utf-8

"""
@author:ygy
contact:1033207632@qq.com
@file:demo_4.py
@project:pycharm
@time:2023/12/15  8:46
"""

p1 = [10,20,1,13,35,23,12,44,13]
p2 = [12,2,17,14,34,24,2,4,3]

dist = 0

"""
确定两点来自同一个空间
"""

if len(p1) != len(p2):
    print('can not compute distance')
    exit(1)

for i1,i2 in zip(p1,p2):
    if i1<0 or i2<0:
        dist = 0
        break
    dist += (i1 - i2)**2
else:
    dist = dist ** 0.5
print(dist)