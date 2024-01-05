#!/usr/bin/python
# encoding: utf-8

"""
@author:ygy
contact:1033207632@qq.com
@file:demo_6.py
@project:pycharm
@time:2023/12/29  8:51
"""

def euDistance(p1,p2):
    dist = 0
    if len(p1) != len(p2):
        print('can not compute distance')
        return -1

    for i1, i2 in zip(p1, p2):
        if i1 < 0 or i2 < 0:
            dist = -1
            break
        dist += (i1 - i2) ** 2
    else:
        dist = dist ** 0.5
    return dist

if __name__ == '__main__':
    print(euDistance((10,20),(20,30)))