# coding=utf-8

a = 20
b = 10
c = 15
d = 5
e = 0

e = (a + b) * c / d
print "(a + b) * c / d 运算结果为：", e

e = ((a + b) * c) / d
print "((a + b) * c) / d 运算结果为：", e

e = (a + b) * (c / d)
print "(a + b) * (c / d) 运算结果为：", e

e = a + (b * c) / d
print "a + (b * c) / d 运算结果为：", e

"""
$ python Basic/operators-8.py
(a + b) * c / d 运算结果为： 90
((a + b) * c) / d 运算结果为： 90
(a + b) * (c / d) 运算结果为： 90
a + (b * c) / d 运算结果为： 50

"""
