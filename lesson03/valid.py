#!/usr/bin/python
# encoding: utf-8

"""
@author:ygy
contact:1033207632@qq.com
@file:valid.py
@project:pycharm
@time:2024/1/10  8:06
"""

import random
def train_test_split(X, y, ratio=0.2):
    train_X, train_y, test_X, test_y = [],[],[],[]
    for sample_x,sample_y in zip(X,y):
        r = random.uniform(0.0,1.0)
        if r < ratio:
            test_X.append(sample_x)
            test_y.append(sample_y)
        else:
            train_X.append(sample_x)
            train_y.append(sample_y)
    return train_X, train_y, test_X, test_y

def cross_valid(model,X, y,splitter,metric):
    train_X, train_y, test_X, test_y = splitter(X,y)
    model.fit(train_X,train_y)

    y_pred = [model.predict(x) for x in test_X ]
    return metric(test_y,y_pred)


if __name__ == '__main__':
    from iris_knn_demo import prepare_data
    X, y = prepare_data()
    #train_X, train_y, test_X, test_y = train_test_split(X,y,0.3)
    #print(len(train_X),len(test_X),len(train_y),len(test_y))
    from knn import KNN
    from metrics import Metrics
    from functools import partial
    splitter = partial(train_test_split, ratio=0.3)

    model = KNN()
    p_score = cross_valid(model,X,y,splitter,Metrics.precision)
    print(p_score)