#!/usr/bin/python
# encoding: utf-8

"""
@author:ygy
contact:1033207632@qq.com
@file:iris_knn_demo.py
@project:pycharm
@time:2024/1/7  20:55
"""

from knn import KNN
def prepare_data():
    X = []
    y = []

    with open('iris.csv') as f:
        for id,line in enumerate(f):
            if id == 0:
                continue
            segs = line.strip().split(',')
            X.append([float(i) for i in segs[:4]])
            y.append(segs[-1])
    return X,y

if __name__ == '__main__':
    X,y = prepare_data()
    model = KNN()
    model.fit(X,y)

    sample = [5.0,3.6,1.4,0.2]
    print (model.predict(sample))