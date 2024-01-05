#!/usr/bin/python
# encoding: utf-8

"""
@author:ygy
contact:1033207632@qq.com
@file:demo_9_plus.py
@project:lesson02
@time:2024/1/4  8:13
"""

from demo_9 import Point

class Vector(Point):
    def dot(self,v2):
        result = 0
        for i,j in zip(self.c,v2.c):
            result += i*j
        return result

    def cosin(self,v2):
        o = Point(*[0 for i in range(len(self.c))])
        d1 = self.dist(o)
        d2 = v2.dist(o)
        result = 1.0 * self.dot(v2) / (d1*d2)
        return result

v1 = Vector(1,1)
v2 = Vector(1,1)
print (v1.cosin(v2))