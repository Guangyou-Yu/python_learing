#!/usr/bin/python
# encoding: utf-8

"""
@author:ygy
contact:1033207632@qq.com
@file:demo_9.py
@project:lesson02
@time:2024/1/4  7:55
"""

class Point(object):

    def __init__(self,*c):
        self.c = c

    def dist(self,p2):
        dist = 0
        if len(self.c) != len(p2.c):
            print('can not compute distance')
            return -1

        for i1, i2 in zip(self.c, p2.c):
            if i1 < 0 or i2 < 0:
                dist = -1
                break
            dist += (i1 - i2) ** 2
        else:
            dist = dist ** 0.5
        return dist
if __name__ == '__main__':
    p1 = Point(1,2,2,2,2)
    p2 = Point(2,3,4,5,6)

    print (p1.dist(p2))
    print (p2.dist(p1))