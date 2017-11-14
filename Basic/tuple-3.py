# coding=utf-8

tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')

# 以下是非法操作
# tup1[0] = 100

tup3 = tup1 + tup2
print tup3

"""
$ python Basic/tuple-3.py
(12, 34.56, 'abc', 'xyz')
"""