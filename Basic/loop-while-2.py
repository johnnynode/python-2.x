# coding=utf-8

i = 1
while i < 10:
    i += 1
    if i % 2 > 0:
        continue
    print i

print

i = 1
while 1:
    print i
    i += 1
    if i > 10:
        break

"""
$ python Basic/loop-while-2.py
2
4
6
8
10

1
2
3
4
5
6
7
8
9
10

"""
