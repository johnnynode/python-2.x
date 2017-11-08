# coding=utf-8

for num in range(10, 20):
    for i in range(2,num):
        if num%i == 0:
            j=num/i
            print '%d 等于 %d * %d' % (num,i,j)
            break
    else:
        print num, '是一个质数'

"""
$ python Basic/loop-for-3.py
10 等于 2 * 5
11 是一个质数
12 等于 2 * 6
13 是一个质数
14 等于 2 * 7
15 等于 3 * 5
16 等于 2 * 8
17 是一个质数
18 等于 2 * 9
19 是一个质数

"""
