#!/usr/bin/python
# encoding: utf-8

"""
@author:ygy
contact:1033207632@qq.com
@file:knn.py
@project:pycharm
@time:2024/1/7  10:17
"""

from point import Point
from vector import Vector
class KNN(object):
    def __init__(self):
        pass

    def _k_nearest_neighbors(self,x,k):
        distances = []
        p = Point(x)
        for id,x2 in enumerate(self.X):
            p2 = Point(x2)
            dist = p.dist(p2)
            distances.append((dist,self.y[id]))
            distances.sort(key=lambda x:x[0])
        return distances[:k]

    def fit(self,X,y=None):
        self.X = X
        self.y = y

    def predict(self,x,k=5):
        ky = self._k_nearest_neighbors(x,k)
        #return ky
        k_dict = {}
        for dist,type in ky:
            if type in k_dict.keys():
                k_dict[type] +=1
            else :
                k_dict[type] = 1

        k_s = sorted(k_dict, key=lambda x:x[0])
        return k_s[0]