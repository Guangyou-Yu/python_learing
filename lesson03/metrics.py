#!/usr/bin/python
# encoding: utf-8

"""
@author:ygy
contact:1033207632@qq.com
@file:metrics.py
@project:pycharm
@time:2024/1/10  7:54
"""

class Metrics(object):

    def precision(y,y_pred):
        cnt = 0
        for y1,y2 in zip(y,y_pred):
            if y1 == y2:
                cnt += 1.0
        return cnt / len(y)

if __name__ == '__main__':
    y = [1,2,3]
    y_pred = [1,2,4]
    print(Metrics.precision(y,y_pred))