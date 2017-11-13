# coding=utf-8

testTup1 = ('physics', 'chemistry', 1997, 2000);
testTup2 = (1,2,3,4,5)
testTup3 = "a", "b", "c", "d";

testTup4 = () # 创建空元组
testTup5 = (50,); # 元组中包含一个元素时，需要在元素后面添加逗号

tup1 = ('physics', 'chemistry', 1997, 2000);
tup2 = (1,2,3,4,5,6,7)

print "tup1[0] ", tup1[0]
print "tup2[1:5]: ", tup2[1:5]

"""
$ python Basic/tuple-2.py
tup1[0]  physics
tup2[1:5]:  (2, 3, 4, 5)
"""