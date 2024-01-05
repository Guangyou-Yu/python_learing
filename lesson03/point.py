#!/usr/bin/python
# encoding: utf-8

"""
@author:ygy
contact:1033207632@qq.com
@file:point.py
@project:pycharm
@time:2024/1/4  10:32
"""

class Point(object):
    def __init__(self,cor):
        self.cor = cor

    def dist(self,p2):
        dist = 0
        if len(self.cor) != len(p2.cor):
            print('can not compute distance')
            return -1

        for i1, i2 in zip(self.cor, p2.cor):
            if i1 < 0 or i2 < 0:
                dist = -1
                break
            dist += (i1 - i2) ** 2
        else:
            dist = dist ** 0.5
        return dist


