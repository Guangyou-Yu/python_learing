#!/usr/bin/python
# encoding: utf-8

"""
@author:ygy
contact:1033207632@qq.com
@file:demo_7.py
@project:lesson02
@time:2024/1/4  7:32
"""


def myopen(filename):
    result = []
    f = open(filename)
    for line in f:
        result = line
        yield result
    f.close()
    return result

logs = myopen('test.log')
for line in logs:
    print(line)