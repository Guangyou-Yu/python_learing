#!/usr/bin/python
# encoding: utf-8

"""
@author:ygy
contact:1033207632@qq.com
@file:vector.py
@project:pycharm
@time:2024/1/4  10:32
"""

from lesson03.point import Point
class Vector(Point):
    def norm(self):
        o = Point([0 for i in self.cor])
        return self.dist(o)

    def dot(self,v2):
        result = 0
        for i, j in zip(self.cor, v2.cor):
            result += i * j
        return result

    def cosin(self,v2):
        result = 0
        d1 = self.norm()
        d2 = v2.norm()
        result = 1.0 * self.dot(v2) / (d1 * d2)
        return result